# DSE Analytics: DSE Analytics, RDDs, Hello World, load data

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, rdds, hello world, load data. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, rdds, hello world, load data.

## Downloads

- [PDF slides](./7544-dse-analytics-rdds-hello-world-load-data.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7544-DU-60%2C%20DSE%20Analytics%2C%20RDDs%2C%20Hello%20World%2C%20load%20data.pptx)

## Converted Slides

## Discussion Unit:

• Complete the big data classic; Hello Discussion Unit: World, (Word Count)

DSE Analytics

• Use DSE Analytics RDDs to load data RDDs, Hello World, Data

from file Load

• Introduce RDD Transforms

• Introduce RDD Actions

• Write data to DSE

000-DTSE-Analytics-7544-60-DU-1 © DataStax, All Rights Reserved, Confidential

DSE Analytics; RDDs, DataFrames,

Datasets

Discussion Lab:

Matching pairs – Match the

attributes on the right with the

areas on the left

000-DTSE-Analytics-7544-60-DU-2 © DataStax, All Rights Reserved, Confidential

DSE Analytics: RDD, Are immutable

DataFrame, Dataset

Reside (mostly) in memory

RDD Are transparently distributed

Historically the core Spark abstraction

The fastest abstraction Spark uses DF

Make data across a cluster of

machines look like a Scala collection

Occasionally manually redistribute DS

Rarely manually redistribute

Java, Scala only (not Python, R)

000-DTSE-Analytics-7544-60-DU-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7544-60-DU-4 © DataStax, All Rights Reserved, Confidential

Working Goal:

From: Maury_Atwater To: DSE_HOTSHOT

Subject: Need this now !!!

Attached are 3 (count) SQL DDL files, customer, orders, and items, and 3 (count) ASCII Text CSV files.

I need these loaded into DSE now !!!

Maury Atwater, President On customer.zipcode, derive an east coast, of Atwater's west coast flag ("E-USA", "W-USA"). Also derive customer.company (company name) to uppercase .

-MA

000-DTSE-Analytics-7544-60-DU-5 © DataStax, All Rights Reserved, Confidential

111, Bob, Mary Hello World ! (Word Count): 222, Ted

333, Alice, Bob, Harold CSV file contents 444, Dave, Bob

val records = sc.textFile("file:///opt/stores_db/7545_HelloWorld.csv")

val words = records. flatMap ( record => record.split(",").drop(1) )

val counts1 = words. map ( word => (word, 1) )

val counts2 = counts1. reduceByKey { case(x, y) => x + y }

counts2. collect() .foreach(println)

Unary transforms ( Dave,1) Input parameters (made up) ( Harold,1) Output data Transformer symbol ( Alice,1)

( Bob,3) Function body ( Mary,1) Action ( Ted,1)

000-DTSE-Analytics-7544-60-DU-6 © DataStax, All Rights Reserved, Confidential

RDD: Class Types

(From previous page.)

records.getClass()

Square brackets // res: Class[_ <: org.apache.spark.rdd.RDD [String] ] = mean What ? class org.apache.spark.rdd. MapPartitionsRDD (Best Scala answer: L) words.getClass()

// res: Class[_ <: org.apache.spark.rdd.RDD [String] ] =

class org.apache.spark.rdd. MapPartitionsRDD Parenthesis mean counts1.getClass() What ? (Best answer: T) // res: Class[_ <: org.apache.spark.rdd.RDD [(String, Int)] ] =

class org.apache.spark.rdd.MapPartitionsRDD

counts2.getClass()

// res: Class[_ <: org.apache.spark.rdd.RDD [(String, Int)] ] =

class org.apache.spark.rdd. ShuffledRDD

Why

000-DTSE-Analytics-7544-60-DU-7 © DataStax, All Rights Reserved, Confidential

Lazy Evaluation

records.foreach(println)

// Above returns nothing, even after action upon it

//

// While records is of type RDD, right now it's basically a file pointer.

records.collect().foreach(println)

111, Bob, Mary

222, Ted

333, Alice, Bob, Harold

444, Dave, Bob

000-DTSE-Analytics-7544-60-DU-8 © DataStax, All Rights Reserved, Confidential

