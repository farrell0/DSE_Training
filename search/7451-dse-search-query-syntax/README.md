# DSE Search: DSE Search, Query Syntax

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Discussion Module

**Customer:** I am working through the DSE Search curriculum and need help with dse search, query syntax. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This discussion module in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, query syntax.

## Downloads

- [PDF slides](./7451-dse-search-query-syntax.pdf)
- [Original PowerPoint](../000-DTSE-Search-7451-DM-60%2C%20DSE%20Search%2C%20Query%20Syntax.pptx)

## Converted Slides

## Discussion

Introduce DSE Search Query Syntax Discussion

Module:

DSE Search, Query

Syntax

000-DTSE-Search-7451-60-DM-1 © DataStax, All Rights Reserved. Confidential.

Describe the Queries on the Pages

That Follow-

Discussion Lab:

Tell Me Something I Don’t

Know

000-DTSE-Search-7451-60-DM-2 © DataStax, All Rights Reserved. Confidential.

Describe the Queries- WHERE col1 = 10;

WHERE col1 LIKE ‘Chuck’;

WHERE col1 = 10 AND col2 = 20;

WHERE col1 = 10 AND col2 = 20

AND col3 > 30;

Core, Search WHERE col1 = 10 and col2 = 20 Field Type, Field Attributes ORDER BY col3; (Other objects)

WHERE solr_query = CQL Predicates '{ "q" : "(name:D* OR name:DAVE~1^8)

AND gender:M AND century:2000" }';

000-DTSE-Search-7451-60-DM-3 © DataStax, All Rights Reserved. Confidential.

Describe the Queries- WHERE col3 > 'ddd';

WHERE col1 = 10 OR col2 = 20;

WHERE solr_query = '{ "q" : "col3:Dave" }' ;

solr_query = '{ "q" : "col3:(Dava Rooney)" }' ;

solr_query = '{ "q" : "col4:(zah hut)" }' ; Core, Search solr_query = '{ "q" : "col4:Starrbux" }' ; Field Type, Field Attributes

(Other objects) solr_query = '{"q":"*:*", "sort":"col0 asc"}' LIMIT 12;

CQL Predicates FROM t3 ORDER BY col6 ASC,

col7 DESC, col3 ASC;

Default Search limit

WHERE col6 > 12.0 AND col7 < 26;

WHERE col6 > 12.0 OR col7 < 26;

000-DTSE-Search-7451-60-DM-4 © DataStax, All Rights Reserved. Confidential.

Describe the Queries-

WHERE solr_query = '{"q" : "col6:

[12.0 TO *] AND col7:[* TO 26]",

"sort":"col6 ASC, col7 DESC, col3 ASC" }';

WHERE col5 LIKE '%ar%';

WHERE col4 IN (2, 4); Core, Search WHERE col9 CONTAINS ('Vault'); Field Type, Field Attributes

(Other objects) WHERE solr_query = 'col8:

[15.9 TO 16.00003]'; CQL Predicates

000-DTSE-Search-7451-60-DM-5 © DataStax, All Rights Reserved. Confidential.

Describe the Queries-

WHERE solr_query = '{ "q" : "col73:

(Chuck David Todd)"}';

WHERE solr_query = '{ "q" : "col73:

(+Chuck +David +Todd)"}'; Core, Search

Field Type, Field Attributes WHERE solr_query='col2:"test space"~10'; (Other objects)

WHERE solr_query='"test space"~2'; CQL Predicates

WHERE solr_query = '{ "q" : Default Search limit "(col73:*huck^8 OR col74:chuck~1)" }' ;

000-DTSE-Search-7451-60-DM-6 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7451-60-DM-7 © DataStax, All Rights Reserved. Confidential.

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

000-DTSE-Search-7451-60-DM-8 © DataStax, All Rights Reserved. Confidential.

DSE Search 6.0: Can not

A DSE Search query can only return column values from the

DSE table proper:

• Not score, not any Solr virtual columns

• Not any Solr function queries DataStax (Returned to DSE No, used on Solr side Yes) Internal Use • No index time boost, only query time boost Only

https://lucene.apache.org/solr/guide/6_6/function-

queries.html

https://datastax.jira.com/browse/DSP-8229

https://datastax.jira.com/browse/DSP-13788

000-DTSE-Search-7451-60-DM-9 © DataStax, All Rights Reserved. Confidential.

DSE Search 6.0: Can not

A DSE Search query can not run DSE UDFs/UDAs-

