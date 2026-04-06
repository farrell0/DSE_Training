# DSE Analytics: DSE Analytics, DataFrames, Datasets, SQL

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, dataframes, datasets, sql. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, dataframes, datasets, sql.

## Downloads

- [PDF slides](./7578-dse-analytics-data-frames-datasets-sql.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7578-DU-60%2C%20DSE%20Analytics%2C%20DataFrames%2C%20Datasets%2C%20SQL.pptx)

## Converted Slides

## Discussion Unit:

• DataFrame optimization; Catalyst, Discussion Unit:

transform resequencing DSE Analytics • DataFrameReader

• DataFrame creation DataFrames, (Datasets, • DataFrame helpers SQL) • DataFrame API; transforms,

actions,expressions

• CassandraSQLConnect API

• Predicate pushdown

• (Examples)

000-DTSE-Analytics-7578-60-DU-1 © DataStax, All Rights Reserved, Confidential

DSE Analytics; DataFrames transforms

and actions, (SQL), other Discussion Lab:

Matching pairs -- Match the

attributes on the right with the

areas on the left

And-

Discuss – SQL/CQL queries

000-DTSE-Analytics-7578-60-DU-2 © DataStax, All Rights Reserved, Confidential

A repartition (shuffle) will DSE Analytics: T | F always write to disk first

DF in, RDD out ?

cache(), persist()

map(), flatMap()

collect()

repartition()

first(), take(), head()

count()

000-DTSE-Analytics-7578-60-DU-3 © DataStax, All Rights Reserved, Confidential

SQL/CQL Queries: SELECT

t1.customer_num, t1.state, How, and what index t2.order_num, t2.paid_date is best ? FROM

ks_7579. customer t1, ks_7579. orders t2

WHERE

t1.customer_num =

t2.customer_num

AND

t2.customer_num = 115;

SELECT

customer_num, company

FROM

ks_7579.customer2 Table access method WHERE Table order customer_num = 104 Index negation ORDER BY company;

000-DTSE-Analytics-7578-60-DU-4 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7578-60-DU-5 © DataStax, All Rights Reserved, Confidential

Working Goal: From: Maury_Atwater To: DSE_HOTSHOT

Subject: Need this now !!!

 Big deal. You previously loaded customer_orders.

Now join the SQL modeled customer, orders, and items, and load the DSE modeled customer_orders2. We need order_total, calculated from items (quantity * price).

I also need Jobs that show: . Predicate pushdown Maury Atwater, President . Optimization of Atwater's

-MA

000-DTSE-Analytics-7578-60-DU-6 © DataStax, All Rights Reserved, Confidential

DSE Analytics: DataFrames, Datasets, (SQL)

• RDD; first (core) abstraction, opaque,

2011

• Dataset; named columns/types,

compile time checking, JVM platforms

only, 2015

• DataFrame; fastest, runtime checking

of columns/types, now alias for

Dataset[Row], 2013

Both- • Optimized execution plans via Catalyst Optimizer • Custom memory management via Project Tungsten

000-DTSE-Analytics-7578-60-DU-7 © DataStax, All Rights Reserved, Confidential

Example

Optimization: val recs_DF = spark.

sql("SELECT customer_num , company " +

"FROM ks_7579.customer")

recs_DF.explain()

Filter // == Physical Plan == Sort // *Scan org.apache.spark.sql.cassandra.CassandraSourceRelation (Exchange) // ks_7579.customer[customer_num#28,company#32]

// ReadSchema: struct<customer_num:int,company:string> Scan

000-DTSE-Analytics-7578-60-DU-8 © DataStax, All Rights Reserved, Confidential

Example val recs_DF = spark. Optimization: sql("SELECT customer_num , company " +

"FROM ks_7579.customer").

orderBy("company")

recs_DF.explain() Filter

// == Physical Plan == Sort

// *Sort [company#85 ASC NULLS FIRST], true, 0 (Exchange) // +- Exchange rangepartitioning(company#85 ASC NULLS FIRST, 200) Scan // +- *Scan org.apache.spark.sql.cassandra.CassandraSourceRelation

