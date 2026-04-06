# DSE Core: DSE Core, JMX

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Core curriculum and need help with dse core, jmx. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Core track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse core, jmx.

## Downloads

- [PDF slides](./6230-dse-core-jmx.pdf)
- [Original PowerPoint](../000-DTSE-Core-6230-DU-60%2C%20DSE%20Core%2C%20JMX.pptx)

## Converted Slides

## Discussion Unit:

Introduce DSE JMX Discussion Unit:

• What does DSE Core JMX offer DSE Core, JMX, What • Why use DSE Core JMX and Why

0000-DTSE-Core-6230-DU-60-1 © DataStax, All Rights Reserved, Confidential

DSE Core JMX, DSE

(Interfaces/Utilities)

Discussion Lab:

Matching pairs – Match the

attributes on the right with the

areas on the left

0000-DTSE-Core-6230-DU-60-2 © DataStax, All Rights Reserved, Confidential

Discussion Lab: Which uses JMX

CQLSH

DSE Studio

Ops Ctr UI to Op Ctr Agent JMX

Ops Ctr Agent to DSE Node

nodetool

DSBulk Loader not-JMX

DSE Java Client Driver

dsetool

0000-DTSE-Core-6230-DU-60-3 © DataStax, All Rights Reserved, Confidential

DSE Core JMX, DSE

(Interfaces/Utilities)

End of

Discussion Lab:

0000-DTSE-Core-6230-DU-60-4 © DataStax, All Rights Reserved, Confidential

Any Server Admin Communication Options-

Is the server Java based ?

• Out of the box management of the

JVM

• Pluggable/standard to most

management agents, solutions

• References many existing Java

interfaces; JNDI, others

• Standard NetBeans IDE interface

• Many existing clients

(others)

0000-DTSE-Core-6230-DU-60-5 © DataStax, All Rights Reserved, Confidential

Getting (JMX like) data from DSE-

• DSE Ops Ctr; Web, GUI

• nodetool; reports on one

node, command line, ASCII

text

• dsetool

• CQL/System tables; Global

(cluster wide view)

• JMX

-- Programmatic,

customizable

-- Default install is local only,

easily remote (security) 0000-DTSE-Core-6230-DU-60-6 © DataStax, All Rights Reserved, Confidential

JMX, MBeans

• JMX: Java Management Extensions,

standard way to manage a Java

application

• Mbeans: Management Beans

-- Provided by the application

-- Attributes, can get() or set()

-- Operations, can invoke

-- Read and write

• Many client programs

0000-DTSE-Core-6230-DU-60-7 © DataStax, All Rights Reserved, Confidential

JMX Clients: (many)

• nodetool, 80+ options, but formatted,

documented, supported

• nodetool sjk

• JConsole

-- In Java SDK since 1.5

-- GUI, graphs too

• mx4j, JMX via Http

• Jolokia, JMX via Http/JSON

• jmxsh, command line (REPL)

• jmxterm, command line

• VisualVM

0000-DTSE-Core-6230-DU-60-8 © DataStax, All Rights Reserved, Confidential

Securing (DSE) JMX-

• Via Ops Center

• Or Manually

• Super important

-- Consider mandatory

for production

-- And when allowing

remote clients

0000-DTSE-Core-6230-DU-60-9 © DataStax, All Rights Reserved, Confidential

Why Secure JMX ?

0000-DTSE-Core-6230-DU-60-10 © DataStax, All Rights Reserved, Confidential

Using JConsole:

jconsole

localhost:7100

• 6 TABs

• Read/write, graphs

• MBeans TAB most

expansive

0000-DTSE-Core-6230-DU-60-11 © DataStax, All Rights Reserved, Confidential

• org.apache.cassandra.db DSE MBeans

caching, table metrics, compaction, ..

• org.apache.cassandra.internal

internal server operations; gossip, hinted

handoff, ..

• org.apache.cassandra.metrics

client read/write request latencies, Bloom

filter false positives, ..

• org.apache.cassandra.net

inter-node comm; StreamingService,

MessagingService, FailureDetector , ..

• org.apache.cassandra.request

Tasks related to; read, write, replication, ..

• org.apache.cassandra.service

Data about; node, ring, tokens, snapshots, ..

0000-DTSE-Core-6230-DU-60-12 © DataStax, All Rights Reserved, Confidential

JConsole/

MBean

Examples:

Tombstones

Higher ratio is worse

0000-DTSE-Core-6230-DU-60-13 © DataStax, All Rights Reserved, Confidential

JConsole/

MBean

Examples:

Compaction

Throttling,

MaximumCompactor

Threads

CoreCompactorThre

ads

0000-DTSE-Core-6230-DU-60-14 © DataStax, All Rights Reserved, Confidential

JConsole/

MBean

Examples:

Hinted

Handoff

3 Hours by default, in

milliseconds

MaxHintsInProgress

0000-DTSE-Core-6230-DU-60-15 © DataStax, All Rights Reserved, Confidential

JConsole/

MBean

Examples:

(Time outs)

RangeRpcTimeout

(range queries)

ReadpcTimeout

(single read op)

RpcTimeout

(misc inter-node ops)

WriteRpcTimeout

(write ops)

TruncateRpcTimeout

(truncates)

0000-DTSE-Core-6230-DU-60-16 © DataStax, All Rights Reserved, Confidential

But really: Use nodetool

• nodetool info

Heap and off heap memory, key cache hit

rate

• nodetool compactionstats

Status, volume, in-flight

• nodetool tablestats

Index summary usage, memtable usage,

read/write latency, partition size,

tombstones per read

• nodetool tablehistograms

Table access read/write latencies Source: https://www.pecheur.com/en/ie/buy-node-tool-stonfo-64402.html • nodetool proxyhistograms

Network read/write latencies

0000-DTSE-Core-6230-DU-60-17 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Core-6230-DU-60-18 © DataStax, All Rights Reserved, Confidential
