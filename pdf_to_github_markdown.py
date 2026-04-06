#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Node:
    page: int
    top: int
    left: int
    width: int
    height: int
    size: int
    family: str
    text: str
    bold: bool
    italic: bool


SECTION_RE = re.compile(r"^(\d+(?:\.\d+)+)\s+(.+)$")
FIGURE_RE = re.compile(r"^Figure\s+\d+-\d+\b")
EXAMPLE_RE = re.compile(r"^Example\s+\d+-\d+\b")


def run(args: list[str]) -> str:
    return subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode(
        "utf-8", "replace"
    )


def inner_text(elem: ET.Element) -> str:
    return "".join(elem.itertext())


def slugify_pdf_stem(stem: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", stem).strip("_")
    return slug or "converted_pdf"


def discover_tools() -> None:
    missing = []
    for tool in ("pdftohtml", "pdfimages"):
        result = subprocess.run(["which", tool], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            missing.append(tool)
    if missing:
        names = ", ".join(missing)
        raise SystemExit(f"Missing required tool(s): {names}")


def extract_images(pdf_path: Path, assets_dir: Path) -> dict[int, list[str]]:
    assets_dir.mkdir(exist_ok=True)
    prefix = assets_dir / "figure"
    subprocess.run(["pdfimages", "-j", str(pdf_path), str(prefix)], check=True)

    page_images: dict[int, list[str]] = {}
    for line in run(["pdfimages", "-list", str(pdf_path)]).splitlines():
        match = re.match(r"\s*(\d+)\s+(\d+)\s+image\s+", line)
        if not match:
            continue
        page = int(match.group(1))
        num = int(match.group(2))
        stem = f"figure-{num:03d}"
        for ext in (".jpg", ".jpeg", ".png", ".ppm", ".pbm"):
            candidate = assets_dir / f"{stem}{ext}"
            if candidate.exists():
                page_images.setdefault(page, []).append(candidate.name)
                break
    return page_images


def parse_pdf_xml(pdf_path: Path) -> list[tuple[int, list[Node]]]:
    xml_text = run(["pdftohtml", "-xml", "-i", str(pdf_path), "-stdout"])
    root = ET.fromstring(xml_text)

    global_fonts: dict[str, dict[str, str | int]] = {}
    for page_elem in root.findall("page"):
        for font in page_elem.findall("fontspec"):
            global_fonts[font.attrib["id"]] = {
                "size": int(font.attrib["size"]),
                "family": font.attrib["family"],
                "color": font.attrib["color"],
            }

    pages: list[tuple[int, list[Node]]] = []
    for page_elem in root.findall("page"):
        page_no = int(page_elem.attrib["number"])
        nodes: list[Node] = []
        for text_elem in page_elem.findall("text"):
            text = inner_text(text_elem).replace("\xa0", " ")
            text = re.sub(r"\s+", " ", text).strip()
            if not text:
                continue

            top = int(text_elem.attrib["top"])
            if text.startswith("MongoDB Developer") and top < 170:
                continue
            if text.startswith("© Copyright") or text.startswith("disclosure restricted"):
                continue
            if re.fullmatch(r"Page \d+\.?", text):
                continue
            if top > 1000:
                continue

            font = global_fonts[text_elem.attrib["font"]]
            serialized = ET.tostring(text_elem, encoding="unicode")
            nodes.append(
                Node(
                    page=page_no,
                    top=top,
                    left=int(text_elem.attrib["left"]),
                    width=int(text_elem.attrib["width"]),
                    height=int(text_elem.attrib["height"]),
                    size=int(font["size"]),
                    family=str(font["family"]),
                    text=text,
                    bold="<b>" in serialized,
                    italic="<i>" in serialized,
                )
            )
        pages.append((page_no, sorted(nodes, key=lambda node: (node.top, node.left))))
    return pages


def build_markdown(pdf_path: Path, assets_dir_name: str, pages: list[tuple[int, list[Node]]], page_images: dict[int, list[str]]) -> str:
    title = pdf_path.stem.replace("_", " ")
    first_page_nodes = pages[0][1] if pages else []
    chapter_label = next((node.text for node in first_page_nodes if node.text.startswith("Chapter ")), "")
    chapter_date = next((node.text for node in first_page_nodes if node.bold and node.size >= 30), "")

    figures_by_page: dict[int, list[tuple[str, str]]] = {}
    for page_no, nodes in pages:
        captions = [node.text for node in nodes if node.italic and FIGURE_RE.match(node.text)]
        figures_by_page[page_no] = list(zip(captions, page_images.get(page_no, [])))

    out: list[str] = []
    state = {"paragraph": [], "in_code": False}
    figure_index_by_page = {page_no: 0 for page_no in figures_by_page}

    def emit(line: str = "") -> None:
        out.append(line)

    def flush_paragraph() -> None:
        if not state["paragraph"]:
            return
        text = " ".join(state["paragraph"])
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            emit(text)
            emit()
        state["paragraph"].clear()

    def open_code(lang: str = "text") -> None:
        flush_paragraph()
        if not state["in_code"]:
            emit(f"```{lang}")
            state["in_code"] = True

    def close_code() -> None:
        if state["in_code"]:
            emit("```")
            emit()
            state["in_code"] = False

    def emit_figure(page_no: int, caption: str) -> None:
        idx = figure_index_by_page.get(page_no, 0)
        pairs = figures_by_page.get(page_no, [])
        if idx < len(pairs):
            cap, img = pairs[idx]
            if cap == caption:
                emit(f"![{caption}](./{assets_dir_name}/{img})")
                emit()
                figure_index_by_page[page_no] = idx + 1
        emit(f"*{caption}*")
        emit()

    emit(f"# {title}")
    emit()
    if chapter_label or chapter_date:
        chapter_heading = " ".join(part for part in (chapter_label, chapter_date) if part).strip()
        if chapter_heading:
            emit(f"## {chapter_heading}")
            emit()

    skip_texts = {value for value in (chapter_label, chapter_date) if value}
    small_headings = {
        "Software versions": "##",
        "Persons who help this month.": "###",
        "Additional resources:": "###",
    }

    for page_no, nodes in pages:
        i = 0
        while i < len(nodes):
            node = nodes[i]
            text = node.text

            if text in skip_texts:
                i += 1
                continue

            if text in small_headings and node.bold:
                flush_paragraph()
                close_code()
                emit(f"{small_headings[text]} {text}")
                emit()
                i += 1
                continue

            section_match = SECTION_RE.match(text)
            if section_match and node.bold and node.size >= 18:
                flush_paragraph()
                close_code()
                emit(f"## {section_match.group(1)} {section_match.group(2)}")
                emit()
                i += 1
                continue

            if node.italic and FIGURE_RE.match(text):
                flush_paragraph()
                close_code()
                emit_figure(page_no, text)
                i += 1
                continue

            if node.italic and EXAMPLE_RE.match(text):
                flush_paragraph()
                close_code()
                emit(f"### {text}")
                emit()
                i += 1
                continue

            if text.startswith("Note:"):
                flush_paragraph()
                close_code()
                parts = [text]
                j = i + 1
                while j < len(nodes):
                    prev = nodes[j - 1]
                    nxt = nodes[j]
                    if nxt.top - prev.top > 26:
                        break
                    if nxt.left < 250:
                        break
                    if nxt.italic and (FIGURE_RE.match(nxt.text) or EXAMPLE_RE.match(nxt.text)):
                        break
                    if nxt.family.endswith("BookMasterGothic"):
                        break
                    if nxt.bold and (SECTION_RE.match(nxt.text) or nxt.text in small_headings):
                        break
                    parts.append(nxt.text)
                    j += 1
                emit("> " + " ".join(parts))
                emit()
                i = j
                continue

            if node.family.endswith("BookMasterGothic"):
                open_code("text")
                emit(text)
                i += 1
                while i < len(nodes):
                    prev = nodes[i - 1]
                    nxt = nodes[i]
                    if not nxt.family.endswith("BookMasterGothic"):
                        break
                    if nxt.top - prev.top > 28:
                        break
                    emit(nxt.text)
                    i += 1
                close_code()
                continue

            if re.match(r"^\d+\.", text):
                flush_paragraph()
                close_code()
                parts = [text]
                j = i + 1
                while j < len(nodes):
                    prev = nodes[j - 1]
                    nxt = nodes[j]
                    if nxt.top - prev.top > 28:
                        break
                    if nxt.text.startswith("Note:") or nxt.text.startswith("– ") or re.match(r"^\d+\.", nxt.text):
                        break
                    if nxt.family.endswith("BookMasterGothic"):
                        break
                    if nxt.italic and (FIGURE_RE.match(nxt.text) or EXAMPLE_RE.match(nxt.text)):
                        break
                    if nxt.bold and (SECTION_RE.match(nxt.text) or nxt.text in small_headings):
                        break
                    parts.append(nxt.text)
                    j += 1
                emit(" ".join(parts))
                emit()
                i = j
                continue

            if text.startswith("– "):
                flush_paragraph()
                close_code()
                parts = [text[2:].strip()]
                j = i + 1
                while j < len(nodes):
                    prev = nodes[j - 1]
                    nxt = nodes[j]
                    if nxt.top - prev.top > 28:
                        break
                    if nxt.text.startswith("Note:") or nxt.text.startswith("– ") or re.match(r"^\d+\.", nxt.text):
                        break
                    if nxt.family.endswith("BookMasterGothic"):
                        break
                    if nxt.italic and (FIGURE_RE.match(nxt.text) or EXAMPLE_RE.match(nxt.text)):
                        break
                    if nxt.bold and (SECTION_RE.match(nxt.text) or nxt.text in small_headings):
                        break
                    parts.append(nxt.text)
                    j += 1
                emit("- " + " ".join(parts))
                emit()
                i = j
                continue

            state["paragraph"].append(text)
            j = i + 1
            while j < len(nodes):
                prev = nodes[j - 1]
                nxt = nodes[j]
                if nxt.top - prev.top > 26:
                    break
                if nxt.text.startswith("Note:") or nxt.text.startswith("– ") or re.match(r"^\d+\.", nxt.text):
                    break
                if nxt.family.endswith("BookMasterGothic"):
                    break
                if nxt.italic and (FIGURE_RE.match(nxt.text) or EXAMPLE_RE.match(nxt.text)):
                    break
                if nxt.bold and (SECTION_RE.match(nxt.text) or nxt.text in small_headings):
                    break
                state["paragraph"].append(nxt.text)
                j += 1
            flush_paragraph()
            i = j

    flush_paragraph()
    close_code()

    text = "\n".join(out)
    text = apply_cleanup(text)
    return text


def apply_cleanup(text: str) -> str:
    replacements = {
        "> Note: Before our boss yells at us (we’re kidding, he’s nice), we have to mention that this section is a very brief, get it up and running set of instructions. If you have more time, or interest, MongoDB runs free online programming and administration classes, the best free classes we’ve ever seen, available at,\n\nhttps://university.mongodb.com/":
            "> Note: Before our boss yells at us (we’re kidding, he’s nice), we have to mention that this section is a very brief, get it up and running set of instructions. If you have more time, or interest, MongoDB runs free online programming and administration classes, the best free classes we’ve ever seen, available at,\n>\n> https://university.mongodb.com/",
        "Consider getting this example to work in its entirety before editing the\n\n> Note: DRDL/YAML file.\n\nIf you do edit the file, a good/free online YAML validation utility is available at the following URL,\n\nhttps://yaml-online-parser.appspot.com/":
            "> Note: Consider getting this example to work in its entirety before editing the DRDL/YAML file. If you do edit the file, a good/free online YAML validation utility is available at the following URL,\n>\n> https://yaml-online-parser.appspot.com/",
        "As a developer’s workbench, Eclipse is extensible and can grow quite\n\n> Note: large. Each of the (frames) on display inside Eclipse is called a view . You could wind up having so many views, that these are organized into groupings called perspectives . A perspective is just a logical grouping of views.":
            "> Note: As a developer’s workbench, Eclipse is extensible and can grow quite large. Each of the (frames) on display inside Eclipse is called a view. You could wind up having so many views, that these are organized into groupings called perspectives. A perspective is just a logical grouping of views.",
        "```text\nhttps://jdbc.postgresql.org/download.html\n```": "https://jdbc.postgresql.org/download.html",
        "```text\nhttps://www.mongodb.com/download-center#enterprise\n```": "https://www.mongodb.com/download-center#enterprise",
        "```text\nhttps://www.youtube.com/watch?v=0kwopDp0bmg\n```": "https://www.youtube.com/watch?v=0kwopDp0bmg",
        "```text\nhttps://docs.mongodb.org/manual/products/bi-connector/\n```": "https://docs.mongodb.org/manual/products/bi-connector/",
        "```text\nhttps://www.mongodb.com/download-center#bi-connector\n```": "https://www.mongodb.com/download-center#bi-connector",
        "```text\nhttps://marketplace.eclipse.org/content/monjadb\n```": "https://marketplace.eclipse.org/content/monjadb",
        "```text\nhttp://app.robomongo.org/download.html\n```": "http://app.robomongo.org/download.html",
        "```text\nhttps://university.mongodb.com/\n```": "https://university.mongodb.com/",
        "rm mongodb-linux-x86_64-enterprise-rhel70-3.2.3.tar mv mongodb-linux-x86_64-enterprise-rhel70-3.2.3 mongo export PATH=$PATH:/opt/mongo/bin":
            "rm mongodb-linux-x86_64-enterprise-rhel70-3.2.3.tar\nmv mongodb-linux-x86_64-enterprise-rhel70-3.2.3 mongo\nexport PATH=$PATH:/opt/mongo/bin",
        "rm eclipse-standard-kepler-SR2-linux-gtk-x86_64.tar export PATH=$PATH:/opt/eclipse":
            "rm eclipse-standard-kepler-SR2-linux-gtk-x86_64.tar\nexport PATH=$PATH:/opt/eclipse",
        "select * from customer Then click the “Execute SQL statement” button in the Worksheet view toolbar. Example as shown in Figure 3-12.":
            "```sql\nselect * from customer\n```\n\nThen click the “Execute SQL statement” button in the Worksheet view toolbar. Example as shown in Figure 3-12.",
        "select * from customer t1, customer_orders t2 where t1._id = t2._id order by t1.cust_name":
            "```sql\nselect * from customer t1, customer_orders t2 where t1._id = t2._id order by t1.cust_name\n```",
        "*Figure 3-2.*\n\n*Figure 3-2 MongoDB install packages, “archive” includes the other 4*":
            "*Figure 3-2 MongoDB install packages, “archive” includes the other 4*",
    }

    for src, dst in replacements.items():
        text = text.replace(src, dst)

    text = text.replace(
        "- Use vi(C) or another program to view the contents of schema.drdl. A brief code review follows: • You see a “tables” section, followed by 2 tables:\n\n```text\ncustomer\n```\n\n, and\n\n```text\ncustomer_orders\n```\n\n. customer maps to our MongoDB collection, customer. Because the MongoDB collection, customer, had an embedded array of documents for customer orders titled,\n\n```text\norders\n```\n\n, the mongodrdl utility defines a second (SQL table) for us titled,\n\n```text\ncustomer_orders\n```\n\n. • The MongoDB (query) framework method titled,\n\n```text\n$unwind\n```\n\n, is used to (pivot) these array elements into separate rows, as is the SQL convention. • The remainder of this document is column names, and data types, as you would expect. • For now, make zero changes to this document; exit the editor, no save.",
        "- Use `vi(C)` or another program to view the contents of `schema.drdl`. A brief code review follows: you see a `tables` section, followed by 2 tables: `customer` and `customer_orders`. `customer` maps to our MongoDB collection, `customer`. Because the MongoDB collection, `customer`, had an embedded array of documents for customer orders titled, `orders`, the `mongodrdl` utility defines a second (SQL table) for us titled, `customer_orders`. The MongoDB (query) framework method titled, `$unwind`, is used to (pivot) these array elements into separate rows, as is the SQL convention. The remainder of this document is column names, and data types, as you would expect. For now, make zero changes to this document; exit the editor, no save."
    )
    text = text.replace(
        "- The first $match clause specifies an equality, that\n\n```text\ncust_num\n```\n\nmust be equal to 101.0.",
        "- The first `$match` clause specifies an equality, that `cust_num` must be equal to `101.0`."
    )
    text = text.replace(
        "- The second $match clause uses the “greater than or equal to” operator, $gte. The target of the operator is the key value titled,\n\n```text\norder_amount\n```\n\n, in the embedded sub-document titled, orders.",
        "- The second `$match` clause uses the “greater than or equal to” operator, `$gte`. The target of the operator is the key value titled, `order_amount`, in the embedded sub-document titled, `orders`."
    )
    text = text.replace(
        "```text\nhttp://www.eclipse.org/downloads/download.php?file=/technology/ep\np/downloads/release/kepler/SR2/eclipse-standard-kepler-SR2-linux-\ngtk-x86_64.tar.gz\n```",
        "http://www.eclipse.org/downloads/download.php?file=/technology/epp/downloads/release/kepler/SR2/eclipse-standard-kepler-SR2-linux-gtk-x86_64.tar.gz"
    )

    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def normalize_drdl_examples(text: str) -> str:
    lines = text.splitlines()
    result: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        if line == "### Example 3-1 Unedited version of our DRDL file":
            result.append(line)
            result.append("")
            i += 1
            while i < len(lines) and lines[i].startswith("```"):
                i += 1
                block: list[str] = []
                while i < len(lines) and lines[i] != "```":
                    block.append(lines[i])
                    i += 1
                if i < len(lines) and lines[i] == "```":
                    i += 1
                if block:
                    result.append("```yaml")
                    result.extend(reindent_yaml(block))
                    result.append("```")
                    result.append("")
                if i < len(lines) and lines[i] == "":
                    i += 1
            continue
        if line == "### Example 3-2 Edited version of the DRDL file, adding a $match clause.":
            result.append(line)
            result.append("")
            i += 1
            while i < len(lines) and lines[i].startswith("```"):
                i += 1
                block = []
                while i < len(lines) and lines[i] != "```":
                    block.append(lines[i])
                    i += 1
                if i < len(lines) and lines[i] == "```":
                    i += 1
                if block:
                    result.append("```yaml")
                    result.extend(reindent_yaml(block))
                    result.append("```")
                    result.append("")
                if i < len(lines) and lines[i] == "":
                    i += 1
            continue
        result.append(line)
        i += 1

    return "\n".join(result).replace("```yaml\n```", "").strip() + "\n"


def reindent_yaml(lines: list[str]) -> list[str]:
    indented: list[str] = []
    indent = 0
    previous_key = ""
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        if line == "tables:":
            indented.append("  tables:")
            indent = 2
            previous_key = "tables"
            continue
        if line.startswith("- db:"):
            indented.append(line)
            indent = 0
            previous_key = "db"
            continue
        if line.startswith("- table:"):
            indented.append("  " + line)
            indent = 2
            previous_key = "table"
            continue
        if line in {"collection: customer", "pipeline: []", "pipeline:", "columns:"}:
            indented.append("    " + line)
            previous_key = line.rstrip(":")
            continue
        if line.startswith("- $unwind:"):
            indented.append("    " + line)
            previous_key = "$unwind"
            continue
        if line.startswith("- $match:"):
            indented.append("    " + line)
            previous_key = "$match"
            continue
        if line.startswith("- Name:"):
            indented.append("    " + line)
            previous_key = "Name"
            continue
        if line.startswith(("MongoType:", "SqlName:", "SqlType:")):
            indented.append("      " + line)
            previous_key = "column"
            continue
        if line.startswith(("includeArrayIndex:", "path:")):
            indented.append("        " + line)
            previous_key = "$unwind_child"
            continue
        if line.startswith("cust_num:"):
            indented.append("        " + line)
            previous_key = "match_child"
            continue
        if line.startswith("orders.order_amount:"):
            indented.append("        " + line)
            previous_key = "match_child"
            continue
        if line.startswith("$gte:"):
            indented.append("          " + line)
            previous_key = "gte"
            continue
        indented.append(line)
    return indented


def convert_pdf(pdf_path: Path) -> tuple[Path, Path]:
    base = slugify_pdf_stem(pdf_path.stem)
    assets_dir = pdf_path.parent / f"{base}.assets"
    md_path = pdf_path.parent / f"{base}.md"

    page_images = extract_images(pdf_path, assets_dir)
    pages = parse_pdf_xml(pdf_path)
    markdown = build_markdown(pdf_path, assets_dir.name, pages, page_images)
    markdown = normalize_drdl_examples(markdown)
    markdown = apply_cleanup(markdown)
    md_path.write_text(markdown, encoding="utf-8")
    return md_path, assets_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert PDF files into GitHub-friendly Markdown with extracted figure assets.")
    parser.add_argument("pdf", nargs="*", help="PDF file(s) to convert. If omitted, convert every PDF in this script directory.")
    args = parser.parse_args()

    discover_tools()

    script_dir = Path(__file__).resolve().parent
    if args.pdf:
        pdfs = [Path(arg).resolve() for arg in args.pdf]
    else:
        pdfs = sorted(script_dir.glob("*.pdf"))

    if not pdfs:
        print("No PDF files found.", file=sys.stderr)
        return 1

    for pdf in pdfs:
        md_path, assets_dir = convert_pdf(pdf)
        print(f"Converted {pdf.name}")
        print(f"  Markdown: {md_path.name}")
        print(f"  Assets:   {assets_dir.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
