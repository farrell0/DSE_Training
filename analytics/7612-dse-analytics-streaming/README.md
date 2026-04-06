# DSE Analytics: DSE Analytics, Streaming

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, streaming. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the runtime model and practical usage patterns. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, streaming.

## Downloads

- [PDF slides](./7612-dse-analytics-streaming.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7612-DU-60%2C%20DSE%20Analytics%2C%20Streaming.pptx)

## Converted Slides

## Discussion Unit:

• Streaming use cases

• Blocking operators

• Streaming sources DSE Analytics

• Reliable receivers

Streaming, Streaming • Spark 2.0; production ready, RDD

Analytics • Spark 2.2; DataFrames, Datasets,

windows, other

• Stateful, stateless transforms

• Window functions

• Window sizing

• Examples

• Writing

000-DTSE-Analytics-7602-60-DU-1 © DataStax, All Rights Reserved, Confidential

Attributes of Streaming, Streaming

Analytics

Discussion Lab:

Matching pairs – Match the

attributes on the right with

the areas on the left

000-DTSE-Analytics-7602-60-DU-2 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Streaming, stdout/stderr (logs) stream from

Not-streaming 100,000 servers, analyzed to correlate

dependencies; will server-A issue

impact server-B ?

Customer on the 800 number routed

to specific customer service agent

based on known conditions-

1200+ sensors on airplane, 4TB of

data from 4 hour flight, monitored to

predict failure before it happens

Inventory nearly gone, raise price

before next price quote

Flow rate sensors on stream, it's

raining hard; will it flood ?

000-DTSE-Analytics-7602-60-DU-3 © DataStax, All Rights Reserved, Confidential

SQL SELECT Clauses-

SELECT

o.order_num,

sum (i.total_price) price

FROM orders o, items i

Describe the clauses ? JOINING Which are blocking ? o.order_num = i.order_num

WHERE o.order_date > '01/01/89' (What is blocking ?) AND o.customer_num > 110

GROUP BY 1

ORDER BY 2

INTO TEMP my_tempTable;

000-DTSE-Analytics-7570-60-DU-4 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7602-60-DU-5 © DataStax, All Rights Reserved, Confidential

DSE Analytics: 5 Major Functional Areas

DataFrames ML Pipelines

Spark Spark SQL Mllib/ML GraphX Streaming

Spark Core

Image Source: DataBricks.com

000-DTSE-Analytics-7602-60-DU-6 © DataStax, All Rights Reserved, Confidential

DSE Analytics/Streaming: Where to Use

Streaming is often utilized in a DSE deployment

• Monitor and act upon data as it is sent to DSE

• Always on query, versus polling

DSE Analytics Streaming sources:

• Kafka, ZeroMQ, MQTT

• JMS systems like MessageQ, ActiveMQ

• Twitter feeds

• Stock feeds

• CDC from other systems

• HDFS, DSEFS, S3

• Flume Receiver Reliability: ACK/no- • TCP sockets ACK, data loss is possible

• (Other)

000-DTSE-Analytics-7602-60-DU-7 © DataStax, All Rights Reserved, Confidential

DSE Analytics/Streaming: History

Spark 2.0 (DSE 5.1), Streaming 'production ready'

• RDD based, Dstreams (discretized)

• Micro batches, each being an RDD

• Fewer transforms (yes join, union; no intersect, .. )

• Highest number of articles, examples

Spark 2.2 (DSE 6.0)

• DataFrame, Dataset

• Down to 1ms batch size

• Catalyst optimizer

• Automatic checkpointing

• State management automatic

• SQL access

000-DTSE-Analytics-7602-60-DU-8 © DataStax, All Rights Reserved, Confidential

DSE

Analytics:

Streaming

000-DTSE-Analytics-7602-60-DU-9 © DataStax, All Rights Reserved, Confidential

DSE Analytics:

Streaming

000-DTSE-Analytics-7602-60-DU-10 © DataStax, All Rights Reserved, Confidential

DSE Analytics,

Streaming

Stateless Transforms

000-DTSE-Analytics-7602-60-DU-11 © DataStax, All Rights Reserved, Confidential

Spark 2+, RDDs: DStream, Unary, Transform

Transformation Description

New DStream, apply f() to elements of source Dstream, filter(f) return where true

