# DSE Core: Bulk Loader

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Core curriculum and need help with bulk loader. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Core track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around bulk loader.

## Downloads

- [PDF slides](./6232-bulk-loader.pdf)
- [Original PowerPoint](../000-DTSE-BulkLoader-6232-DU-60%2C%20Bulk%20Loader.pptx)

## Converted Slides

## Discussion Unit:

DSE Bulk Loader Introduce the DSE Bulk Loader

0000-DTSE-BulkLoader-6244-DU-60-1 © DataStax, All Rights Reserved, Confidential

Discussion Lab:

Bulk Loader versus Custom

Client Side Program-

0000-DTSE-BulkLoader-6244-DU-60-2 © DataStax, All Rights Reserved, Confidential

Discussion Lab: Bulk Load, or Custom Program ?

PreparedStatement

Parser

Multi-statement

Q Optimizer Transaction/Batch

(Memory management) Q Processor

(Restart on failure)

(Run time) (Issues w/ data)

Client Server

0000-DTSE-BulkLoader-6244-DU-60-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

0000-DTSE-BulkLoader-6244-DU-60-4 © DataStax, All Rights Reserved, Confidential

DSBulk: Overview

• Load, unload

• CSV, JSON

• Linux, Windows

• File, directories, stdin/stdout, Web Url

• 2-3 times faster than CQLSH/COPY

• Secure, Kerberos, other

• Configurable data parsing

• Command line

• Tunable

0000-DTSE-BulkLoader-6244-DU-60-5 © DataStax, All Rights Reserved, Confidential

DSBulk: One of

many loaders

0000-DTSE-BulkLoader-6244-DU-60-6 © DataStax, All Rights Reserved, Confidential

DSBulk: Loading Workflow

0000-DTSE-BulkLoader-6244-DU-60-7 © DataStax, All Rights Reserved, Confidential

DSBulk: Unloading Workflow

0000-DTSE-BulkLoader-6244-DU-60-8 © DataStax, All Rights Reserved, Confidential

DSBulk: Simple Loading/Unloading

dsbulk unload -url myData.csv -k ks1 -t table1

dsbulk load -url export.csv -k ks1 -t table1 -h \

'10.200.1.3, 10.200.1.4' -header true

dsbulk load -url https://svr/data/export.csv -k ks1 -t table1 -h \

'10.200.1.3, 10.200.1.4' -port 9876

cat abc.csv | dsbulk load -url stdin:/ -k ks1 -t table1

0000-DTSE-BulkLoader-6244-DU-60-9 © DataStax, All Rights Reserved, Confidential

DSBulk:

############ MyConfFile.conf ############ Load/Unload

w/ config file dsbulk {

# The name of the connector to use

connector.name = "csv"

# CSV field delimiter

dsbulk load -f MyConfFile.conf \ connector.csv.delimiter = "|"

# The keyspace to connect to -url export.csv -k ks1 -t table1

schema.keyspace = "myKeyspace"

# The table to connect to

schema.table = "myTable"

# The field-to-column mapping

schema.mapping = "0=name, 1=age, 2=email"

}

0000-DTSE-BulkLoader-6244-DU-60-10 © DataStax, All Rights Reserved, Confidential

0000-DTSE-BulkLoader-6244-DU-60-11 © DataStax, All Rights Reserved, Confidential