CREATE OR REPLACE FUNCTION my_sum( i_arg1 int, i_arg2 int )

RETURNS NULL ON NULL INPUT

RETURNS int DataStax LANGUAGE JAVA AS ' Internal Use return i_arg1 + i_arg2 ; '; Only

SELECT col1, my_sum(col3, col4) FROM t10

WHERE solr_query = '{ "q" : "col3 > 0" }';

// InvalidRequest: Error from server: code=2200 [Invalid query] message= // "Aliased column names, UDFs and similar features are not available for // Solr queries. Offending inputs are [col4] and [ks_7451.my_sum(col3, col4)]."

000-DTSE-Search-7451-60-DM-10 © DataStax, All Rights Reserved. Confidential.

CQL SELECT: Search

solr_query = “”

• CQL (non JSON)

• JSON

Have already seen:

• “q”

• Word + -

• Phrase ( + - )

• Boost ^

• Fuzzy ~

• sort

Source: https://docs.datastax.com/en/dse/6.0/cql/cql/cql_using/search_index/ siQuerySyntax.html#siQuerySyntax

000-DTSE-Search-7451-60-DM-11 © DataStax, All Rights Reserved. Confidential.

The next few pages detail the

runtime environment used (tables,

data, indexes) in the sample

Runtine used in queries to follow-

the examples

that follow

000-DTSE-Search-7451-60-DM-12 © DataStax, All Rights Reserved. Confidential.

Sample Runtime Used .. page 1 of 3

DROP KEYSPACE ks_7451; CREATE TABLE t10

CREATE KEYSPACE ks_7451 WITH (

REPLICATION = {'class': col1 TEXT,

'SimpleStrategy', col2 TEXT,

'replication_factor': 1}; col3 INT,

USE ks_7451; col4 INT,

col5 TEXT,

CREATE TYPE my_udt col6 TEXT,

( col7 TEXT,

colm TEXT, col8 TEXT,

coln TEXT col9 SET <TEXT>,

); col0 FROZEN<my_udt>,

PRIMARY KEY ((col1, col2)) );

000-DTSE-Search-7451-60-DM-13 © DataStax, All Rights Reserved. Confidential.

Sample Runtime Used .. page 2 of 3

INSERT INTO t10

(col1, col2, col3, col4, col5, VALUES col6, col7, col8, col9, col0) ('ccc', 'ccc', 1, 5, 'Dave', VALUES 'Dog Mule Cat', 'ccc', 'ccc', ('aaa', 'aaa', 1, 2, 'Mary', {'Sprite', '7-Up'}, 'Dog Cat Bird', 'aaa', 'aaa', { colm : 'ccc' , coln : 'ccc' } ); {'Coke', 'Diet Coke'},

{ colm : 'aaa' , coln : 'aaa' } ); VALUES

('ddd', 'ddd', 1, 6, 'David', VALUES 'Cat Dog Bird', 'ddd', 'ddd', ('bbb', 'bbb', 3, 4, 'Harry', {'Orange'}, 'Dog Mouse Cat', 'bbb', 'bbb', { colm : 'ddd' , coln : 'ddd' } ); {'Mtn Dew', 'Vault'},

{ colm : 'bbb' , coln : 'bbb' } );

000-DTSE-Search-7451-60-DM-14 © DataStax, All Rights Reserved. Confidential.

Sample Runtime Used .. page 3 of 3

CREATE SEARCH INDEX ON t10 WITH

COLUMNS col1, col2, col3,

col4, col9, col0 { docValues : true }; ALTER SEARCH INDEX SCHEMA ON t10

ADD fields.field[@name=' col6 ', ALTER SEARCH INDEX SCHEMA ON t10 @type='TextField_10', @indexed='true', ADD types.fieldType[@name='TextField_10', @multiValued='false', @stored='true']; @class='solr.TextField']

with '{"analyzer":{"tokenizer": RELOAD SEARCH INDEX ON t10; {"class":"solr. StandardTokenizerFactory "} }}'; REBUILD SEARCH INDEX ON t10;

ALTER SEARCH INDEX SCHEMA ON t10

ADD fields.field[@name=' col5 ', What did each column @type='TextField_10', @indexed='true', receive index wise ? @multiValued='false', @stored='true'];

000-DTSE-Search-7451-60-DM-15 © DataStax, All Rights Reserved. Confidential.

DSE Search CQL

SELECT Syntax