// ks_7579.customer[customer_num#81,company#85] ReadSchema:

// struct<customer_num:int,company:string>

000-DTSE-Analytics-7578-60-DU-9 © DataStax, All Rights Reserved, Confidential

Example val recs_DF2 = recs_DF.

where("company > 'M'") Optimization:

recs_DF2.explain()

// == Physical Plan == Filter // *Sort [company#85 ASC NULLS FIRST], true, 0 Sort // +- Exchange rangepartitioning(company#85 ASC NULLS FIRST, 200)

// +- *Filter (company#85 > M) (Exchange) // +- *Scan org.apache.spark.sql.cassandra.CassandraSourceRelation

// ks_7579.customer[customer_num#81,company#85] Scan // PushedFilters: [*IsNotNull(company), GreaterThan(company,M)],

// ReadSchema: struct<customer_num:int,company:string>

000-DTSE-Analytics-7578-60-DU-10 © DataStax, All Rights Reserved, Confidential

DataFrames:

Creation

000-DTSE-Analytics-7578-60-DU-11 © DataStax, All Rights Reserved, Confidential

val recs = sc.parallelize(Array( DataFrames: How to (111, "Bob, Mary"), Create, Reflection (222, "Ted"), (333, "Alice, Bob, Harold"), (444, "Dave, Bob") ) ) recs.getClass // res: Class[_ <: org.apache.spark.rdd.RDD[(Int, String)]] = class org.apache.spark.rdd.ParallelCollectionRDD

val recs_DF = recs. toDF // recs_DF: org.apache.spark.sql. DataFrame = [_1: int, _2: string]

recs_DF.getClass // res: Class [_ <: org.apache.spark.sql.DataFrame] = class org.apache.spark.sql.Dataset

recs_DF. printSchema() // root Where have we seen // |-- _1 : integer (nullable = false) ordinals before ? // |-- _2 : string (nullable = true)

000-DTSE-Analytics-7578-60-DU-12 © DataStax, All Rights Reserved, Confidential

DataFrames: How to case class My_Record ( pk: Int, value: String)

Create, Reflection val recs = sc.parallelize(Array( My_Record(111, "Bob, Mary"), ... My_Record(444, "Dave, Bob") ) ) recs.getClass // res: Class[_ <: org.apache.spark.rdd.RDD[My_Record]] = class org.apache.spark.rdd.ParallelCollectionRDD

val recs_DF = recs. toDF () // recs_DF: org.apache.spark.sql.DataFrame = [pk: int, value: string]

recs_DF.getClass // res: Class [_ <: org.apache.spark.sql.DataFrame] = class org.apache.spark.sql.Dataset

recs_DF.printSchema() // root // |-- pk: integer (nullable = false) // |-- value: string (nullable = true)

000-DTSE-Analytics-7578-60-DU-13 © DataStax, All Rights Reserved, Confidential

DataFrames: How to case class My_Record ( pk: Int, value: String) Create, Reflection

val recs = sc.parallelize(Array( My_Record(111, "Bob, Mary"), ... My_Record(444, "Dave, Bob") ) )

val recs_DF = recs. toDF ("pk", "value")

recs_DF: org.apache.spark.sql.DataFrame = [pk: int, value: string]

recs_DF.getClass // res: Class [_ <: org.apache.spark.sql.DataFrame] = class org.apache.spark.sql.Dataset

recs_DF. printSchema() // root // |-- pk: integer (nullable = false) // |-- value: string (nullable = true)

000-DTSE-Analytics-7578-60-DU-14 © DataStax, All Rights Reserved, Confidential

From the Earlier

RDD Example

(RDD) val recs = sc. textFile ("file:///opt/stores_db/7542_HelloWorld.csv")

recs.getClass() // res: Class [_ <: org.apache.spark.rdd.RDD[String] ] = class org.apache.spark.rdd.MapPartitionsRDD

