# DSE Analytics: DSE Analytics, RDD part 2

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, rdd part 2. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, rdd part 2.

## Downloads

- [PDF slides](./7570-dse-analytics-rdd-part-2.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7570-DU-60%2C%20DSE%20Analytics%2C%20RDD%20part%202.pptx)

## Converted Slides

## Discussion Unit:

• Complete the topics relative to just RDDs part 2 RDDs Complete the discussion

on RDDs • More on sc.CassandraTable(),

sc.saveToCassandra()

• More (Scala)/RDD examples, more

transforms, more use cases

000-DTSE-Analytics-7570-60-DU-1 © DataStax, All Rights Reserved, Confidential

DSE Analytics; Cardinality between

Terms, 1:1, 1:Many, Many:1

Discussion Lab:

Matching pairs – Match the

attributes on the right with the

areas on the left

000-DTSE-Analytics-7570-60-DU-2 © DataStax, All Rights Reserved, Confidential

flatMap() Relationship between Terms:

map()

Binary Transform 1:1

Task to Partition

1:M (optionally 1:1) Stage to Action

Stage to Transform M:1 (optionally 1:1)

Action to Job

Job to Stage

Logical, or Physical Task to Thread on a JVM

DSEFS to DSE Cluster

000-DTSE-Analytics-7570-60-DU-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7570-60-DU-4 © DataStax, All Rights Reserved, Confidential

Working Goal: From: Maury_Atwater To: DSE_HOTSHOT

Subject: Need this now !!!

 Big deal. You previously loaded 3 tables.

Now join the SQL modeled customer and orders, and load the DSE modeled customer_orders.

I also need Jobs for: . Customers without orders . Count of orders by state . Orders where paid_date is null Maury Atwater, President . Count of orders by customer, sort by of Atwater's count descending

-MA

000-DTSE-Analytics-7570-60-DU-5 © DataStax, All Rights Reserved, Confidential

CQL Assets to

Work with:

customer, orders, data

000-DTSE-Analytics-7570-60-DU-6 © DataStax, All Rights Reserved, Confidential

CQL Assets to Work With ..

DROP KEYSPACE IF EXISTS ks_7571;

CREATE KEYSPACE ks_7571 WITH REPLICATION =

{'class': 'SimpleStrategy',

'replication_factor': 1};

USE ks_7571;

000-DTSE-Analytics-7570-60-DU-7 © DataStax, All Rights Reserved, Confidential

CQL Assets to Work With ..

CREATE TABLE customer

(

customer_num INT PRIMARY KEY,

fname TEXT,

lname TEXT,

company TEXT,

address1 TEXT,

address2 TEXT, // 6'th column ?

city TEXT,

state TEXT,

zipcode TEXT,

phone TEXT

);

000-DTSE-Analytics-7570-60-DU-8 © DataStax, All Rights Reserved, Confidential

CQL Assets to

INSERT INTO customer Work With .. (customer_num, fname, lname, company, address1, address2, city, state, zipcode, phone) VALUES ( 101, 'Ludwig', 'Pauli', 'All Sports Supplies', null '213 Erstwild Court', , 'Sunnyvale', 'CA', '94086',

'408-789-8075'); ... VALUES ( 102, 'Carole', 'Sadler', 'Sports Spot', null '785 Geary St', , 'San Francisco', 'CA', '94117',

'415-822-1289'); VALUES ( 103, 'Philip', 'Currie', 'Phils Sports', Watch '654 Poplar', 'P. O. Box 3498 ', 'Palo Alto', 'CA', '94303', '415-328-4543'); address2 VALUES ( 104, 'Anthony', 'Higgins', 'Play Ball!', and nulls 'East Shopping Cntr.', ' 422 Bay Road ', 'Redwood City', 'CA', '94026', '415-368-1100');

000-DTSE-Analytics-7570-60-DU-9 © DataStax, All Rights Reserved, Confidential

CQL Assets to Work CREATE TABLE customer2

( With ..

customer_num INT,

fname TEXT,

lname TEXT,

company TEXT,

address1 TEXT,

address2 TEXT,

city TEXT, Same data as customer, state TEXT, different PK zipcode TEXT,

phone TEXT,

PRIMARY KEY ((customer_num), company)

);

000-DTSE-Analytics-7570-60-DU-10 © DataStax, All Rights Reserved, Confidential

CQL Assets to Work CREATE TABLE orders ( With .. order_num INT PRIMARY KEY, order_date TEXT, customer_num INT, ship_instruct TEXT, backlog TEXT, po_num TEXT, ship_date TEXT, ship_weight TEXT, ship_charge TEXT, paid_date TEXT );

VALUES ( 1001, '05/20/1998', 104, 'express', 'n', 'B77836', '06/01/1998', '20.4', '10.0', '07/22/1998');

(and 22 more orders)

000-DTSE-Analytics-7570-60-DU-11 © DataStax, All Rights Reserved, Confidential

cassandraTable()

Examples using cassandraTable()

000-DTSE-Analytics-7570-60-DU-12 © DataStax, All Rights Reserved, Confidential

Scala (data): Tuples, Case Classes, other

val rows = sc.cassandraTable[ (Int, String) ]("ks_7545", "hello_world")

// rdd.CassandraTableScanRDD[ (Int, String) ]]

case class My_Record (pk: Int, value: String)

//

val rows = sc.cassandraTable[My_Record]("ks_7545", "hello_world")

//rdd.CassandraTableScanRDD[ My_Record ]]

000-DTSE-Analytics-7570-60-DU-13 © DataStax, All Rights Reserved, Confidential

sc.cassandraTable() .. From earlier

Pick one, don't need both case class My_Record (pk: Int, value: String)

val rows = sc.cassandraTable [My_Record] ("ks_7545", "hello_world").

where("pk=111").

select("pk", "value").

as( (i:Int, s:String ) => new My_Record(i, s) )

rows.getClass()