map(f) New DStream, apply f() to each element, 1:1 input/output

flatMap(f) New DStream, apply f(), 1:M input/output

New DStream, single element, number of elements in count() source DStream

New DStream, count each distinct value in source, n == countByValue(n) numTasks

000-DTSE-Analytics-7602-60-DU-12 © DataStax, All Rights Reserved, Confidential

Spark 2+, RDDs: DStream, Unary, Transform

Transformation Description

New DStream, produce single element which is aggregate reduce(f) from source DStream

New DStream, similar to union(oRDD), both DS must union(oDS) agree on time

New DStream, similar to foreach(), apply f() to every RDD transform(f) in source DStream

Binary version of above. Both DStreams must agree on transformWith(oDS, f) time

000-DTSE-Analytics-7602-60-DU-13 © DataStax, All Rights Reserved, Confidential

Spark 2+, Pair RDDs: DStream, Unary, Transforms

Transformation Description

New DStream, f(), each element of pair RDD, known to mapValues(f) preserve key, 1:1

flatMapValues(f) Similar to above, 1:M

reduceByKey(f [,n]) Aggregate function f(), n == num tasks

Aggregate, no custom function, n == num tasks groupByKey(n)

Complex; combiner and merge f()'s, also merge combineByKey( .. ) combiners, can be written with multiples of above

000-DTSE-Analytics-7602-60-DU-14 © DataStax, All Rights Reserved, Confidential

Spark 2+, Pair RDDs: DStream, Binary, Transforms

Transformation Description

cogroup(oDS [,n])) New DStream, similar to groupByKey()

join(oDS [,n]) New Dstream, similar to join()

leftOuterJoin( .. ) Left outer

Right outer rightOuterJoin( .. )

** Each above: each participant must agree on time

000-DTSE-Analytics-7602-60-DU-15 © DataStax, All Rights Reserved, Confidential

DSE Analytics,

Streaming

Stateful Transforms

000-DTSE-Analytics-7602-60-DU-16 © DataStax, All Rights Reserved, Confidential

Spark 2+, RDDs: DStream, Unary, w/ State

Transformation Description

New "state" DStream formed, apply f() on each key updateStateByKey(f [,n]) of source RDD, n == num tasks

** Above: must enable checkpointing

000-DTSE-Analytics-7602-60-DU-17 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Windows, Slide or Tumble

000-DTSE-Analytics-7602-60-DU-18 © DataStax, All Rights Reserved, Confidential

Spark 2+, RDDs: DStream, Window Transforms

Transformation Description

New DStream, combine all windowed batches from source window(l, [i]) DS, length, slideInterval

countByWindow(l [,i]) New DStream, Returns single element, count

countByWindowAnd New DStream, Count for each distinct element in source DS Value(l, i [,n])

New DStream, apply f() to each element in source DS, reduceByWindow(f, l ,i) aggregate

Similar to above, second function to subtract, Ie., running reduceByWindow( .. ) average

000-DTSE-Analytics-7602-60-DU-19 © DataStax, All Rights Reserved, Confidential

Spark 2+, Pair RDDs: DStream, Window Transforms

Transformation Description

Similar to reduceByKey, Pair RDD, additive reduceByKeyAnd Window( .. )

reduceByKeyAnd Similar to above, add and subtract Window( .. )

groupByKeyAnd Aggregate, no function Window( .. )

000-DTSE-Analytics-7602-60-DU-20 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Window Length

Window Length

• Minute scale window length reasonable

• Hour scale not recommended

• (Totals/Aggregates) okay

Window Sliding Interval

• Per application requirements

000-DTSE-Analytics-7602-60-DU-21 © DataStax, All Rights Reserved, Confidential

DSE Analytics,

Examples

000-DTSE-Analytics-7602-60-DU-22 © DataStax, All Rights Reserved, Confidential

Example 1: now now now is the time for all good persons

keysspaces can span what? Stateless, Word

------------------------------------------- Count Time: 1533397030000 ms ------------------------------------------- (persons,1) (is,1) (,3) (now,3) (all,1) • Sample input (good,1) (for,1) • Sample output (time,1) (the,1) ------------------------------------------- • Second terminal, Time: 1533397040000 ms nc –lk 9999 ------------------------------------------- (can,1) (span,1) (keysspaces,1) (what?,1)

