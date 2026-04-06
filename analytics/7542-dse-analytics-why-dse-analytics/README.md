# DSE Analytics: DSE Analytics, Why DSE Analytics

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, why dse analytics. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, why dse analytics.

## Downloads

- [PDF slides](./7542-dse-analytics-why-dse-analytics.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7542-DU-60%2C%20DSE%20Analytics%2C%20Why%20DSE%20Analytics.pptx)

## Converted Slides

## Discussion Unit:

Why of Analytics • Understand the Discussion Unit:

Why DSE • Four Primary Functional Areas to DSE Analytics

(Introduction to Analytics) • History of Apache Spark (history of

Apache Hadoop)

• 5 Functional Areas to (DSE Analytics)

• Business Value of DSE Analytics, Use

Cases

000-DTSE-Analytics-7542-60-DU-1 © DataStax, All Rights Reserved, Confidential

DSE Analytics; Hadoop versus

Spark, languages and functions

Discussion Lab:

Matching pairs – Match the

attributes on the right with the

areas on the left

000-DTSE-Analytics-7542-60-DU-2 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Hadoop Distributed Filesystem (HDFS)

versus Spark Computing engine, not a storage

system

Composable API based on functional

programming

Operates on Key/Value (K/V) pairs

K/V classes have to be serializable by

the framework

M/R: Input reader, Mapper, Partitioner,

Comparator, Reducer, Output Writer

RDD, DataFrame/Dataset

Distributed programming model, user

specifies transforms to build up a

directed acyclic graph

000-DTSE-Analytics-7542-60-DU-3 © DataStax, All Rights Reserved, Confidential

Language Adjectives/Terms:

Declarative

Structured Programming

Fluent API

Lazy Evaluation

Lambda

Imperative Programming

Object Oriented awk cat grep

Functional Programming

000-DTSE-Analytics-7542-60-DU-4 © DataStax, All Rights Reserved, Confidential

In Many Languages ..

Function Body (or { } Block), if not named, it is

an anonymous function,

or lambda

( ) Parameters to Function

000-DTSE-Analytics-7542-60-DU-5 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7542-60-DU-6 © DataStax, All Rights Reserved, Confidential

The 4 Primary Functional Areas to DSE

• All 4 primary functional areas

provide query processing The Why

• DSE Analytics Query -- Parallel Query Processing processing Horizontal scaling

Index and High Speed

query -- Batch, Streaming,

processing Iterative

Interactive

000-DTSE-Analytics-7542-60-DU-7 © DataStax, All Rights Reserved, Confidential

DSE Analytics: 5 Major Functional Areas

DataFrames ML Pipelines

Spark Spark SQL Mllib/ML GraphX Streaming

Spark Core

000-DTSE-Analytics-7542-60-DU-8 © DataStax, All Rights Reserved, Confidential

DSE Analytics: What is it-

Enhanced version of Apache Spark

• DSE manages Spark Master and auto restarts without any other third party software

-- Restart of a Master with information on who is Master to whole cluster

-- Restart of any failed workers

• Ability to submit jobs to any Spark nodes, rather than having to know who the master is

• With DSE to Cassandra the data sits on the nodes with Spark , less data shuffling

-- Spark attempts to optimize jobs to pull data on local node primarily

-- In DSE 5.1 and above, both the Master and Worker run in the same JVM as DSE

-- Able to inherit unified DSE security features

• DSE drivers to Cassandra

-- Continuous paging for speed in returning data

-- Integrate DSE Graph with Spark GraphFrames

-- Integration with DSE Search

• Always on SQL Server replacing the non fault tolerant Thrift Server

000-DTSE-Analytics-7542-60-DU-9 © DataStax, All Rights Reserved, Confidential

DSE Analytics: What is it-

Integrated Platform for Advanced Analytics

• An end-to-end, integrated platform; Spark has no persistent data tier

-- One-stop-shop for data ingestion, transformation and analytics (SparkSQL,

MLlib, ML) via Spark integration

• Workload isolation - No data movement between OLTP and OLAP systems

• Transactional data immediately available for analysis

• Drill down from analysis to current transactional data

• Reduce the need for multiple copies of same data

000-DTSE-Analytics-7542-60-DU-10 © DataStax, All Rights Reserved, Confidential

DSE Analytics: What is it-

Integrated Platform for Operational Analytics

• Integrated with DSE