Source: https://www.autoblog.com/2018/02/12/range-rover- phev-china-heavens-gate/

000-DTSE-Search-7451-60-DM-16 © DataStax, All Rights Reserved. Confidential.

Query: Term

SELECT col1, col5 FROM t10 WHERE

solr_query = '{ "q" : "col5:Mary" }';

Data is : col1 | col5

'aaa', 'Mary' , 'Dog Cat Bird' ------+------

'bbb', 'Harry', 'Dog Mouse Cat' aaa | Mary

'ccc', 'Dave' , 'Dog Mule Cat'

solr_query = '{ "q" : "col5:(Mary || Harry)" }'; 'ddd', 'David', 'Cat Dog Bird'

col1 | col5

------+-------

bbb | Harry

aaa | Mary

000-DTSE-Search-7451-60-DM-17 © DataStax, All Rights Reserved. Confidential.

Query: Term

SELECT col1, col6 FROM t10 WHERE

Data is : solr_query = '{ "q" : "col6:Dog" }';

'aaa', 'Mary' , 'Dog Cat Bird'

'bbb', 'Harry', 'Dog Mouse Cat' col1 | col6 'ccc', 'Dave' , 'Dog Mule Cat' ------+--------------- 'ddd', 'David', 'Cat Dog Bird' ddd | Cat Dog Bird

ccc | Dog Mule Cat

bbb | Dog Mouse Cat

aaa | Dog Cat Bird

000-DTSE-Search-7451-60-DM-18 © DataStax, All Rights Reserved. Confidential.

SELECT col1, col6 FROM t10 Query: Phrase WHERE solr_query = '{ "q" :

"col6: (Dog Mule Cat) " }';

Boolean ?

col1 | col6

------+--------------- Data is : ccc | Dog Mule Cat

'aaa', 'Mary' , 'Dog Cat Bird' ddd | Cat Dog Bird

'bbb', 'Harry', 'Dog Mouse Cat' bbb | Dog Mouse Cat

'ccc', 'Dave' , 'Dog Mule Cat' aaa | Dog Cat Bird 'ddd', 'David', 'Cat Dog Bird'

WHERE solr_query = '{ "q" :

"col6: (+Dog +Mule +Cat) " }';

col1 | col6 Boolean ?

------+--------------

ccc | Dog Mule Cat

000-DTSE-Search-7451-60-DM-19 © DataStax, All Rights Reserved. Confidential.

SELECT col1, col6 FROM t10 Query: Phrase WHERE solr_query = '{ "q" :

"col6: (+Dog +Cat && -Mouse -Mule) " }';

col1 | col6

------+-------------- Data is : ddd | Cat Dog Bird 'aaa', 'Mary' , 'Dog Cat Bird' aaa | Dog Cat Bird 'bbb', 'Harry', 'Dog Mouse Cat'

'ccc', 'Dave' , 'Dog Mule Cat' WHERE solr_query = '{ "q" : 'ddd', 'David', 'Cat Dog Bird' "col6: (+Dog -Mule +Cat) " }';

col1 | col6

------+---------------

ddd | Cat Dog Bird

bbb | Dog Mouse Cat

aaa | Dog Cat Bird

000-DTSE-Search-7451-60-DM-20 © DataStax, All Rights Reserved. Confidential.

Query: Range SELECT col1, col4 FROM t10

WHERE solr_query = '{ "q" :

"col4:[4 TO 5]" }';

col1 | col4 Data is : ------+------

ccc | 5 'aaa', 'Mary' , 'Dog Cat Bird'

bbb | 4 'bbb', 'Harry', 'Dog Mouse Cat'

'ccc', 'Dave' , 'Dog Mule Cat'

SELECT col1, col6 FROM t10 'ddd', 'David', 'Cat Dog Bird'

WHERE solr_query = '{ "q" :

"col6: [Mouse TO Mule] " }';

col1 | col6

------+---------------

ccc | Dog Mule Cat

bbb | Dog Mouse Cat

000-DTSE-Search-7451-60-DM-21 © DataStax, All Rights Reserved. Confidential.

Query: Substring SELECT col1, col5 FROM t10 WHERE

solr_query = '{ "q" : "col5:Mar*" }';

solr_query = '{ "q" : "col5:*ary" }';

Data is : col1 | col5

'aaa', 'Mary' , 'Dog Cat Bird' ------+------ (Both) 'bbb', 'Harry', 'Dog Mouse Cat' aaa | Mary

