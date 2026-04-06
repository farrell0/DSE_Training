# DSE Search: DSE Search, Debugging, Sounds Like, Char Filter, docValues

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Discussion Module

**Customer:** I am working through the DSE Search curriculum and need help with dse search, debugging, sounds like, char filter, docvalues. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This discussion module in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, debugging, sounds like, char filter, docvalues.

## Downloads

- [PDF slides](./7445-dse-search-debugging-sounds-like-char-filter-doc-values.pdf)
- [Original PowerPoint](../000-DTSE-Search-7445-DM-60%2C%20DSE%20Search%2C%20Debugging%2C%20Sounds%20Like%2C%20Char%20Filter%2C%20docValues.pptx)

## Converted Slides

## Discussion

Use tools to validate/debug what is

happening inside DSE Seach / Apache Solr-

• Solr Admin screen Module: • Lucene index (Key) Explorer (LuKE)

DSE Search, Debugging, • dsetool Sounds Like, Char Filters, • (CQLSH, Other) More

Using these text analytics-

• Sounds Like

• Char Filters

• docValues (just part 1)

000-DTSE-Search-7445-60-DM-1 © DataStax, All Rights Reserved. Confidential.

• DSE cluster, with Search enabled

• Authority to make tables, other

• CQLSH/Studio access-

• A modified version from the example in

End to End Discussion Module 7443.

• Added to, and we’ll (validate/debug). Example:

Synonym, case insensitive

000-DTSE-Search-7445-60-DM-2 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 1 of 12

DROP KEYSPACE ks_7445; CREATE KEYSPACE ks_7445 WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}; INSERT INTO t1 USE ks_7445; (col1, col2, col3, col4, col5, CREATE TABLE t1 col6, col7, col8, col9, col0) ( VALUES ('aaa', 'aaa', 'Davie ' , 'aaa', 'aaa', col1 TEXT, 'aaa', 'aaa', 'aaa', 'aaa', 'aaa'); col2 TEXT, col3 TEXT, VALUES ('bbb', 'bbb', 'Elizabeth ', 'bbb', 'bbb', col4 TEXT, 'bbb', 'bbb', 'bbb', 'bbb', 'bbb'); col5 TEXT, col6 TEXT, CREATE SEARCH INDEX ON t1 col7 TEXT, WITH COLUMNS col1, col8 TEXT, * { excluded : true }; col9 TEXT, col0 TEXT, PRIMARY KEY ((col1, col2)) );

000-DTSE-Search-7445-60-DM-3 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 2 of 12

dsetool write_resource ks_7445.t1 name=7445_my_synonyms.txt file=7445_my_synonyms.txt

# # My synonyms file !! # Robert, Bob, Bobbie Prerequisites ? Dave, David, Davie, Dava Roonie Charles, Chuck, Charlie, Barkley Elizabeth, Beth, Liz, Lizzie, Tina

000-DTSE-Search-7445-60-DM-4 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 3 of 12

ALTER SEARCH INDEX SCHEMA ON t1 ADD types.fieldType[@name='TextField_17', @class='solr.TextField', @termVectors='false', @termPositions='false', @termOffsets='false', @omitNorms='true'] with '{"analyzer":{"tokenizer": {"class":"solr.StandardTokenizerFactory"}, "filter":{"class":"solr.SynonymFilterFactory", "synonyms":"7445_my_synonyms.txt"}}}';

ALTER SEARCH INDEX SCHEMA ON t1 ADD fields.field[@name='col3', @type='TextField_17', @indexed='true', @multiValued='false', @stored='true']; col3

000-DTSE-Search-7445-60-DM-5 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 4 of 12

