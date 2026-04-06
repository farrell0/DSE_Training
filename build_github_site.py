#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
CONVERTER = ROOT / "pdf_to_github_markdown.py"
TRACKS = [
    ("core", "DSE Core"),
    ("search", "DSE Search"),
    ("analytics", "DSE Analytics"),
    ("graph", "DSE Graph"),
]
ROLE_LABELS = {
    "DU": "Demonstration Unit",
    "PL": "Practical Lab",
    "DM": "Discussion Module",
}
TRACK_INTROS = {
    "core": "The DSE Core track is the Cassandra-oriented foundation of the training archive, covering cluster setup, security, operations, drivers, Studio, OpsCenter, and supporting platform services.",
    "search": "The DSE Search track focuses on the Solr and Lucene side of DataStax Enterprise, moving from first analyzers and query syntax into debugging, scalar fields, spatial search, and tuning.",
    "analytics": "The DSE Analytics track preserves the Spark-oriented training modules for DSE, including RDDs, DataFrames, DSEFS, machine learning, streaming, and capacity planning.",
    "graph": "The DSE Graph track is retained in the navigation so the archive structure stays complete, even though no graph training modules are currently present in this repository snapshot.",
}


@dataclass(frozen=True)
class Module:
    track_key: str
    track_label: str
    pptx_name: str
    module_id: int
    role_code: str
    title: str
    slug: str

    @property
    def track_dir(self) -> Path:
        return ROOT / self.track_key

    @property
    def pptx_path(self) -> Path:
        return self.track_dir / self.pptx_name

    @property
    def folder_path(self) -> Path:
        return self.track_dir / self.slug

    @property
    def pdf_name(self) -> str:
        return f"{self.slug}.pdf"

    @property
    def pdf_path(self) -> Path:
        return self.folder_path / self.pdf_name

    @property
    def role_label(self) -> str:
        return ROLE_LABELS.get(self.role_code, self.role_code)

    @property
    def page_title(self) -> str:
        return f"{self.track_label}: {self.title}"


def slugify(text: str) -> str:
    text = text.replace("&", " and ")
    text = text.replace(",", " ")
    text = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", text)
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "module"


def md_path(path: str) -> str:
    return quote(path, safe="/-_.")


def nav_table(active_track: str | None, prefix: str) -> str:
    cells = []
    for track_key, track_label in TRACKS:
        target = f"{prefix}{track_key}/README.md"
        if active_track == track_key:
            cells.append(f"<td><strong>{track_label}</strong></td>")
        else:
            cells.append(f'<td><a href="{md_path(target)}"><strong>{track_label}</strong></a></td>')
    return "<table>\n  <tr>\n    " + "".join(cells) + "\n  </tr>\n</table>\n"