'ccc', 'Dave' , 'Dog Mule Cat'

solr_query = '{ "q" : "col5:*ar*" }'; 'ddd', 'David', 'Cat Dog Bird'

col1 | col5 Performance implication ? ------+-------

bbb | Harry

aaa | Mary

000-DTSE-Search-7451-60-DM-22 © DataStax, All Rights Reserved. Confidential.

Query: Substring, and negate

SELECT col1, col6 FROM t10 WHERE Data is : solr_query = '{ "q" : "col6: 'aaa', 'Mary' , 'Dog Cat Bird' (+Dog +Cat && -M*)" }'; 'bbb', 'Harry', 'Dog Mouse Cat'

'ccc', 'Dave' , 'Dog Mule Cat' col1 | col6 'ddd', 'David', 'Cat Dog Bird' ------+--------------

ddd | Cat Dog Bird

aaa | Dog Cat Bird

000-DTSE-Search-7451-60-DM-23 © DataStax, All Rights Reserved. Confidential.

Query: Fuzzy Search

SELECT col1, col5 FROM t10 Data is :

WHERE solr_query = '{ "q" : 'aaa', 'Mary' , 'Dog Cat Bird'

'bbb', 'Harry', 'Dog Mouse Cat' " col5:arry~2 " }';

'ccc', 'Dave' , 'Dog Mule Cat'

'ddd', 'David', 'Cat Dog Bird' col1 | col5

------+-------

bbb | Harry

aaa | Mary

000-DTSE-Search-7451-60-DM-24 © DataStax, All Rights Reserved. Confidential.

Query: Word Proximity

SELECT col1, col6 FROM t10 WHERE

solr_query = 'col6:" Cat Bird"~0 ';

Data is : col1 | col6 'aaa', 'Mary' , 'Dog Cat Bird' ------+-------------- 'bbb', 'Harry', 'Dog Mouse Cat' aaa | Dog Cat Bird 'ccc', 'Dave' , 'Dog Mule Cat'

'ddd', 'David', 'Cat Dog Bird' solr_query = 'col6: "Cat Bird"~1 ;

col1 | col6

------+--------------

aaa | Dog Cat Bird

ddd | Cat Dog Bird

000-DTSE-Search-7451-60-DM-25 © DataStax, All Rights Reserved. Confidential.

Query: Boosting SELECT col1, col6 FROM t10 WHERE

solr_query = '{ "q" : "(col6:Mule OR

col6:Mouse^16)" }';

col1 | col6 Data is : ------+--------------- 'aaa', 'Mary' , 'Dog Cat Bird' bbb | Dog Mouse Cat 'bbb', 'Harry', 'Dog Mouse Cat' ccc | Dog Mule Cat 'ccc', 'Dave' , 'Dog Mule Cat'

'ddd', 'David', 'Cat Dog Bird' SELECT col1, col6 FROM t10 WHERE

solr_query = '{ "q" : " (col6:Mule OR

col6:Mouse^=1.0)" }' LIMIT 1 ;

col1 | col6

------+---------------

bbb | Dog Mouse Cat

000-DTSE-Search-7451-60-DM-26 © DataStax, All Rights Reserved. Confidential.

Query: Joins Apache Solr joins do not equal SQL joins;

most similar to a nested SELECT;

https://wiki.apache.org/solr/Join

In effect, this Apache Solr search statement,

WHERE solr_query='{"q":"*:*", "fq":

"{!join from=cola to=col5 force=true

fromIndex=ks_7451.t11} colb:Bob"}';

Would equal the legacy SQL SELECT statement,

SELECT ...

WHERE outer_id IN (SELECT inner_id

FROM collection1 where cola = col5

AND colb = “Bob”;

000-DTSE-Search-7451-60-DM-27 © DataStax, All Rights Reserved. Confidential.

Query: Joins, how to DROP TABLE t11;

CREATE TABLE t11

(

cola TEXT,

colb TEXT,

PRIMARY KEY ((cola))

);

INSERT INTO t11 (cola, colb)

VALUES ('Mary', 'Schulte');

VALUES ('Harry', 'Johnson');

VALUES ('Dave', 'Wilson');

VALUES ('David', 'Bowie');

CREATE SEARCH INDEX ON t11;

000-DTSE-Search-7451-60-DM-28 © DataStax, All Rights Reserved. Confidential.

SELECT col1, col5 FROM t10 Query: Joins, how to WHERE solr_query='{"q":"*:*", "fq":

"{ !join from=cola to=col5 force=true

fromIndex=ks_7451.t11 } colb:Schulte "}'; Data is :