-- Masterless, distributed architecture

-- Multi-Data Center support

-- Multi-model platform

• Inherits all the enterprise-class benefits of DSE:

-- Contextual insights (with Graph capability)

-- Always-on

-- Massively scalable

-- High-performance

-- Ease to use and manage, one less cluster

000-DTSE-Analytics-7542-60-DU-11 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Key Use Cases

DataStax customers use DSE Analytics in the following areas:

• Data Ingestion from streaming sources, with/without transformation/aggregation

• Data Quality – primarily with respect to data ingestion

• ETL – from one internal store to another and from external sources to internal

stores

• Pre-calculated Aggregates – scheduled “mini-batch”

• Machine Learning on Operational Data

• Real-time personalization & recommendation

• Business Intelligence – via ODBC/JDBC connectivity

• Primarily Tableau, working on partnering with additional BI vendors

000-DTSE-Analytics-7542-60-DU-12 © DataStax, All Rights Reserved, Confidential

Objections: Why use OSS Apache Spark

• Different number of Spark nodes than Cassandra nodes

-- In DSE, collocated Spark/Cassandra nodes means 1:1 sizing

-- DSE 5.1+ supports “Spark-only DCs” and “Spark-only Clusters”

• Separate Spark and Cassandra processing to avoid resource contention

-- While Spark can be somewhat controlled, Cassandra is less well behaved

-- The sacrifice is that reads are remote

• Newer version of Spark than is in DSE

-- Largely this is spurious. Most customers can’t point to new feature they

need (but some really can)

-- That said, Spark does not keep bug-fixing old releases

-- There has not been a Spark release past X.Y.2 (e.g., there was no 2.0.3)

-- Spark has performance optimizations to their core in new releases

-- The Catalyst optimizer has been a focus and will continue to be

• Separate/existing customer team for Spark

000-DTSE-Analytics-7542-60-DU-13 © DataStax, All Rights Reserved, Confidential

• DSE Analytics process

architecture

• User Interfaces

• [ The ] Primary Spark API; DSE Analytics RDDs, DataFrames, Dataset

(Apache Spark):

Operational Details

000-DTSE-Analytics-7542-60-DU-14 © DataStax, All Rights Reserved, Confidential

DSE

Analytics:

Process

Architecture

000-DTSE-Analytics-7542-60-DU-15 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Process

Architecture 4

1:M Task/Partition 5 3

2

...

1

000-DTSE-Analytics-7542-60-DU-16 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Process Architecture

000-DTSE-Analytics-7542-60-DU-17 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Process Architecture, (Outlier topics)

• DSE Analytics Streaming;

one executor only, always

on (?)

• Driver can be hosted locally

or remote

• DSE 5.1+, can have

analytics only nodes; no

local data

• For executors, data must be

available via same path on

every node; DSEFS

000-DTSE-Analytics-7542-60-DU-18 © DataStax, All Rights Reserved, Confidential

• dse spark DSE

:quit Analytics: • dse spark-sql UIs quit;

• dse pyspark

quit()

• dse sparkR

(Will fail without R)

• dse spark-submit xxx.jar

Java, Scala , Python, R • http:// (master node) :7080 will automatically find Spark Master • http:// (driver host) :4040 41, 42

• (Other)

000-DTSE-Analytics-7542-60-DU-19 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Resource Math

On the server; dse.yaml, spark- On the client; in code, or ENV

• Subject to server limits env.sh, other

• RAM, Cores, other • Tiered, many, non-trivial

• See Url • RAM, Cores, other

• See Url

000-DTSE-Analytics-7542-60-DU-20 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Programming Model

Advanced Structured Libraries Analytics Streaming & Ecosystem

Structured APIs

Datasets SQL DataFrames

Low Level APIs

Image Source: DataBricks.com RDDs Distributed Variables

Source: https://www.amazon.com/Spark-Definitive-Guide-Processing-Simple/dp/1491912219

000-DTSE-Analytics-7542-60-DU-21 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Programming Model

Image Source: DataBricks.com

000-DTSE-Analytics-7542-60-DU-22 © DataStax, All Rights Reserved, Confidential

• What is Functional Programming

(FP), and Why You Care

DSE Analytics

(Apache Spark):

Functional Programming

000-DTSE-Analytics-7542-60-DU-23 © DataStax, All Rights Reserved, Confidential

