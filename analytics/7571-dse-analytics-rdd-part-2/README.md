# DSE Analytics: DSE Analytics, RDD part 2

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, rdd part 2. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, rdd part 2.

## Downloads

- [PDF slides](./7571-dse-analytics-rdd-part-2.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7571-PL-60%2C%20DSE%20Analytics%2C%20RDD%20part%202.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on Discussion

Unit 7570, where most of the objects we create

in this lab were introduced.

• This Practice Lab has as a prerequisite Practice

Lab 7445, where we loaded the DSE tables

customer, orders, items from CSV. Practice Lab:

• This Practice Lab requires a working DSE DSE Analytics, Join, nulls, system, with DSE Analytics enabled.

.isDefined, .get, map,

• Because of the dependency on the "dse spark" filter, .saveToCassandra,

utility, this Practice Lab requires a ssh(C) and more

prompt on at least one node operating DSE

Analytics.

• Or, compile and run programs using an IDE.

000-DTSE-Analytics-7571-60-PL-1 © DataStax, All Rights Reserved. Confidential.

Working Goal: From: Maury_Atwater To: DSE_HOTSHOT

Subject: Need this now !!!

 Big deal. You previously loaded 3 tables.

Now join the SQL modeled customer and orders, and load the DSE modeled customer_orders.

I also need Jobs for: . Customers without orders . Count of orders by state . Orders where paid_date is null Maury Atwater, President . Count of orders by customer, sort by of Atwater's count descending

-MA

000-DTSE-Analytics-7571-60-PL-2 © DataStax, All Rights Reserved, Confidential

CQL Assets for DROP KEYSPACE IF EXISTS ks_7571;

Reference: CREATE KEYSPACE ks_7571 WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}; USE ks_7571;

CREATE TABLE customer ( customer_num INT PRIMARY KEY, fname TEXT, lname TEXT, company TEXT, address1 TEXT, address2 TEXT, city TEXT, state TEXT, zipcode TEXT, phone TEXT );

000-DTSE-Analytics-7571-60-PL-3 © DataStax, All Rights Reserved, Confidential

CQL Assets for CREATE TABLE orders ( Reference: order_num INT PRIMARY KEY, order_date TEXT, customer_num INT, ship_instruct TEXT, backlog TEXT, po_num TEXT, ship_date TEXT, ship_weight FLOAT, ship_charge FLOAT, paid_date TEXT ); CREATE TABLE customer_orders ( order_num INT, paid_date TEXT, customer_num INT, state TEXT, PRIMARY KEY((order_num), customer_num) );

000-DTSE-Analytics-7571-60-PL-4 © DataStax, All Rights Reserved, Confidential

Challenge 1: Customers with no Orders

• Read from customer and orders

• Use a leftOuterJoin

• Then filter using .isDefined

• Just read; customer_num (both

tables), state, order_num,

paid_date

• Why ? We can re-use these

RDDs later Source:https://www.pinterest.com/pin/5629568257464509/

• There are 11 rows by count

000-DTSE-Analytics-7571-60-PL-5 © DataStax, All Rights Reserved, Confidential

Challenge 2: Load

far By the hardest of the challenges customer_orders

• It's always the little things; nulls, nits

in the APIs, yadda

• Keep it simple; we're only keeping 4

columns to reduce burden

• Best effort, then check answer at end

of unit

• You need customer_orders for the

remaining challenges

• All other challenges are do-able

000-DTSE-Analytics-7571-60-PL-6 © DataStax, All Rights Reserved, Confidential

Challenge 3: Count of Orders by State

• Need customer_orders

• 4 lines; map, and reduceByKey()

• Output just state and count

Source: https://www.eater.com/2016/9/26/13051528/most-ordered-food-delivery-america

000-DTSE-Analytics-7571-60-PL-7 © DataStax, All Rights Reserved, Confidential

Challenge 4: Rows where paid_date is (null)

• Mismatch between: DSE, Spark,

Scala

• Advice in Scala is to remove nulls

immediately; use a constant

• Spark has methods

• DSE has other ideas of its own

• Our solution used a constant, ("N/A")

000-DTSE-Analytics-7571-60-PL-8 © DataStax, All Rights Reserved, Confidential

Challenge 5: High Value Customers

• Count of orders by customer, sort

by count descending

• Output customer number and

count

• Bonus: also output state

• 5 lines

000-DTSE-Analytics-7571-60-PL-9 © DataStax, All Rights Reserved, Confidential

Lessons learned

000-DTSE-Analytics-7571-60-PL-10 © DataStax, All Rights Reserved. Confidential.

End of Unit:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Analytics-7571-60-PL-11

Additional Detail:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Analytics-7571-60-PL-12

Answer to just challenge 2 is on the Notes page-

000-DTSE-Analytics-7571-60-PL-13 © DataStax, All Rights Reserved, Confidential
