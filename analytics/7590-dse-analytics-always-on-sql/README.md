# DSE Analytics: DSE Analytics, Always On SQL

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, always on sql. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, always on sql.

## Downloads

- [PDF slides](./7590-dse-analytics-always-on-sql.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7590-DU-60%2C%20DSE%20Analytics%2C%20Always%20On%20SQL.pptx)

## Converted Slides

## Discussion Unit:

DSE Analytics, • Discussed briefly, enabled in DSE

Always-On SQL Studio Discussion Unit 6210/6211

• One (two ?) settings in dse.yaml, (AOS)

alwayson_sql_options:

enabled: true

• More settings, more function

000-DTSE-Analytics-7590-60-DU-1 © DataStax, All Rights Reserved, Confidential

DSE Analytics; Spark/SQL, SQL

(thus far)

Discussion Lab:

Discuss-

000-DTSE-Analytics-7590-60-DU-2 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Spark SQL

• Using "dse spark-sql"; How was

your statement executed ? (Did

you see an (n) step progress bar ?)

• What was your fastest return time ?

• What was happening that took a

good portion of that time ?

• Was DSE Studio SQL faster ?

000-DTSE-Analytics-7590-60-DU-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7590-60-DU-4 © DataStax, All Rights Reserved, Confidential

DSE Always-On SQL (AOS):

dse.yaml,

alwayson_sql_options: # Change T|F requires node restart

enabled: true

dse client-tool alwayson-sql start|stop|status|restart|reconfig

Example,

dse client-tool alwayson-sql status // Also host:9077

dse client-tool alwayson-sql stop

dse client-tool alwayson-sql start

dse client-tool alwayson-sql --dc dc-west start

dse client-tool alwayson-sql reconfig

000-DTSE-Analytics-7590-60-DU-5 © DataStax, All Rights Reserved, Confidential

DSE Always-On SQL: reconfig

dse.yaml

reserve_port_wait_time_ms

alwayson_sql_status_check_wait_time_mas

log_dsefs_dir

runtime_max_errors

spark/conf/spark-alwayson-sql.con

50 lines, mostly security

000-DTSE-Analytics-7590-60-DU-6 © DataStax, All Rights Reserved, Confidential

DSE Always-On SQL: What/Why-

Per analytics DC

Aimed at BI tools; Tableau, others

Offers a JDBC/ODBC like interface for that reason

And DSE Studio

Pre-instantiated resource, performance

000-DTSE-Analytics-7590-60-DU-7 © DataStax, All Rights Reserved, Confidential

DSE Always-On SQL: Has evolved with Spark

• 2015 • > 2014 • Catalyst • Shark, SharkServer

-- Tree Manipulation FW -- Hive, Read HiveQL -- Spark streaming -- Read Hadoop formats -- Graphframes -- M/R job atop Spark -- Enable predicate pushdown

-- Support for TPC/DS

• Jobs on Spark FW (RDD, ..)

000-DTSE-Analytics-7590-60-DU-8 © DataStax, All Rights Reserved, Confidential

DSE Always-On

SQL: Recent DSE 5.1 used Spark ThriftServer (HiveServer2)

• Spark Thrift Server, not related to past DSE Thrift, Spark Thrift Server Thrift • thrift.apache.org DSE 6.0 • Fast/lightweight means to

• HA, Node in DC elected to be connection point deliver RPC interface

• Security incompleteness; (CP), failure, new election

runs as single app, single • Driver transparently knows CP user token (id) • SQL syntax, cached to DSEFS (shared) • (No) H/A • Incremental collect() -- No agent auto restart • Uses native CQL comm protocol; async, and -- Data not cached w/ new server notifications agent

• Single, long running app

• Must read Url on Notes page- -- No sharing w/ other

apps, no shared

SparkContext

000-DTSE-Analytics-7590-60-DU-9 © DataStax, All Rights Reserved, Confidential

DSE Always-On SQL: SQL commands

spark-sql> cache table ks_7579.customer;

// Time taken: 10.445 seconds

spark-sql> cache table as select customer_num from ks_7579.customer;

// Time taken: 1.239 seconds

spark-sql> uncache table ks_7579.customer;

// Time taken: 0.158 seconds

spark-sql> clear cache;

// Time taken: 0.004 seconds

Sugar for df.cache

-- DSEFS or local disk as configured

000-DTSE-Analytics-7590-60-DU-10 © DataStax, All Rights Reserved, Confidential

DSE Always-On SQL: SQL commands

spark-sql> select count(*) from ks_7579.customer;

// 28

// Time taken: 9.78 seconds, Fetched 1 row(s)

spark-sql> insert into ks_7579.customer2 select * from ks_7579.customer;

// Time taken: 2.934 seconds

spark-sql> select count(*) from ks_7579.customer2;

// 28

// Time taken: 0.546 seconds, Fetched 1 row(s)

000-DTSE-Analytics-7590-60-DU-11 © DataStax, All Rights Reserved, Confidential

DSE Always-On SQL: SQL commands, Explain

spark-sql> explain select count(*) from ks_7579.customer;

== Physical Plan ==

*HashAggregate(keys=[], functions=[count(1)])

+- Exchange SinglePartition

+- *HashAggregate(keys=[], functions=[partial_count(1)])

+- *Scan org.apache.spark.sql.cassandra.CassandraSourceRelation

ks_7579.customer[] ReadSchema: struct<>

Time taken: 0.156 seconds, Fetched 1 row(s)

000-DTSE-Analytics-7590-60-DU-12 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7590-60-DU-13 © DataStax, All Rights Reserved, Confidential
