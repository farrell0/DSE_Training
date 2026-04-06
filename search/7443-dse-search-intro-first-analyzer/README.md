# DSE Search: DSE Search Intro, First Analyzer

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Discussion Module

**Customer:** I am working through the DSE Search curriculum and need help with dse search intro, first analyzer. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This discussion module in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search intro, first analyzer.

## Downloads

- [PDF slides](./7443-dse-search-intro-first-analyzer.pdf)
- [Original PowerPoint](../000-DTSE-Search-7443-DM-60%2C%20DSE%20Search%20Intro%2C%20First%20Analyzer.pptx)

## Converted Slides

## Discussion

Introduce the briefest amount of material Discussion possible to get our first DSE Search (text Module: analytics/search) index in place, and run

queries DSE Search, Intro, First

Analyzer • A DSE Search index in place to support

synonyms. E.g., Dave, David, Davie,

‘Dava Roonie’

• Useful for product/catalog searches;

(mobile phone, cellular phone, smart

phone), (car, auto, automobile, vehicle),

(bike, bicycle, tricycle, moped), other

000-DTSE-Search-7443-60-DU-1 © DataStax, All Rights Reserved. Confidential.

DSE Functional Areas: Core, Search

Discussion Lab:

Matching pairs – Match the

attributes on the right with the

areas on the left

000-DTSE-Search-7443-60-DU-2 © DataStax, All Rights Reserved. Confidential.

Discussion Lab: Which DSE Functional Area

100-250+ ms Response

0-10 ms Response

DSE Search Exact Match

Near Match (or exact match) DSE Core

Hash Index

Tf-Idf (bitmap) Index

New Query Predicates

000-DTSE-Search-7443-60-DU-3 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7443-60-DU-4 © DataStax, All Rights Reserved. Confidential.

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

Catalog of Available Analyzer Options:

• Chained Analyzers-

– Char Filters (8+), https://

lucene.apache.org/solr/guide/6_6/charfilterfactories.html

– Tokenizers (10+), https://

lucene.apache.org/solr/guide/6_6/tokenizers.html

– Filters (40+), https://

lucene.apache.org/solr/guide/6_6/filter-descriptions.html

• Unchained Analyzers (6+30) ,

https://www.solr-start.com/info/analyzers/

000-DTSE-Search-7443-60-DU-7 © DataStax, All Rights Reserved. Confidential.

DSE Search,: Field Types, Fields

2 (8+, not including the data types)

name

class (data type)

docValues ? (10+) positionIncrementGap name 1 (Other) type (refers to field

type class name)

docValues

multiValued

indexed

(Other)

000-DTSE-Search-7443-60-DU-8 © DataStax, All Rights Reserved. Confidential.

Catalog of Available Field Type / Field Options:

Field Type attributes/properties (8+ not including data types) :

https://

lucene.apache.org/solr/guide/6_6/field-type-definitions-and-prope rties.html

Field attributes/properties (20+) :

https://

lucene.apache.org/solr/guide/6_6/field-properties-by-use-case.ht ml

https://lucene.apache.org/solr/guide/6_6/defining-fields.html

000-DTSE-Search-7443-60-DU-9 © DataStax, All Rights Reserved. Confidential.

Field Types <- Analyzers (Indexes), Fields: How are

These Created-

• dsetool: schema.xml, solrconfig.xml

• CQL

– (CREATE TABLE)

– CREATE SEARCH INDEX ...

– ALTER SEARCH INDEX ...

– RELOAD SEARCH INDEX ...

– REBUILD SEARCH INDEX ... CREATE : 1

– DESCRIBE ACTIVE | PENDING Copyright: The Muppets Studio, LLC SEARCH INDEX ALTER, ALTER, SCHEMA | CONFIG .. ALTER, ... : M – DROP SEARCH INDEX ...

• Gremlin (for Graph only)

000-DTSE-Search-7443-60-DU-10 © DataStax, All Rights Reserved. Confidential.

• DSE cluster, with Search enabled

• Authority to make tables, other

• CQLSH/Studio access-

• Will leave it case sensitive, but will offer

End to End clues for actual Practice Lab that

follows Example:

Synonym, case sensitive

000-DTSE-Search-7443-60-DU-11 © DataStax, All Rights Reserved. Confidential.

Synonym: CREATE KEYSPACE

DROP KEYSPACE ks_7443;

CREATE KEYSPACE ks_7443 WITH REPLICATION =

{'class': 'SimpleStrategy', 'replication_factor': 1};

USE ks_7443;

000-DTSE-Search-7443-60-DU-12 © DataStax, All Rights Reserved. Confidential.

Synonym: CREATE TABLE

CREATE TABLE t1

(

col1 TEXT,

col2 TEXT,

col3 TEXT,

col4 TEXT,

col5 TEXT,

col6 TEXT,

col7 TEXT,

col8 TEXT,

PRIMARY KEY ((col1, col2)) );

