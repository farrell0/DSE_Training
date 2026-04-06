# DSE Analytics: DSEFS

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dsefs. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dsefs.

## Downloads

- [PDF slides](./7560-dsefs.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7560-DU-60%2C%20DSEFS.pptx)

## Converted Slides

## Discussion Unit:

• The goal of this Discussion Unit is to

DSE Analytics configure and use DSEFS.

DSEFS

000-DTSE-Analytics-7560-60-DU-1 © DataStax, All Rights Reserved, Confidential

DSE Analytics; DSEFS, HDFS, NAS,

RDD, Map/Reduce

Discussion Lab:

Matching pairs – Match the

attributes on the right with the

areas on the left

000-DTSE-Analytics-7560-60-DU-2 © DataStax, All Rights Reserved, Confidential

DSE Analytics: HDFS, RDD, DSEFS, M/R, NAS

Core to Spark

Core to Hadoop

POSIX compliant

DSEFS Local to computation

Remote from computation Map/ Reduce

Schema on read

SAN Schema on write

000-DTSE-Analytics-7560-60-DU-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7560-60-DU-4 © DataStax, All Rights Reserved, Confidential

• Staging for import/export

• Intermediate results in a DAG, Workflow DSEFS: What and • Distributing Jars; save work for driver and

Why executor

• Scan heavy workloads

• Unstructured data

• DSE 5.0+ (CFS, 2.0 to 5.1)

• HDFS compatible storage

• Compression (HW level encryption)

• Shared nothing

• Same JVM as DSE Core

• Secure, Local DSE, LDAP, Kerberos, also

TLS/SSL

• Performant; option to disable fsync

000-DTSE-Analytics-7560-60-DU-5 © DataStax, All Rights Reserved, Confidential

DSEFS: Features

• Creating, listing, moving, renaming, deleting files and directories, wildcard

expansion

• Optional password / token authentication and Kerberos authentication in

Spark

• POSIX permissions and file attributes

• Interactive console with access to DSEFS, local file system, and other

HDFS-compatible filesystems

• Querying block locations for efficient data local processing in Spark or

Hadoop

• Replication and block size control

• Transparent optional LZ4 compression

• Utility to check filesystem integrity (fsck)

• Utility to view status of the cluster (e.g. disk usage)

000-DTSE-Analytics-7560-60-DU-6 © DataStax, All Rights Reserved, Confidential

DSEFS: Just DSE Analytics (Apache Spark)

• Checkpointing (DAG)

• Distributing Jars; save work for driver and

executor

• Intermediate results; (Parquet, good choice)

• Starts by default with DSE Analytics

• dse.yaml

• Prefer; separate disk-drive/controller

• Managed as Keyspace; RF and Replication

Strategy

• Also RF per directory, per file

• One per DC. Multiple DCs ?, Different DSEFS

names

000-DTSE-Analytics-7560-60-DU-7 © DataStax, All Rights Reserved, Confidential

DSEFS: Architecture

• No single point of failure;

shared nothing

• Same JVM as DSE Core

000-DTSE-Analytics-7560-60-DU-8 © DataStax, All Rights Reserved, Confidential

DSEFS: Architecture

• Metadata is DSE

Core

• Data-data as

blocks on

DSEFS

000-DTSE-Analytics-7560-60-DU-9 © DataStax, All Rights Reserved, Confidential

DSEFS: Roundtrip using DSE Spark

val rows = sc.textFile(

"file:///opt/stores_db/7545_HelloWorld.csv")

rows.collect().foreach(println)

rows.saveAsTextFile(

"dsefs:///tmp/7545_HelloWorld.csv")

000-DTSE-Analytics-7560-60-DU-10 © DataStax, All Rights Reserved, Confidential

DSEFS: Verify via "dse fs"

# dse fs dsefs dsefs://127.0.0.1:5598/ > ls -l Type Permission Owner Group Length Modified Name dir rwx-wx-wx none none - 2018-07-19 17:09:49-0600 tmp dsefs dsefs://127.0.0.1:5598/ > cd tmp dsefs dsefs://127.0.0.1:5598/tmp/ > ls -l Type Permission Owner Group Length Modified Name dir rwx-wx-wx none none - 2018-07-19 17:09:49-0600 hive

... After job on previous page runs

dsefs dsefs://127.0.0.1:5598/tmp/ > ls -l Type Permission Owner Group Length Modified Name dir rwxrwxrwx none none - 2018-07-19 17:21:54-0600 7545_HelloWorld.csv dir rwx-wx-wx none none - 2018-07-19 17:09:49-0600 hive

000-DTSE-Analytics-7560-60-DU-11 © DataStax, All Rights Reserved, Confidential

