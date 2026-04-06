# DSE Search: Prereqs, Review prior to DSE Search

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Discussion Module

**Customer:** I am working through the DSE Search curriculum and need help with prereqs, review prior to dse search. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This discussion module in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around prereqs, review prior to dse search.

## Downloads

- [PDF slides](./7442-prereqs-review-prior-to-dse-search.pdf)
- [Original PowerPoint](../000-DTSE-Search-7442-DM-60%2C%20Prereqs%2C%20Review%20prior%20to%20DSE%20Search.pptx)

## Converted Slides

## Discussion

Review the briefest amount of material

related to DSE and DSE Core, so that we

may start to understand the Why and What Module: of DSE Search.

DSE Search Prerequisites • (One) DSE Object Hierarchy

• Brewer’s CAP Theorem, Consistency

Level (CL)

• Four Primary functional Areas to DSE

• Index (types/options) in DSE Core

000-DTSE-Search-7442-60-DM-1 © DataStax, All Rights Reserved. Confidential.

DSE Object Hierarchy

Discussion Lab:

Refrigerator Magnets - Match

the terms on the right with

the boxes on the left

000-DTSE-Search-7442-60-DM-2 © DataStax, All Rights Reserved. Confidential.

Discussion Lab: (One) DSE Object Hierarchy

• Replication Strategy E == G + H A: • Keyspace

• Clustering Column E: F: • Node (host)

B: • Table

• Cluster

• Primary Key C: • Replication Factor

• Rack D: E: F: • Data center

• Partitioning Key

J == K + M And answer the questions on the Notes Page-

000-DTSE-Search-7442-60-DM-3 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7442-60-DM-4 © DataStax, All Rights Reserved. Confidential.

Wikiepdia.com: Brewer’s CAP Theorem

Generally , choose two:

• “Consistency - Every read receives the most recent write or an error

• “Availability - Every request receives a (non-error) response

- without guarantee that it contains the most recent write

• “Partition - The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes

• “CAP is frequently misunderstood as if one has to choose to abandon one of the three guarantees at all times. In fact, the choice is really between consistency and availability only when a network partition or failure happens; at all other times, no trade-off has to be made.

Source: https://en.wikipedia.org/wiki/CAP_theorem

000-DTSE-Search-7442-60-DM-5 © DataStax, All Rights Reserved. Confidential.

CAP: Data Centers and Consistency Level (CL)

Data Center 1 Data Center 2 DB Network DB DB Interruption

DB

DB DB DB DB

App App

Clients

Clients

000-DTSE-Search-7442-60-DM-6 © DataStax, All Rights Reserved. Confidential.

The 4 Primary Functional Areas to DSE

• Only 2 of the 4 primary

functional areas to DSE

provide indexing technology

– DSE Core, primarily hash

– DSE Search, Tf-Idf (bitmap) Query

processing • All 4 primary functional areas

provide query processing Index and

query – Differentiated query predicates, processing or functionality

– Specific performance abilities

000-DTSE-Search-7442-60-DM-7 © DataStax, All Rights Reserved. Confidential.

Why DSE Core: 2 of (M) Value Propositions

000-DTSE-Search-7442-60-DM-8 © DataStax, All Rights Reserved. Confidential.

Wikipedia.com: B-Tree+ Index

• “In computer science, a B-tree is a self-

balancing tree data structure that keeps data

sorted and allows searches, sequential

access, insertions, and deletions in

logarithmic time.

• “An algorithm is said to take logarithmic time if

T(n) = O(log n). ... AnO(log n) algorithm is

considered highly efficient, as the ratio of the

number of operations to the size of the input

decreases, and tends to zero when n

increases. Source: https://en.wikipedia.org/wiki/B-tree

Source: https://en.wikipedia.org/wiki/Time_complexity#Loga rithmic_time

000-DTSE-Search-7442-60-DM-9 © DataStax, All Rights Reserved. Confidential.

Wikipedia.com: (Hash Index, time constant)

“In a well-dimensioned hash table, the average

cost (number of instructions) for each lookup