000-DTSE-Search-7443-60-DU-13 © DataStax, All Rights Reserved. Confidential.

Synonym: (Add Data)

INSERT INTO t1

(col1, col2, col3, col4,

col5, col6, col7, col8)

VALUES ('aaa', 'aaa', ' Davie ' ,

'aaa', 'aaa', 'aaa', 'aaa', 'aaa');

INSERT INTO t1

(col1, col2, col3, col4,

col5, col6, col7, col8)

VALUES ('bbb', 'bbb', ' Elizabeth ',

'bbb', 'bbb', 'bbb', 'bbb', 'bbb');

000-DTSE-Search-7443-60-DU-14 © DataStax, All Rights Reserved. Confidential.

Synonym: CREATE SEARCH INDEX

CREATE SEARCH INDEX ON t1 WITH COLUMNS col1,

* { excluded : true };

>>Warnings :

>>Please remember this operation is DC specific and should be

>>repeated on each desired DC.

000-DTSE-Search-7443-60-DU-15 © DataStax, All Rights Reserved. Confidential.

Synonym: DESCRIBE TABLE

DESCRIBE TABLE t1;

>>CREATE TABLE ks_7443.t1 ( >> col1 text, >> col2 text, ... >> col8 text, >> solr_query text, >> PRIMARY KEY ((col1, col2)) >>) WITH bloom_filter_fp_chance = 0.01 >> AND caching = ... >> AND comment = '' >> AND compaction = ... ... >> AND speculative_retry = '99PERCENTILE'; >>CREATE CUSTOM INDEX ks_7443_t1_solr_query_index >> ON ks_7443.t1 (solr_query) USING >> 'com.datastax.bdp.search.solr.Cql3SolrSecondaryIndex';

000-DTSE-Search-7443-60-DU-16 © DataStax, All Rights Reserved. Confidential.

Synonym: DESCRIBE ... SEARCH INDEX

DESCRIBE PENDING SEARCH INDEX SCHEMA ON t1;

>> <?xml version="1.0" encoding="UTF-8" standalone="no"?> >> <schema name="autoSolrSchema" version="1.5"> >> <types> >> <fieldType class="org.apache.solr.schema.StrField" >> name="StrField"/> >> </types> >> <fields> >> <field indexed="true" multiValued="false" col2 ?? col1 StrField >> name=" " type=" "/> >> <field indexed="true" multiValued="false" StrField -vs- TextField col2 StrField >> name=" " type=" "/> >> </fields> ( >= DSE 6.0 ) >> <uniqueKey>(col1,col2)</uniqueKey> >> </schema>

000-DTSE-Search-7443-60-DU-17 © DataStax, All Rights Reserved. Confidential.

Synonym: Make an ASCII Text Field, Submit

dsetool write_resource ks_7443.t1 \

name=7443_my_synonyms.txt \

file=7443_my_synonyms.txt

Dropped if

# you drop # My synonyms file !! the index #

Robert, Bob, Bobbie

Dave, David, Davie, Dava Roonie

Charles, Chuck, Charlie, Barkley

Elizabeth, Beth, Liz, Lizzie, Tina

000-DTSE-Search-7443-60-DU-18 © DataStax, All Rights Reserved. Confidential.

Synonym: Progressive Examples, surplus steps-

ALTER SEARCH INDEX SCHEMA ON t1

ADD fieldType[ @name=' TextField_5 ',

@class='solr.TextField'];

ALTER SEARCH INDEX SCHEMA ON t1

ADD fieldType[@name= 'TextField_6 ',

@class='solr.TextField',

Saves @termVectors='false',

disk space, Not using HighLighting or other @termPositions='false', functionality that depends on it other @termOffsets='false',

@omitNorms='true']; Not using term Boosting

000-DTSE-Search-7443-60-DU-19 © DataStax, All Rights Reserved. Confidential.

Apache Solr, Impact on Disk Space, termVectors,

more ..

Source: Slide 36, https://www.slideshare.net/DataStax/solr47-f-inal ? https://data.world/datasets/twitter

000-DTSE-Search-7443-60-DU-20 © DataStax, All Rights Reserved. Confidential.

Synonym: Field Type (minimum)

ALTER SEARCH INDEX SCHEMA ON t1

ADD types.fieldType[@name='TextField_7',

@class='solr.TextField'] with '{"analyzer":{"tokenizer":

{"class":"solr.StandardTokenizerFactory"},

"filter":{"class":"solr.SynonymFilterFactory","synonyms":"7443_my_synonyms.txt"}

} }';

// File not loaded ?

// InvalidRequest: Error from server: code=2200 [Invalid query] message=

// "The search index schema is not valid because: java.io.IOException: Could not find: 47_my_synonyms.txt"

000-DTSE-Search-7443-60-DU-21 © DataStax, All Rights Reserved. Confidential.

Synonym: Field Type (actual)

