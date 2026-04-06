# DSE Search: DSE Search, Scalars

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Discussion Module

**Customer:** I am working through the DSE Search curriculum and need help with dse search, scalars. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This discussion module in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, scalars.

## Downloads

- [PDF slides](./7447-dse-search-scalars.pdf)
- [Original PowerPoint](../000-DTSE-Search-7447-DM-60%2C%20DSE%20Search%2C%20Scalars.pptx)

## Converted Slides

## Discussion

Scalars: Non-tokenized column values, Discussion letters, numbers

Module:

DSE Search, Scalars

000-DTSE-Search-7447-60-DM-1 © DataStax, All Rights Reserved. Confidential.

Discussion Lab:

Matching pairs – Match the

query on the right with the

scalar, non-scalar label on the

left

000-DTSE-Search-7447-60-DM-2 © DataStax, All Rights Reserved. Confidential.

Discussion Lab: Queries- Scalar, Non-scalar

col1 = x AND col2 = y

col1 = x OR col2 = y

col1 = x ORDER BY col2

(Non-scalar) col1 > x AND col2 < y

col1 LIKE ‘Dav*’

solr_query = '{"q":"col4:stARrbUx"}'

solr_query = '{"q":"col4:stARrbUcks"}'

000-DTSE-Search-7447-60-DM-3 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7447-60-DM-4 © DataStax, All Rights Reserved. Confidential.

docValues: field type property, and/or field property

• https://

lucene.apache.org/solr/guide/6_6/do

cvalues.html#DocValues-EnablingDo

cValues

• Supported column types

– StrField, UUIDField

– Any Trie*; numeric fields, date fields,

EnumField

– Boolean

– Int, Long, Float, Double, DatePointField

• TextField with KeywordTokenizer

000-DTSE-Search-7447-60-DM-5 © DataStax, All Rights Reserved. Confidential.

docValues: Why-

The standard way that Solr builds the index is with an inverted index . This style builds a list of terms found in all the documents in the index and next to each term is a list of documents that the term appears in ( as well as how many times the term appears in that document ). This makes search very fast - since users search by terms, having a ready list of term-to-document values makes the query process faster.

For other features that we now commonly associate with search, such as sorting, faceting, and highlighting , this approach is not very efficient . The faceting engine , for example, must look up each term that appears in each document that will make up the result set and pull the document IDs in order to build the facet list . In Solr, this is maintained in memory , and can be slow to load (depending on the number of documents, terms, etc.).

In Lucene 4.0, a new approach was introduced. DocValue fields are now column-oriented fields with a document-to-value mapping built at index time. This approach promises to relieve some of the memory requirements of the fieldCache and make lookups for faceting, sorting , and grouping much faster .

Source: https://lucene.apache.org/solr/guide/6_6/docvalues.html#DocValues-EnablingDocValues

000-DTSE-Search-7447-60-DM-6 © DataStax, All Rights Reserved. Confidential.

docValues: Why, short version-

A shorter version ?

• The column value is not

stored in a Tf-Idf index.

• Tokens are stored in the Tf-

Idf index.

• You can reassemble the

column value from tokens,

but ..

000-DTSE-Search-7447-60-DM-7 © DataStax, All Rights Reserved. Confidential.

StrField versus TextField: (2012 article)

“A text field is a sequence of terms that has been tokenized while a string field is a single term (although it can also be multivalued). “ Punctuation and spacing is ignored for text fields . Text tends to be lowercased, stemmed , and even stop words removed . You tend to search text using a handful of keywords whose exact order is not required , although quoted phrases can be used as well. Fuzzy queries can be done on individual terms (words). Wild cards as well.

“ String fields are literal character strings with all punctuation, spacing, and case preserved. Anything other than exact match is done using wild cards , although (a fuzzy query is also supported). “String fields are useful for facets and filter queries or display. Text fields are useful for keyword search.

“Synonyms are a token filtering, which applies to text fields, not string fields. “A fuzzy query would not work properly for a synonym expansion in which some of the terms are phrases, but should otherwise work for a text field term.

Source: http://lucene.472066.n3.nabble.com/Difference-between-textfield-and-strfield-td3986916.html

000-DTSE-Search-7447-60-DM-8 © DataStax, All Rights Reserved. Confidential.

KeywordTokenizer: the default for TextField

• The non-tokenizer tokenizer-

• Officially grey per,

https://lucene.apache.org/solr/guide/6_6/docvalue s.html#DocValues-EnablingDocValues

• docValues this

• Can chain; lowercase filter ??

• Was default < 6.x

000-DTSE-Search-7447-60-DM-9 © DataStax, All Rights Reserved. Confidential.

• DSE cluster, with Search enabled

• Authority to make tables, other

• CQLSH/Studio access-

• All new example; scalars

End to End

Example:

Scalars; StrField, (numerics),

TextField with

KeywordTokenizer