'aaa', 'Mary' , 'Dog Cat Bird' col1 | col5 'bbb', 'Harry', 'Dog Mouse Cat' ------+------ 'ccc', 'Dave' , 'Dog Mule Cat' aaa | Mary 'ddd', 'David', 'Cat Dog Bird‘

WHERE solr_query='{"q":"*:*", "fq": 'Mary', 'Schulte' "{!join from=cola to=col5 force=true 'Harry', 'Johnson' fromIndex=ks_7451.t11} *:* "}'; 'Dave', 'Wilson'

'David', 'Bowie' col1 | col5

------+-------

ddd | David

ccc | Dave

bbb | Harry

aaa | Mary 000-DTSE-Search-7451-60-DM-29 © DataStax, All Rights Reserved. Confidential.

Query: Collections (Set, List, Map)

CREATE TABLE ...

col9 SET <TEXT>

SELECT col1, col9 FROM t10 WHERE

solr_query='col9:" Mtn Dew "';

col1 | col9

------+----------------------

bbb | {'Mtn Dew', 'Vault'}

000-DTSE-Search-7451-60-DM-30 © DataStax, All Rights Reserved. Confidential.

Query: UDTs

SELECT col1, col0 FROM t10

WHERE solr_query='{!tuple}col0.colm:ddd';

col1 | col0

------+----------------------------

ddd | {colm: 'ddd', coln: 'ddd'}

WHERE solr_query='-{!tuple}col0.colm:ddd';

col1 | col0

------+----------------------------

ccc | {colm: 'ccc', coln: 'ccc'}

bbb | {colm: 'bbb', coln: 'bbb'}

aaa | {colm: 'aaa', coln: 'aaa'}

000-DTSE-Search-7451-60-DM-31 © DataStax, All Rights Reserved. Confidential.

Query: Solr Server Side “Function Queries”

SELECT col1, col3, col4 FROM t10

WHERE • See solr_query = '{ "q":"*:*", ,https://lucene.apache.org/solr/gu "sort":"sum(col3, col4) asc" }'; ide/6_6/function-queries.html

• 20 or more by count, not all are col1 | col3 | col4 relevant ------+------+------

aaa | 1 | 2 • Used in predicates, value can not ccc | 1 | 5

ddd | 1 | 6 be returned to the client

bbb | 3 | 4

000-DTSE-Search-7451-60-DM-32 © DataStax, All Rights Reserved. Confidential.

Query: DSE UDF/UDA and Search

cassandra.yaml SELECT col1, my_sum(col3, col4) enable_user_defined_functions=true FROM t10

WHERE solr_query = '{ "q" : "col3 > 0" }'; CREATE OR REPLACE FUNCTION

my_sum( i_arg1 int, i_arg2 int ) InvalidRequest: Error from server: RETURNS NULL ON NULL INPUT code=2200 [Invalid query] message= RETURNS int "Aliased column names, UDFs and LANGUAGE JAVA AS ' similar features are not available for return i_arg1 + i_arg2 ; Solr queries. ‘;

000-DTSE-Search-7451-60-DM-33 © DataStax, All Rights Reserved. Confidential.

Query: Regex

SELECT col1, col6 FROM t10 WHERE

solr_query = '{ "q" : "col6:/[Dd]og/" }';

Also available as a Filter;

PatternReplaceFilter col1 | col6

------+---------------

ddd | Cat Dog Bird

ccc | Dog Mule Cat

bbb | Dog Mouse Cat

aaa | Dog Cat Bird

000-DTSE-Search-7451-60-DM-34 © DataStax, All Rights Reserved. Confidential.

DSE Search,

Query: Facets

000-DTSE-Search-7451-60-DM-35 © DataStax, All Rights Reserved. Confidential.

Query: Facets, “facet”

“facet”

SELECT * FROM t10 WHERE Data is : solr_query='{"q":"*:*", 'aaa', 'aaa', 1, 2, 'aaa', "facet":{"field":"col3"}}'; 'bbb', 'bbb', 3, 4, 'bbb',

'ccc', 'ccc', 1, 5, 'ccc', facet_fields 'ddd', 'ddd', 1, 6, 'ddd', ------------------------

{"col3":{"1":3,"3":1}}

