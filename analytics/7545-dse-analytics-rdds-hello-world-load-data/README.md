# DSE Analytics: DSE Analytics, RDDs, Hello World, load data

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, rdds, hello world, load data. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, rdds, hello world, load data.

## Downloads

- [PDF slides](./7545-dse-analytics-rdds-hello-world-load-data.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7545-PL-60%2C%20DSE%20Analytics%2C%20RDDs%2C%20Hello%20World%2C%20load%20data.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on Discussion

Unit 7544, where most of the objects we create

in this lab were introduced.

• This Practice Lab requires a working DSE

system, with DSE Analytics enabled.

• Because of the dependency on the "dse spark" Practice Lab: utility, this Practice Lab requires a ssh(C)

prompt on at least one node operating DSE DSE Analytics, Word Analytics. Count (first example),

RDDs, Transforms, • Artifacts created in this Practice Lab are used

Actions, read and write by other Practice Labs that follow . So, it is

from DSE important you complete the minimal challenges

as outlined.

000-DTSE-Analytics-7545-60-PL-1 © DataStax, All Rights Reserved. Confidential.

Challenge 1: Locate the Spark Master, state

# from any DSE node (both commands)

dse client-tool spark master-address 9042 ??

127.0.0.1: 9042 dse:// ?connection.local_dc=DC1;connection.host=;

dsetool ring

Address DC Rack Workload Graph Status State Load Owns Token Health [0,1]

127.0.0.1 DC1 RAC1 Analytics( SM ) no Up Normal 116.01 KiB ? -5915474479483571799 0.40

> Note: you must specify a keyspace to get ownership information.

SM == Spark Master

000-DTSE-Analytics-7545-60-PL-2 © DataStax, All Rights Reserved. Confidential.

Challenge 2: Spark UIs • All of the REPLs are idiomatic,

which you see from the exit

commands dse spark-sql

exit; • Spark/SQL, generally ANSI

SQL/99+, Hive/QL(Hive/SQL)

1.2.2; OLAP, not OLTP dse pyspark

• pyspark is a Python command quit() interpreter

• sparkR will fail without given R dse sparkR # Will fail language dependencies being

met

000-DTSE-Analytics-7545-60-PL-3 © DataStax, All Rights Reserved. Confidential.

Challenge 2: Spark UIs

Stay in "dse spark", and start a second subsequent session in another terminal window minutes later dse spark

These are actually Scala interpreters; CONTROL-L // to clear screen you don't need to run Spark

:quit An 'action' submits a Spark jop

Creating a new Spark Session

Spark context Web UI available at http://172.16.119.194:4040

Spark Context available as 'sc' (master = dse://?, app id = app-20180619165450-0001).

Spark Session available as 'spark'.

Spark SqlContext (Deprecated use Spark Session instead) available as 'sqlContext'

000-DTSE-Analytics-7545-60-PL-4 © DataStax, All Rights Reserved. Confidential.

Challenge 2: http::// (Spark master IP) :7080

000-DTSE-Analytics-7545-60-PL-5 © DataStax, All Rights Reserved. Confidential.

Challenge 2: dse spark, options

dse spark

--master spark://127.0.0.1:7080

--name NNN

--driver-memory 512M

--executor-memory 1G

--total-executor-cores N

Exit all but one

Spark REPL

000-DTSE-Analytics-7545-60-PL-6 © DataStax, All Rights Reserved. Confidential.

About the REPLs:

• Connects to Spark master, [ Spark commands ] run

as jobs from a DAG, ..

• All rules apply; lazy evaluation, other

• SparkContext predefined as, sc

• SparkSession as, spark (SQL, Hive, other

resources)

• Some cheats available; syntax not entirely

same/rigid as a true program. (Similar to Gremlin

development versus production.)

000-DTSE-Analytics-7545-60-PL-7 © DataStax, All Rights Reserved. Confidential.

• Implement Word Count from

Discussion Unit 7544

• As a simple 2-4 line task, we'll use Challenge 3

the spark REPL as our IDE (Optional): • Easier to check classes, other.

• Read/write to/from DSE using Word Count (Hello World) RDDs.

000-DTSE-Analytics-7545-60-PL-8 © DataStax, All Rights Reserved. Confidential.

Challenge 3 (Optional): Simple ASCII text file

Create a simple ASCII text file with

data similar to,

111, Bob, Mary

222, Ted

333, Alice, Bob, Harold

444, Dave, Bob

Short/simple absolute pathname

000-DTSE-Analytics-7545-60-PL-9 © DataStax, All Rights Reserved. Confidential.

val records = sc.textFile("file:///opt/stores_db/7545_HelloWorld.csv")

val words = records. flatMap ( record => record.split(",").drop(1) )

val counts1 = words. map ( word => (word, 1) )

val counts2 = counts1. reduceByKey { case(x, y) => x + y }

counts2. collect() .foreach(println)

( Dave,1)

( Harold,1)

( Alice,1) Challenge 3: ( Bob,3)

( Mary,1) The Scala, ( Ted,1) Spark code

000-DTSE-Analytics-7545-60-PL-10 © DataStax, All Rights Reserved. Confidential.

Challenge 3: Two Transforms (Derivations)

val recs_withDerived = counts2.map

{ case(name, cnt) =>

(name, cnt, name.toUpperCase ) }

000-DTSE-Analytics-7545-60-PL-11 © DataStax, All Rights Reserved. Confidential.

Challenge 3: Two object MyFunctions {

def generateFlag(arg: String) : String = Transforms

{ (Derivations) if (arg > "M")

"E-USA"

else

"W-USA"

}

}

val recs_withDerived = counts2.map

{ case(name, cnt) =>

(name, cnt, name.toUpperCase,

MyFunctions.generateFlag(name) ) }

recs_withDerived.collect().foreach(println

)

000-DTSE-Analytics-7545-60-PL-12 © DataStax, All Rights Reserved. Confidential.

Challenge 3: Read/Write to/from DSE Use

getClass() to

prove this.

• At this point, you've likely

created a 4 column RDD.

Sample code is for 2 columns.

• Using CQLSH, create a

similarly structured DSE/CQL

table to read and write from.

000-DTSE-Analytics-7545-60-PL-13 © DataStax, All Rights Reserved. Confidential.

Challenge 3: Write to DSE using RDDs

case class My_Record (pk: Int, value: String)

val my_records = sc.parallelize(Seq(

new My_Record(555, "Luis, Earl"),

new My_Record(666, "Ann, Sally, Bob"),

new My_Record(111, "Bob, Tony" )

))

my_records.saveToCassandra("ks_7545", "hello_world",

SomeColumns ("pk", "value"))

// From CQLSH

SELECT * FROM ks_7545.hello_world ;

000-DTSE-Analytics-7545-60-PL-14 © DataStax, All Rights Reserved. Confidential.

Challenge 3: Read from DSE using RDDs

val rows = sc.cassandraTable[My_Record]("ks_7545", "hello_world").

select("pk", "value").

as( (i:Int, s:String ) => new My_Record(i, s) )

rows.collect().foreach(println)

000-DTSE-Analytics-7545-60-PL-15 © DataStax, All Rights Reserved. Confidential.

• We need to load the customer, orders,

and items tables from CSV; we use

these tables in later Practice Labs,

and need these tables to exist and

have data.

• Some degree of busy work; load at

least customer using Spark. You can

cheat and use CQL/other for orders Challenge 4:

and items.

Load customer, orders, items • Derive the DSE models from the SQL DSE tables from CSV DDL. Do all DDL using CQLSH.

• Add two columns to customer to

support the new, derived data.

000-DTSE-Analytics-7545-60-PL-16 © DataStax, All Rights Reserved. Confidential.

Working Goal:

From: Maury_Atwater To: DSE_HOTSHOT

Subject: Need this now !!!

Attached are 3 (count) SQL DDL files, customer, orders, and items, and 3 (count) ASCII Text CSV files.

I need these loaded into DSE now !!!

Maury Atwater, President On customer.zipcode, derive an east coast, of Atwater's west coast flag ("E-USA", "W-USA"). Also derive customer.company (company name) to uppercase .

-MA

000-DTSE-Analytics-7545-60-DU-17 © DataStax, All Rights Reserved, Confidential

Challenge 4: The instructor will specify the location of (n) Load customer, ASCII text files-

order, items • SQL DDL for customer, order, items. Convert

to CQL DDL; create whatever keyspace and

tables.

• Load all 3 tables from CSV; use Spark/Scala

for at least customer.

• Derive the 2 new columns for customer as

specified on previous page.

• Don't worry about optimizing the data model.

that work will come. Just do a 1:1 SQL -> CQL

mapping.

000-DTSE-Analytics-7545-60-PL-18 © DataStax, All Rights Reserved. Confidential.

Challenge 4: You are done when ..

• All three tables exist in DSE and

have data; customer, orders, items

• You have at least the steps to

complete customer in a nice (list)

000-DTSE-Analytics-7545-60-PL-19 © DataStax, All Rights Reserved. Confidential.

Lessons learned

000-DTSE-Analytics-7545-60-PL-20 © DataStax, All Rights Reserved. Confidential.

End of Unit:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Analytics-7545-60-PL-21