000-DTSE-Search-7447-60-DM-10 © DataStax, All Rights Reserved. Confidential.

Example Scalars .. page 1 of 6

DROP KEYSPACE ks_7447; CREATE KEYSPACE ks_7447 WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}; CREATE SEARCH INDEX ON t3 WITH USE ks_7447; COLUMNS col1, CREATE TABLE t3 * { excluded : true }; ( col1 TEXT, col2 TEXT, col3 TEXT, col4 TEXT, col5 TEXT, col6 DOUBLE, col7 INT, col8 DOUBLE, col9 INT, col0 TEXT, PRIMARY KEY ((col1, col2)) );

000-DTSE-Search-7447-60-DM-11 © DataStax, All Rights Reserved. Confidential.

Example Scalars .. page 2 of 6

INSERT INTO t3 (col1, col2, col3, col4, col5, col6, col7, col8, col9, col0) VALUES ( 'aaa ', 'aaa', 'Dave ', 'Dave ', 'aaa',

17.76 , 17,

17.76 , 17, 'aaa');

VALUES ( 'bbb ', 'bbb', 'David ', 'David ', 'bbb',

17.092 , 17,

17.092 , 17, 'bbb');

VALUES ( 'ccc ', 'ccc', 'Davidia ', 'Davidia ', 'ccc',

16.003 , 16,

16.003 , 16, 'ccc');

VALUES ( 'ddd ', 'ddd', 'Sophie ', 'Stinky ', 'ddd',

16.00002 , 16,

16.00002 , 16, 'ddd');

000-DTSE-Search-7447-60-DM-12 © DataStax, All Rights Reserved. Confidential.

Example Scalars .. page 3 of 6

ALTER SEARCH INDEX SCHEMA ON t3 ALTER SEARCH INDEX SCHEMA ON t3 ADD types.fieldtype[@class= ADD types.fieldtype[@class= 'org.apache.solr.schema .StrField ', 'org.apache.solr.schema .TrieDoubleField ', @name='StrField53']; @name='TrieDoubleField55'];