// res: Class[_ <: com.datastax.spark.connector.rdd. CassandraTableScanRDD // [My_Record]] = class com.datastax.spark.connector.rdd.CassandraTableScanRDD

000-DTSE-Analytics-7570-60-DU-14 © DataStax, All Rights Reserved, Confidential

[ What ] is interacting There are JDBC, ODBC, Parquet, (other)

connectors built into Spark, but there is not a with DSE ? (Cassandra) one

Java, Java Driver DataStax provides 2 drivers that work

interactively DSE • DSE Java Driver (See Discussion Unit,

6244/6245) (not Spark)

• Spark Cassandra Connector (Spark) DSE Spark -- Open source, AND enterprise license Cassandra features Connector DSE -- Spark objects, activities

Spark Spark These allow you to connect to DSE directly from Driver

Spark, like using a JDBC driver, more

000-DTSE-Analytics-7570-60-DU-15 © DataStax, All Rights Reserved, Confidential

DSE Analytics Spark Cassandra Connector

API Call Description

cassandraTable(k, t) Returns RDD, SparkContext

Optional, subset/all columns select(c1, c2), ..

Optional, WHERE clause, may be parameterized where( pred, [params], ..)

withAscOrder, Optional, ORDER BY, single DSE partition based withDescOrder on clustering columns, (runtime error if no CC)

000-DTSE-Analytics-7570-60-DU-16 © DataStax, All Rights Reserved, Confidential

DSE Analytics Spark Cassandra Connector

API Call Description

limit(n) Optional, how many rows to return

Return column of known Type/t, Scala equivalent of DSE getType(c1) column type; primitive, collection, UDT, tuple (runtime get[t](c1) error if c1 does not exist, empty collections are returned)

Best practice ; essentially, set a default value of getTypeOption(c1) (column) otherwise NULL get[O[t ]]( c1)

Using function, map DSE cols to Scala; tuple, case as(f) class, other

000-DTSE-Analytics-7570-60-DU-17 © DataStax, All Rights Reserved, Confidential

DSE Analytics Spark Cassandra Connector

API Call Description

Convert DSE rows into Key/Value RDD, k and keyBy[k](c1, c2, ..) (cols) usually defined as Scala case class

000-DTSE-Analytics-7570-60-DU-18 © DataStax, All Rights Reserved, Confidential

Predicate Processing-

Are these Jobs, Stages,

Tasks ?

case class My_Record (pk: Int, value: String) How is each executed ?

val rows = sc.cassandraTable("ks_7571", "customer"). Which has the great where("fname > 'D'") likelihood to be more rows.collect().foreach(println) efficient ?

val rows = sc.cassandraTable("ks_7571", "customer"). If there is no (index or

similar), on the server filter(r => r.getString("fname") > "D") side, is one statement still rows.collect().foreach(println) more efficient ?

000-DTSE-Analytics-7570-60-DU-19 © DataStax, All Rights Reserved, Confidential

val rows = sc.cassandraTable("ks_7571", " customer ").

where("fname > 'D' ")

.withAscOrder()

val rows = sc.cassandraTable("ks_7571", " customer ").

where("fname > 'D' ").

withAscOrder

val rows = sc.cassandraTable("ks_7571", " customer2 ").

where("fname > 'D' ").

withAscOrder

val rows = sc.cassandraTable("ks_7571", " customer2 "). Which compile ? withAscOrder Which Work ?

When do they rows = sc.cassandraTable("ks_7571", " customer2 "). fail ? where("customer_num = 101").

withAscOrder

000-DTSE-Analytics-7570-60-DU-20 © DataStax, All Rights Reserved, Confidential

Case insensitive with a substring-

val rows = sc.cassandraTable("ks_7571", "customer").

filter(r => r.getString("company").

toLowerCase.contains("sport") )

rows.collect().foreach(println)