Fluent val records = sc.textFile("file:///opt/stores_db/7545_HelloWorld.csv")

val words = records.flatMap( record => record.split(",").drop(1) ) API val counts1 = words.map( word => (word, 1) )

val counts2 = counts1.reduceByKey{ case(x, y) => x + y }

Why an absolute // replaced by pathname ?

val records = sc.textFile(" file:///opt/stores_db/7545_HelloWorld.csv ")

val words = records.flatMap( record => record.split(",").drop(1) )

val counts = words.map( word => (word, 1) ).reduceByKey{ case(x, y) => x + y }

// replaced by

val records = sc.textFile("file:///opt/stores_db/7545_HelloWorld.csv")

val counts = records.flatMap( record => record.split(",").drop(1) ).

map( word => (word, 1) ).reduceByKey{ case(x, y) => x + y }

000-DTSE-Analytics-7544-60-DU-9 © DataStax, All Rights Reserved, Confidential

What does this do ?

val records = sc.textFile("file:///opt/stores_db/7545_HelloWorld.csv")

val words = records.flatMap( record => record.split(",").drop(1) )

val counts = words.map( word => (word, 1) ).reduceByKey{ case(x, y) => x + y }

// replaced by

val records = sc.textFile("file:///opt/stores_db/7545_HelloWorld.csv")

val words = records.flatMap( record => record.split(",").drop(1) )

val counts = words.map( x => (x, 1) ).reduceByKey{ _ + _ }

Underscore means What ?

000-DTSE-Analytics-7544-60-DU-10 © DataStax, All Rights Reserved, Confidential

DSE Analytics:

RDD Transforms and Actions

Source: https://www.sigmoid.com/apache-spark-internals/

000-DTSE-Analytics-7544-60-DU-11 © DataStax, All Rights Reserved, Confidential

How are RDDs Created :

case class My_Record (pk: Int, value: String) • Parallelize a List

val my_records = sc. parallelize (Seq( • Load data from new My_Record(555, "Luis, Earl"),

new My_Record(666, "Ann, Sally, Bob"), stable storage Transform new My_Record(111, "Bob, Tony") or Action ?

)) • Transform another

RDD my_records.getClass()

// res: Class[_ <: org.apache.spark.rdd .RDD[My_Record] ] =

class org.apache.spark.rdd.ParallelCollectionRDD

000-DTSE-Analytics-7544-60-DU-12 © DataStax, All Rights Reserved, Confidential

Common RDD Unary Transforms (RDDs)

Transformation Description

Return a new dataset formed by selecting those elements of the source on filter(f) which function returns true.

Return a new distributed dataset formed by passing each element of the map(f) source through a function.

Similar to map, but each input item can be mapped to 0 or more output flatMap(f) items (so function should return a Sequence rather than a single item).

Return a new dataset that contains the distinct elements of the source distinct(n) dataset.

Sample a fraction of the data, with or without replacement, using a given sample( ... ) random number generator seed.

000-DTSE-Analytics-7544-60-DU-13 © DataStax, All Rights Reserved, Confidential

Common RDD Unary Transforms (RDDs)

Transformation Description

Similar to map, but runs separately on each partition (block) of the RDD, so func must be mapPartitions(f) of type Iterator<T> => Iterator<U> when running on an RDD of type T.

Similar to mapPartitions, but also provides func with an integer value representing the mapPartitionsWithIndex(f) index of the partition, so func must be of type (Int, Iterator<T>) => Iterator<U> when running on an RDD of type T.

Pipe each partition of the RDD through a shell command, e.g. a Perl or bash script. RDD pipe(envVars) elements are written to the process' stdin and lines output to its stdout are returned as an RDD of strings.

Decrease the number of partitions in the RDD to numPartitions. Useful for coalesce(n) running operations more efficiently after filtering down a large dataset.

Reshuffle the data in the RDD randomly to create either more or fewer partitions and repartition(n) balance it across them. This always shuffles all data over the network.

000-DTSE-Analytics-7544-60-DU-14 © DataStax, All Rights Reserved, Confidential

Common RDD Unary Transforms (RDDs)

Transformation Description

