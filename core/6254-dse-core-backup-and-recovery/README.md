# DSE Core: DSE Core, Backup and Recovery

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Core curriculum and need help with dse core, backup and recovery. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Core track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse core, backup and recovery.

## Downloads

- [PDF slides](./6254-dse-core-backup-and-recovery.pdf)
- [Original PowerPoint](../000-DTSE-Core-6254-DU-60%2C%20DSE%20Core%2C%20Backup%20and%20Recovery.pptx)

## Converted Slides

## Discussion Unit:

Introduce one means to DSE Backup

and Recovery

DSE Core Backup and

Recovery

0000-DTSE-Core-6254-DU-60-1 © DataStax, All Rights Reserved, Confidential

Discussion Lab:

List Why ? (You might

restore when ________ ?) Source: www.dilbert.com

0000-DTSE-Core-6254-DU-60-2 © DataStax, All Rights Reserved, Confidential

List Use Cases: You might restore when ______ ?

1.

2.

3.

4.

Source: https://www.pinterest.com/pin/16958936066982309/

0000-DTSE-Core-6254-DU-60-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

0000-DTSE-Core-6254-DU-60-4 © DataStax, All Rights Reserved, Confidential

DSE: Backup and Restore

node 0

• Ops Center Backup Server,

including to S3 DSE Cluster • sstabledump

• snapshots node node 2 • Other 1

And what about consistency on restore ?

0000-DTSE-Core-6254-DU-60-5 © DataStax, All Rights Reserved, Confidential

Review of

cassandra.yaml Runtime- data_file_directories:

- /opt/dse/node1/data/data

cd /opt/dse/node1/data/data

ls -l What are drwxr-xr-x 4 root root 4096 Jul 1 11:59 dse_leases these ? drwxr-xr-x 3 root root 4096 Jul 1 11:59 dse_perf

drwxr-xr-x 5 root root 4096 Jul 1 11:58 dse_security

drwxr-xr-x 3 root root 4096 Jul 1 11:59 dse_system

drwxr-xr-x 3 root root 4096 Jul 1 11:59 dse_system_local

drwxr-xr-x 3 root root 4096 Jul 1 11:59 solr_admin

drwxr-xr-x 18 root root 4096 Jul 1 11:58 system

drwxr-xr-x 5 root root 4096 Jul 1 11:58 system_auth

drwxr-xr-x 7 root root 4096 Jul 1 11:58 system_distributed

drwxr-xr-x 12 root root 4096 Jul 1 11:58 system_schema

drwxr-xr-x 4 root root 4096 Jul 1 11:58 system_traces

0000-DTSE-Core-6254-DU-60-6 © DataStax, All Rights Reserved, Confidential

Make a Keyspace/Table (cust_orders) ..

...

drwxr-xr-x 3 root root 4096 Jul 1 11:59 dse_system_local

drwxr-xr-x 3 root root 4096 Jul 1 11:59 ks_6254

drwxr-xr-x 3 root root 4096 Jul 1 11:59 solr_admin

...

cd ks_6254

ls -l

drwxr-xr-x 3 root root 4096 Jul 1 11:59 cust_orders- 8eda10 ...

Why the cd cust* UUID ? ls -l

drwxr-xr-x 2 root root 4096 Jul 1 11:59 backups

cd back*

ls -l

(All above just empty directories)

0000-DTSE-Core-6254-DU-60-7 © DataStax, All Rights Reserved, Confidential

Take a snapshot

nodetool cleanup ks_6254

nodetool snapshot -t ks_6254-snap1 ks_6254

Requested creating snapshot(s) for [ks_6254] with

snapshot name [ks_6254-snap1] and options {skipFlush=false}

Snapshot directory: ks_6254-snap1

0000-DTSE-Core-6254-DU-60-8 © DataStax, All Rights Reserved, Confidential

Contents of keyspace data directory

pwd /opt/dse/node1/data/data/ks_6254/cust_orders- 8eda10d17d5811e8839b2baf872cd95b

