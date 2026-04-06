# DSE Search: DSE Search, Day 2 Review

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Discussion Module

**Customer:** I am working through the DSE Search curriculum and need help with dse search, day 2 review. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This discussion module in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, day 2 review.

## Downloads

- [PDF slides](./7499-dse-search-day-2-review.pdf)
- [Original PowerPoint](../000-DTSE-Search-7499-DM-60%2C%20DSE%20Search%2C%20Day%202%20Review.pptx)

## Converted Slides

## Discussion

Review of What We Covered on Day 1

Module:

Search, Day 2 Review

000-DTSE-Search-7459-60-DM-1 © DataStax, All Rights Reserved. Confidential.

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

000-DTSE-Search-7442-60-DM-4 © DataStax, All Rights Reserved. Confidential.

DSE Search Index 1 Integer, Double, String, ...

Sounds Like 2 Case Insensitive

• Sorting Stemming

• Facet (Group by) (Other) • Wildcard (Text)

• Boosting

GeoSpatial • Proximity

• (Other) 3

Distance from point

Contained (other); Box, rectangle, polygon

(Time Series)

000-DTSE-Search-7443-60-DU-5 © DataStax, All Rights Reserved. Confidential.

DSE Search: the Analyzer

Analysis Phase: Index|

Query|(Both)

Unchained Analyzer (6+30)

Document (Column Value) Chained Analyzer

Char Tokenizer Filter Filter Document (Column Value) 0:M ! 1 0:M

40+ 10+ 8+

000-DTSE-Search-7443-60-DU-6 © DataStax, All Rights Reserved. Confidential.

Apache Solr, Impact on Disk Space, termVectors,

more ..

Source: Slide 36, https://www.slideshare.net/DataStax/solr47-f-inal ? https://data.world/datasets/twitter

000-DTSE-Search-7443-60-DU-7 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 6 of 12

ALTER SEARCH INDEX SCHEMA ON t1 ADD types.fieldType[@name='TextField18', @class='solr.TextField'] with '{"analyzer":{"tokenizer": {"class":"solr.StandardTokenizerFactory"}, "filter":{"class":"solr.BeiderMorseFilterFactory", "nameType":"GENERIC", "ruleType":"APPROX", "concat":"true", "languageSet":"auto"}}}'; ALTER SEARCH INDEX SCHEMA ON t1 ADD fields.field[@name='col4', @type='TextField18', @indexed='true', @multiValued='false', @stored='true']; RELOAD SEARCH INDEX ON t1; REBUILD SEARCH INDEX ON t1; col4

000-DTSE-Search-7445-60-DM-8 © DataStax, All Rights Reserved. Confidential.

Solr Admin UI: Core -> Analysis -> Column

• Debug existing analyzer

– (Have to manually decompose: Technique)

• Index | Query | (Both)

• Displays (resource file

data)

000-DTSE-Search-7445-60-DM-9 © DataStax, All Rights Reserved. Confidential.

Solr Admin UI: Core ->

Query

• $$$

• Adhoc queries

• fl, *.score

• debugQuery (SET EXPLAIN)

• Much more

000-DTSE-Search-7445-60-DM-10 © DataStax, All Rights Reserved. Confidential.

Field Type, Field, indexed=true

Attributes: Covered indexed=false

stored=t|f

docValues=t|f

multiValued=true

StrField multiValued=false

default= str

TextField precisionStep=n

positionIncrementGap=n TrieDoubleField termVectors=t|f

termPositions=t|f

termOffsets=t|f

omitNorms=t|f

000-DTSE-Search-7449-60-DM-11 © DataStax, All Rights Reserved. Confidential.

Field Type, Field,

Attributes: Covered

StrField

KeywordTokenizer

TextField

StandardTokenizer

TrieDoubleField

docValues Word Proximity

docValues

000-DTSE-Search-7449-60-DM-12 © DataStax, All Rights Reserved. Confidential.

CQL SELECT: (Core, other)

(JOINS)

SELECT ..

1.2.1 FROM ..

+

2.2.0.14 WHERE ..

GROUP BY ..

ORDER BY .. ;

• LIMIT | PARTITION LIMIT

• UDFs, UDAs, (+ native funcs & aggs)

(Core Yes, Core + Search, No)

• Paging (Not graph; Core and Search Yes)

000-DTSE-Search-7451-60-DM-13 © DataStax, All Rights Reserved. Confidential.

Query: Solr Server Side “Function Queries”

SELECT col1, col3, col4 FROM t10

WHERE • See solr_query = '{ "q":"*:*", ,https://lucene.apache.org/solr/gu "sort":"sum(col3, col4) asc" }'; ide/6_6/function-queries.html

• 20 or more by count, not all are col1 | col3 | col4 relevant ------+------+------

aaa | 1 | 2 • Used in predicates, value can not ccc | 1 | 5

ddd | 1 | 6 be returned to the client

bbb | 3 | 4

000-DTSE-Search-7451-60-DM-14 © DataStax, All Rights Reserved. Confidential.

Standard Query Parser: SELECT col1, col6 FROM t10

WHERE solr_query = '{ "q" : Parameters, q.op " {! q.op=AND} col6:(Mouse Mule)" }';

col1 | col6 Data is : ------+------ 'aaa', 'Mary' , 'Dog Cat Bird' (0 rows) 'bbb', 'Harry', 'Dog Mouse Cat'

'ccc', 'Dave' , 'Dog Mule Cat' ... 'ddd', 'David', 'Cat Dog Bird' '{ "q" : "{! q.op=OR}col6:(Mouse Mule)" }';

col1 | col6

------+---------------

ccc | Dog Mule Cat

bbb | Dog Mouse Cat

000-DTSE-Search-7451-60-DM-15 © DataStax, All Rights Reserved. Confidential.

Query: Facet, "col3,col4" : "field" : "col3", “distributed pivot facet”, "value" : 1, aka, decision tree” "count" : 3, "pivot" : "field" : "col4", "value" : 2, SELECT col1 FROM t10 "count" : 1 WHERE solr_query='{"q":"col1:*", "field" : "col4", "value" : 5, "facet":{"pivot":"col3,col4", "count" : 1 "limit":"-1"}}'; "field" : "col4", "value" : 6, See formatted query result on notes page. "count" : 1 "field" : "col3", "value" : 3, "count" :1, "pivot" : "field" : "col4", "value" :4, "count" : 1

000-DTSE-Search-7451-60-DM-16 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7459-60-DM-17