000-DTSE-Search-7451-60-DM-36 © DataStax, All Rights Reserved. Confidential.

Query: Facets, “query facet” “query facet”

SELECT * FROM t10

WHERE solr_query='{"q":"*:*",

"facet":{"query":"col3:1"}}';

Data is : facet_queries 'aaa', 'aaa', 1, 2, 'aaa', --------------- 'bbb', 'bbb', 3, 4, 'bbb', {"col3:1":3} 'ccc', 'ccc', 1, 5, 'ccc',

'ddd', 'ddd', 1, 6, 'ddd', solr_query='{"q":"col3:1",

"facet":{"field":"col3"}}';

facet_fields

------------------------

{"col3":{"1":3,"3":0}}

000-DTSE-Search-7451-60-DM-37 © DataStax, All Rights Reserved. Confidential.

Query, Facets, “multiple query”

SELECT * FROM t10

Data is : WHERE solr_query='{"q":"*:*",

'aaa', 'aaa', 1, 2, 'aaa', "facet":{"query":["col3:[0 TO *]",

'bbb', 'bbb', 3, 4, 'bbb', "col4:[* TO 5]"]}}'; 'ccc', 'ccc', 1, 5, 'ccc',

'ddd', 'ddd', 1, 6, 'ddd', facet_queries

---------------------------------------

{"col3:[0 TO *]":4,"col4:[* TO 5]":3}

000-DTSE-Search-7451-60-DM-38 © DataStax, All Rights Reserved. Confidential.

Query: Facet, "col3,col4" : "field" : "col3", “distributed pivot facet”, "value" : 1, aka, decision tree” "count" : 3, "pivot" : "field" : "col4", "value" : 2, SELECT col1 FROM t10 "count" : 1 WHERE solr_query='{"q":"col1:*", "field" : "col4", "value" : 5, "facet":{"pivot":"col3,col4", "count" : 1 "limit":"-1"}}'; "field" : "col4", "value" : 6, See formatted query result on notes page. "count" : 1 "field" : "col3", "value" : 3, "count" :1, "pivot" : "field" : "col4", "value" :4, "count" : 1

000-DTSE-Search-7451-60-DM-39 © DataStax, All Rights Reserved. Confidential.

Query: Facets, range facet,

aka “bucketing” "col3" :

"counts" :

"-10" : 0,

"-8" : 0, SELECT * FROM t10 "-6" : 0, WHERE solr_query= "-4" : 0, '{"q":"col1:*", "-2" : 0, "facet":{"range":"col3", "0" : 3, "f.col3.range.start":-10, "2" : 1,

"f.col3.range.end":10, "4" : 0,

"6" : 0, "range.gap":2} }'; "8" : 0

"gap" : 2,

"start" : -10,

"end" : 10

000-DTSE-Search-7451-60-DM-40 © DataStax, All Rights Reserved. Confidential.

DSE Search,

Query:

(switches), query parsers,

“q” / “fq”

000-DTSE-Search-7451-60-DM-41 © DataStax, All Rights Reserved. Confidential.

SELECT * FROM t10 Query: (switches)

WHERE solr_query = '{"q" : "*:*",

"distrib.singlePass" : true }';

Single pass (true):

• More disk, network total // Value is in ms, this example 30 secs • Saves 1 network round trip SELECT * FROM t10

• Generally, less efficient, more WHERE solr_query = '{"q" : "*:*",

expensive "timeAllowed":30000 }';

• Why ? Huge network latency

• Directing a Search query to a specific

node; see Url

• Other

000-DTSE-Search-7451-60-DM-42 © DataStax, All Rights Reserved. Confidential.

Query: Parsers Default is: Standard Query Parser

https:// lucene.apache.org/solr/guide/6_6/th e-standard-query-parser.html SELECT col1, col6 FROM t10

WHERE solr_query='{"q" : Many others (Urls on notes page):

"{!edismax qf=col6}Dog AND Cat"}'; • dismax

• edismax (Extended dismax)

• (others) col1 | col6

------+--------------- Why:

ddd | Cat Dog Bird • Change default Boolean

behavior ccc | Dog Mule Cat • Better/easier support for phrases bbb | Dog Mouse Cat • Need new predicates-

aaa | Dog Cat Bird • 10+ other reasons

000-DTSE-Search-7451-60-DM-43 © DataStax, All Rights Reserved. Confidential.

Query: “q” and “fq” (query, filter query)

“This parameter can be used to • Most queries thus far (JSON) have specify a query that can be used to been “q”, query predicate restrict the super set of documents