def load_converter_module(script_path: Path):
    spec = importlib.util.spec_from_file_location("pdf_to_github_markdown", script_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load converter at {script_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def discover_tools() -> None:
    missing = []
    for tool in ("libreoffice", "pdftohtml", "pdfimages"):
        if shutil.which(tool) is None:
            missing.append(tool)
    if missing:
        raise RuntimeError("Missing required tool(s): " + ", ".join(missing))


def parse_module(track_key: str, track_label: str, pptx_path: Path) -> Module:
    stem = pptx_path.stem
    match = re.match(r"^000-[^-]+(?:-[^-]+)*-(\d+)-([A-Z]+)-60,\s*(.+)$", stem)
    if not match:
        raise ValueError(f"Unexpected module filename: {pptx_path.name}")
    module_id = int(match.group(1))
    role_code = match.group(2)
    title = re.sub(r"\s+", " ", match.group(3).strip())
    slug = f"{module_id}-{slugify(title)}"
    return Module(
        track_key=track_key,
        track_label=track_label,
        pptx_name=pptx_path.name,
        module_id=module_id,
        role_code=role_code,
        title=title,
        slug=slug,
    )


def collect_modules() -> dict[str, list[Module]]:
    collected: dict[str, list[Module]] = {}
    for track_key, track_label in TRACKS:
        track_dir = ROOT / track_key
        modules = [parse_module(track_key, track_label, path) for path in sorted(track_dir.glob("*.pptx"))]
        collected[track_key] = sorted(modules, key=lambda module: (module.module_id, module.title.lower()))
    return collected


def module_description(module: Module) -> str:
    title = module.title
    track = module.track_label
    lower = title.lower()

    if "lab" in lower:
        verb = "walks through a hands-on lab"
    elif "install" in lower or "config" in lower:
        verb = "explains the installation and configuration workflow"
    elif "troubleshooting" in lower:
        verb = "focuses on troubleshooting methods and operational diagnostics"
    elif "security" in lower:
        verb = "covers the security model and the administrative steps needed to apply it"
    elif "capacity planning" in lower or "tuning" in lower:
        verb = "reviews performance, sizing, and tuning considerations"
    elif "machine learning" in lower or "streaming" in lower:
        verb = "introduces the runtime model and practical usage patterns"
    else:
        verb = "introduces the topic and shows how it fits into the overall platform"

    return (
        f"This {module.role_label.lower()} in the {track} track {verb}. "
        f"It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around {title.lower()}."
    )


def customer_question(module: Module) -> str:
    return (
        f"I am working through the {module.track_label} curriculum and need help with {module.title.lower()}. "
        f"What does this training module cover, and when should I use the techniques it introduces?"
    )


def convert_pptx_to_pdf(module: Module) -> None:
    module.folder_path.mkdir(parents=True, exist_ok=True)
    if module.pdf_path.exists():
        module.pdf_path.unlink()
    subprocess.run(
        [
            "libreoffice",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            str(module.folder_path),
            str(module.pptx_path),
        ],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    generated_pdf = module.folder_path / f"{module.pptx_path.stem}.pdf"
    if not generated_pdf.exists():
        raise RuntimeError(f"LibreOffice did not produce a PDF for {module.pptx_name}")
    if generated_pdf != module.pdf_path:
        if module.pdf_path.exists():
            module.pdf_path.unlink()
        generated_pdf.rename(module.pdf_path)


def convert_pdf_to_markdown(converter_module, module: Module) -> str:
    assets_dir = module.folder_path / "assets"
    if assets_dir.exists():
        shutil.rmtree(assets_dir)
    page_images = converter_module.extract_images(module.pdf_path, assets_dir)
    pages = converter_module.parse_pdf_xml(module.pdf_path)
    markdown = converter_module.build_markdown(module.pdf_path, assets_dir.name, pages, page_images)
    markdown = converter_module.apply_cleanup(markdown)
    return markdown


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def normalize_converted_markdown(text: str) -> str:
    lines = text.strip().splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines.pop(0)
    normalized = "\n".join(lines).strip()
    normalized = re.sub(r"\bAKC[pP][A-Za-z0-9]{20,}\b", "[REDACTED_API_KEY]", normalized)
    return normalized


def module_page(module: Module, converted_markdown: str) -> str:
    return f"""
# {module.page_title}

{nav_table(module.track_key, "../../")}

**Module Type:** {module.role_label}

**Customer:** {customer_question(module)}

**Daniel:** {module_description(module)}

## Downloads

- [PDF slides](./{md_path(module.pdf_name)})
- [Original PowerPoint](../{md_path(module.pptx_name)})

## Converted Slides

{normalize_converted_markdown(converted_markdown)}
""".strip()


def track_page(track_key: str, modules: list[Module]) -> str:
    lines = [
        f"# {dict(TRACKS)[track_key]}",
        "",
        nav_table(track_key, "../"),
        "",
        TRACK_INTROS[track_key],
        "",
    ]
    if not modules:
        lines.extend(
            [
                "## Modules",
                "",
                "No converted training modules are present for this track in the current repository snapshot.",
            ]
        )
        return "\n".join(lines)

    lines.extend(["## Modules", ""])
    for module in modules:
        lines.extend(
            [
                f"### [{module.title}](./{md_path(module.slug + '/README.md')})",
                "",
                f"**Module Type:** {module.role_label}",
                "",
                module_description(module),
                "",
            ]
        )
    return "\n".join(lines).strip()


def root_page(modules_by_track: dict[str, list[Module]]) -> str:
    lines = [
        "# DataStax Enterprise Training Archive",
        "",
        nav_table(None, ""),
        "",
        "This repository preserves a set of training modules for DataStax Enterprise 6.8. The archive is organized by platform track and each PowerPoint deck is converted into a PDF-backed Markdown article so the material is readable directly on GitHub.",
        "",
    ]
    for track_key, track_label in TRACKS:
        modules = modules_by_track[track_key]
        lines.extend([f"## [{track_label}]({md_path(track_key + '/README.md')})", ""])
        if modules:
            for module in modules:
                lines.append(f"- [{module.title}]({md_path(track_key + '/' + module.slug + '/README.md')})")
        else:
            lines.append("- No modules currently present.")
        lines.append("")
    return "\n".join(lines).strip()


def clean_generated_dirs(modules_by_track: dict[str, list[Module]]) -> None:
    expected = {module.slug for modules in modules_by_track.values() for module in modules}
    for track_key, _ in TRACKS:
        track_dir = ROOT / track_key
        for child in track_dir.iterdir():
            if child.is_dir() and child.name not in expected:
                if child.name == "__pycache__":
                    shutil.rmtree(child)


def main() -> int:
    discover_tools()
    if not CONVERTER.exists():
        raise RuntimeError(f"Missing converter: {CONVERTER}")
    converter_module = load_converter_module(CONVERTER)
    converter_module.discover_tools()

    modules_by_track = collect_modules()
    clean_generated_dirs(modules_by_track)

    for track_key, modules in modules_by_track.items():
        for module in modules:
            convert_pptx_to_pdf(module)
            converted_markdown = convert_pdf_to_markdown(converter_module, module)
            write_text(module.folder_path / "README.md", module_page(module, converted_markdown))
        write_text(ROOT / track_key / "README.md", track_page(track_key, modules))

    write_text(ROOT / "README.md", root_page(modules_by_track))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