Repartition the RDD according to the given partitioner and, within each resulting partition, sort records by their keys. This is more efficient than repartitionAndSort calling repartition and then sorting within each partition because it can withinPartitions(p) push the sorting down into the shuffle machinery.

000-DTSE-Analytics-7544-60-DU-15 © DataStax, All Rights Reserved, Confidential

Common RDD Unary Transforms (Pair RDDs)

Transformation Description

ノ When called on a dataset of (K, V) pairs, returns a dataset of (K, Iterable<V>) pairs. te: If you are groupByKey(n) grouping in order to perform an aggregation (such as a sum or average) over each key, ノ using reduceByKey or aggregateByKey will yield much better performance. te: By default, the level of parallelism in the output depends on the number of partitions of the parent RDD. You can pass an optional numTasks argument to set a different number of tasks.

When called on a dataset of (K, V) pairs, returns a dataset of (K, V) pairs where the values for each key are aggregated using the given reduce function func, which must be of type (V,V) => V. Like reduceByKey(f, n) in groupByKey, the number of reduce tasks is configurable through an optional second argument.

When called on a dataset of (K, V) pairs, returns a dataset of (K, U) pairs where the values for each key aggregateByKey( ... ) are aggregated using the given combine functions and a neutral "zero" value. Allows an aggregated value type that is different than the input value type, while avoiding unnecessary allocations. Like in groupByKey, the number of reduce tasks is configurable through an optional second argument. When called on a dataset of (K, V) pairs where K implements Ordered, returns a dataset sortByKey(asc, n) of (K, V) pairs sorted by keys in ascending or descending order, as specified in the boolean ascending argument.

000-DTSE-Analytics-7544-60-DU-16 © DataStax, All Rights Reserved, Confidential

Common RDD Binary Transforms (RDDs)

Transformation Description

Return a new dataset that contains the union of the elements in the union(otherRDD) source dataset and the argument.

Return a new RDD that contains the intersection of elements in the intersection(otherRDD) source dataset and the argument.

A new RDD Contains those elements from the source RDD that are not in subtract(otherRDD) otherRDD. Duplicates are allowed. Input RDDs must be union compatible.

cartesian(otherRDD) When called on datasets of types T and U, returns a dataset of (T, U) pairs (all pairs of elements).

"union compatible" ?

000-DTSE-Analytics-7544-60-DU-17 © DataStax, All Rights Reserved, Confidential

Common RDD Binary Transforms (RDDs)

Transformation Description

When called on datasets of type (K, V) and (K, W), returns a dataset of (K, (V, join(otherRDD, n) W)) pairs with all pairs of elements for each key. Outer joins are supported through leftOuterJoin, rightOuterJoin, and fullOuterJoin.

When called on datasets of type (K, V) and (K, W), returns a dataset of (K, cogroup(otherRDD, n) (Iterable<V>, Iterable<W>)) tuples. This operation is also called groupWith.

000-DTSE-Analytics-7544-60-DU-18 © DataStax, All Rights Reserved, Confidential

Common RDD Actions (RDDs)

Transformation Description

Aggregate the elements of the dataset using a function func (which takes two arguments reduce(f) and returns one). The function should be commutative and associative so that it can be computed correctly in parallel.

Return all the elements of the dataset as an array at the driver program. This is usually collect() useful after a filter or other operation that returns a sufficiently small subset of the data.

Return the number of elements in the dataset. count()

Return the first element of the dataset (similar to take(1)). first()

Return an array with the first n elements of the dataset. take(n)

000-DTSE-Analytics-7544-60-DU-19 © DataStax, All Rights Reserved, Confidential

Common RDD Actions (RDDs)

Transformation Description

Return an array with a random sample of num elements of the dataset, with or without takeSample( ... ) replacement, optionally pre-specifying a random number generator seed.

Return the first n elements of the RDD using either their natural order or a custom takeOrdered( ... ) comparator.

Run a function func on each element of the dataset. This is usually done for side effects foreach(n) such as updating an Accumulator or interacting with external storage systems. Note: modifying variables other than Accumulators outside of the foreach() may result in undefined behavior. See Understanding closures for more details.

Write the elements of the dataset as a text file (or set of text files) in a given directory in saveAsTextFile(p) the local filesystem, HDFS or any other Hadoop-supported file system. Spark will call toString on each element to convert it to a line of text in the file.