000-DTSE-Analytics-7602-60-DU-23 © DataStax, All Rights Reserved, Confidential

Example 1:

Stateless, Word package com.datastax.enablement.bootcamp

Count

// Spark Core

import org.apache.spark.{SparkConf, SparkContext}

import org.apache.spark.SparkContext._

// Spark streaming

import org.apache.spark.streaming._

import org.apache.spark.streaming.StreamingContext._

// DSE Spark Cassandra Connector

import com.datastax.spark.connector._

import com.datastax.spark.connector.streaming._

000-DTSE-Analytics-7602-60-DU-24 © DataStax, All Rights Reserved, Confidential

Example 1:

Stateless, Word

object App { Count

def main(args: Array[String]) {

val conf = new SparkConf(true).

setAppName("My App").

setMaster("dse://127.0.0.1?").

set("spark.cleaner.ttl", "3600")

val ssc = new StreamingContext(conf, Seconds(10))

val stream = ssc.socketTextStream("127.0.0.1", 9999)

000-DTSE-Analytics-7602-60-DU-25 © DataStax, All Rights Reserved, Confidential

Example 1:

Stateless, Word

Count

stream. flatMap (r => r.split(" ") ).

map(t => (t, 1)) .

reduceByKey(_ + _) .

print()

ssc.start()

ssc.awaitTermination()

}

000-DTSE-Analytics-7602-60-DU-26 © DataStax, All Rights Reserved, Confidential

Example 2:

Stateless,

IOT, Apache Http Web server reduceByCount()

10.14.246.11

122.93.102.53 - - [25/Oct/2011:01:41:00 -0500]

"GET /download/download6.zip HTTP/1.1" 200 3067

"-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; \

rv:1.9.0.19) Gecko/2010031422 Firefox/3.0.19"

• Sample input

000-DTSE-Analytics-7602-60-DU-27 © DataStax, All Rights Reserved, Confidential

Example 2: ------------------------------------------- Time: 1533397460000 ms Stateless, ------------------------------------------- (10.14.246.11,2) reduceByCount() (10.14.246.12,7) (10.14.246.10,1)

------------------------------------------- Time: 1533397470000 ms ------------------------------------------- (10.14.246.11,3) (10.14.246.13,3) • Sample output (10.14.246.12,4)

------------------------------------------- Time: 1533397480000 ms ------------------------------------------- (10.14.246.11,2) (10.14.246.12,8)

000-DTSE-Analytics-7602-60-DU-28 © DataStax, All Rights Reserved, Confidential

Example 2: #!/usr/bin/bash

Stateless, l_cntr1=0 l_cntr2=0 reduceByCount()