ls -l -rw-r--r-- 2 root root 47 Jul 1 12:04 aa-1-bti-CompressionInfo.db -rw-r--r-- 2 root root 135 Jul 1 12:04 aa-1-bti-Data.db -rw-r--r-- 2 root root 10 Jul 1 12:04 aa-1-bti-Digest.crc32 -rw-r--r-- 2 root root 16 Jul 1 12:04 aa-1-bti-Filter.db -rw-r--r-- 2 root root 73 Jul 1 12:04 aa-1-bti-Partitions.db -rw-r--r-- 2 root root 0 Jul 1 12:04 aa-1-bti-Rows.db -rw-r--r-- 2 root root 4782 Jul 1 12:04 aa-1-bti-Statistics.db -rw-r--r-- 2 root root 94 Jul 1 12:04 aa-1-bti-TOC.txt drwxr-xr-x 2 root root 4096 Jul 1 11:59 backups drwxr-xr-x 3 root root 4096 Jul 1 12:04 snapshots

0000-DTSE-Core-6254-DU-60-9 © DataStax, All Rights Reserved, Confidential

Contents of snapshot directory

cd snapshots ls -l drwxr-xr-x 2 root root 4096 Jul 1 12:04 ks_6254-snap1 cd ks* ls -l -rw-r--r-- 2 root root 47 Jul 1 12:04 aa-1-bti-CompressionInfo.db -rw-r--r-- 2 root root 135 Jul 1 12:04 aa-1-bti-Data.db -rw-r--r-- 2 root root 10 Jul 1 12:04 aa-1-bti-Digest.crc32 -rw-r--r-- 2 root root 16 Jul 1 12:04 aa-1-bti-Filter.db -rw-r--r-- 2 root root 73 Jul 1 12:04 aa-1-bti-Partitions.db -rw-r--r-- 2 root root 0 Jul 1 12:04 aa-1-bti-Rows.db -rw-r--r-- 2 root root 4782 Jul 1 12:04 aa-1-bti-Statistics.db -rw-r--r-- 2 root root 94 Jul 1 12:04 aa-1-bti-TOC.txt -rw-r--r-- 1 root root 31 Jul 1 12:04 manifest.json -rw-r--r-- 1 root root 942 Jul 1 12:04 schema.cql

0000-DTSE-Core-6254-DU-60-10 © DataStax, All Rights Reserved, Confidential

Truncate table ..

cqlsh> truncate table ks_6254.cust_orders; cqlsh> selec * from ks_6254.cust_orders; (0 rows)

pwd /opt/dse/node1/data/data/ks_6254/cust_orders- \ 8eda10d17d5811e8839b2baf872cd95b/snapshots

ls -l drwxr-xr-x 2 root root 4096 Jul 1 12:04 ks_6254-snap1 drwxr-xr-x 2 root root 4096 Jul 1 12:11 truncated-1530468681275-cust_orders

nodetool clearsnapshot --all What is Or, snapshot name this ?

(Don't do this now.)

0000-DTSE-Core-6254-DU-60-11 © DataStax, All Rights Reserved, Confidential

From snapshot can ..

Can restore to new cluster; see Url on Notes page

Can restore to original cluster,

cp

/opt/dse/node1/data/data/ks_6254/cust_orders-

8eda10d17d5811e8839b2baf872cd95b/snapshots/ks_6254-snap1/* \

/opt/dse/node1/data/data/ks_6254/cust_orders-8eda10d17d5811e8839b2baf872cd95b

cp source destination

cp snapshot_dir /* data_dir

0000-DTSE-Core-6254-DU-60-12 © DataStax, All Rights Reserved, Confidential

nodetool refresh, Check results

nodetool refresh ks_6254 cust_orders

cqlsh:ks_6254> select * from cust_orders;

region | cust_name | ord_num | other

--------+-----------+---------+---------------

NA | SEARS | 101 | Shoes, Washer

NA | SEARS | 102 | Oranges

EMEA | IKEA | 101 | Shoes

NA | MACYS | 101 | Dress, Tie

(4 rows)

0000-DTSE-Core-6254-DU-60-13 © DataStax, All Rights Reserved, Confidential

What about multi-node ?

Same exact procedure, run on each node

concurrently

By the nature of the snapshots (each taken

milliseconds/seconds apart), data is

restored to 'eventual consistency'

DSE runtime will create a consistent result

0000-DTSE-Core-6254-DU-60-14 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Core-6254-DU-60-15 © DataStax, All Rights Reserved, Confidential