CassandraRow{customer_num: 103, address1: 654 Poplar, ...

CassandraRow{customer_num: 102, address1: 785 Geary St, ...

CassandraRow{customer_num: 101, address1: 213 Erstwild Court, ...

000-DTSE-Analytics-7570-60-DU-21 © DataStax, All Rights Reserved, Confidential

Concatenate fields, default out null field

val rows = sc.cassandraTable("ks_7571", "customer").

map{ r => r.getString("address1") + ", " +

r.getStringOption("address2"). getOrElse("N/A") +

", " + r.getString("city") }

rows.collect().foreach(println)

654 Poplar, P. O. Box 3498, Palo Alto

East Shopping Cntr., 422 Bay Road, Redwood City

785 Geary St, N/A, San Francisco

213 Erstwild Court, N/A, Sunnyvale

000-DTSE-Analytics-7570-60-DU-22 © DataStax, All Rights Reserved, Confidential

Handling nulls-

val rows = sc.cassandraTable[ (Int, String, String, String,

String, String, String, String,

String, String) ]("ks_7571", "customer")

rows.collect().foreach(println)

// WARN 2018-07-20 17:37:40,994

// org.apache.spark.scheduler.TaskSetManager:

// Lost task 6.0 in stage 20.0 (TID 208, 127.0.0.1, executor 0):

// java.lang.NullPointerException:

// Unexpected null value of column address2 in ks_7571.customer.

// If you want to receive null values from Cassandra, please wrap

// the column type into Option or use JavaBeanColumnMapper

000-DTSE-Analytics-7570-60-DU-23 © DataStax, All Rights Reserved, Confidential

Handling nulls-

Why ?

val rows = sc.cassandraTable[ (Int, String, String, String,

String, Option[String] , String, String,

String, String) ]("ks_7571", "customer")

rows.collect().foreach(println)

// Still fails

val rows = sc.cassandraTable[ (String, String) ]("ks_7571", "customer").

select("address1", "address2")

rows.collect().foreach(println)

// Still fails

000-DTSE-Analytics-7570-60-DU-24 © DataStax, All Rights Reserved, Confidential

Handling nulls-

val rows = sc.cassandraTable[ (String, Option[String] ) ]("ks_7571", "customer").

select("address1", "address2")

rows.collect().foreach(println)

(654 Poplar,Some(P. O. Box 3498))

(East Shopping Cntr.,Some(422 Bay Road))

(785 Geary St,None)

(213 Erstwild Court,None)

000-DTSE-Analytics-7570-60-DU-25 © DataStax, All Rights Reserved, Confidential

Handling nulls-

case class My_Record ( address1: String, address2: Option[String] )

//

val rows = sc.cassandraTable[My_Record]("ks_7571", "customer").

select("address1", "address2")

rows.collect().foreach(println)

My_Record(654 Poplar,Some(P. O. Box 3498))

My_Record(East Shopping Cntr.,Some(422 Bay Road))

My_Record(785 Geary St,None)

My_Record(213 Erstwild Court,None)

000-DTSE-Analytics-7570-60-DU-26 © DataStax, All Rights Reserved, Confidential

Handling nulls-

val rows = sc.cassandraTable("ks_7571", "customer").

select("address1", "address2").

map(r => ( r.getString("address1"), r.getStringOption("address2") ))

rows.collect().foreach(println)

(654 Poplar,Some(P. O. Box 3498))

(East Shopping Cntr.,Some(422 Bay Road)) Less efficient

(785 Geary St,None)

(213 Erstwild Court,None)

000-DTSE-Analytics-7570-60-DU-27 © DataStax, All Rights Reserved, Confidential

Checking for nulls-

val rows = sc.cassandraTable("ks_7571", "customer").

select("address1", "address2"). Must use get() filter{ r => r.get[Option[String]]("address2").isDefined }

rows.collect().foreach(println)

CassandraRow{address1: 654 Poplar, address2: P. O. Box 3498}

CassandraRow{address1: East Shopping Cntr., address2: 422 Bay Road}

000-DTSE-Analytics-7570-60-DU-28 © DataStax, All Rights Reserved, Confidential

Grouping and

Sorting:

000-DTSE-Analytics-7570-60-DU-29 © DataStax, All Rights Reserved, Confidential

SQL Aggregation Example-

How many columns are

SELECT output ?

As any aggregate query, o.order_num,

(n types) of columns are sum (i.total_price) price output. What are these FROM orders o, items i types ? WHERE o.order_date > '01/01/89'

AND o.customer_num > 110 Which table is read first ? AND o.order_num = i.order_num What indexes would you GROUP BY 1 have in place ?

ORDER BY 2;

000-DTSE-Analytics-7570-60-DU-30 © DataStax, All Rights Reserved, Confidential

Grouping, reduceByKey()

val rows = sc.cassandraTable("ks_7571", "customer").

select("phone", "company"). What is the most map( r => ( r.getString("phone").substring(0,3) , 1 ) ). precise name for the reduceByKey(_ + _) type of RDD that is rows.collect().foreach(println) output ?

(415,3) What does "1" do ? (408,1)

What is "_" ?

000-DTSE-Analytics-7570-60-DU-31 © DataStax, All Rights Reserved, Confidential

Grouping, groupByKey()

val rows = sc.cassandraTable("ks_7571", "customer").

select("phone", "company").

How is this different map( r => ( r.getString("phone").substring(0,3),

than the SQL query r.getString("company") ) ).

that proceeded ? groupByKey()

rows.collect().foreach(println)

(415,CompactBuffer(Phils Sports, Play Ball!, Sports Spot))

(408,CompactBuffer(All Sports Supplies))

000-DTSE-Analytics-7570-60-DU-32 © DataStax, All Rights Reserved, Confidential

Grouping, groupByKey and map()

val rows = sc.cassandraTable("ks_7571", "customer").

select("phone", "company").

map( r => ( r.getString("phone").substring(0,3),

r.getString("company") ) ).

groupByKey(). That's called a map(r => ( r._2.size, r._1, r._2 )) Sequence rows.collect().foreach(println)

(3,415, CompactBuffer(Phils Sports, Play Ball!, Sports Spot))

(1,408, CompactBuffer(All Sports Supplies))

000-DTSE-Analytics-7570-60-DU-33 © DataStax, All Rights Reserved, Confidential

Grouping, groupByKey and map(), add sortBy()

val rows = sc.cassandraTable("ks_7571", "customer").

select("phone", "company").

map( r => ( r.getString("phone").substring(0,3), r.getString("company") ) ).

groupByKey().

map(r => (r._2.size, r._1, r._2)). What are the sortBy( _._1, true ) arguments to rows.collect().foreach(println) sortBy() ?

(1,408,CompactBuffer(All Sports Supplies))

(3,415,CompactBuffer(Phils Sports, Play Ball!, Sports Spot))

000-DTSE-Analytics-7570-60-DU-34 © DataStax, All Rights Reserved, Confidential

Grouping, countByKey()

A value is returned.

Why: Where is the

collect () ? val rows = sc.cassandraTable("ks_7571", "customer"). What type of RDD is select("phone", "company"). returned ? map( r => ( r.getString("phone").substring(0,3), 1) ).

countByKey()

rows: scala.collection.Map[String,Long] = Map(415 -> 3, 408 -> 1)

000-DTSE-Analytics-7570-60-DU-35 © DataStax, All Rights Reserved, Confidential

Grouping: DSE side grouping

API Call Description

Group values for each key in the source Cassandra spanByKey() based RDD. Grouping is performed on the DSE

side based on primary key columns.

Group elements of type V in the Cassandra based spanBy() RDD. Grouping is performed on the DSE side

based primary key columns.

000-DTSE-Analytics-7570-60-DU-36 © DataStax, All Rights Reserved, Confidential

Grouping: DSE side counting

API Call Description

Returns a number of rows in the source Cassandra cassandraCount() RDD.

Similar to where/filter: requires reference to whole of partitioning key

000-DTSE-Analytics-7570-60-DU-37 © DataStax, All Rights Reserved, Confidential

Joins: A Binary

Transform

000-DTSE-Analytics-7570-60-DU-38 © DataStax, All Rights Reserved, Confidential

Joining-

val c_rows = sc.cassandraTable("ks_7571", " customer ").

select( "customer_num", "company", "state" ).

as((customer_num:Int, company:String, state:String) => What is up (customer_num, (company, state))) with the green

parenthesis ? val o_rows = sc.cassandraTable("ks_7571", " orders ").

select( "customer_num", "order_num", "order_date" ). What type of as((customer_num:Int, order_num:Int, order_date:String) => RDD is this ? (customer_num, (order_num, order_date)))

000-DTSE-Analytics-7570-60-DU-39 © DataStax, All Rights Reserved, Confidential

Joining: join() (standard inner join)

val j_rows = c_rows.join(o_rows)

j_rows.collect().foreach(println)

Also; (101,((All Sports Supplies,CA),(1002,05/21/1998))) leftOuterJoin(), (104,((Play Ball!,CA),(1013,06/22/1998))) rightOuterJoin(), (104,((Play Ball!,CA),(1011,06/18/1998))) fullOuterJoin() (104,((Play Ball!,CA),(1001,05/20/1998)))

(104,((Play Ball!,CA),(1003,05/22/1998)))

000-DTSE-Analytics-7570-60-DU-40 © DataStax, All Rights Reserved, Confidential

Joining: same, different (than prior page) ?

val j_rows = o_rows.join(c_rows)

j_rows.collect().foreach(println)

How does the (101,((1002,05/21/1998),(All Sports Supplies,CA))) output differ (104,((1013,06/22/1998),(Play Ball!,CA))) than the prior (104,((1011,06/18/1998),(Play Ball!,CA))) page ? (104,((1001,05/20/1998),(Play Ball!,CA)))

(104,((1003,05/22/1998),(Play Ball!,CA)))

000-DTSE-Analytics-7570-60-DU-41 © DataStax, All Rights Reserved, Confidential

Joining: leftOuterJoin()

val j_rows = o_rows.leftOuterJoin(c_rows)

Inner join ? j_rows.collect().foreach(println) Outer join ?

How do they (119,((1016,06/29/1998),None)) differ ? ...

(115,((1010,06/17/1998),None))

(101,((1002,05/21/1998),Some((All Sports Supplies,CA))))

(116,((1005,05/24/1998),None))

...

000-DTSE-Analytics-7570-60-DU-42 © DataStax, All Rights Reserved, Confidential

Joining: Where no match-pair exists

val j_rows = o_rows.leftOuterJoin(c_rows).

filter{case (pk, (row_o, row_c)) => !row_c.isDefined}

j_rows.collect().foreach(println)

(119,((1016,06/29/1998),None))

(112,((1006,05/30/1998),None)) Use case ? (126,((1022,07/24/1998),None))

(120,((1017,07/09/1998),None))

...

000-DTSE-Analytics-7570-60-DU-43 © DataStax, All Rights Reserved, Confidential

Scala: How do you pick that apart ?

(119,((1016, null ), Some(NJ) ))

(126,((1022, 09/02/1998 ), Some(CO) ))

The Some() will map{r => ( r._1, r._2._1._2, r._2._1._1, r._2._2 )} come from an outer

join. (119,null,1016,Some(NJ)) .get will ditch that (126,09/02/1998,1022,Some(CO))

Tuple => Ordinals map{r => ( r._1, Option(r._2._1._2) , r._2._1._1, r._2._2 )}.

map{r => ( r._1, r._2.getOrElse("N/A") , r._3, r._4. get )} Option(),

then .getOrElse to (119, N/A ,1016, NJ ) lose the null (126, 09/02/1998 ,1022, CO )

000-DTSE-Analytics-7570-60-DU-44 © DataStax, All Rights Reserved, Confidential

Joining: DSE side joining

val c_rows = sc.cassandraTable("ks_7571", " customer ").

select("customer_num", "company", "state").

as((customer_num:Int, company:String, state:String) =>

(customer_num, (company, state)))

val o_rows = sc.cassandraTable("ks_7571", " orders ").

select("customer_num", "order_num", "order_date").

as((customer_num:Int, order_num:Int, order_date:String) =>

(customer_num, (order_num, order_date)))

000-DTSE-Analytics-7570-60-DU-45 © DataStax, All Rights Reserved, Confidential

Joining: DSE side joining

val j_rows = c_rows.joinWithCassandraTable("ks_7571", "orders").

on(SomeColumns("customer_num"))

j_rows.collect().foreach(println)

// java.lang.IllegalArgumentException: requirement failed:

// Can't join without the full partition key. Missing: [ Set(order_num) ]

val j_rows = o_rows.joinWithCassandraTable("ks_7571", "customer").

on(SomeColumns("customer_num"))

j_rows.collect().foreach(println)

//java.lang.IllegalArgumentException: requirement failed:

// Can't join without the full partition key. Missing: [ Set(order_num) ]

000-DTSE-Analytics-7570-60-DU-46 © DataStax, All Rights Reserved, Confidential

Joining: DSE side joining

val o_rows = sc.cassandraTable("ks_7571", "orders").

select("customer_num", "order_num", "order_date").

keyBy[Tuple1[Int]]("customer_num")

val j_rows = o_rows.joinWithCassandraTable("ks_7571", "customer").

on(SomeColumns("customer_num"))

j_rows.collect().foreach(println)

// ERROR 2018-07-21 20:46:03,465 org.apache.spark.scheduler.TaskSetManager:

// Lost task 1.0 in stage 0.0 (TID 1, 127.0.0.1, executor 0):

// com.datastax.spark.connector.types.TypeConversionException:

// Cannot convert object (110) of type class scala.Tuple1 to java.lang.Integer.

000-DTSE-Analytics-7570-60-DU-47 © DataStax, All Rights Reserved, Confidential

Joining: DSE side joining

val o_rows = sc.cassandraTable("ks_7571", "orders").

select("customer_num", "order_num", "order_date").

keyBy(row => row.getInt("customer_num"))

val j_rows = o_rows.joinWithCassandraTable("ks_7571", "customer").

on(SomeColumns("customer_num"))

j_rows.collect().foreach(println)

((101,CassandraRow{customer_num: 101, order_num: 1002, ...

((104,CassandraRow{customer_num: 104, order_num: 1013, ...

...

000-DTSE-Analytics-7570-60-DU-48 © DataStax, All Rights Reserved, Confidential

Working with

Key/Value RDDs

000-DTSE-Analytics-7570-60-DU-49 © DataStax, All Rights Reserved, Confidential

Key/Value RDD Unary Transforms

API Call Description

Create new RDD, apply f() to each element from mapValues(f) source RDD . Keys retained without change.

Same as above; one to many input to output, if f() flatMapValues(f) returns a Sequence

When called on a dataset of (K, V) pairs, returns a dataset of (K, V) pairs where the values for each key are aggregated using the given reduce function func, reduceByKey(f, n) which must be of type (V,V) => V. Like in groupByKey, the number of reduce tasks is configurable through an optional second argument.

foldByKey(z, n, f) (Complex: See Notes page)

000-DTSE-Analytics-7570-60-DU-50 © DataStax, All Rights Reserved, Confidential

Key/Value RDD Unary Transforms

API Call Description

combineByKey( .. ) (Complex: See Notes page)

ノ When called on a dataset of (K, V) pairs, returns a dataset of (K, Iterable<V>) pairs. te: If you are grouping in order to perform an aggregation (such as a sum or average) over each groupByKey(n) ノ key, using reduceByKey or aggregateByKey will yield much better performance. te: By default, the level of parallelism in the output depends on the number of partitions of the parent RDD. You can pass an optional numTasks argument to set a different number of tasks.

When called on a dataset of (K, V) pairs where K implements Ordered, returns a sortByKey(ASC, n) dataset of (K, V) pairs sorted by keys in ascending or descending order, as specified in the boolean ascending argument.

000-DTSE-Analytics-7570-60-DU-51 © DataStax, All Rights Reserved, Confidential

Key/Value RDD Actions

API Call Description

lookup(k) (Example on pages that follow.)

Returns a map of key/value pairs from source RDD. collectAsMap()

Only available on RDDs of type (K, V). Returns a countByKey() hashmap of (K, Int) pairs with the count of each key.

000-DTSE-Analytics-7570-60-DU-52 © DataStax, All Rights Reserved, Confidential

val c_rows = sc.cassandraTable("ks_7571", "customer").

select("customer_num", "company", "state").

as((customer_num:Int, company:String, state:String) =>

(customer_num, (company, state)))

Key/Value RDD: val c_rows_k = c_rows .keys

c_rows_k.collect().foreach(println) (support) transforms 103

104

...

val c_rows_v = c_rows .values

c_rows_v.collect().foreach(println)

(Phils Sports,CA)

(Play Ball!,CA)

...

000-DTSE-Analytics-7570-60-DU-53 © DataStax, All Rights Reserved, Confidential

val rows2 = c_rows. Key/Value RDD: mapValues{case (v) => (v, "New Value")}

mapValues(), rows2.collect().foreach(println)

collectAsMap() (103,((Phils Sports,CA),New Value))

(104,((Play Ball!,CA),New Value))

...

rows2.getClass

res: Class[_ <: org.apache.spark.rdd.RDD[(Int, ((String, String), String))]] = class

org.apache.spark.rdd.MapPartitionsRDD

val map1 = rows2.collectAsMap()

map1.getClass

res: Class[_ <: scala.collection.Map[Int,((String, String), String)]] = class

scala.collection.mutable.HashMap

000-DTSE-Analytics-7570-60-DU-54 © DataStax, All Rights Reserved, Confidential

Key/Value RDD: lookup()

What is the source

of that error ?

val row_102 = rows2.lookup(103)

row_102.collect().foreach(println)

// Not an RDD anymore

// error: not enough arguments for method collect:

// (pf: PartialFunction[((String, String), String),B])

// (implicit bf: scala.collection.generic.CanBuildFrom[Seq[((String, String), String)],B,That])

// That. Unspecified value parameter pf.

row_102

res: Seq[((String, String), String)] = WrappedArray(((Phils Sports,CA),New

Value))

000-DTSE-Analytics-7570-60-DU-55 © DataStax, All Rights Reserved, Confidential

Key/Value RDD,

Binary

Transforms:

union(),

intersection(),

difference()

"Union compatible", same number

and type of columns

000-DTSE-Analytics-7570-60-DU-56 © DataStax, All Rights Reserved, Confidential

Key/Value RDD: union(), intersection(), difference()

val c_rows1 = sc.cassandraTable("ks_7571", "customer").

where("customer_num = 101").

select("customer_num", "company", "state").

as((customer_num:Int, company:String, state:String) =>

(customer_num, (company, state)))

What are the

c_rows1.collect().foreach(println) key cols ?

Value cols ?

(101,(All Sports Supplies,CA))

000-DTSE-Analytics-7570-60-DU-57 © DataStax, All Rights Reserved, Confidential

Key/Value

RDD: union(),

val c_rows2 = sc.cassandraTable("ks_7571", "customer"). intersection(), where("customer_num > 102"). difference() select("customer_num", "company", "state").

as((customer_num:Int, company:String, state:String) =>

(customer_num, (company, state)))

c_rows2.collect().foreach(println)

// java.lang.UnsupportedOperationException: Why does this // Range predicates on partition key columns fail ? // (here: customer_num) are not supported in When does // where. Use filter instead. this fail ?

000-DTSE-Analytics-7570-60-DU-58 © DataStax, All Rights Reserved, Confidential

Key/Value

RDD: union(),

intersection(), val c_rows2 = sc.cassandraTable("ks_7571", "customer").

select("customer_num", "company", "state"). difference()

as((customer_num:Int, company:String, state:String) =>

(customer_num, (company, state))).

filter{case (customer_num, (company, state)) => (customer_num > 102)}

c_rows2.collect().foreach(println)

(103,(Phils Sports,CA))

(104,(Play Ball!,CA))

000-DTSE-Analytics-7570-60-DU-59 © DataStax, All Rights Reserved, Confidential

Key/Value RDD: union()

val u_rows = c_rows1.union(c_rows2)

u_rows.collect().foreach(println)

(101,(All Sports Supplies,CA))

(103,(Phils Sports,CA))

(104,(Play Ball!,CA))

000-DTSE-Analytics-7570-60-DU-60 © DataStax, All Rights Reserved, Confidential

Partitioning:

000-DTSE-Analytics-7570-60-DU-61 © DataStax, All Rights Reserved, Confidential

• An (RDD) is a distributed collection of Partitioning:

partitions

• Spark automatically partitions based on

source and target, and type of action RDD

• Rarely manually re-partition when using

DataFrames, Datasets; no need, optimizer

takes care of that. DF

• RDDs, no optimizer.

• But, RDDs will automatically match

partitioning of DSE table due to DSE DS Analytics Spark Cassandra Connector

• Reshuffling/repartitioning; perhaps the

most expensive operation

000-DTSE-Analytics-7570-60-DU-62 © DataStax, All Rights Reserved, Confidential

Partitioning: Rules, and more

• RDD.partitions Returns array of partition objects

• RDD.partitions.size Length of above

• RDD.partitioner Returns partitioner name

• Range partitioner, used for sorting

• None (partitioner), random

• Custom (partitioner), example: (DSE Core)

• Number of partitions == number of tasks (per stage)

• sc.defaultParallelism

-- Outputs setting

-- Default number of tasks that can execute concurrently

-- Equal to number of DSE cores, by default

000-DTSE-Analytics-7570-60-DU-63 © DataStax, All Rights Reserved, Confidential

Partitioning: Rules, and more

Default partitioning behavior-

Local Scala collection

None partitioner, sc.defaultParallelism

DSE Core table

None partitioner or,

com.datastax.spark.connector.rdd. \

partitioner.CassandraPartitioner (you decide)

sc.defaultParallelism or

approx data size / 64MB, whichever is greater

HDFS/DSEFS

None partitioner, sc.defaultParallelism, or

number of file blocks, whichever is greater

000-DTSE-Analytics-7570-60-DU-64 © DataStax, All Rights Reserved, Confidential

Result of transforms- Partitioning: • filter(), map(), flatMap(), distinct(), .. Rules, and • None partitioner, exception: filter uses parent

more

union(), Sum of two RDD partition sizes

intersect(), Max of two RDD partition sizes

subtract(), Parent RDD partitioner size

cartesian(), Two RDD partition sizes multiplied

Key based transforms-

• reduceByKey(), foldByKey(), combineByKey(), groupByKey, .. HashPartitioner,

same as parent RDD

• mapValues(), flatMapValues(), Same as parent RDD

• cogroup(), join(), leftOuterJoin(), .. HashPartitioner, Same as parent RDD, or

configurable

000-DTSE-Analytics-7570-60-DU-65 © DataStax, All Rights Reserved, Confidential

Partitioning: Setting-

• Optimal ? 2x number of cores

• 100ms+ Task execution time

-- Too few: possible data skew, increased memory pressure,

longer recovery from failure

-- Too many: Task scheduling may take longer than task

execution, more lineage information to record

• The custom partitioner used to read/write to/from DSE Core

• val my_data = sc.parallelize(List( ... )).

partitionBy(new org.apache.spark.HashPartitioner(9)) // 9 partitions

000-DTSE-Analytics-7570-60-DU-66 © DataStax, All Rights Reserved, Confidential

Repartitioning/Shuffling-

Cost Factors

• Disk I/O

• Network traffic

• Partitioning execution

• External sorting

• Serialization/deserialization

• Data compression

000-DTSE-Analytics-7570-60-DU-67 © DataStax, All Rights Reserved, Confidential

Shuffling tunables: spark-env.sh

Property Description Default

spark.shuffle.manager sort Data shuffling strategy; sort or hash

spark.shuffle.spill true Enables spilling data to disk by reduce tasks

spark.shuffle.memoryFraction

0.2 Spilling threshold as fraction of Java heap

spark.shuffle.sort. No merge-sort if number of reduce tasks not greater and 200 bypassMergeThreshold no map-side aggregation

spark.shuffle.compress true Enable compression for shuffle writes

spark.shuffle.spill.compress true Enable compression for spilled data

000-DTSE-Analytics-7570-60-DU-68 © DataStax, All Rights Reserved, Confidential

Partitioning: Examples, suboptimal (from DSA)

val rows = sc.cassandraTable("k1", "t1").

keyBy(row => row.getInt("release_year")).

repartition (2*sc.defaultParallelism)

3 shuffles; val rowsCountByYear = rows. countByKey().

repartition(), foreach(println)

countByKey(),

groupByKey() val rowsByYear = rows. groupByKey() .

collect.

foreach(println)

000-DTSE-Analytics-7570-60-DU-69 © DataStax, All Rights Reserved, Confidential

Partitioning: Examples, optimal (from DSA)

val rows= sc.cassandraTable("k1", "t1").

keyBy(row => row.getInt("release_year")).

partitionBy (new org.apache.spark.HashPartitioner(2*sc.defaultParallelism)).

cache

val rowsCountByYear = rows.countByKey().

foreach(println)

1 shuffle val rowsByYear = rows.groupByKey().

collect.

foreach(println)

000-DTSE-Analytics-7570-60-DU-70 © DataStax, All Rights Reserved, Confidential

Partitioning: Which operations cause reshuffling

• repartition

• coalesce

• partitionBy

• reduceByKey

• foldByKey

• combineByKey • cache to set one/best partitioning • groupByKey scheme • cogroup • filter early

• join, leftOuterJoin, .. • spanByKey()

• sortByKey • spanBy(f)

• lookup • repartitionByCassandraReplica( ... )

• applyPartitionerFrom( ... )

000-DTSE-Analytics-7570-60-DU-71 © DataStax, All Rights Reserved, Confidential

case class My_Record (pk: Int, value: String)

//

val rows1 = sc.parallelize(Seq( Partitioning:

new My_Record(400, "K-Mart"), Examples new My_Record(401, "Wal*Mart"),

new My_Record(402, "Piggly Wiggly")

))

println( rows1.partitions.size )

// 3

println( rows1.partitioner )

// None

// This box has 4 cores, DSE cores defaults to 4 - 1

val rows2 = rows1. repartition(2*sc.defaultParallelism)

println(rows2.partitions.size)

// 6

000-DTSE-Analytics-7570-60-DU-72 © DataStax, All Rights Reserved, Confidential

Partitioning:

// To change partitioner, need a K/V pair RDD Examples // Since pk is unique, just need a groupBy

val rows2_kv = rows2. groupBy(_.pk)

rows2_kv.collect().foreach(println)

Why 6 ? (402,CompactBuffer(My_Record(402,Piggly Wiggly)))

(400,CompactBuffer(My_Record(400,K-Mart)))

(401,CompactBuffer(My_Record(401,Wal*Mart)))

println(rows2_kv. partitioner )

// Some(org.apache.spark.HashPartitioner@6)

000-DTSE-Analytics-7570-60-DU-73 © DataStax, All Rights Reserved, Confidential

Partitioning: Examples

val rows3 = rows2_kv. partitionBy(new org.apache.spark.HashPartitioner(9) )

println(rows3.partitioner)

// Some(org.apache.spark.HashPartitioner@9)

000-DTSE-Analytics-7570-60-DU-74 © DataStax, All Rights Reserved, Confidential

Partitioning

Matching DSE: val c_rows = sc.cassandraTable("ks_7571", "customer").

select("customer_num", "company", "state") Examples

println(c_rows.partitioner)

// None

val c_rows = sc.cassandraTable("ks_7571", "customer"). Which is better ? select("customer_num", "company", "state").

keyBy[Tuple1[Int]]("customer_num", "company", "state")

println(c_rows.partitioner)

// Some(com.datastax.spark.connector.rdd.partitioner.CassandraPartitioner@4da90f6c)

** First Url on Notes page

000-DTSE-Analytics-7570-60-DU-75 © DataStax, All Rights Reserved, Confidential

Partitioning Matching DSE: Examples, RDD

case class My_Record (customer_num: Int, company: String, state: String)

//

val rows1 = sc.parallelize(Seq(

new My_Record(400, "K-Mart", "MI"),

new My_Record(401, "Wal*Mart", "AR"),

new My_Record(402, "Piggly Wiggly", "WI")

))

000-DTSE-Analytics-7570-60-DU-76 © DataStax, All Rights Reserved, Confidential

Partitioning Matching DSE: Examples, RDD

val rows2 = rows1. repartitionByCassandraReplica("ks_7571", "customer", 10)

println(rows2.partitioner)

// Some(com.datastax.spark.connector.rdd.partitioner.ReplicaPartitioner@4b3be6f7)

println(rows2.partitions.size)

// 10

Use case ?

000-DTSE-Analytics-7570-60-DU-77 © DataStax, All Rights Reserved, Confidential

Partitioning Matching

DSE: Examples, DSE

Table

val o_rows1 = sc.cassandraTable("ks_7571", "orders").

select("order_num", "customer_num", "order_date").

keyBy[Tuple1[Int]]("order_num", "customer_num", "order_date")

val c_rows = sc.cassandraTable("ks_7571", "customer").

select("customer_num", "company", "state").

keyBy[Tuple1[Int]]("customer_num", "company", "state")

val o_rows1b = o_rows1.applyPartitionerFrom(c_rows)

000-DTSE-Analytics-7570-60-DU-78 © DataStax, All Rights Reserved, Confidential

Writing to DSE:

000-DTSE-Analytics-7570-60-DU-79 © DataStax, All Rights Reserved, Confidential

Same Action:

• RDD of tuples Writing to DSE:

• RDD of case class objects

• RDD of CassandraRow objects

API Call

• saveToCassandra(ks, tb [, SomeColumns (c1, c2, ..)])

insert/update (upserts all), delete

• saveAsCassandraTable(ks, tb [, SomeColumns(c1, c2, ..)])

Makes table too, first column PK only

• saveAsCassandraTableEx(tab-def [, SomeColumns(c1, c2, ..)])

Makes table extended , more property control

Mechanics of this-

• CQL insert for every row in the RDD, grouped in unlogged batches

• Default CL is LOCAL_QUORUM

000-DTSE-Analytics-7570-60-DU-80 © DataStax, All Rights Reserved, Confidential

Writing to DSE:

val rows1 = sc.parallelize(List( Tuples (400, "K-Mart", "MI"),

(401, "Wal*Mart", "AR"),

(402, "Piggly Wiggly", "WI")

))

rows1.saveToCassandra("ks_7571", "customer",

SomeColumns("customer_num", "company", "state"))

Controlling val rows2 = sc.parallelize(List( column (500, "New Company", "AK") assignments ))

rows2.saveToCassandra("ks_7571", "customer",

SomeColumns( "customer_num" as "_1", "company" as "_3", "state" as "_2" ))

000-DTSE-Analytics-7570-60-DU-81 © DataStax, All Rights Reserved, Confidential

Writing to DSE: case class objects

case class My_Record (customer_num: Int, company: String, state: String)

//

val rows3 = sc.parallelize(Seq(

new My_Record(500, "BlockBuster", "TX"),

new My_Record(501, "NetFlix", "CA"),

new My_Record(502, "RST Video", "NJ")

))

rows3.saveToCassandra("ks_7571", "customer",

SomeColumns("customer_num", "company", "state"))

000-DTSE-Analytics-7570-60-DU-82 © DataStax, All Rights Reserved, Confidential

Writing to DSE: CassandraRow Objects

val rdd1 = sc.cassandraTable("ks_7571", "customer").

where("customer_num = 101").

select("customer_num", "company", "state")

val rdd2 = rdd1.map{ r => (701, "New Company", "AK") }

// rdd2.collect().foreach(println)

rdd2.saveToCassandra("ks_7571", "customer",

SomeColumns("customer_num", "company", "state"))

000-DTSE-Analytics-7570-60-DU-83 © DataStax, All Rights Reserved, Confidential

Write to

DSE: if

not exists case class My_Customer (customer_num: Int,

company: String, state: String)

val df1 = spark.createDataset(Seq(My_Customer( 901,

"New Company 1", "AK" )))

val df2 = spark.createDataset(Seq(My_Customer( 901,

"New Company 2", "AK" ))) write() is

actually a

df1. write .format("org.apache.spark.sql.cassandra"). DataFrame

options(Map("table" -> "customer", "keyspace" -> method, not

"ks_7571", "spark.cassandra.output.ifNotExists" -> RDD

"true" )).mode( SaveMode.Append ).save()

000-DTSE-Analytics-7570-60-DU-84 © DataStax, All Rights Reserved, Confidential

Write to DSE: if not exists

cqlsh> select * from customer;

customer_num | address1 | address2 | city | company | fname | lname | phone | state | zipcode --------------+----------+----------+------+---------------+-------+-------+-------+-------+--------- 901 | null | null | null | New Company 1 | null | null | null | AK | null

df2.write.format("org.apache.spark.sql.cassandra").

options(Map("table" -> "customer", "keyspace" -> "ks_7571",

"spark.cassandra.output.ifNotExists" ->

"true")).mode(SaveMode.Append).save()

// same output as first line; write did not occur

000-DTSE-Analytics-7570-60-DU-85 © DataStax, All Rights Reserved, Confidential

Writing to DSE: (collections, UDTs, TTL, nulls)

It's all there; nulls in particular is above Scala-101

Supports operations on collections:

• append/add, (lists, sets, maps)

• prepend, (lists)

• remove, (lists, sets)

• overwrite, (lists, sets, maps) (Default)

• UDTs, case class, and UDTValue.fromMap( ... )

• Tombstones; needs advanced Scala function

• TTL/WRITETIME, uses WriteConf () (DataFrame for now ?)

See Url on Notes page for examples to all-

000-DTSE-Analytics-7570-60-DU-86 © DataStax, All Rights Reserved, Confidential

Writing to DSE: Deletes

val rows = sc.cassandraTable("ks_7571", "customer").

filter(r => r.getInt("customer_num") > 102)

rows.collect().foreach(println)

CassandraRow{customer_num: 103, ...

CassandraRow{customer_num: 104, ...

rows.deleteFromCassandra("ks_7571", "customer")

val rows = sc.cassandraTable("ks_7571", "customer")

rows.collect().foreach(println)

CassandraRow{customer_num: 102, ...

CassandraRow{customer_num: 101, ...

000-DTSE-Analytics-7570-60-DU-87 © DataStax, All Rights Reserved, Confidential

Writing to DSE: Deletes, specific columns

val rows = sc.cassandraTable("ks_7571", "customer").

filter(r => r.getInt("customer_num") > 102)

rows.deleteFromCassandra("ks_7571", "customer",

SomeColumns("state", "city"))

val rows = sc.cassandraTable("ks_7571", "customer").

select("customer_num", "city", "state")

rows.collect().foreach(println)

CassandraRow{customer_num: 103, city: null, state: null }

CassandraRow{customer_num: 104, city: null, state: null }

CassandraRow{customer_num: 102, city: San Francisco, state: CA}

CassandraRow{customer_num: 101, city: Sunnyvale, state: CA}

000-DTSE-Analytics-7570-60-DU-88 © DataStax, All Rights Reserved, Confidential

Writing to DSE: Deletes, partition deletes

• DSE Core has an optimization to delete an entire partition, called

a "range delete"

• Supported here too

• Can also delete on a time stamp to row

• Check the Jira on the Notes page.

000-DTSE-Analytics-7570-60-DU-89 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7570-60-DU-90 © DataStax, All Rights Reserved, Confidential

Additional Detail:

000-DTSE-Analytics-7570-60-DU-91 © DataStax, All Rights Reserved, Confidential

Shared Variables:

• Not specific to RDDs

• Actually, hard to do on a shared nothing platform

• Broadcast variables

-- Read-only at Task level

-- Writable at Driver level

-- Workers move this around

-- Use case ? Symbol table, other

• Accumulators

-- Native support for numeric (double, long,

float), can program other types

-- Use case ? Counting, aggregation

-- Returned to driver for final (sum)

000-DTSE-Analytics-7570-60-DU-92 © DataStax, All Rights Reserved, Confidential

val bv = sc. broadcast (Set( 102, 104 )) Shared val ac = sc. accumulator (0)

Variables:

val rows = sc.cassandraTable("ks_7571", "customer"). Example select("customer_num", "company").

filter(r => bv.value contains r.getInt("customer_num")).

cache

rows.collect().foreach(println)

CassandraRow{customer_num: 104 , company: Play Ball!}

CassandraRow{customer_num: 102 , company: Sports Spot} Why the cache ?

rows.foreach{ r => ac += r.getString("company").length }

println( ac )

31 // Will add across executors, nodes

000-DTSE-Analytics-7570-60-DU-93 © DataStax, All Rights Reserved, Confidential