function slow_cat() { while read do [ "$l_cntr1" -ge 10 ] && { sleep 10 (>&2 echo " Loop Counter (10 rows output): "${l_cntr2}) l_cntr1=0 } # ((++l_cntr1)) ((++l_cntr2)) • Signal generator # echo "$REPLY" done }

cat 02_WebLogAll.txt | slow_cat | nc -lk 9999

000-DTSE-Analytics-7602-60-DU-29 © DataStax, All Rights Reserved, Confidential

Example 2:

Stateless, package com.datastax.enablement.bootcamp reduceByCount()

// Spark Core

import org.apache.spark.{SparkConf, SparkContext}

import org.apache.spark.SparkContext._

// Spark Streaming

import org.apache.spark.streaming._

import org.apache.spark.streaming.StreamingContext._

// DSE Spark Cassandra Connector

import com.datastax.spark.connector._

import com.datastax.spark.connector.streaming._

000-DTSE-Analytics-7602-60-DU-30 © DataStax, All Rights Reserved, Confidential

Example 2:

Stateless, object App {

reduceByCount()

def main(args: Array[String]) {

// This area has changed alot since 5.x.

//

// Code below tested and works on 6.0

val conf = new SparkConf(true).

setAppName("My App").

setMaster("dse://127.0.0.1?").

set("spark.cleaner.ttl", "3600")

val ssc = new StreamingContext(conf, Seconds(10))

val stream = ssc.socketTextStream("127.0.0.1", 9999)

000-DTSE-Analytics-7602-60-DU-31 © DataStax, All Rights Reserved, Confidential

Example 2:

Stateless, stream.map (r => (r.split(" ")(0), 1)) .

reduceByKey(_+_) . reduceByCount()

print()

// Or, more simply

//

// stream.map (r => r.split(" ")(0)) .

// countByValue() .

// print()

ssc.start()

ssc.awaitTermination()

}

}

000-DTSE-Analytics-7602-60-DU-32 © DataStax, All Rights Reserved, Confidential

------------------------------------------- Example 3: Stateful, Time: 1533397610000 ms updateStateByKey() -------------------------------------------

(10.14.246.13, 10 )

(10.14.246.10, 12 )

(10.14.246.11, 1 )

(10.14.246.12, 37 )

------------------------------------------- • Sample output

Time: 1533397620000 ms

-------------------------------------------

(10.14.246.13, 10 )

(10.14.246.10, 13 )

(10.14.246.11, 10 )

(10.14.246.12, 37 )

000-DTSE-Analytics-7602-60-DU-33 © DataStax, All Rights Reserved, Confidential

package com.datastax.enablement.bootcamp Example 3: Stateful,

updateStateByKey()

// Spark Core

import org.apache.spark.{SparkConf, SparkContext}

import org.apache.spark.SparkContext._

// Spark Streaming

import org.apache.spark.streaming._

import org.apache.spark.streaming.StreamingContext._

// DSE Spark Cassandra Connector

import com.datastax.spark.connector._

import com.datastax.spark.connector.streaming._

000-DTSE-Analytics-7602-60-DU-34 © DataStax, All Rights Reserved, Confidential

Example 3: Stateful,

updateStateByKey() object App {

def main(args: Array[String]) {

val conf = new SparkConf(true).

setAppName("My App").

setMaster("dse://127.0.0.1?").

set("spark.cleaner.ttl", "3600")

val ssc = new StreamingContext(conf, Seconds(10))

//

ssc.checkpoint("dsefs:///tmp")

val stream = ssc.socketTextStream("127.0.0.1", 9999)

000-DTSE-Analytics-7602-60-DU-35 © DataStax, All Rights Reserved, Confidential

Example 3: Stateful,

updateStateByKey()

def updateRunningCount(newValues: Seq[Long],

oldValues: Option[Long]) : Option[Long] = {

if (newValues.isEmpty)

Some(oldValues.getOrElse(0L))

else

Some(oldValues.getOrElse(0L) + newValues(0))

}

stream.map(r => r.split(" ")(0)).

countByValue() .

updateStateByKey [Long]( updateRunningCount _).

print()

000-DTSE-Analytics-7602-60-DU-36 © DataStax, All Rights Reserved, Confidential

Example 3: Stateful,

updateStateByKey()

// stream.map(r => r.split(" ")(0)).

// reduceByWindow({ (nv, ov) => nv+ov}, Seconds(60),

// Seconds(10)).

// print()

//

// Essentially a concat of the IP addr; not useful

ssc.start()

ssc.awaitTermination()

}

}

000-DTSE-Analytics-7602-60-DU-37 © DataStax, All Rights Reserved, Confidential

Example 4: Stateful,

with initial values

-------------------------------------------

Time: 1533398970000 ms

-------------------------------------------

(10.14.246.13, 1087 )

(10.14.246.13, 1088 )

(10.14.246.13, 1089 ) • Sample output (10.14.246.11,86)

(10.14.246.12, 633 )

(10.14.246.12, 634 )

(10.14.246.12, 635 )

(10.14.246.12, 636 )

(10.14.246.12, 637 )

(10.14.246.12, 638 )

000-DTSE-Analytics-7602-60-DU-38 © DataStax, All Rights Reserved, Confidential

Example 4: Stateful,

with initial values

package com.datastax.enablement.bootcamp

// Spark Core

import org.apache.spark.{SparkConf, SparkContext}

import org.apache.spark.SparkContext._

// Spark Streaming

import org.apache.spark.streaming._

import org.apache.spark.streaming.StreamingContext._

// DSE Spark Cassandra Connector

import com.datastax.spark.connector._

import com.datastax.spark.connector.streaming._

000-DTSE-Analytics-7602-60-DU-39 © DataStax, All Rights Reserved, Confidential

Example 4: Stateful, with

initial values

object App {

def main(args: Array[String]) {

val conf = new SparkConf(true).

setAppName("My App").

setMaster("dse://127.0.0.1?").

set("spark.cleaner.ttl", "3600")

val ssc = new StreamingContext(conf, Seconds(10))

//

ssc.checkpoint("dsefs:///tmp")

val lines = ssc.socketTextStream("127.0.0.1", 9999)

000-DTSE-Analytics-7602-60-DU-40 © DataStax, All Rights Reserved, Confidential

Example 4: Stateful, with

initial values

val initialRDD = ssc.sparkContext.parallelize(List(

("10.14.246.12", 500), ("10.14.246.13", 1000)))

val wordDstream = lines.map(r => (r.split(" ")(0), 1))

val mappingFunc = (word: String, one: Option[Int],

state: State[Int]) => {

val sum = one.getOrElse(0) + state.getOption.getOrElse(0)

val output = (word, sum)

state.update(sum)

output

}

000-DTSE-Analytics-7602-60-DU-41 © DataStax, All Rights Reserved, Confidential

Example 4: Stateful,

with initial values

val stateDstream = wordDstream.mapWithState(

StateSpec.function(mappingFunc).initialState(initialRDD))

stateDstream.print()

ssc.start()

ssc.awaitTermination()

}

}

000-DTSE-Analytics-7602-60-DU-42 © DataStax, All Rights Reserved, Confidential

Example 5: // ------------------------------------------- // Batch: 29 Datasets (stateful) // ------------------------------------------- // +------------+-----+ G/A July 2, 2018 // | value|count| // +------------+-----+ // |10.14.246.11| 69| // |10.14.246.12| 177| // |10.14.246.13| 63| // |10.14.246.10| 71| // +------------+-----+ // • Sample output // ------------------------------------------- // Batch: 30 // ------------------------------------------- // +------------+-----+ // | value|count| // +------------+-----+ // |10.14.246.11| 78| // |10.14.246.12| 177| // |10.14.246.13| 63| // |10.14.246.10| 72| // +------------+-----+

000-DTSE-Analytics-7602-60-DU-43 © DataStax, All Rights Reserved, Confidential

package com.datastax.enablement.bootcamp

import org.apache.spark.sql.SparkSession

Example 5: object App {

Datasets (stateful) def main(args: Array[String]) {

val host = "localhost"

val port = 9999

val spark = SparkSession

.builder

.appName("My App")

.getOrCreate()

import spark.implicits._

000-DTSE-Analytics-7602-60-DU-44 © DataStax, All Rights Reserved, Confidential

Example 5: val lines = spark.readStream

.format("socket") Datasets (stateful) .option("host", host)

.option("port", port)

.load()

val words = lines.as[String].map(r => r.split(" ")(0))

// println(words.getClass)

// class org.apache.spark.sql.Dataset

val wordCounts = words.groupBy("value").count()

val query = wordCounts.writeStream

.outputMode("complete")

.format("console")

.start()

000-DTSE-Analytics-7602-60-DU-45 © DataStax, All Rights Reserved, Confidential

Example 5:

Datasets (stateful)

query.awaitTermination()

}

}

000-DTSE-Analytics-7602-60-DU-46 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Spark 2.2+

• For all new work

• G/A July 2, 2018

• DataFrames/Datasets

• Auto checkpoint/stateful

• More complete transforms

000-DTSE-Analytics-7602-60-DU-47 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Other

Parallelism

• Number of receivers invoked

• Number of partitions (same as before)

Persistence

• Same as before (cache(), ..) ssc.checkpoint("dsefs:///tmp") Checkpointing

ssc.checkpoint(Seconds(20)) • Some transforms auto-checkpoint

• updateStateByKey( .. ) • Frequent, slower perf • countByWindow( .. ) • Infrequent, slower failure recovery

• (Other) • Recommend: 5-10 x slide interval • All window transforms

000-DTSE-Analytics-7602-60-DU-48 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Writing

Output Operation Description

print() Print first 10 elements of each RDD in the source DStream

saveAsTextFiles() Save each DStream in format/location specified. saveAsObjectFiles() saveAsHadoopFiles()

Apply f() to each RDD in source DStream. Can use any foreachRDD(f) transform/actions on input RDD.

saveToCassandra() Write to DSE Core; ks, table, [columns]

000-DTSE-Analytics-7602-60-DU-49 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7602-60-DU-50 © DataStax, All Rights Reserved, Confidential