000-DTSE-Analytics-7544-60-DU-20 © DataStax, All Rights Reserved, Confidential

Common RDD Actions (RDDs)

Transformation Description

Write the elements of the dataset as a Hadoop SequenceFile in a given path saveAsSequenceFile(p) in the local filesystem, HDFS or any other Hadoop-supported file system. This is available on RDDs of key-value pairs that implement Hadoop's Writable interface. In Scala, it is also available on types that are implicitly convertible to Writable (Spark includes conversions for basic types like Int, Double, String, etc).

Write the elements of the dataset in a simple format using Java saveAsObjectFile(p) serialization, which can then be loaded using SparkContext.objectFile().

Stores all elements of the source RDD into a DSE table (t) in a saveToCassandra(k, t, c) given keyspace (k). Table columns may be specified if needed.

000-DTSE-Analytics-7544-60-DU-21 © DataStax, All Rights Reserved, Confidential

Common RDD Actions (Pair RDDs)

Transformation Description

Only available on RDDs of type (K, V). Returns a hashmap of countByKey() (K, Int) pairs with the count of each key.

000-DTSE-Analytics-7544-60-DU-22 © DataStax, All Rights Reserved, Confidential

About Actions:

Triggers work to start Optimization • Calling an action says it is now time to evaluate

• Sent to the DAG Scheduler and off it goes

• Scalar value is returned to the driver

-- Avoid calling actions then transformations then actions then transformations as this

means data is sent to driver, back out to the cluster, then to driver, back out, etc.

.. Lot of avoidable data movement

.. Can drastically slow down your performance

.. Can create an OOM on driver

I.e. load data from cassandra, run a map, collect, then flatmap, foreach, and

then filter. If you would/could have done your filter, map, flatmap then collect

would have saved a lot of data transmission, on a set of data you did not need

• Instead do all transformations up front

-- If you have multiple actions then with final RDD maybe apply a persistence (caching)

mechanism on it to save, then do multiple actions (else you have to trigger the

evaluation again)

000-DTSE-Analytics-7544-60-DU-23 © DataStax, All Rights Reserved, Confidential

Function examples from DSA-

Toy Story, 1995

rdd.filter(m => m.substring(m.length - 4, m.length).toInt ==2010)

rdd.filter(m => m.split(",").last.trim.toInt ==2010)

Toy Story, 1995

rdd.map(m => m.substring(0, m.length – 6).length).

reduce{ case (x, y) => x + y } What do each of these do ? Toy Story, 1995

rdd.map(m => m.substring(0, m.length – 6).length).

foreach{ 1 => totalCount += 1; totalLength += 1 }

println(totalLength.value / totalCount.value)

println(totalLength.value.toDouble / totalCount.value)

000-DTSE-Analytics-7544-60-DU-24 © DataStax, All Rights Reserved, Confidential

Function examples from DSA-

// String, Set(String)

rdd.flatMap{case (m, g) => g}.distinct

// String, Int What do each of these do ? rdd.filter{ case (t, y) => y > 2010}

// data not provided

rdd.map( m => (m, Set("aaa", "bbb"))) Why do we sometimes pass // rdd1 = org.apache.spark.rdd.RDD[String] {} to a transform, and other times rdd2 = rdd1.cartesian(rdd1).filter{case (s, t) => s != t} () ? Best answer: E // hint: outputs, RDD[(String, String)] and F

000-DTSE-Analytics-7544-60-DU-25 © DataStax, All Rights Reserved, Confidential

DSE Analytics:

Reading and writing to DSE

using RDDs

000-DTSE-Analytics-7544-60-DU-26 © DataStax, All Rights Reserved, Confidential

DROP KEYSPACE IF EXISTS ks_7545;

CREATE KEYSPACE ks_7545 WITH REPLICATION = CQL Assets to {'class': 'SimpleStrategy', work with 'replication_factor': 1};

USE ks_7545;

CREATE TABLE hello_world

(

pk INT PRIMARY KEY,

value TEXT

);

INSERT INTO hello_world (pk, value)

VALUES (111, 'Bob, Mary' );

...

VALUES (222, 'Ted' );