ALTER SEARCH INDEX SCHEMA ON t3 ALTER SEARCH INDEX SCHEMA ON t3 ADD fieldType[@name='TextField54', ADD types.fieldtype[@class= @class='solr. TextField '] WITH 'org.apache.solr.schema. TrieIntField ', '{"analyzer":{"tokenizer":{"class": @name='TrieIntField56']; "solr .KeywordTokenizer Factory"}, "filter":{"class":"solr .LowerCaseFilter Factory"}}}';

000-DTSE-Search-7447-60-DM-13 © DataStax, All Rights Reserved. Confidential.

Example Scalars .. page 4 of 6

ALTER SEARCH INDEX SCHEMA ON t3 ADD fields.field[@name='col3', @type='StrField53', @docValues='true']; ALTER SEARCH INDEX SCHEMA ON t3 ADD fields.field[@name='col4', @type='TextField54', @docValues='true']; ALTER SEARCH INDEX SCHEMA ON t3 ADD fields.field[@name='col6', @type='TrieDoubleField55', @docValues='true']; ALTER SEARCH INDEX SCHEMA ON t3 ADD fields.field[@name='col7', @type='TrieIntField56', @docValues='true'];

RELOAD SEARCH INDEX ON t3; REBUILD SEARCH INDEX ON t3;

000-DTSE-Search-7447-60-DM-14 © DataStax, All Rights Reserved. Confidential.

Example Scalars .. page 5 of 6

SELECT * FROM t3 ORDER BY col6 ASC, col7 DESC, col3 ASC; SELECT * FROM t3 WHERE col6 > 12.0 AND col7 < 26;

// The statement below fails SELECT * FROM t3 WHERE col6 > 12.0 OR col7 < 26;

SELECT * FROM t3 WHERE solr_query = 'col6:[12.0 TO *] OR col7:[* TO 26]'; SELECT * FROM t3 WHERE solr_query = 'col6:[12.0 TO *] AND col7:[* TO -10]';

// The statement below fails SELECT * FROM t3 WHERE solr_query = 'col6:[12.0 TO *] AND col7:[* TO 26]' ORDER BY col6 ASC;

SELECT * FROM t3 WHERE solr_query = '{"q" : "col6:[12.0 TO *] AND col7:[* TO 26]", "sort":"col6 ASC, col7 DESC, col3 ASC" }';

000-DTSE-Search-7447-60-DM-15 © DataStax, All Rights Reserved. Confidential.

Example Scalars .. page 6 of 6

SELECT * FROM t3 WHERE col3 LIKE 'Dav% '; col3

WHERE col3 LIKE 'dav% ';

SELECT * FROM t3 WHERE col4 LIKE 'Dav% ';

col4 WHERE col4 LIKE 'dav% ';

WHERE col4 LIKE ' %av% ';

000-DTSE-Search-7447-60-DM-16 © DataStax, All Rights Reserved. Confidential.

End to End

Example:

Scalars; StrField, (numerics),

TextField with

KeywordTokenizer Review

000-DTSE-Search-7447-60-DM-17 © DataStax, All Rights Reserved. Confidential.

Search predicates: CQL or JSON

https:// docs.datastax.com/en/datastax_enterprise/4.8/data stax_enterprise/srch/srchJSON.html CQL (search predicates)

https://docs.datastax.com/en/datastax_enterprise/

4.8/datastax_enterprise/srch/srchCql.html

WHERE solr_query = 'col6:[12.0 TO *] OR col7:[* TO 26]';

WHERE solr_query = '{"q" : "col6:[12.0 TO *] AND col7:[* TO 26]", "sort":"col6 ASC, col7 DESC, col3 ASC" }'; JSON (search predicates)

000-DTSE-Search-7447-60-DM-18 © DataStax, All Rights Reserved. Confidential.

CQL Completeness: DSE 6.x, and pre 6.x

• > < <= => = !=

• IS NOT NULL

• IS NULL (Fails: 6.0 and before)

• IN (col in list of static values)

• CONTAINS (Array/collection types: Set, List Map)

• LIKE (StrField, fails on TextField )

000-DTSE-Search-7447-60-DM-19 © DataStax, All Rights Reserved. Confidential.

CONTAINS multiValued : field property

• Collections: SET, LIST, MAP

CREATE TABLE my_table positionIncrementGap ( col1 TEXT, Used for tokenized text only- col2 TEXT, col3 TEXT, Field type property ?? col4 TEXT, col8 SET<TEXT>, “For multivalued fields, specifies a PRIMARY KEY (col1) distance between multiple values,

which prevents spurious phrase ); matches

• Use cases:

– Tags – 32K column value limit – (Other)

000-DTSE-Search-7447-60-DM-20 © DataStax, All Rights Reserved. Confidential.

Where does the word Trie “In computer science, a trie, also called digital tree and sometimes radix tree or come from ? prefix tree (as they can be searched by prefixes), is a kind of search tree—an ordered tree data structure that is used to store a dynamic set or associative array where the keys are usually strings.

Unlike a binary search tree, no node in the tree stores the key associated with that node; instead, its position in the tree defines the key with which it is associated. All the descendants of a node have a common prefix of the string associated with that node, and the root is associated with the empty string.

Values are not necessarily associated with every node. Rather, values tend only to be Source: http://mentaldetritus.blogspot.com/2013/01/grokking-solr-trie-fields.htmlhttp:// associated with leaves, and with some inner mentaldetritus.blogspot.com/2013/01/grokking-solr-trie-fields.html nodes that correspond to keys of interest~ https://en.wikipedia.org/wiki/Trie

000-DTSE-Search-7447-60-DM-21 © DataStax, All Rights Reserved. Confidential.

Trie* : precisionStep, ALTER SEARCH INDEX SCHEMA ON t3 ADD types.fieldtype[@class= field type property 'org.apache.solr.schema.TrieDoubleField', @name='TrieDoubleField61', @precisionStep='16' ];

ALTER SEARCH INDEX SCHEMA ON t3 ADD types.fieldtype[@class= • A lower value has more 'org.apache.solr.schema.TrieDoubleField', index entries ( > disk size) and @name='TrieDoubleField62', @precisionStep='4 ']; faster index processing.

• A higher value has fewer ALTER SEARCH INDEX SCHEMA ON t3 DROP fields.field[@name='col6']; index entries ( < disk size) and

slower index processing. ALTER SEARCH INDEX SCHEMA ON t3 ADD fields.field[@name='col6', @type='TrieDoubleField61', @docValues='true']; • Default == 8 ALTER SEARCH INDEX SCHEMA ON t3 • 0 (zero) == fastest ADD fields.field[@name='col8', @type='TrieDoubleField62', @docValues='true'];

000-DTSE-Search-7447-60-DM-22 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7447-60-DM-23

Additional Content:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7447-60-DM-24

DSE to Solr field type mappings-

https://

docs.datastax.com/en/data stax_enterprise/5.0/datast ax_enterprise/srch/solrTyp eMapping.html

https://

lucene.apache.org/solr/

guide/6_6/field-types-

included-with-solr.html

000-DTSE-Search-7447-60-DM-25 © DataStax, All Rights Reserved. Confidential.

Solutions:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7447-60-DM-26

Discussion Lab: Queries- Scalar, Non-scalar

col1 = x AND col2 = y

col1 = x OR col2 = y

col1 = x ORDER BY col2

(Non-scalar) col1 > x AND col2 < y

col1 LIKE ‘Dav*’

solr_query = '{"q":"col4:stARrbUx"}'

solr_query = '{"q":"col4:stARrbUcks"}'

000-DTSE-Search-7447-60-DM-27 © DataStax, All Rights Reserved. Confidential.