is independent of the number of elements

stored in the table.

Many hash table designs also allow arbitrary

insertions and deletions of key-value pairs, at

(amortized[2]) constant average cost per

operation.

Source: https://en.wikipedia.org/wiki/Hash_table

000-DTSE-Search-7442-60-DM-10 © DataStax, All Rights Reserved. Confidential.

DSE Core/(hash)

• Which Query Predicates are

Supported ,

• Which Queries are Core/Search?

Discussion Lab:

Design

000-DTSE-Search-7442-60-DM-11 © DataStax, All Rights Reserved. Confidential.

Discussion Lab: Just Core, Which Query

Predicates are Supported

SELECT * WHERE ... CREATE TABLE t1 ...

col? = (

col? > col1 TEXT,

AND ... / OR ... col2 TEXT, ...

ORDER BY PRIMARY KEY ((col1, col2)

col? ; col3, col4)

col?, col? ; ) WITH CLUSTERING ORDER BY

GROUP BY (col3 DESC, col4 ASC);

col?, col? ;

000-DTSE-Search-7442-60-DM-12 © DataStax, All Rights Reserved. Confidential.

Discussion Lab: Which are

Core/Search Queries SELECT * FROM t1

WHERE col1 = 10;

WHERE col1 LIKE ‘Chuck’;

WHERE col1 = 10 AND col2 = 20;

WHERE col1 = 10 AND col2 = 20 and col3 > 30; CREATE TABLE t1 ... ?? ; WHERE col1 = 10 and col2 = 20 ORDER BY col3;

WHERE solr_query =

'{ "q" : "(name:D* OR name:DAVE~1^8)

AND gender:M AND century:2000" }';

000-DTSE-Search-7442-60-DM-13 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7442-60-DM-14 © DataStax, All Rights Reserved. Confidential.

Other DSE Core (Indexes)

• Materialized Views

• Secondary Indexes

• (Custom Indexes)

• SASI Indexes

• (DSE Query Tables) Copyright: Village Roadshow Pictures

000-DTSE-Search-7442-60-DM-15 © DataStax, All Rights Reserved. Confidential.

DSE Core: Materialized Views

CREATE MATERIALIZED VIEW t1_v1 CREATE TABLE t1 ... AS PRIMARY KEY SELECT col1, ... , col8 ((col1, col2)) ); FROM t1

WHERE

col1 IS NOT NULL AND col2 IS NOT NULL

AND col7 IS NOT NULL

PRIMARY KEY (col1, col2, col7);

OR, PRIMARY KEY ((col8), col2, col1); OR, OR ..

000-DTSE-Search-7442-60-DM-16 © DataStax, All Rights Reserved. Confidential.

Materialized Views: You may not

CREATE MATERIALIZED VIEW t1_v2 AS CREATE TABLE t1 SELECT col1, ... , col8 ... FROM t1

PRIMARY KEY WHERE

col1 IS NOT NULL AND col2 IS NOT NULL AND ((col1, col2)) ); col7 IS NOT NULL AND col5 IS NOT NULL

PRIMARY KEY ( col1, col2, col7, col5 );

// InvalidRequest: Error from server: code=2200 [Invalid query]

// message="Cannot include more than one non-primary key column

// 'col5' in materialized view primary key"

000-DTSE-Search-7442-60-DM-17 © DataStax, All Rights Reserved. Confidential.

Materialized Views: You may not

CREATE MATERIALIZED VIEW t1_v2 AS

SELECT col1, ... , col8 CREATE TABLE t1

FROM t1 ..

WHERE PRIMARY KEY col1 IS NOT NULL AND col2 IS NOT NULL AND

((col1, col2)) ); col7 IS NOT NULL

PRIMARY KEY ( col1, col7 );

// InvalidRequest: Error from server: code=2200 [Invalid query]

// message="Cannot create Materialized View t1_v2 without

// primary key columns from base t1 (col2)"

000-DTSE-Search-7442-60-DM-18 © DataStax, All Rights Reserved. Confidential.

Materialized Views: You may not