VALUES (333, 'Alice, Bob, Harold');

VALUES (444, 'Dave, Bob' );

000-DTSE-Analytics-7544-60-DU-27 © DataStax, All Rights Reserved, Confidential

Reading

from DSE

using RDDs val rows = sc.cassandraTable(" ks_7545 ", " hello_world ")

rows.collect().foreach(println)

CassandraRow{pk: 111, value: Bob, Mary }

CassandraRow{pk: 222, value: Ted}

CassandraRow{pk: 444, value: Dave, Bob}

CassandraRow{pk: 333, value: Alice, Bob, Harold}

rows.getClass()

// res: Class[_ <: com.datastax.spark.connector.rdd. CassandraTableScanRDD [

com.datastax.spark.connector.CassandraRow]] =

class com.datastax.spark.connector.rdd.CassandraTableScanRDD

000-DTSE-Analytics-7544-60-DU-28 © DataStax, All Rights Reserved, Confidential

case class My_Record (pk: Int, value: String) Writing to DSE

using RDDs val my_records = sc.parallelize(Seq(

new My_Record(555, "Luis, Earl"),

new My_Record(666, "Ann, Sally, Bob"), Case class; like struct new My_Record(111, "Bob, Tony" ) in C, POJO in Java ))

SomeColumns is a

my_records.getClass() keyword

// res: Class[_ <: org.apache.spark.rdd.RDD[My_Record]] =

class org.apache.spark.rdd.ParallelCollectionRDD

// SomeColumns is a keyword

//

my_records.saveToCassandra("ks_7545", "hello_world",

SomeColumns ("pk", "value"))

000-DTSE-Analytics-7544-60-DU-29 © DataStax, All Rights Reserved, Confidential

Insert verify

val rows = sc.cassandraTable("ks_7545", "hello_world")

rows.collect().foreach(println)

CassandraRow{pk: 111, value: Bob, Tony }

CassandraRow{pk: 222, value: Ted}

CassandraRow{pk: 444, value: Dave, Bob}

CassandraRow{pk: 555, value: Luis, Earl}

CassandraRow{pk: 666, value: Ann, Sally, Bob}

CassandraRow{pk: 333, value: Alice, Bob, Harold}

Source: https://www.rottentomatoes.com/m/theres_something_about_mary/

000-DTSE-Analytics-7544-60-DU-30 © DataStax, All Rights Reserved, Confidential

Is a PK retrieval still a

(Table Scan) ?

val rows = sc.cassandraTable [My_Record] ("ks_7545", "hello_world").

where("pk=111").

select("pk", "value").

as( (i:Int, s:String ) => new My_Record(i, s) )

rows.collect().foreach(println)

//

rows.getClass()

// res: Class[_ <: com.datastax.spark.connector.rdd. CassandraTableScanRDD [My_Record]] = class com.datastax.spark.connector.rdd.CassandraTableScanRDD

Pick one, don't need both

000-DTSE-Analytics-7544-60-DU-31 © DataStax, All Rights Reserved, Confidential

Various casts, val rows = sc.cassandraTable("ks_7545", "hello_world") on read // com.datastax.spark.connector. rdd.CassandraTableScanRDD [

com.datastax.spark.connector. CassandraRow ]]

val rows = sc.cassandraTable[ (Int, String) ]("ks_7545", "hello_world")

// rdd.CassandraTableScanRDD[ (Int, String) ]]

case class My_Record (pk: Int, value: String)

//

val rows = sc.cassandraTable[My_Record]("ks_7545", "hello_world") Scala REPL //rdd.CassandraTableScanRDD[ My_Record ]] versus Scala

compiler val rows = sc.cassandraTable[My_Record]("ks_7545", "hello_world").

select("pk", "value").

as( (i:Int, s:String ) => new My_Record(i, s) )

// rdd.CassandraTableScanRDD[ My_Record ]]

000-DTSE-Analytics-7544-60-DU-32 © DataStax, All Rights Reserved, Confidential

Working

CREATE TABLE customer with CSVs, ( RDDs, customer_num INT PRIMARY KEY,

fname TEXT, writing lname TEXT,

company TEXT,

address1 TEXT,

address2 TEXT,

city TEXT,

state TEXT,

zipcode TEXT,

phone TEXT

);