recs.printschema() // <console>: error: value printschema is not a member of org.apache.spark.rdd.RDD[String] // recs.printschema()

// Contents of CSV file, // 111, Bob, Mary // 222, Ted Harold // 333, Alice, Bob, // 444, Dave, Bob

000-DTSE-Analytics-7578-60-DU-15 © DataStax, All Rights Reserved, Confidential

From the Earlier RDD val recs_asDF = spark.read .format("csv"). Example (Data) option("header", "false"). load("file:///opt/stores_db/ zzz.csv ")

recs_asDF.collect().foreach(println) // Note: the output below is not correct. Schema was inferred, and is wrong. // [111, Bob, Mary] // [222, Ted,null] // [333, Alice, Bob] Harold ? DataFrameReader did not // [444, Dave, Bob] like the original file name-

recs_asDF.getClass() // res21: Class [_ <: org.apache.spark.sql.DataFrame] = class org.apache.spark.sql.Dataset

recs_asDF.printSchema() // root // |-- _c0: string (nullable = true) // |-- _c1: string (nullable = true) // |-- _c2: string (nullable = true) Where's Harold ? Harold ?

000-DTSE-Analytics-7578-60-DU-16 © DataStax, All Rights Reserved, Confidential

DataFrames: Works

with JSON case class My_Record (pk: String, value: Array[String] )

// ** Notice JSON file has col as int, while case class defined it as string

// These 2 lines are the same val recs_asDF = spark.read.format("json").load("file:///opt/stores_db/zzz.json").as[My_Record] val recs_asDF = spark.read.json("file:///opt/stores_db/zzz.json").as[My_Record]

// recs_asDF: org.apache.spark.sql.Dataset[My_Record] = [pk: bigint , value: array<string>]

recs_asDF.collect().foreach(println) // My_Record(111,[Ljava.lang.String; @49ae0a5 ) // My_Record(222,[Ljava.lang.String; @11ac2720 ) // My_Record(333,[Ljava.lang.String; @498623f0 ) println() does not provide // My_Record(444,[Ljava.lang.String; @eaf0124 ) an overloaded method for Array[] So, use .show() next page

000-DTSE-Analytics-7578-60-DU-17 © DataStax, All Rights Reserved, Confidential

recs_asDF. show() +---+--------------------+ DataFrames: How to | pk| value| +---+--------------------+ Create, Reflection |111| [Bob, Mary]| |222| [Ted]| |333|[Alice, Bob, Harold]| |444| [Dave, Bob]| +---+--------------------+

recs_asDF. show(2) +---+-----------+ | pk| value| +---+-----------+ |111|[Bob, Mary]| |222| [Ted]| +---+-----------+ only showing top 2 rows

000-DTSE-Analytics-7578-60-DU-18 © DataStax, All Rights Reserved, Confidential

DataFrames: How to

Create, Reflection

recs_asDF.getClass() // res: Class [_ <: org.apache.spark.sql.Dataset[My_Record]] = class org.apache.spark.sql.Dataset

recs_asDF.printschema() // root // |-- pk: long (nullable = true) // |-- value : array (nullable = true) // | |-- element: string (containsNull = true)

000-DTSE-Analytics-7578-60-DU-19 © DataStax, All Rights Reserved, Confidential

DataFrames: How to Create,

Programmatically

import org.apache.spark.sql.Row import org.apache.spark.sql.types._

val recs = sc.parallelize(Array( (111, "Bob, Mary"), (222, "Ted"), These will not be in the (333, "Alice, Bob, Harold"), Scala REPL (444, "Dave, Bob") ) ). map{case (pk, value) => Row(pk, value) } // recs: org.apache.spark.rdd. RDD[org.apache.spark.sql.Row] = MapPartitionsRDD[3] at map

recs.printschema() // <console>: error: value printschema is not a member of org.apache.spark.rdd.RDD[String] // recs.printschema()

