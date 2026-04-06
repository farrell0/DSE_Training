# DSE Core: Studio, Install, config, and first steps

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Core curriculum and need help with studio, install, config, and first steps. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Core track explains the installation and configuration workflow. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around studio, install, config, and first steps.

## Downloads

- [PDF slides](./6210-studio-install-config-and-first-steps.pdf)
- [Original PowerPoint](../000-DTSE-Studio-6210-DU-60%2C%20Studio%2C%20Install%2C%20config%2C%20and%20first%20steps.pptx)

## Converted Slides

## Discussion Unit:

Introduce DSE Studio

• Understand where Studio fits in the DSE Discussion Unit: portfolio

• Understand when/how you may choose DSE Studio, Overview, to use DSE Studio (planned use)

0000-DTSE-Studio-6210-DU-60-1 © DataStax, All Rights Reserved, Confidential

Discussion Lab:

Matching pairs – Match the

attributes on the right with the NCSA Mosaic, or simply Mosaic, is the web browser that popularized the World Wide Web and the Internet. It was also a client for earlier internet areas on the left protocols such as File Transfer Protocol, Network News Transfer Protocol, and Gopher. The browser was named for its support of multiple internet protocols. Source: https://en.wikipedia.org/wiki/Mosaic_(web_browser)

0000-DTSE-Studio-6210-DU-60-2 © DataStax, All Rights Reserved, Confidential

Discussion Lab: Clients to DSE Ops Center version 6 ?

Studio

Dev Center

DSBulk DSE

DSFiber (H-NAS only) Not DSE

GraphLoader

DSE supported drivers

Open source drivers

Box of Tissues Source: http://www.spencer1984.com/my_models/beverly-hillbillies.php

0000-DTSE-Studio-6210-DU-60-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

0000-DTSE-Studio-6210-DU-60-4 © DataStax, All Rights Reserved, Confidential

DSE Studio:

• Based on Zeppelin notebook

• Runs locally; (lightweight)

Web app

• Supports:

-- CQL (and Search)

-- Spark/SQL (w/ Always

on SQL)

-- Gremlin

-- Markdown

• Import/export, w/w-o data

• Content assist (Shift-ENTER)

0000-DTSE-Studio-6210-DU-60-5 © DataStax, All Rights Reserved, Confidential

DSE Studio:

Download, boot

Download from

Academy

./server.sh

0000-DTSE-Studio-6210-DU-60-6 © DataStax, All Rights Reserved, Confidential

DSE Studio: Boot process

# ./server.sh Starting Studio. This may take a few minutes. You will be notified here when Studio is ready. SLF4J: Class path contains multiple SLF4J bindings. SLF4J: Found binding in [jar:file:/opt/studio/lib/log4j-slf4j-impl-2.9.0.jar!/org/slf4j/impl/StaticLogg erBinder.class] SLF4J: Found binding in [jar:file:/opt/studio/tomcat.9091/webapps/api/WEB-INF/lib/log4j-slf4j-impl-

2.9.0.jar!/org/slf4j/impl/StaticLoggerBinder.class] SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation. SLF4J: Actual binding is of type [org.apache.logging.slf4j.Log4jLoggerFactory]

Studio is now running at: http://localhost:9091

NOTE: Studio by default will only be accessible on this machine since it is bound to localhost. Studio is intended to be used as a desktop application. To allow remote connections(which can be a security risk) modify the httpBindAddress setting in configuration.yaml to either a publicly accessible address or 0.0.0.0 Please visit https://docs.datastax.com/en/dse/6.0/dse-dev/datastax_enterprise/studio/configStudio.html for more information on configuration

0000-DTSE-Studio-6210-DU-60-7 © DataStax, All Rights Reserved, Confidential

DSE Studio: First Steps

0000-DTSE-Studio-6210-DU-60-8 © DataStax, All Rights Reserved, Confidential

DSE Studio: Create new (CQL) Notebook

0000-DTSE-Studio-6210-DU-60-9 © DataStax, All Rights Reserved, Confidential

DSE Studio: Language within a Cell

0000-DTSE-Studio-6210-DU-60-10 © DataStax, All Rights Reserved, Confidential

DSE Studio: Running CQL

0000-DTSE-Studio-6210-DU-60-11 © DataStax, All Rights Reserved, Confidential

DSE Studio: Standard

CQL

0000-DTSE-Studio-6210-DU-60-12 © DataStax, All Rights Reserved, Confidential

DSE Studio: Chart

Types

0000-DTSE-Studio-6210-DU-60-13 © DataStax, All Rights Reserved, Confidential

DSE Studio: More Chart Types

0000-DTSE-Studio-6210-DU-60-14 © DataStax, All Rights Reserved, Confidential

DSE Studio: Subject to the underlying DSE

0000-DTSE-Studio-6210-DU-60-15 © DataStax, All Rights Reserved, Confidential

DSE Studio: Subject to the underlying DSE

0000-DTSE-Studio-6210-DU-60-16 © DataStax, All Rights Reserved, Confidential

DSE Studio: Successful Spark/SQL

0000-DTSE-Studio-6210-DU-60-17 © DataStax, All Rights Reserved, Confidential

DSE Studio:

Schema Explorer

0000-DTSE-Studio-6210-DU-60-18 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Studio-6210-DU-60-19 © DataStax, All Rights Reserved, Confidential