INSERT INTO t1 (col1, col2, col3, col4, col5, RELOAD SEARCH INDEX ON t1; col6, col7, col8, col9, col0) REBUILD SEARCH INDEX ON t1; VALUES ('aaa', 'aaa', 'Davie ' , 'aaa', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa'); SELECT col1, col2, col3 FROM t1 INSERT INTO t1 WHERE solr_query = '{ "q" : "col3:Dave" }' ; (col1, col2, col3, col4, col5, col6, col7, col8, col9, col0) WHERE solr_query = '{ "q" : VALUES ('bbb', 'bbb', 'Elizabeth ', 'bbb', 'bbb', "col3:(Dava Rooney)" }' ; 'bbb', 'bbb', 'bbb', 'bbb', 'bbb');

WHERE solr_query = '{ "q" : "col3:dave" }' ; Dave, David, Davie, Dava Roonie Charles, Chuck, Charlie, Barkley Elizabeth, Beth, Liz, Lizzie, Tina

col3

000-DTSE-Search-7445-60-DM-6 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 5 of 12

INSERT INTO t1 (col1, col2, col3, col4, col5, col6, col7, col8, col9, col0) VALUES ('ccc', 'ccc', 'Stuart', 'Pizza Hut ', 'ccc', 'ccc', 'ccc', 'ccc', 'ccc', 'ccc');

VALUES ('ddd', 'ddd', 'Mary', 'Starbucks ', 'ddd', 'ddd', 'ddd', 'ddd', 'ddd', 'ddd');

VALUES ('eee', 'eee', 'Eli', 'Kranburrees ', 'eee', 'eee', 'eee', 'eee', 'eee', 'eee');

col4

000-DTSE-Search-7445-60-DM-7 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 6 of 12

ALTER SEARCH INDEX SCHEMA ON t1 ADD types.fieldType[@name='TextField18', @class='solr.TextField'] with '{"analyzer":{"tokenizer": {"class":"solr.StandardTokenizerFactory"}, "filter":{"class":"solr.BeiderMorseFilterFactory", "nameType":"GENERIC", "ruleType":"APPROX", "concat":"true", "languageSet":"auto"}}}'; ALTER SEARCH INDEX SCHEMA ON t1 ADD fields.field[@name='col4', @type='TextField18', @indexed='true', @multiValued='false', @stored='true']; RELOAD SEARCH INDEX ON t1; REBUILD SEARCH INDEX ON t1; col4

000-DTSE-Search-7445-60-DM-8 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 7 of 12

INSERT INTO t1 (col1, col2, col3, col4, col5, SELECT col1, col2, col3, col4 FROM t1 col6, col7, col8, col9, col0) VALUES ('ccc', 'ccc', 'Stuart', 'Pizza Hut ', 'ccc', WHERE solr_query = '{ "q" : "col4:(Pizzah Hutt)" }' ; 'ccc', 'ccc', 'ccc', 'ccc', 'ccc'); WHERE solr_query = '{ "q" : "col4:(Pizzah utt)" }' ; WHERE solr_query = '{ "q" : "col4:(zah hut)" }' ; VALUES ('ddd', 'ddd', 'Mary', ' Starbucks ', 'ddd', WHERE solr_query = '{ "q" : "col4:Starrbux" }' ; 'ddd', 'ddd', 'ddd', 'ddd', 'ddd'); WHERE solr_query = '{ "q" : "col4:stARrbUx" }' ; WHERE solr_query = '{ "q" : "col4:cranberry" }' ; VALUES ('eee', 'eee', 'Eli', ' Kranburrees ', 'eee', 'eee', 'eee', 'eee', 'eee', 'eee');

000-DTSE-Search-7445-60-DM-9 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 8 of 12

ALTER SEARCH INDEX SCHEMA ON t1 ADD fieldType[@name='TextField19', @class='solr.TextField'] WITH '{ "analyzer" : { "charFilter" : { "class" : "solr.HTMLStripCharFilterFactory" }, "tokenizer" : { "class" : "solr.StandardTokenizerFactory" }, "filter" : { "class" : "solr.LowerCaseFilterFactory" }}}';

ALTER SEARCH INDEX SCHEMA ON t1 ADD fields.field[@name='col5', @type='TextField19'];

RELOAD SEARCH INDEX ON t1; REBUILD SEARCH INDEX ON t1;

col5

000-DTSE-Search-7445-60-DM-10 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 9 of 12

INSERT INTO t1 (col1, col2, col3, col4, col5, SELECT col1, col5 FROM t1 WHERE col6, col7, col8, col9, col0) solr_query = '{ "q" : "col5:( my link )" }' ; VALUES ('fff', 'fff', 'Bart', 'fff', 'my link2 ', 'fff', 'fff', 'fff', 'fff', 'fff');

VALUES ('ggg', 'ggg', 'Peggy', 'ggg', ' my <a href=\”www.foo.bar\”>link</a> ', 'ggg', 'ggg', 'ggg', 'ggg', 'ggg');

Which rows ? VALUES ('hhh', 'hhh', 'Earl', 'hhh', What col5 column value ? ' <bold>my link</bold> ', 'hhh', 'hhh', 'hhh', 'hhh', 'hhh');

col5

000-DTSE-Search-7445-60-DM-11 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 10 of 12

ALTER SEARCH INDEX SCHEMA ON t1 SET types.fieldtype[@class='org.apache.solr.schema.StrField'] @name='TextField20'; ALTER SEARCH INDEX SCHEMA ON t1 SET types.fieldtype[@class='org.apache.solr.schema.StrField', @docValues='true']@name='TextField21'; // ALTER SEARCH INDEX SCHEMA ON t1 SET types.fieldtype[@class='org.apache.solr.schema.TextField'] @name='TextField22'; ALTER SEARCH INDEX SCHEMA ON t1 SET types.fieldtype[@class='org.apache.solr.schema.TextField', What tokenizers ? @docValues='true']@name='TextField23';

000-DTSE-Search-7445-60-DM-12 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 11 of 12

ALTER SEARCH INDEX SCHEMA ON t1 ADD fields.field[@name='col6', @type='TextField20']; ALTER SEARCH INDEX SCHEMA ON t1 ADD fields.field[@name='col7', @type='TextField21', @docValues='true']; ALTER SEARCH INDEX SCHEMA ON t1 ADD fields.field[@name='col8', @type='TextField22']; ALTER SEARCH INDEX SCHEMA ON t1 ADD fields.field[@name='col9', @type='TextField23', @docValues='true'];

RELOAD SEARCH INDEX ON t1; REBUILD SEARCH INDEX ON t1; COMMIT SEARCH INDEX ON t1;

col6, 7, 8, 9 000-DTSE-Search-7445-60-DM-13 © DataStax, All Rights Reserved. Confidential.

Example to test with .. page 12 of 12

SELECT * FROM t1 WHERE solr_query = '{"q":"*:*", "sort":"col6 asc"}'; // these both will fail SELECT * FROM t1 WHERE solr_query = '{"q":"*:*", "sort":"col6 desc"}';

SELECT * FROM t1 WHERE solr_query = '{"q":"*:*", "sort":"col7 asc"}';

SELECT * FROM t1 WHERE solr_query = '{"q":"*:*", "sort":"col8 asc"}'; // this will fail

SELECT * FROM t1 WHERE solr_query = '{"q":"*:*", "sort":"col9 asc"}';

000-DTSE-Search-7445-60-DM-14 © DataStax, All Rights Reserved. Confidential.

• Prepare to validate/debug-

End to End

Example:

Synonym, case insensitive,

Review

000-DTSE-Search-7445-60-DM-15 © DataStax, All Rights Reserved. Confidential.

On by default. Can be locked down-

http://localhost:8983/solr/#/

http://localhost:8983/solr/#/ks.tab

http://localhost:8983/solr/#/ ks.tab /...

(Also REST API, Curl)

Apache Solr On line doc page,

Admin UI https://

lucene.apache.org/solr/guide/6_6/overvi

ew-of-the-solr-admin-ui.html

• Read (write)

• Ad-hoc queries

• (System administration)

• Debugging/tracing

• Other

000-DTSE-Search-7445-60-DM-16 © DataStax, All Rights Reserved. Confidential.

Solr Admin UI:

Home page

• All 5 (first) TABs, read-only

• Dashboard; memory

utilization

• (Remainder); Largely

engineering debug

000-DTSE-Search-7445-60-DM-17 © DataStax, All Rights Reserved. Confidential.

Solr Admin UI: After Core selection

Overview TAB-

• Row count

• Install base directory

• Data file directories

000-DTSE-Search-7445-60-DM-18 © DataStax, All Rights Reserved. Confidential.

Solr Admin UI: Core -> Analysis -> Column

• Debug existing analyzer

– (Have to manually decompose: Technique)

• Index | Query | (Both)

• Displays (resource file

data)

000-DTSE-Search-7445-60-DM-19 © DataStax, All Rights Reserved. Confidential.

Solr Admin UI: Core -> Config

• Shortcut to Files, Config

• (Resource files)

• schema.xml

– DESCRIBE ACTIVE SEARCH INDEX SCHEMA ON ks.tab;

• solrconfig.xml

– DESCRIBE PENDING SEARCH INDEX CONFIG ON ks.tab;

000-DTSE-Search-7445-60-DM-20 © DataStax, All Rights Reserved. Confidential.

Solr Admin UI: Core -> Plugins/Stats -> ..

• (Many, 8)

• Jars

• Resource per core,

detailed

000-DTSE-Search-7445-60-DM-21 © DataStax, All Rights Reserved. Confidential.

Solr Admin UI: Core ->

Query

• $$$

• Adhoc queries

• fl, *.score

• debugQuery (SET EXPLAIN)

• Much more

000-DTSE-Search-7445-60-DM-22 © DataStax, All Rights Reserved. Confidential.

Query Processing: ANDs and ORs-

The OR-topped query is a famous

discussion point-

Discussion Lab:

Discuss

000-DTSE-Search-7445-60-DM-23 © DataStax, All Rights Reserved. Confidential.

B-Tree+ Index: Query Processing

SELECT ... WHERE

col1 = x AND col2 = y;

SELECT ... WHERE • Assume B-Tree+ col1 = x OR col2 = y;

• Add any index

• How are rows processed

• (Table order)

• Access methods

• (Join methods) ?

000-DTSE-Search-7445-60-DM-24 © DataStax, All Rights Reserved. Confidential.

Tf-IDF (Bitmap) Index: Query Processing

SELECT ... WHERE

col1 = x AND col2 = y;

SELECT ... WHERE

col1 = x OR col2 = y; Image Source: https://docs.oracle.com/cd/E18283_01/server.112/e16579/indexes.htm

• Assume Tf-Idf (Bitmap)

• Add any index

• How are rows processed

• (Table order)

• Access methods

• (Join methods) ? 000-DTSE-Search-7445-60-DM-25 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7445-60-DM-26 © DataStax, All Rights Reserved. Confidential.

Solr Admin UI: Core -> Schema Browser

• Similar to LuKE (later),

some prefer LuKE (lower

level)

000-DTSE-Search-7445-60-DM-27 © DataStax, All Rights Reserved. Confidential.

Solr Admin UI: Core -> Segments Info

• SSTables segments, but

for index data

• Important on

volatile/large systems

– (Compaction strategy)

– (Deleting tombstones)

000-DTSE-Search-7445-60-DM-28 © DataStax, All Rights Reserved. Confidential.

• Recall that Lucene is the layer below Solr

• Should match DESCRIBE SEARCH

INDEX

• Should match Solr Admin UI -> Core ->

Schema Browser

• On line doc page,

https://wiki.apache.org/solr/LukeRequestHandler LuKE

• h ttp://localhost:8983/solr/ ks.tab /admin/luke • h ttp://localhost:8983/solr/ ks.tab /admin/luke?id=aaa Lucene index (Key) Explorer • h ttp://localhost:8983/solr/ ks.tab /admin/luke?docid=1

000-DTSE-Search-7445-60-DM-29 © DataStax, All Rights Reserved. Confidential.

LuKE: (display schema)

• docValues is particularly

troublesome (many field

types do not support it)

• fieldType -> field

– Also properties related; Inheritance did it push forward (can it)

000-DTSE-Search-7445-60-DM-30 © DataStax, All Rights Reserved. Confidential.

• nodetool

• dsetool ( --help)

• 180+ lines, many functions

• core_indexing_status

• create_core

• get_core_config

• get_core_schema

DESCRIBE • index_checks dsetool SEARCH INDEX • infer_solr_schema

• list_index_files

• perf RELOAD | REBUILD • rebuild_indexes SEARCH INDEX • rebuild_core

• stop_core_reindex

• unload_core

• upgrade_index_files

• write_resource

000-DTSE-Search-7445-60-DM-31 © DataStax, All Rights Reserved. Confidential.

dsetool core_indexing_status ks.tab

Expect all lowercase identifiers for (Lucene/DSE Search) !

https://docs.datastax.com/en/dse/6.0/dse-dev/datastax_enterprise/tools/dsetool/dsetool.html https://docs.datastax.com/en/dse/6.0/dse-dev/datastax_enterprise/tools/dsetool/dsetoolCore_indexing_status.html

000-DTSE-Search-7445-60-DM-32 © DataStax, All Rights Reserved. Confidential.

dsetool index_checks ks.tab

dsetool index_checks ks_7445.t1

LUKE handler info: ... ------------------ numDocs:11 lockFactory=org.apache.lucene.store.NativeFSLockFac maxDoc:11 tory@2405262d deletedDocs:0 segmentsFile:segments_4 indexHeapUsageBytes:3850 segmentsFileSizeInBytes:162 version:19 userData:{commitTimeMSec=1525441177156} segmentCount:1 lastModified:Fri May 04 07:39:37 MDT 2018 current:true hasDeletions:false directory:org.apache.lucene.store.MMapDirect ory:MMapDirectory@/opt/dse/node1/data/ data/solr.data/ks_7445.t1/index ...

000-DTSE-Search-7445-60-DM-33 © DataStax, All Rights Reserved. Confidential.

dsetool list_index_files ks.tab

dsetool list_index_files ks_7445.t1

Filename Encryption Disk usage Decrypted size Encryption overhead -------- ---------- ---------- -------------- ------------------- _4.fnm N/A

1.58K N/A N/A _4.nvd N/A 92 bytes N/A N/A _4.nvm N/A 118 bytes N/A N/A _4.si N/A 556 bytes N/A N/A _4_BloomFilter_0.blm N/A 119 bytes N/A N/A _4_BloomFilter_0.doc N/A 113 bytes N/A N/A _4_BloomFilter_0.pos N/A 80 bytes N/A N/A _4_BloomFilter_0.tim N/A 379 bytes N/A N/A _4_BloomFilter_0.tip N/A 105 bytes N/A N/A _4_Lucene50_0.doc N/A 124 bytes N/A N/A _4_Lucene50_0.pos N/A 223 bytes N/A N/A _4_Lucene50_0.tim N/A

3.19K N/A N/A _4_Lucene50_0.tip N/A 376 bytes N/A N/A _4_Lucene54_0.dvd N/A 550 bytes N/A N/A _4_Lucene54_0.dvm N/A 431 bytes N/A N/A segments_4 N/A 162 bytes N/A N/A write.lock N/A 0 bytes N/A N/A

000-DTSE-Search-7445-60-DM-34 © DataStax, All Rights Reserved. Confidential.

dse perf ( options )

000-DTSE-Search-7445-60-DM-35 © DataStax, All Rights Reserved. Confidential.

dsetool stop_core_reindex | write_resource ks.tab

• Graceful, minutes to wait- dsetool write_resource ks_7445.t1 name=7445_my_synonyms.txt • Not restartable file=7445_my_synonyms.txt

dsetool core_indexing_status ks_16.my_mapdata Uploaded resource 7445_my_synonyms.txt for [ ks_16.my_mapdata]: INDEXING, 90% complete, ks_7445.t1 ETA 10950 milliseconds (10 seconds)

dsetool stop_core_reindex ks_16.my_mapdata Successfully stopped reindex for core ks_16.my_mapdata.

000-DTSE-Search-7445-60-DM-36 © DataStax, All Rights Reserved. Confidential.

• DESCRIBE ACTIVE | PENDING SEARCH

INDEX SCHEMA | CONFIG

CQLSH/CQL • trace on | off (CQLSH only, not a CQL

command)

Describe, trace on|off

000-DTSE-Search-7445-60-DM-37 © DataStax, All Rights Reserved. Confidential.

CQLSH: tracing on | off

cqlsh:ks_7445> tracing off Disabled Tracing. cqlsh:ks_7445> tracing on Now Tracing is enabled cqlsh:ks_7445> select * from t1 where col3 LIKE 'aaa';

col1 | col2 | col0 | col3 | col4 | col5 | col6 | col7 | col8 | col9 | solr_query ------+------+------+------+------+------+------+------+------+------+------------ (0 rows)

Tracing session: 1495de60-4fd3-11e8-98c6-630a381113b4 activity | timestamp | source | source_elapsed | client -------------------+-------------------+-----------+----------------+----------- Execute CQL3 query | 2018-05-04 ... | 127.0.0.1 | 0 | 127.0.0.1 Parsing select * from t1 where col3 LIKE 'aaa'; ... Preparing statement ... Processed response from shard 127.0.0.1:8609/solr/ks_7445.t1: maxScore numFound: 0, : null, elapsed time: 5 ms, token ranges: [(-9223372036854775808,-9223372036854775808]] [Solr CQL query thread-0] | ... ...

000-DTSE-Search-7445-60-DM-38 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7445-60-DM-39

Additional Detail:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7445-60-DM-40

Beider Morse Phonetic Matching

Image Source: http://horwitzfam.org/beider_and_book.htm Image Source: https://upgs.wordpress.com/2007/11/02/steve-morse/ https://en.wikipedia.org/wiki/Alexander_Beider https://en.wikipedia.org/wiki/Stephen_P._Morse

000-DTSE-Search-7445-60-DM-41 © DataStax, All Rights Reserved. Confidential.