• “fq” are a further set of predicates that can be returned, without

influencing score. applied to the results of “q”

- Not a correlated subquery or It can be very useful for speeding up similar, (no new columns, rows) complex queries since the queries - Just further (filtering) specified with fq are cached

independently from the main query.

• fq filter activity does not affect Caching means the same filter is score used again for a later query.

• Most common means to OOM: DSE

Source: https://wiki.apache.org/solr/CommonQueryParameters#fq Tech Support, use wisely

000-DTSE-Search-7451-60-DM-44 © DataStax, All Rights Reserved. Confidential.

Query: “q” and “fq” (query, filter query)

SELECT col1, col6 FROM t10

WHERE solr_query = '{ "q" :"col6:Dog",

"fq" : "col6:Cat", "fq" : "col6:Bird" } ';

col1 | col6

------+--------------

ddd | Cat Dog Bird

aaa | Dog Cat Bird

000-DTSE-Search-7451-60-DM-45 © DataStax, All Rights Reserved. Confidential.

DSE Search CQL

SELECT Syntax

Review

000-DTSE-Search-7451-60-DM-46 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7451-60-DM-47

Additional Content:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7451-60-DM-48

Standard Query Parser: Parameters

• “q”, the standard, required

parameter we have seen

throughout

• “df”, specify a query time

default field

• “q.op”, change the default OR

condition to AND

• Begin with “{!”, end with “}”,

any number of key value pairs

000-DTSE-Search-7451-60-DM-49 © DataStax, All Rights Reserved. Confidential.

Standard Query Parser: Parameters, df

SELECT col1, col6 FROM t10

WHERE solr_query = Data is : ‘{ "q" : "col6:(Mouse Mule)" }'; 'aaa', 'Mary' , 'Dog Cat Bird'

'bbb', 'Harry', 'Dog Mouse Cat' '{ "q" : " {! df=col6} (Mouse Mule)" }'; 'ccc', 'Dave' , 'Dog Mule Cat'

'ddd', 'David', 'Cat Dog Bird' col1 | col6

------+---------------

ccc | Dog Mule Cat

bbb | Dog Mouse Cat

000-DTSE-Search-7451-60-DM-50 © DataStax, All Rights Reserved. Confidential.

Standard Query Parser: SELECT col1, col6 FROM t10

WHERE solr_query = '{ "q" : Parameters, q.op " {! q.op=AND} col6:(Mouse Mule)" }';

col1 | col6 Data is : ------+------ 'aaa', 'Mary' , 'Dog Cat Bird' (0 rows) 'bbb', 'Harry', 'Dog Mouse Cat'

'ccc', 'Dave' , 'Dog Mule Cat' ... 'ddd', 'David', 'Cat Dog Bird' '{ "q" : "{! q.op=OR}col6:(Mouse Mule)" }';

col1 | col6

------+---------------

ccc | Dog Mule Cat

bbb | Dog Mouse Cat

000-DTSE-Search-7451-60-DM-51 © DataStax, All Rights Reserved. Confidential.

dismax Query Parser: Parameters

• “q” , the standard

• “q.alt” , Calls the standard query parser and defines query input strings, when the

q parameter is not used.

• “qf” , Query Fields: specifies the fields in the index on which to perform the query.

If absent, defaults to df.

• “mm” , Minimum "Should" Match: specifies a minimum number of clauses that

must match in a query.

• “pf” , Phrase Fields: boosts the score of documents in cases where all of the

terms in the q parameter appear in close proximity.

• “ps” , Phrase Slop: specifies the number of positions two terms can be apart in

order to match the specified phrase.

000-DTSE-Search-7451-60-DM-52 © DataStax, All Rights Reserved. Confidential.

dismax Query Parser: Parameters

• “qs” , Query Phrase Slop: specifies the number of positions two terms can be

apart in order to match the specified phrase. Used specifically with the qf

parameter.

• “tie” , Tie Breaker: specifies a float value (which should be something much less

than 1) to use as tiebreaker in DisMax queries. Default: 0.0

• “bq” , Boost Query: specifies a factor by which a term or phrase should be

"boosted" in importance when considering a match.

• “bf” , Boost Functions: specifies functions to be applied to boosts. (See for details

about function queries.)

000-DTSE-Search-7451-60-DM-53 © DataStax, All Rights Reserved. Confidential.

edismax Query Parser: Parameters