000-DTSE-Analytics-7578-60-DU-20 © DataStax, All Rights Reserved, Confidential

DataFrames: How to

Create, Programmatically

val My_Schema = StructType ( List( StructField ( "pk", IntegerType, true ), // t|f nullable StructField("value", StringType, true) ) ) // My_Schema: org.apache.spark.sql.types.StructType = // StructType(StructField(pk,IntegerType,true), StructField(value,StringType,true))

This will not be import spark.implicits._ in the Scala REPL val recs_DF = spark. createDataFrame(recs, My_Schema ) // recs_DF: org.apache.spark.sql.DataFrame = [pk: int, value: string]

recs_DF.getClass // res: Class [_ <: org.apache.spark.sql.DataFrame] = class org.apache.spark.sql.Dataset

recs_DF.printSchema() // root // |-- pk: integer (nullable = true) // |-- value: string (nullable = true)

000-DTSE-Analytics-7578-60-DU-21 © DataStax, All Rights Reserved, Confidential

DataFrames: How to Create, Programmatically

val recs_DF = spark.sql ("SELECT customer_num, company FROM ks_7579.customer") // recs_DF: org.apache.spark.sql.DataFrame = [customer_num: int, company: string]

recs_DF.getClass // res: Class [_ <: org.apache.spark.sql.DataFrame] = class org.apache.spark.sql.Dataset

recs_DF.printSchema() // root // |-- customer_num: integer (nullable = true) // |-- company: string (nullable = true)

000-DTSE-Analytics-7578-60-DU-22 © DataStax, All Rights Reserved, Confidential

DataFrames: How to Create, DataFrameReader

val recs_DF = spark. read . format("org.apache.spark.sql.cassandra"). options(Map("keyspace" -> "ks_7579", "table" -> "customer")). load

recs_DF.getClass // res: Class [_ <: org.apache.spark.sql.DataFrame] = class org.apache.spark.sql.Dataset

// Human readable recs_DF.printSchema() // root // |-- customer_num: integer (nullable = false) // |-- address1: string (nullable = true) // |-- address2: string (nullable = true)

000-DTSE-Analytics-7578-60-DU-23 © DataStax, All Rights Reserved, Confidential

recs_DF. printSchema() // root // |-- customer_num: integer (nullable = false) // |-- address1: string (nullable = true) DataFrames: ...

Helpers recs_DF. dtypes res: Array[(String, String)] = Array( (customer_num,IntegerType), (address1,StringType), ...

recs_DF. schema res: org.apache.spark.sql.types.StructType = StructType(StructField(customer_num,IntegerType,false), StructField(address1,StringType,true),

Source: The Simpsons recs_DF. columns res: Array[String] = Array(customer_num, address1, ...

000-DTSE-Analytics-7578-60-DU-24 © DataStax, All Rights Reserved, Confidential

DataFrames: Helpers

val recs_DF = spark. sql("SELECT customer_num, company FROM ks_7579.customer"). first() // recs_DF: org.apache.spark.sql.Row = [103,Phils Sports]

println(recs_DF (0) ) println(recs_DF. getInt(0) ) 103 These are called, (DataFrame) primitives println(recs_DF. isNullAt(1) ) false

000-DTSE-Analytics-7578-60-DU-25 © DataStax, All Rights Reserved, Confidential

DataFrames: API

000-DTSE-Analytics-7578-60-DU-26 © DataStax, All Rights Reserved, Confidential

DataFrame: Transforms, Repartitioning, Persistence

Transform Description

repartition(n) Full reshuffle of the data, guaranteed balance across nodes

coalesce(n) Above; no data movement, only change count of partitions

persist(sl) MEMORY_ONLY, DISK_ONLY ..

Same as: persist(MEMORY_ONLY) cache()

unpresist() Clears (RDD, DF) from persistence list, equal to NONE

000-DTSE-Analytics-7578-60-DU-27 © DataStax, All Rights Reserved, Confidential

DataFrame: Transforms, DataFrame to RDD

Transform Description

map(f) Same as RDD, outputs RDD

flatMap(f) Same as RDD; outputs RDD

Casts a DataFrame/Dataset to RDD, giving access to RDD rdd only transforms

Converts the given data/schema to same data, JSON toJSON format/schema

000-DTSE-Analytics-7578-60-DU-28 © DataStax, All Rights Reserved, Confidential

DataFrame: Actions

Transform Description

collect() Returns an array of all rows in source DataFrame

count() Returns an int/bigint

first(), head() Returns the first row

Returns an array with (n) rows take(n), head(n)

Displays first n rows, 20 default, strings more than 20L show() are truncated, human readable format

000-DTSE-Analytics-7578-60-DU-29 © DataStax, All Rights Reserved, Confidential

DataFrame: Actions

Transform Description

foreach() Executes f() on each row in source DataFrame.

000-DTSE-Analytics-7578-60-DU-30 © DataStax, All Rights Reserved, Confidential

DataFrame: Query API, Unary Transforms

Transform Description

select(c1, c2, ..) Subset (or all) columns to return; accept * and AS

withColumnRenamed( Ability to rename column; oc=old-column, nc=new-column oc, nc)

distinct() Eliminating duplicate rows by comparing all column values

where(p) where/filter, synonyms; a column expression/predicate filter(p)

Apply aggregate functions to one or more columns; very agg( expr ) similar to SQL

Also know as: "Language-integrated queries"

000-DTSE-Analytics-7578-60-DU-31 © DataStax, All Rights Reserved, Confidential

DataFrame: Query API, Unary Transforms

Transform Description

Similar to SQL; required when returning non-agg column groupBy(c1, ..) (just like SQL)

orderBy(c1, ..) orderBy/sort, synonyms; sort(c1, ..)

limit(n) Return the first (n) rows

000-DTSE-Analytics-7578-60-DU-32 © DataStax, All Rights Reserved, Confidential

DataFrame: Query API, Binary Transforms

Transform Description

join(oDF [,p], [t]) Similar to a SQL join, inner/outer joins (t), p/join-predicates

unionAll(oDF) Similar to a SQL UNION-ALL (no duplicate remove)

intersect(oDF Rows common to both DataFrames; union compatible

Rows in source, not in oDF (other DataFrame) except(oDF)

000-DTSE-Analytics-7578-60-DU-33 © DataStax, All Rights Reserved, Confidential

DataFrame: Expressions

Transform Description

Aggregate avg, count, max, min, sum

Collection array_contains, sort_array, size, ..

current_date, current_timestamp, second, hour, month, Date-time year, ..

ceil, floor, round, pow, sqrt, log, sum, sin, cos, tan Math

Sorting asc, desc

import org.apache.spark.sql.functions._

000-DTSE-Analytics-7578-60-DU-34 © DataStax, All Rights Reserved, Confidential

DataFrame: Expressions

Transform Description

String concat, length, substring, trim, ..

UDF udf, callUDF

Windowing denseRank, percentRank, rank, lag, lean, ..

col, column, rand, randn, .. Miscellaneous

import org.apache.spark.sql.functions._

000-DTSE-Analytics-7578-60-DU-35 © DataStax, All Rights Reserved, Confidential

CassandraSQLContext API-

Method Description

setKeyspace(k) Sets a default keyspace for any SQL/CQL queries

sql() Method to Spark/SQL. (cassandraSQL(), deprecated.) cassandraSql()

Registers source DataFrame as a temp table (df) that can registerTempTable(df) have SQL executed against it; no keyspace reference

Output the query plan in human readable format explain()

000-DTSE-Analytics-7578-60-DU-36 © DataStax, All Rights Reserved, Confidential

DataFrame,

CassandraSQLCont ext

API Examples-

000-DTSE-Analytics-7578-60-DU-37 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext:

val recs_DF = spark.read . format(" org.apache.spark.sql.cassandra "). options(Map("keyspace" -> "ks_7579", "table" -> "customer")) . load // recs_DF: org.apache.spark.sql.DataFrame = [ customer_num: int, address1: string ... 8 more fields]

recs_DF.show() +------------+--------------------+-------------------+- |customer_num| address1| address2| ... +------------+--------------------+-------------------+- | 103| 654 Poplar| P. O. Box 3498| | 114| 947 Waverly Place| null| | 110| 520 Topaz Way| null| ... only showing top 20 rows

000-DTSE-Analytics-7578-60-DU-38 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: column expression

val recs_DF = spark. sql("SELECT customer_num + 5 , upper(company) " + "FROM ks_7579.customer")

recs_DF.show Use case ? +------------------+--------------------+ | (customer_num + 5) | upper(company) | +------------------+--------------------+ | 108 | PHILS SPORTS | | 119 | SPORTING PLACE | | 115 | AA ATHLETICS | ...

000-DTSE-Analytics-7578-60-DU-39 © DataStax, All Rights Reserved, Confidential

DataFrame, import org.apache.spark.sql._ // Row import org.apache.spark.sql.types._ // StructType CassandraSQL import org.apache.spark.sql.functions.lit import org.apache.spark.sql.functions._ Context: column

val recs_DF = spark. expression sql("SELECT customer_num, company " + "FROM ks_7579.customer")

val recs_DF2 = recs_DF. withColumn (" col8 ", functions.lit("Another String") ) recs_DF2.show +------------+--------------------+--------------+ |customer_num| company| col8 | +------------+--------------------+--------------+ | 103| Phils Sports| Another String | | 114| Sporting Place| Another String | | 110| AA Athletics| Another String | | 128| Phoenix University| Another String | Use case ? | 117| Kids Korner| Another String | | 120| Century Pro Shop| Another String |

000-DTSE-Analytics-7578-60-DU-40 © DataStax, All Rights Reserved, Confidential

import org.apache.spark.sql._ // Row import org.apache.spark.sql.types._ // StructType import org.apache.spark.sql.functions.lit DataFrame, import org.apache.spark.sql.functions._

CassandraSQLContext: val my_upper: (String => String) = (arg: String) => { arg.toUpperCase } column expression // my_upper: String => String = <function1>

val sqlfunc = udf ( my_upper ) // sqlfunc: org.apache.spark.sql.expressions.UserDefinedFunction = UserDefinedFunction(<function1>,StringType,Some(List(StringType)))

val recs_DF3 = recs_DF2.withColumn(" col2 ", sqlfunc ( col ("company"))) recs_DF3.show +------------+--------------------+--------------+--------------------+ |customer_num| company| col8| col2 | +------------+--------------------+--------------+--------------------+ udf() use case ? | 103| Phils Sports|Another String| PHILS SPORTS | | 114| Sporting Place|Another String| SPORTING PLACE | | 110| AA Athletics|Another String| AA ATHLETICS | | 128| Phoenix University|Another String| PHOENIX UNIVERSITY |

000-DTSE-Analytics-7578-60-DU-41 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: RDD cast

import org.apache.spark.sql._ // Row import org.apache.spark.sql.types._ // StructType import org.apache.spark.sql.functions.lit import org.apache.spark.sql.functions._

val recs_RDD = spark. sql("SELECT customer_num + 5, upper(company) " + "FROM ks_7579.customer"). rdd Use case ?

000-DTSE-Analytics-7578-60-DU-42 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: Aggregation

import org.apache.spark.sql.functions._

recs_DF. filter ("customer_num > 102"). groupBy ("state"). agg (Map("*" -> "count")). withColumnRenamed ("COUNT(1)", "state_count"). select ("state", "state_count"). orderBy (desc("state_count")). limit(5). show +-----+-----------+ |state|state_count| +-----+-----------+ | CA| 16| | NJ| 2| | AZ| 2| | NY| 1| | MA| 1| +-----+-----------+

000-DTSE-Analytics-7578-60-DU-43 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: Aggregation

val recs_DF = spark. sql("SELECT company, MAX (zipcode) AS max_zipcode " + "FROM ks_7579.customer GROUP BY company"). show +--------------------+-----------+ | company|max_zipcode| +--------------------+-----------+ | Bay Sports| 32256| | Kids Korner| 94063| ... only showing top 20 rows

val recs_DF = spark. sql("SELECT company, MAX(zipcode) AS max_zipcode " + "FROM ks_7579.customer GROUP BY company") ...

000-DTSE-Analytics-7578-60-DU-44 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: Aggregation

... val recs_DF = spark. sql("SELECT company, MAX(zipcode) AS max_zipcode " + Why do some stages "FROM ks_7579.customer GROUP BY company") repeat ?

recs_DF. explain == Physical Plan == SortAggregate (key=[company#1319], functions=[max(zipcode#1324)]) +- * Sort [company#1319 ASC NULLS FIRST], false, 0 +- Exchange hashpartitioning(company#1319, 200) +- SortAggregate (key=[company#1319], functions=[partial_max(zipcode#1324)]) +- * Sort [company#1319 ASC NULLS FIRST], false, 0 +- * Scan org.apache.spark.sql.cassandra.CassandraSourceRelation ks_7579.customer[company#1319,zipcode#1324] ReadSchema: struct<company:string,zipcode:string>

000-DTSE-Analytics-7578-60-DU-45 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: Writing

val recs_DF = spark. read . format("org.apache.spark.sql.cassandra"). options(Map("keyspace" -> "ks_7579", "table" -> " customer2 ")). load. count() // recs_DF: Long = 0

// DataFrameReader val recs_DF = spark. read . format("org.apache.spark.sql.cassandra"). options(Map("keyspace" -> "ks_7579", "table" -> " customer ")). load // recs_DF: org.apache.spark.sql.DataFrame = [customer_num: int, address1: string ... 8 more fields]

...

000-DTSE-Analytics-7578-60-DU-46 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: Writing

...

recs_DF. write . format("org.apache.spark.sql.cassandra"). options(Map( "keyspace" -> "ks_7579", "table" -> "customer2" )). save // no output;

val recs_DF = spark.read. format("org.apache.spark.sql.cassandra"). options(Map("keyspace" -> "ks_7579", "table" -> "customer2")). load. count() // recs_DF: Long = 28

000-DTSE-Analytics-7578-60-DU-47 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: Transform Before Write

// cqlsh: truncate customer2;

val recs_DF = spark.read. format("org.apache.spark.sql.cassandra"). options(Map("keyspace" -> "ks_7579", "table" -> "customer2")). load. count() // recs_DF: Long = 0

val recs_DF = spark.read. format("org.apache.spark.sql.cassandra"). options(Map("keyspace" -> "ks_7579", "table" -> "customer")). load. filter($"fname" === "Frank" || $"lname" === "Miller") // recs_DF: org.apache.spark.sql.Dataset[org.apache.spark.sql.Row] = [customer_num: int, address1: string ... 8 more fields]

...

000-DTSE-Analytics-7578-60-DU-48 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: Transform Before Write

...

recs_DF. write . format("org.apache.spark.sql.cassandra"). options(Map( "keyspace" -> "ks_7579", "table" -> "customer2" )). save // no output;

val recs_DF = spark.read. format("org.apache.spark.sql.cassandra"). options(Map("keyspace" -> "ks_7579", "table" -> "customer2")). load. count() // recs_DF: Long = 3

000-DTSE-Analytics-7578-60-DU-49 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: write mode

val recs_DF = spark. sql("SELECT customer_num, company FROM ks_7579.customer"). filter($"fname" === "Frank" || $"lname" === "Miller")

recs_DF.write. format("org.apache.spark.sql.cassandra"). options(Map( "keyspace" -> "ks_7579", "table" -> "customer2" )). save // java.lang.UnsupportedOperationException: 'SaveMode is set to ErrorIfExists and Table // ks_7579.customer2 already exists and contains data. // Perhaps you meant to set the DataFrame write mode to Append?

000-DTSE-Analytics-7578-60-DU-50 © DataStax, All Rights Reserved, Confidential

DataFrame, CassandraSQLContext: write mode

// Write with proper Append mode-

val recs_DF = spark. sql("SELECT customer_num, company FROM ks_7579.customer"). filter($"fname" === "Frank" || $"lname" === "Miller")

// append, overwite, other, // See, // https://spark.apache.org/docs/2.2.0/api/java/org/apache/spark/sql/DataFrameWriter.html recs_DF.write. mode("append"). format("org.apache.spark.sql.cassandra"). options(Map( "keyspace" -> "ks_7579", "table" -> "customer2" )).

000-DTSE-Analytics-7578-60-DU-51 © DataStax, All Rights Reserved, Confidential

Any predicate that is valid in CQL is

pushed from (Spark) down to DSE for

processing when .. DSE Analytics:

Predicate • Supported by a partition key

• Support by a clustering key Pushdown

000-DTSE-Analytics-7578-60-DU-52 © DataStax, All Rights Reserved, Confidential

Predicate Pushdown: Example

val recs_DF = spark. Scan sql("SELECT customer_num , company " + Filter "FROM ks_7579.customer"). orderBy("company") (Exchange) val recs_DF2 = recs_DF. Sort where("customer_num > 115")

recs_DF2.explain() // == Physical Plan == // * Sort [company#106 ASC NULLS FIRST], true, 0 // +- Exchange rangepartitioning(company#106 ASC NULLS FIRST, 200) // +- * Filter (customer_num#102 > 115) // +- * Scan org.apache.spark.sql.cassandra.CassandraSourceRelation PushedFilters ks_7579.customer[customer_num#102,company#106] : [*IsNotNull(customer_num), GreaterThan(customer_num,115)], ReadSchema: struct<customer_num:int,company:string>

000-DTSE-Analytics-7578-60-DU-53 © DataStax, All Rights Reserved, Confidential

Predicate Pushdown: Example

Scan Filter

val recs_DF2 = recs_DF. (Exchange) where("customer_num = 115")

Sort recs_DF2.explain() // == Physical Plan == // *Sort [company#106 ASC NULLS FIRST], true, 0 // +- Exchange rangepartitioning(company#106 ASC NULLS FIRST, 200) // +- *Scan org.apache.spark.sql.cassandra.CassandraSourceRelation PushedFilters ks_7579.customer[customer_num#102,company#106] : [*IsNotNull(customer_num), *EqualTo(customer_num,115)], ReadSchema: struct<customer_num:int,company:string>

000-DTSE-Analytics-7578-60-DU-54 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7578-60-DU-55 © DataStax, All Rights Reserved, Confidential

Additional Content:

000-DTSE-Analytics-7578-60-DU-56 © DataStax, All Rights Reserved, Confidential

Limited API Allows Catalyst

Parsed From API

Catalyst is an Optimizer which can Re-plan User requests

ds.groupBy('value).count.explain(true) == Parsed Logical Plan == Find all Attributes, 'Aggregate ['value], [unresolvedalias('value, None), count(1) AS count#47L] Expand Wildcards +- LocalRelation [value#22]

== Analyzed Logical Plan == value: string, count: bigint Aggregate [value#22], [value#22, count(1) AS count#47L] Reorganize Plan +- LocalRelation [value#22]

== Optimized Logical Plan == Aggregate [value#22], [value#22, count(1) AS count#47L] +- LocalRelation [value#22] Actually Figure == Physical Plan == Out Operations *HashAggregate(keys=[value#22], functions=[count(1)], output=[value#22, count#47L]) +- Exchange hashpartitioning(value#22, 200) +- *HashAggregate(keys=[value#22], functions=[partial_count(1)], output=[value#22, count#53L]) +- LocalTableScan [value#22]

000-DTSE-Analytics-7578-60-DU-57 © DataStax, All Rights Reserved, Confidential