000-DTSE-Analytics-7544-60-DU-33 © DataStax, All Rights Reserved, Confidential

Working

val rows20 = sc.textFile( with CSVs, "file:///opt/stores_db/customer.csv") RDDs,

val rows21 = rows20.map ( line => line.split (",")) writing

val rows22 = rows21.map ( p => My_Record ( p(0).toInt,

p(1).toString, p(2).toString, p(3).toString, p(4).toString,

p(5).toString, p(6).toString, p(7).toString, p(8).toString,

p(9).toString ))

rows22.saveToCassandra("ks_7545", "customer",

SomeColumns( "customer_num" , "fname",

"lname" , "company" ,

"address1" , "address2" ,

"city" , "state" , Not our first choice: "zipcode" , "phone" )) positional, fragile

000-DTSE-Analytics-7544-60-DU-34 © DataStax, All Rights Reserved, Confidential

Working

with CSVs,

RDDs, val My_Schema = StructType(Array(

StructField("customer_num" , IntType, true), writing StructField("fname" , StringType, true),

StructField("lname" , StringType, true),

StructField("company" , StringType, true),

StructField("address1" , StringType, true),

StructField("address2" , StringType, true),

StructField("city" , StringType, true),

StructField("state" , StringType, true),

StructField("zipcode" , StringType, true),

StructField("phone" , StringType, true)

))

000-DTSE-Analytics-7544-60-DU-35 © DataStax, All Rights Reserved, Confidential

Technically, this CSV read is into a DataFrame; hence, the cast to RDD val rows30 =

spark.read.schema(My_Schema).csv(

Working "file:///opt/stores_db/customer.csv")

with CSVs, val rows31 = rows30. rdd RDDs,

rows31.saveToCassandra("ks_7545", "customer", writing

SomeColumns( "customer_num" , "fname",

"lname" , "company" ,

"address1" , "address2" ,

"city" , "state" ,

"zipcode" , "phone" ))

000-DTSE-Analytics-7544-60-DU-36 © DataStax, All Rights Reserved, Confidential

Back to

Atwater's

000-DTSE-Analytics-7544-60-DU-37 © DataStax, All Rights Reserved, Confidential

Working Goal:

From: Maury_Atwater To: DSE_HOTSHOT

Subject: Need this now !!!

Attached are 3 (count) SQL DDL files, customer, orders, and items, and 3 (count) ASCII Text CSV files.

I need these loaded into DSE now !!!

Maury Atwater, President On customer.zipcode, derive an east coast, of Atwater's west coast flag ("E-USA", "W-USA"). Also derive customer.company (company name) to uppercase .

-MA

000-DTSE-Analytics-7544-60-DU-38 © DataStax, All Rights Reserved, Confidential

CREATE TABLE customer _plus_derived ( SQL Assets you customer_num INT PRIMARY KEY, fname TEXT, work with in the lname TEXT, lab to follow company TEXT, address1 TEXT, address2 TEXT, city TEXT, state TEXT, zipcode TEXT, phone TEXT, company_upshift TEXT, ew_flag TEXT ); INSERT INTO customer (customer_num, fname, lname, company, address1, address2, city, state, zipcode, phone) VALUES ( 101, 'Ludwig', 'Pauli', 'All Sports Supplies ', '213 Erstwild Court', '', 'Sunnyvale', 'CA', ' 94086 ', '408-789-8075');

000-DTSE-Analytics-7544-60-DU-39 © DataStax, All Rights Reserved, Confidential

From Before .. 111, Bob, Mary

222, Ted (or, specifically the CSV handing 333, Alice, Bob, Harold code shown) 444, Dave, Bob

val records = sc.textFile("file:///opt/stores_db/7545_HelloWorld.csv")

val words = records. flatMap ( record => record.split(",").drop(1) )

val counts1 = words. map ( word => (word, 1) )

val counts2 = counts1. reduceByKey { case(x, y) => x + y }

counts2. collect() .foreach(println)

( Dave,1)

( Harold,1)

( Alice,1)

( Bob,3)

( Mary,1)

( Ted,1)

000-DTSE-Analytics-7544-60-DU-40 © DataStax, All Rights Reserved, Confidential