• “sow” , Split on whitespace: if set to false, whitespace-separated term sequences

will be provided to text analysis in one shot, enabling proper function of analysis

filters that operate over term sequences, e.g. multi-word synonyms and

shingles. Defaults to true: text analysis is invoked separately for each individual

whitespace-separated term.

• “mm.autoRelax” , If true, the number of clauses required (minimum should

match) will automatically be relaxed if a clause is removed (by e.g. stopwords

filter) from some but not all qf fields.

• “boost” , A multivalued list of strings parsed as queries with scores multiplied by

the score from the main query for all matching documents.

• “lowercaseOperators” , A Boolean parameter indicating if lowercase "and" and

"or" should be treated the same as operators "AND" and "OR".

000-DTSE-Search-7451-60-DM-54 © DataStax, All Rights Reserved. Confidential.

edismax Query Parser: Parameters

• “ps” , Default amount of slop on phrase queries built with pf, pf2 and/or pf3 fields

(affects boosting).

• “pf2” , A multivalued list of fields with optional weights, based on pairs of word

shingles.

• “ps2” , This is similar to ps but overrides the slop factor used for pf2. If not

specified, ps is used.

• “pf3” , A multivalued list of fields with optional weights, based on triplets of word

shingles. Similar to pf, except that instead of building a phrase per field out of all

the words in the input, it builds a set of phrases for each field out of each triplet

of word shingles.

000-DTSE-Search-7451-60-DM-55 © DataStax, All Rights Reserved. Confidential.

edismax Query Parser: Parameters

• “ps3” , This is similar to ps but overrides the slop factor used for pf3. If not

specified, ps is used.

• “stopwords” , A Boolean parameter indicating if the StopFilterFactory configured

in the query analyzer should be respected when parsing the query: if it is false,

then the StopFilterFactory in the query analyzer is ignored.

• “uf” , Specifies which schema fields the end user is allowed to explicitly query.

This parameter supports wildcards. The default is to allow all fields, equivalent

to uf=*. To allow only title field, use uf=title. To allow title and all fields ending

with '_s', use uf=title,*_s. To allow all fields except title, use uf=*,-title. To disallow

all fielded searches, use uf=-*.

• “qf” , Per-field overrides of the qf parameter may be specified to provide 1-to-

many aliasing from field names specified in the query string, to field names used

in the underlying query. By default, no aliasing is used and field names specified

in the query string are treated as literal field names in the index.

000-DTSE-Search-7451-60-DM-56 © DataStax, All Rights Reserved. Confidential.

edismax Query Parser: Parameters

• “_val_” , If the magic field name _val_ is used in a term or phrase query, the

value is parsed as a function.It provides a hook into FunctionQuery syntax.

Quotes are necessary to encapsulate the function when it includes parentheses.

For example:_val_:myfield_val_:"recip(rord(myfield),1,2,3)“

• “_query_” , The Solr Query Parser offers nested query support for any type of

query parser (via QParserPlugin). Quotes are often necessary to encapsulate

the nested query if it contains reserved characters.

For example:_query_:"{!dismax qf=myfield}how now brown cow"

000-DTSE-Search-7451-60-DM-57 © DataStax, All Rights Reserved. Confidential.

Paging-

• Defined as; not for batch or related, but for end user activity, return a

large set of rows in manageable chunks

• Basic pagination, use Solr “start” and “rows” parameters. Use

queryResultCache, and queryResultWindowSize parameters.

• The above can be disabled in dse.yaml when

cql_solr_query_paging:off.

• Cursor based pagination, use the “paging:driver” query parameter.

Example-

solr_query = {“q”:””, “sort”:”col1 asc”, “paging”:”driver”}’;

000-DTSE-Search-7451-60-DM-58 © DataStax, All Rights Reserved. Confidential.

QueryResponseWriter

• Only applicable to Http queries. (The same used by SolrJ,

the Solr Admin UI, other.)

• BinaryResponseWriter is used internally by CQL for

serialization/deserialization of SolrQueryResponse.

DataStax • CQL operates on rows, or JSON Internal Use SELECT json col1, col5 FROM t10 WHERE Only

solr_query = '{ "q" : "col5:(Mary || Harry)" }';

[json]

----------------------------------

{"col1": "bbb", "col5": "Harry"}

{"col1": "aaa", "col5": "Mary"}

000-DTSE-Search-7451-60-DM-59 © DataStax, All Rights Reserved. Confidential.
