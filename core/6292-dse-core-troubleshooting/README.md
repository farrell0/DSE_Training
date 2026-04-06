# DSE Core: DSE Core, Troubleshooting

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Core curriculum and need help with dse core, troubleshooting. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Core track focuses on troubleshooting methods and operational diagnostics. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse core, troubleshooting.

## Downloads

- [PDF slides](./6292-dse-core-troubleshooting.pdf)
- [Original PowerPoint](../000-DTSE-Core-6292-DU-60%2C%20DSE%20Core%2C%20Troubleshooting.pptx)

## Converted Slides

## Discussion Unit:

Introduce DSE Core Troubleshooting Discussion Unit:

DSE Core,

Troubleshooting

0000-DTSE-Core-6292-DU-60-1 © DataStax, All Rights Reserved, Confidential

DSE Core Troubleshooting, Sources

of Error, Name 2

Discussion Lab:

Name 2

0000-DTSE-Core-6292-DU-60-2 © DataStax, All Rights Reserved, Confidential

Discussion Lab: Sources of (Trouble)

config files

OS/Network

You already know a lot- application

code

List 2 sources of

error/trouble per area on CQL the left .. data model

0000-DTSE-Core-6292-DU-60-3 © DataStax, All Rights Reserved, Confidential

DSE Core Troubleshooting, Sources

of Error, Name 2

End of

Discussion Lab:

0000-DTSE-Core-6292-DU-60-4 © DataStax, All Rights Reserved, Confidential

Troubleshooting: Examples

Complaint : Cluster is not consistent

Configuration files differ

• Manual change instead of repository

• Forget to change on one node

• Typos on some nodes not others

• Not version controlled so can’t tell who did what

Bad networking

• Check network stats

• May require a change to phi conviction

0000-DTSE-Core-6292-DU-60-5 © DataStax, All Rights Reserved, Confidential

Troubleshooting: Examples

Complaint : reads/writes are slow

Using spinning disks and have all paths on the same disk

• Break each operation (commit logs, data, etc) to different disks

-- This can even be helpful for SSD’s but not near the drastic change

-- NO SAN, NAS, SAMBA or attached storage

Lots of tombstones (reads)

Writing large blocks of data

• May be dependent on network/disk speed

-- General physics

Over Allocation of JVM memory (reads)

• Not allowing any memory for page cache

0000-DTSE-Core-6292-DU-60-6 © DataStax, All Rights Reserved, Confidential

Troubleshooting: Examples

Compaction or repairs are eating all resources

• Are compaction strategies correct?

• May need more memory or CPU or both

-- Could be hardware limitations, do they follow the

sizing guide according to workload

Wrong sort order for clustering columns

• Have to read all the partition on the system then pull

data from bottom of CC rather than reading the top and

stopping

0000-DTSE-Core-6292-DU-60-7 © DataStax, All Rights Reserved, Confidential

Troubleshooting: Expert Level

• Every setting in every configuration file; identifiers,

tunables, capacities

-- Is each setting too high/low, What (nodetool),

other to confirm

• Read DSE Jiras; a lot of data is already known

• Meet with significant customers; what standards do

they adopt and why

• Solid engineering; decomposition, change one

variable at a time

0000-DTSE-Core-6292-DU-60-8 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Core-6292-DU-60-9 © DataStax, All Rights Reserved, Confidential