ALTER SEARCH INDEX SCHEMA ON t1

ADD types.fieldType[@name='TextField_7',

@class='solr.TextField',@termVectors='false',@termPositions='false',

@termOffsets='false',@omitNorms='true'] with

'{"analyzer":{"tokenizer":{"class":"solr.StandardTokenizerFactory"},

"filter":{"class":"solr.SynonymFilterFactory","synonyms":"7443_my_synonyms.txt"}}}';

000-DTSE-Search-7443-60-DU-22 © DataStax, All Rights Reserved. Confidential.

Synonym: Add Field, and Deploy

ALTER SEARCH INDEX SCHEMA ON t1

ADD fields.field[@name='col3', @type='TextField_7',

@indexed='true', @multiValued='false', @stored='true'];

RELOAD SEARCH INDEX ON t1;

// Warnings :

// Please remember this operation is DC specific and should be repeated on each desired DC.

REBUILD SEARCH INDEX ON t1;

// Warnings :

// Please remember this operation is DC specific and should be repeated on each desired DC.

000-DTSE-Search-7443-60-DU-23 © DataStax, All Rights Reserved. Confidential.

Synonym: Test, CQL SELECT

SELECT col1, col2, col3 FROM t1 WHERE solr_query = '{ "q" : "col3:Dave" }' ;

>> col1 | col2 | col3

>> aaa | aaa | Davie

>> (1 rows)

SELECT col1, col2, col3 FROM t1 WHERE solr_query = '{ "q" : "col3:(Dava Rooney)" }' ;

>> col1 | col2 | col3

>> aaa | aaa | Davie

>> (1 rows)

SELECT col1, col2, col3 FROM t1 WHERE solr_query = '{ "q" : "col3:dave" }' ;

>> col1 | col2 | col3

>> (0 rows)

000-DTSE-Search-7443-60-DU-24 © DataStax, All Rights Reserved. Confidential.

Synonym: Debugging (page 1 of 2)

DESCRIBE ACTIVE SEARCH INDEX SCHEMA ON t1;

>> <?xml version="1.0" encoding="UTF-8" standalone="no"?>

>> <schema name="autoSolrSchema" version="1.5">

>> <types>

>> <fieldType class="org.apache.solr.schema.StrField" name="StrField"/>

>> <fieldType class="solr.TextField" name="TextField_7" omitNorms="true"

>> termOffsets="false" termPositions="false" termVectors="false">

>> <analyzer>

>> <filter class="solr.SynonymFilterFactory"

>> synonyms="7443_my_synonyms.txt"/>

>> <tokenizer class="solr.StandardTokenizerFactory"/>

...

000-DTSE-Search-7443-60-DU-25 © DataStax, All Rights Reserved. Confidential.

Synonym: Debugging (page 2 of 2)

...

>> </analyzer>

>> </fieldType>

>> </types>

>> <fields>

>> <field indexed="true" multiValued="false" name="col1" type="StrField"/>

>> <field indexed="true" multiValued="false" name="col2" type="StrField"/>

>> <field indexed="true" multiValued="false" name="col3" stored="true"

>> type="TextField_7"/>

>> </fields>

>> <uniqueKey>(col1,col2)</uniqueKey>

>> </schema>

000-DTSE-Search-7443-60-DU-26 © DataStax, All Rights Reserved. Confidential.

• CREATE SEARCH INDEX ... (PK)

• Synonym -> dsetool write_resource

• ALTER ... ADD types.fieldType ...

• ALTER ... ADD fields.field ... End to End

• (deploy) Example:

• Case insensitive ? (Next page) Synonym, case sensitive,

Review

000-DTSE-Search-7443-60-DU-27 © DataStax, All Rights Reserved. Confidential.

Two code fragments: Lower case, and multiple

filters

ALTER SEARCH INDEX SCHEMA ON t2

ADD fieldType[@name='TextField44',class='solr.TextField‘]

WITH '{"analyzer":{"tokenizer":{"class":"solr.StandardTokenizerFactory"},

"filter":{"class":"solr.LowerCaseFilterFactory"}}}';

ALTER SEARCH INDEX SCHEMA ON t2

ADD fieldType[@name='TextField41',class='solr.TextField']

WITH '{"analyzer":{"tokenizer":{"class":"solr.StandardTokenizerFactory"},

"filter":[{"class":"solr.LowerCaseFilterFactory"},

{"class":"solr.EnglishMinimalStemFilterFactory"}]}}';

000-DTSE-Search-7443-60-DU-28 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7443-60-DU-29

Solutions:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7443-60-DU-30

Discussion Lab: Which DSE Functional Area

100-250+ ms Response

0-10 ms Response

DSE Search Exact Match

Near Match (or exact match) DSE Core

Hash Index

Tf-Idf (bitmap) Index

New Query Predicates

000-DTSE-Search-7443-60-DU-31 © DataStax, All Rights Reserved. Confidential.