CREATE MATERIALIZED VIEW t2_v1 AS

SELECT col1, ... , col8 CREATE TABLE t1 FROM t2 .. WHERE PRIMARY KEY col1 IS NOT NULL AND col2 IS NOT NULL AND

((col1, col2), col3 IS NOT NULL AND col6 IS NOT NULL

PRIMARY KEY ( col1, col2, col3, col6 ); col3, col4) ); // InvalidRequest: Error from server: code=2200 [Invalid query]

// message="Cannot create Materialized View t2_v1 without

// primary key columns from base t2 (col4)"

000-DTSE-Search-7442-60-DM-19 © DataStax, All Rights Reserved. Confidential.

DSE Core: Secondary Indexes

SELECT * FROM T1 CREATE TABLE t1 .. Scatter/gather WHERE col3 = 'ddd'; PRIMARY KEY

(( col1, col2 )) );

SELECT * FROM T1 CREATE INDEX i2 WHERE col3 = 'ddd‘ Node local ON t1 (col3); AND col1 = ‘ddd’

AND col2 = ‘ddd’;

000-DTSE-Search-7442-60-DM-20 © DataStax, All Rights Reserved. Confidential.

Secondary Indexes: You may not

SELECT * FROM T1 WHERE col3 > 'ddd';

// InvalidRequest: Error from server: code=2200 [Invalid query]

// message="Cannot execute this query as it might involve data

// filtering and thus may have unpredictable performance.

// If you want to execute this query despite the performance

// unpredictability, use ALLOW FILTERING"

000-DTSE-Search-7442-60-DM-21 © DataStax, All Rights Reserved. Confidential.

Secondary Indexes: You may not

SELECT * FROM T1 WHERE col3 = 'ddd' ORDER BY col3;

// InvalidRequest: Error from server: code=2200 [Invalid query]

// message="ORDER BY with 2ndary indexes is not supported."

000-DTSE-Search-7442-60-DM-22 © DataStax, All Rights Reserved. Confidential.

Secondary Indexes: You may not

CREATE INDEX i3 ON t1 (col5, col6);

// InvalidRequest: Error from server: code=2200 [Invalid query]

// message="Only CUSTOM indexes support multiple columns"

000-DTSE-Search-7442-60-DM-23 © DataStax, All Rights Reserved. Confidential.

DSE Core: Two (?) Custom Indexes