val names = List("Bob", "Nancy", "Dirk")

def myUC( Args : List[String] ) : List[String] = {

var myList: List[String] = List() Scala: What does

// this fragment for (s <- Args) {

output ? myList = s.toUpperCase :: myList

}

myList

}

val capNames = myUC(names)

capNames.foreach(println)

000-DTSE-Analytics-7542-60-DU-24 © DataStax, All Rights Reserved, Confidential

val names = List("Bob", "Nancy", "Dirk") Scala: What

do these val capNames = for (e <- names) yield e.toUpperCase

fragments capNames.foreach(println)

output ?

val capNames = names.map(_.toUpperCase)

capNames.foreach(println)

val nums = List(1, 2, 3)

val nums2 = nums.map(_ * 2)

nums2.foreach(println)

000-DTSE-Analytics-7542-60-DU-25 © DataStax, All Rights Reserved, Confidential

Definition of: map()

• Factor out common patterns

• Iterate over List elements

• Term comes from the mathematics

domain

• Things that can be mapped over

are called functors

• Methods of Scala's collections

classes: drop(), filter(), map(),

reduce()

000-DTSE-Analytics-7542-60-DU-26 © DataStax, All Rights Reserved, Confidential

Functional Programming (FP): Why Do You Care ?

• 98% of the examples you seek

to use from books and on

Google, will be FP (you need to

be able to read)

• Knowing FP required to move

from beginner to beyond ...

beginner

• The best way to write parallel Source: https://medium.com/@ cscalfani/so-you-want-to-be-a-functional- and concurrent applications ; programmer-part-1-1f15e387e536

thread safe, no sync issues

000-DTSE-Analytics-7542-60-DU-27 © DataStax, All Rights Reserved, Confidential

Functional Programming (FP): Why Do You Care ?

FP Language Features-

• Immutable data , first class functions, tail call

optimization

FP Programming Techniques-

• Mapping , reducing, pipelining , recursing ,

currying, higher order functions (HOF)

FP Advantages- ... • Easier to parallelize , lazy evaluation , easier to Which test , determinism entity in the Spark PF == ODI + NSE RT is Output pipelining No Side Pure Depends ? Effects Functions on Input Source: https://medium.com/@ cscalfani/so-you-want-to-be-a-functional- programmer-part-1-1f15e387e536 FP is the opposite of imperative programming

000-DTSE-Analytics-7542-60-DU-28 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Intermediate and above level

Functional Programming • FP, and imperative programming styles • FP for transforms, imperative for UI • What Spark is written in; examples, other • Immutability, thread safe, concurrency, out of the box • Rich Java package library

000-DTSE-Analytics-7542-60-DU-29 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Must Reads ?

000-DTSE-Analytics-7542-60-DU-30 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7542-60-DU-31 © DataStax, All Rights Reserved, Confidential

Additional Detail:

000-DTSE-Analytics-7542-60-DU-32 © DataStax, All Rights Reserved, Confidential

History of Apache Spark

A Brief History of Spark-

• Spark was initially started by Matei Zaharia at UC Berkeley's AMPLab in 2009,

and open sourced in 2010 under a BSD license.

• In 2013, the project was donated to the Apache Software Foundation and

switched its license to Apache 2.0. In February 2014, Spark became a Top-

Level Apache Project.

• In November 2014, Spark founder M. Zaharia's company Databricks set a new

world record in large scale sorting using Spark.

• Spark had in excess of 1000 contributors in 2015, making it one of the most

active projects in the Apache Software Foundation and one of the most active

open source big data projects.

000-DTSE-Analytics-7542-60-DU-33 © DataStax, All Rights Reserved, Confidential

History of Apache Spark

Spark was originally developed to address the limitations of MapReduce.

• It is a distributed computing system, utilizing many machines to do a job

• While MapReduce reduces and writes to disk, Spark was developed as a shared memory

system

-- Most work and data being held in memory

-- Spilled over to disk if memory capacity is met

• Because of this Spark is touted as being orders of magnitude faster than MapReduce

• Major speed enhancements came out it

-- 1.6 with solidifying DataFrames

-- 2.0 with solidifying DataSets and Tungsten execution backend

-- 2.2 Structured Streaming

• Easier to program and code

• Can do analytics in real time as well as batch

-- MapReduce is not a real time analytics engine