DSEFS: Verify via "dse fs"

dsefs dsefs://127.0.0.1:5598/tmp/ > cd 75* dsefs dsefs://127.0.0.1:5598/tmp/7545_HelloWorld.csv/ > ls -l Type Permission Owner Group Length Modified Name file rw-r--r-- none none 0 2018-07-19 17:21:55-0600 _SUCCESS file rw-r--r-- none none 48 2018-07-19 17:21:54-0600 part-00000 file rw-r--r-- none none 15 2018-07-19 17:21:55-0600 part-00001

dsefs dsefs://127.0.0.1:5598/tmp/7545_HelloWorld.csv/ > cat part* 111, Bob, Mary 222, Ted 333, Alice, Bob, Harold 444, Dave, Bob

dsefs dsefs://127.0.0.1:5598/tmp/7545_HelloWorld.csv/ >

000-DTSE-Analytics-7560-60-DU-12 © DataStax, All Rights Reserved, Confidential

DSEFS: Settings, dse.yaml

dsefs_options:

enabled:

keyspace_name: dsefs

work_dir: /var/lib/dsefs

public_port: 5598

private_port: 5599

data_directories:

- dir: /var/lib/dsefs/data

storage_weight: 1.0

min_free_space: 5368709120 # Change to 1024 for dev

" ... DSEFS nodes are either unavailable or low on free space ... "

000-DTSE-Analytics-7560-60-DU-13 © DataStax, All Rights Reserved, Confidential

All of DSE Analytics: Keyspace RF/Strategy

• dse_analytics

• dse_leases

• dsefs Different; 1 DSEFS per DC

• "HiveMetaStore"

• See DSE Core Practice

Lab, 6207/Keyspaces

ALTER KEYSPACE dsefs

WITH REPLICATION = {

'class': 'NetworkTopologyStrategy',

'Analytics': '3'};

000-DTSE-Analytics-7560-60-DU-14 © DataStax, All Rights Reserved, Confidential

• append DSEFS: Nearly • cat

• cd POSIX • chgrp, chmod, chown compliant • cp

• df

• echo

• exit

• fsck

• get

• ls

• mkdir, rmdir, rm [ -r ]

• mv, rename

• put

• pwd, realpath

• stat

• truncate

• umount

000-DTSE-Analytics-7560-60-DU-15 © DataStax, All Rights Reserved, Confidential

DSEFS: REST Interface

curl -L -X PUT 'localhost:5598/webhdfs/v1/fs/a/b/c/d/e?op=MKDIRS'

curl -L -X PUT -T logfile.txt

'127.0.0.1:5598/webhdfs/v1/fs/log?op=CREATE&overwrite=\

true&blocksize=50000&rf=1'

curl -L -X POST logfile.txt \

'localhost:5598/webhdfs/v1/fs/log?op=APPEND'

Or from the DSE Spark shell:

val rdd1 = sc.textFile(

"webhdfs://localhost:5598/webhdfs/v1/fs/log")

000-DTSE-Analytics-7560-60-DU-16 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7560-60-DU-17 © DataStax, All Rights Reserved, Confidential

Additional Detail:

000-DTSE-Analytics-7560-60-DU-18 © DataStax, All Rights © DataStax, All Rights Reserved, Confidential Reserved. Confidential.

Using HDFS

Not part of the DSE system but is part of Hadoop

• Can be used for long term data storage

• Spark is able to connect to any existing HDFS

• Additionally Spark is designed to be file system independent

• Thus Spark can also connect to systems like HBase or S3

000-DTSE-Analytics-7560-60-DU-19 © DataStax, All Rights © DataStax, All Rights Reserved, Confidential Reserved. Confidential.

DSEFS Compared to: HDFS, CFS

Benefits of DSEFS over HDFS Benefits of DSEFS over CFS

No single point of failure No impact on DSE Core

No overhead from compactions, No NameNode commit log writes

No SecondaryNameNode No data density impact

No Zookeeper Immediate deletes, no overhead

000-DTSE-Analytics-7560-60-DU-20 © DataStax, All Rights © DataStax, All Rights Reserved, Confidential Reserved. Confidential.

DSEFS Questions:

• What should the replication factor be on metadata?

• What should be the replication factor on a given file?

• What if the file is a jar needed to run a spark job (dse spark-submit -jars

dsefs://myjob/jars/xyz.jar)?

• Where would you use DSEFS?

• Does DSEFS data count towards data density on a DSE node?

• Why use webhdfs?

000-DTSE-Analytics-7560-60-DU-21 © DataStax, All Rights Reserved, Confidential