CREATE TABLE ks_15.t1 (

An object titled, “custom index’ col1 text, ... displays in a DESCRIBE TABLE DESCRIBE TABLE t1; as the result of: CREATE CUSTOM INDEX • CREATE CUSTOM INDEX ... ks_15_t1_solr_query_index

These are “SASI Indexes”, ON ks_15.t1 (solr_query) USING covered next- 'com.datastax.bdp.search.solr.Cql3SolrSecondaryIndex';

• CREATE SEARCH INDEX ... CREATE CUSTOM INDEX i5 ON ks_15.t1 (col7)

USING These are DSE Search indexes

'org.apache.cassandra.index.sasi.SASIIndex';

000-DTSE-Search-7442-60-DM-24 © DataStax, All Rights Reserved. Confidential.

DSE Core: (Custom) SASI Indexes

CREATE CUSTOM INDEX i5

ON ks_15.t1 (col7)

USING

Beta 'org.apache.cassandra.index.sasi.SASIIndex' ;

// Warnings :

// SASI index was enabled for 'ks_15.t1'. SASI is still

// in beta, take extra caution when using it in

// production.

000-DTSE-Search-7442-60-DM-25 © DataStax, All Rights Reserved. Confidential.

DSE Core: (Query Tables)

SQL/relational-

• Data modeled regardless of use

• Codd/Date, Third Normal Form

• No/few redundant attributes

• Limiting cost factor, disk space/capacity

Post-relational/NoSQL-

• Data modeled entirely by use

• Derived/redundant data for performance

• Limiting cost factor, labor

000-DTSE-Search-7442-60-DM-26 © DataStax, All Rights Reserved. Confidential.

Given 3 DSE Core CQL Queries, Create

a Logical Data Model.

Practice Lab:

Design

000-DTSE-Search-7442-60-DM-27 © DataStax, All Rights Reserved. Confidential.

Practice Lab: DSE Core, Discuss How to Model-

• Select all guests that checked in at

a particular hotel on a given day,

sorted by time descending.

• Select all guest check ins for any

given hotel within any given 10-

minute window (E.g. 10:00-10:10,

13:42-13:52), regardless of day.

Order the results by check in time

descending.

• How many room-nights were at

hotel ‘Buena Vista’ on 2015-12-15 ?

000-DTSE-Search-7442-60-DM-28 © DataStax, All Rights Reserved. Confidential.

End of Practice

Lab:

000-DTSE-Search-7442-60-DM-29 © DataStax, All Rights Reserved. Confidential.

When to use Core, Search, (Analytics,

Graph) ?

Discussion Lab:

Design

000-DTSE-Search-7442-60-DM-30 © DataStax, All Rights Reserved. Confidential.

Discussion Lab: When to use Core, Search,

(Analytics, Graph) ?

• SLA must be within 0-10 ms, or can be

higher (100-250 ms+)

• Routine’s frequency, concurrency, spread

(capacity planning, cost)

• Syntactically/functionally, can it even be

done

000-DTSE-Search-7442-60-DM-31 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7442-60-DM-32 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7442-60-DM-33

Additional Detail:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7442-60-DM-34

WAN Ping Latencies:

Source: https://wondernetwork.com/pings

000-DTSE-Search-7442-60-DM-35 © DataStax, All Rights Reserved. Confidential.

Wikipedia.com: Tf-Idf Style Indexes

• “Nowadays, Tf-Idf is one of the most popular term-

weighting schemes; 83% of text-based recommender

systems in the domain of digital libraries use tf-idf.

• “Term frequency - the simplest choice is to use the

raw count of a term in a document.

• “Inverse document frequency - is a measure of how

much information the word provides, that is, whether

the term is common or rare across all documents. It is

the inverse fraction of the documents that contain the

word, obtained by dividing the total number of

documents by the number of documents containing

the term.

Source: https://en.wikipedia.org/wiki/Tf-idf https://en.wikipedia.org/wiki/Bitmap_index

000-DTSE-Search-7442-60-DM-36 © DataStax, All Rights Reserved. Confidential.

Tf-Idf (bitmap index) example- The y-axis is populated

with terms (tokens)

extracted from a given

column value.

The x-axis is the primary

key to a given row.

1 represents true, zero

false.

Which rows contain the

value, “trot” ?

Which rows contain the

values “trot” and

“ponies” ?

000-DTSE-Search-7442-60-DM-37 © DataStax, All Rights Reserved. Confidential.

Product Compatibility Matrix:

DSE and Cassandra

Determining which version of DSE maps

to which version of Cassandra-

Source: https://docs.datastax.com/en/landing_page/doc/landin g_page/compatibility.html

000-DTSE-Search-7442-60-DM-38 © DataStax, All Rights Reserved. Confidential.

Performance: Mat.View versus “The performance

difference is dramatic Secondary Indexes

even for small clusters,

but even more important

we see that indexed

performance levels off

when doubling from 8 to

16 nodes in the (AWS

m3.xl) cluster, as the

scatter/gather overhead

starts to become

significant.

Source: https://www.datastax.com/dev/bl og/materialized-view- performance-in-cassandra-3-x

000-DTSE-Search-7442-60-DM-39 © DataStax, All Rights Reserved. Confidential.

Solutions:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7442-60-DM-40

Discussion Lab: (One) DSE Object Hierarchy

A: Cluster Keyspace E == G + H

Table E: F: Keyspace == Replication Strategy

+ Replication Factor B: Data center

J == K + M

C: Rack Primary Key == Partitioning Key

+ Clustering Column

Node (host) D: E: F: Table

Keyspace

000-DTSE-Search-7442-60-DM-41 © DataStax, All Rights Reserved. Confidential.
