# DSE Analytics: DSE Analytics, DataFrames, Datasets, SQL

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, dataframes, datasets, sql. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, dataframes, datasets, sql.

## Downloads

- [PDF slides](./7579-dse-analytics-data-frames-datasets-sql.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7579-PL-60%2C%20DSE%20Analytics%2C%20DataFrames%2C%20Datasets%2C%20SQL.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Unit 7578, where most of

the objects we create in this lab

were introduced.

• In this Practice Lab, we use DSE Analytics,

DataFrames CassandraSQLContext to read from

(customer, orders, items), and

populate a DSE Core table

containing attributes from all 3,

including an aggregate.

• Witness predicate pushdown

• Witness optimization

000-DTSE-Analytics-7579-PL-60-1 © DataStax, All Rights Reserved, Confidential

Challenge 1: Prerequisites

Prerequisites:

• Instructions are provided for Linux

• We will operate below recommended

settings; 1 OS node only, minimum 8

GB RAM, 12 GB RAM preferred

• That you have an operating single

node DSE Core cluster with DSE

Analytics enabled.

• All work done as ‘root’

000-DTSE-Analytics-7579-PL-60-2 © DataStax, All Rights Reserved, Confidential

Working Goal: From: Maury_Atwater To: DSE_HOTSHOT

Subject: Need this now !!!

 Big deal. You previously loaded customer_orders.

Now join the SQL modeled customer, orders, and items, and load the DSE modeled customer_orders2. We need order_total, calculated from items (quantity * price).

I also need Jobs that show: . Predicate pushdown Maury Atwater, President . Optimization of Atwater's

-MA

000-DTSE-Analytics-7579-60-PL-3 © DataStax, All Rights Reserved, Confidential

Challenge 1: Load DSE from 3 (SQL) tables

• In Practice Lab 7545 we loaded (customers,

orders, items); largely one CSV file per one

SQL modeled table.

• In Practice Lab 7571, we joined (customer

and orders) and loaded a merged DSE table

titled, customer_orders.

• Now we need to load customer_orders2

from all 3 SQL tables.

• Data from the third table, items, will be

calculated; order_total (from items: quantity

* price)

• Use CassandraSQLContext

• Use the Spark REPL

000-DTSE-Analytics-7579-PL-60-4 © DataStax, All Rights Reserved, Confidential

Challenge 1: SQL/CQL Assets

DROP KEYSPACE IF EXISTS

ks_7579;

CREATE KEYSPACE ks_7579 WITH

REPLICATION =

{'class':

'SimpleStrategy',

'replication_factor': 1};

USE ks_7579;

000-DTSE-Analytics-7579-PL-60-5 © DataStax, All Rights Reserved, Confidential

Challenge 1: SQL/CQL Assets

CREATE TABLE customer

(

customer_num INT PRIMARY KEY,

fname TEXT,

lname TEXT,

company TEXT,

address1 TEXT,

address2 TEXT,

city TEXT,

state TEXT,

zipcode TEXT,

phone TEXT

);

000-DTSE-Analytics-7579-PL-60-6 © DataStax, All Rights Reserved, Confidential

Challenge 1: SQL/CQL Assets

CREATE TABLE orders

(

order_num INT PRIMARY KEY,

order_date TEXT,

customer_num INT,

ship_instruct TEXT,

backlog TEXT,

po_num TEXT,

ship_date TEXT,

ship_weight TEXT,

ship_charge TEXT,

paid_date TEXT

);

000-DTSE-Analytics-7579-PL-60-7 © DataStax, All Rights Reserved, Confidential

Challenge 1: SQL/CQL Assets

CREATE TABLE items

(

item_num INT,

order_num INT,

stock_num INT,

manu_code TEXT,

quantity INT,

total_price FLOAT,

PRIMARY KEY ((order_num), item_num)

);

000-DTSE-Analytics-7579-PL-60-8 © DataStax, All Rights Reserved, Confidential

Challenge 1: SQL/CQL Assets

CREATE TABLE customer_orders2

(

order_num INT,

paid_date TEXT, All columns need a value // copied or derived from the customer_num INT, 3 source tables.

state TEXT,

order_total FLOAT,

PRIMARY KEY((order_num), customer_num)

);

000-DTSE-Analytics-7579-PL-60-9 © DataStax, All Rights Reserved, Confidential

Challenge 1: More ..

• After (n) minutes, cheat; there is a

partial solution at the end of this

unit (a 2 table/incomplete

solution)

• Save your work, you'll need it

later.

000-DTSE-Analytics-7579-PL-60-10 © DataStax, All Rights Reserved, Confidential

Challenge 2: Predicate Pushdown

• Create the entire runtime

environment to replicate the

predicate pushdown example

from Discussion Unit 7578

• You need/want two DataFrames;

Show qualifying and not

qualifying.

000-DTSE-Analytics-7579-PL-60-11 © DataStax, All Rights Reserved, Confidential

Challenge 3: DAG Optimization

• Create the entire runtime

environment to replicate the DAG

Optimization (sort before filter)

example from Discussion Unit

7578

• You need/want two DataFrames;

One to sort, and a second that

filters from the first.

000-DTSE-Analytics-7579-PL-60-12 © DataStax, All Rights Reserved, Confidential

Challenge 4 (Optional): Port Challenge 1 to IDE

• Take the steps you used to

complete challenge 1, and move

them to a true Scala program.

• Compile and run using the

Eclipse/IDE steps outlined in

Practice Lab 7554.

000-DTSE-Analytics-7579-PL-60-13 © DataStax, All Rights Reserved, Confidential

Lessons Learned

000-DTSE-Analytics-7579-PL-60-14 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7579-PL-60-15 © DataStax, All Rights Reserved, Confidential

Additional Detail:

000-DTSE-Analytics-7579-PL-60-16 © DataStax, All Rights Reserved, Confidential

Challenge 1: Hint

val recs_DF = spark.

sql(

"SELECT " +

" t2.order_num, " +

" (t3.quantity * t3.total_price) as order_total " +

"FROM " +

" ks_7579.orders t2, " +

" ks_7579.items t3 " +

"WHERE " +

" t2.order_num = " +

" t3.order_num " +

"GROUP BY " +

" t2.order_num, " +

" order_total "

)

000-DTSE-Analytics-7579-PL-60-17 © DataStax, All Rights Reserved, Confidential