Add the first column

derivation

val recs_withDerived = counts2.map { case(name, cnt) =>

(name, cnt, name.toUpperCase ) }

recs_withDerived.collect().foreach(println)

( Dave,1, DAVE)

( Harold,1, HAROLD)

( Alice,1, ALICE)

( Bob,3, BOB)

( Mary,1, MARY)

( Ted,1, TED)

000-DTSE-Analytics-7544-60-DU-41 © DataStax, All Rights Reserved, Confidential

object MyFunctions { Add the second def generateFlag(arg: String) : String = { column derivation if (arg > "M")

"E-USA"

else

"W-USA"

}

} You will val recs_withDerived = counts2.map { case(name, cnt) => use (name, cnt, name.toUpperCase, zipcode MyFunctions.generateFlag(name) ) }

recs_withDerived.collect().foreach(println) Extra

credit for ( Dave,1, DAVE,W-USA) an integer ( Harold,1, HAROLD,W-USA) ( Alice,1, ALICE,W-USA) ( Bob,3, BOB,W-USA) ( Mary,1, MARY,W-USA) ( Ted,1, TED,W-USA)

000-DTSE-Analytics-7544-60-DU-42 © DataStax, All Rights Reserved, Confidential

Using Records

case class My_Record (pk: Int, value: String)

//

val rows = sc.cassandraTable[My_Record]("ks_7545", "hello_world")

rows.collect().foreach(println)

My_Record(111,Bob, Tony)

My_Record(222,Ted)

My_Record(444,Dave, Bob)

My_Record(555,Luis, Earl)

My_Record(666,Ann, Sally, Bob)

My_Record(333,Alice, Bob, Harold)

000-DTSE-Analytics-7544-60-DU-43 © DataStax, All Rights Reserved, Confidential

Using Records

val rows2 = rows.map { case(row) => (row.value, row.pk,

row.value.toUpperCase, MyFunctions.generateFlag(row.value) ) }

rows2.collect().foreach(println)

(Bob, Tony,111,BOB, TONY,W-USA)

(Ted,222,TED,E-USA)

(Dave, Bob,444,DAVE, BOB,W-USA)

(Luis, Earl,555,LUIS, EARL,W-USA)

(Ann, Sally, Bob,666,ANN, SALLY, BOB,W-USA)

(Alice, Bob, Harold,333,ALICE, BOB, HAROLD,W-USA)

000-DTSE-Analytics-7544-60-DU-44 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7544-60-DU-45 © DataStax, All Rights Reserved, Confidential

Additional Detail:

000-DTSE-Analytics-7544-60-DU-46 © DataStax, All Rights © DataStax, All Rights Reserved, Confidential Reserved. Confidential.

Other UIs: Using DSE Analytics w/ Notebooks

DSE Studio is a notebook (based on Zeppelin); there are

three main notebooks in addition to Studio