000-DTSE-Analytics-7542-60-DU-34 © DataStax, All Rights Reserved, Confidential

Spark is New, Fast Moving

Young and a very active open source project

• It has moved fast in the last couple of years

• Version changes coming very quickly

• Major API changes

• It is anticipated that like many open source projects this will slow down and the

API will start becoming more stable

• But for now still very inventive

• This implies DSE may lag a few releases behind

-- 5.1.x DSE comes with Spark 2.0.x

-- 2.1.0 of Spark was already released when 5.1.0 was released

-- 6.0.0 released with the latest, Spark 2.2.x

000-DTSE-Analytics-7542-60-DU-35 © DataStax, All Rights Reserved, Confidential

Spark Cluster Managers: Spark Standalone The Spark Standalone cluster manager is a simple cluster manager available as part of the Spark distribution. It has HA for the master, is resilient to worker failures, has capabilities for managing resources per application, and can run alongside of an existing Hadoop deployment and access HDFS (Hadoop Distributed File System) data. The distribution includes scripts to make it easy to deploy either locally or in the cloud on Amazon EC2. It can run on Linux, Windows, or Mac OSX.

Apache Mesos Apache Mesos, a distributed systems kernel, has HA for masters and slaves, can manage resources per application, and has support for Docker containers. It can run Spark jobs, Hadoop MapReduce, or any other service application. It has API’s for Java, Python, and C++. It can run on Linux or Mac OSX.

Hadoop YARN Hadoop YARN, a distributed computing framework for job scheduling and cluster resource management, has HA for masters and slaves, support for Docker containers in non-secure mode, Linux and Windows container executors in secure mode, and a pluggable scheduler. It can run on Linux and Windows.

Or, Datastax Analytics

Source: http://www.agildata.com/apache-spark-cluster-managers-yarn-mesos-or-standalone/

000-DTSE-Analytics-7542-60-DU-36 © DataStax, All Rights Reserved, Confidential

Useful Links:

• https://spark.apache.org/ • http://spark.apache.org/docs/2.0.2/programming-guide.html • http://spark.apache.org/docs/2.0.2/configuration.html • https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html (not quite there

for DSE 5.1) • https://github.com/datastax/spark-cassandra-connector/tree/master/doc • https://www.youtube.com/watch?v=cKIHRD6kUOc&index=40&list=PLm-EPIkBI3YoiA- 02vufoEj4CgYvIQgIk (Russ!) • https://support.datastax.com/hc/en-us/articles/204939759-Spark-shell-with-SSL-enabled-clusters • http://www.bigsynapse.com/controlling-the-number-of-partitions-in-spark • http://blog.cloudera.com/blog/2015/03/how-to-tune-your-apache-spark-jobs-part-1/ • https://www.dezyre.com/article/top-10-machine-learning-algorithms/202 • http://c2fo.io/c2fo/spark/aws/emr/2016/07/06/apache-spark-config-cheatsheet/ • http://www.sparktutorials.net/analyzing-flight-data:-a-gentle-introduction-to-graphx-in-spark

000-DTSE-Analytics-7542-60-DU-37 © DataStax, All Rights Reserved, Confidential

Useful Links:

• https://databricks.com/blog/2016/10/03/voice-from-cern-apache-spark-2-0-performance- improvements-investigated-with-flame-graphs.html • https://databricks.com/blog/2016/05/23/apache-spark-as-a-compiler-joining-a-billion-rows-per- second-on-a-laptop.html • https://www.gitbook.com/book/jaceklaskowski/mastering-apache-spark/details • https://www.analyticsvidhya.com/blog/2015/07/difference-machine-learning-statistical-modeling/ • http://www.doanduyhai.com/blog/?p=2325 (Setting up Zeppelin) • https://databricks.com/blog/2017/10/19/introducing-natural-language-processing-library-apache- spark.html • https://databricks.com/blog/2017/08/31/cost-based-optimizer-in-apache-spark-2-2.html • http://www.stratio.com/blog/optimizing-spark-streaming-applications-apache-kafka/ • https://techvidvan.com/tutorials/apache-spark-performance-tuning/ • http://shop.oreilly.com/product/0636920046967.do (High Performance Spark Book) • https://www.gitbook.com/book/jaceklaskowski/mastering-apache-spark/details (Book)

000-DTSE-Analytics-7542-60-DU-38 © DataStax, All Rights Reserved, Confidential