• Jupyter (http://jupyter.org/ )

• Zeppelin (https://zeppelin.apache.org/ )

• Spark Notebook (http://spark-notebook.io/ )

DSE 6.0+ there are options to run notebooks against DSE

more natively

• dse exec

• Launches a shell command with environment variables set

by DSE. Example, dse exec bin/spark-notebook

000-DTSE-Analytics-7544-60-DU-47 © DataStax, All Rights © DataStax, All Rights Reserved, Confidential Reserved. Confidential.

More

You've loaded data before; it's all about the munge- Scala:

Munging case class Person (fname: String, lname: String, age: Int)

records .. // Emily gets married

val emily1 = Person("Emily", "Means", 40)

val emily2 = emily1.copy(lname = "Walls", age = 42)

// also

// val emily1 = Person(lname = "Means", fname = "Emily", age = 40)

val fullName = (p: Person) => s"${p.fname} ${p.lname}"

val xx = fullName(emily1)

// xx: String = Emily Means

000-DTSE-Analytics-7544-60-DU-48 © DataStax, All Rights Reserved, Confidential

More Scala: val double = (i: Int) => i * 2 Functions as data val isEven = (i: Int) => i % 2 == 0

val x = 42

val y = double(x)

val y = isEven(x)

val ints = List(1, 2, 4)

// filter expects a boolean

// map expects a list

//

val y = ints.map(double)

val y = ints.filter(isEven)

000-DTSE-Analytics-7544-60-DU-49 © DataStax, All Rights Reserved, Confidential

More Scala: val isEven = (i: Int) => i % 2 == 0 Functions as data

// Also,

val isEven = (i: Int) => { i % 2 == 0 }

val isEven = (i: Int) => if ( i % 2 == 0 ) true else false

val isEven = (i: Int) => { if ( i % 2 == 0 ) true else false }

val isEven = (i: Int) => {

if ( i % 2 == 0 ) { isEven field name true (i: Int) input params } else { => transformer symbol false i % 2 == 0 function body }

}

000-DTSE-Analytics-7544-60-DU-50 © DataStax, All Rights Reserved, Confidential

case class My_Record (pk: Int, value: String)

More Scala:

val my_records = sc.parallelize(Seq( Helper function, new My_Record(555, "Luis, Earl"),

toDF new My_Record(666, "Ann, Sally, Bob"),

new My_Record(111, "Bob, Tony"),

new My_Record(111, "Jennifer")

))

my_records.count

val my_records_asDF = my_records.toDF

my_records_asDF.count

...

000-DTSE-Analytics-7544-60-DU-51 © DataStax, All Rights Reserved, Confidential

...

my_records_asDF.show

my_records_asDF.orderBy("value").show More Scala:

+---+---------------+ Helper function, | pk| value| toDF +---+---------------+

|666|Ann, Sally, Bob|

|111| Bob, Tony|

|555| Luis, Earl|

+---+---------------+

my_records_asDF.orderBy("value").take(1)

my_records_asDF.printSchema()

root

|-- pk: integer (nullable = false)

|-- value: string (nullable = true)

000-DTSE-Analytics-7544-60-DU-52 © DataStax, All Rights Reserved, Confidential

More Scala: Helper function, toDF

my_records_asDF.groupBy("pk").count.show()

my_records_asDF.groupBy("pk").count.orderBy("pk").show

my_records_asDF.groupBy("pk").count.orderBy("count").show

my_records_asDF.groupBy("pk").count.orderBy($"count".desc).show()

my_records_asDF.groupBy("pk").count.orderBy("pk").show

000-DTSE-Analytics-7544-60-DU-53 © DataStax, All Rights Reserved, Confidential

[ What ] is interacting There are JDBC, ODBC, Parquet, (other)

connectors built into Spark, but there is not a with DSE ? (Cassandra) one

DataStax provides 2 drivers that work

interactively

• DSE Java Driver (See Discussion Unit,

6244/6245) (not Spark)

• Spark Cassandra Connector (Spark)

-- Open source, AND enterprise license

features

-- Spark objects, activities

These allow you to connect to DSE directly from

Spark, like using a JDBC driver, more

000-DTSE-Analytics-7544-60-DU-54 © DataStax, All Rights Reserved, Confidential

DSE Java Driver-

On top of the open source driver sits the DSE Driver-

• Specific extensions for DSE

-- Authenticator implementations that use the authentication

scheme negotiation in the server-side DseAuthenticator

-- Value classes for geospatial types, and type codecs that

integrate them seamlessly

-- Continuous Paging

-- DSE graph integration

-- https://github.com/datastax/java-dse-driver

• Only allowed to use if you have a valid DSE License

000-DTSE-Analytics-7544-60-DU-55 © DataStax, All Rights Reserved, Confidential

DSE Spark (Cassandra) Connector-

• Exposes (Cassandra) tables as Spark RDDs, DataFrames, Datasets

• Read, write, and more

• Execute arbitrary CQL queries in your Spark applications

• Used with the Cassandra Java Driver

• Open Source Apache 2.0 license

• DataStax Github Repository, https://

github.com/datastax/spark-cassandra-connector

Use cases:

• Streaming data into DSE

• Analyzing the data in place

• Migrating from bad data model

000-DTSE-Analytics-7544-60-DU-56 © DataStax, All Rights Reserved, Confidential

Spark Client Web

UI: Extra TAB

when streaming

000-DTSE-Analytics-7544-60-DU-57 © DataStax, All Rights Reserved, Confidential
