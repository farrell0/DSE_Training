# DSE Search: DSE Search, Text Part 2

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Discussion Module

**Customer:** I am working through the DSE Search curriculum and need help with dse search, text part 2. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This discussion module in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, text part 2.

## Downloads

- [PDF slides](./7449-dse-search-text-part-2.pdf)
- [Original PowerPoint](../000-DTSE-Search-7449-DM-60%2C%20DSE%20Search%2C%20Text%20Part%202.pptx)

## Converted Slides

## Discussion

Wrap up remainder of Text Analytics. Discussion

Module: Not these, these are coming-

• A better treatment of query predicate, DSE Search, Text Analytics - query functions, other. Part 2

• Geospatial/spatial (time series)

• Capacity planning, tuning

000-DTSE-Search-7449-60-DM-1 © DataStax, All Rights Reserved. Confidential.

Discussion Lab:

What do you have, What do you

need-

000-DTSE-Search-7449-60-DM-2 © DataStax, All Rights Reserved. Confidential.

Amazon, Uber Eats: Name 3 You Have|Need

000-DTSE-Search-7449-60-DM-3 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7449-60-DM-4 © DataStax, All Rights Reserved. Confidential.

DSE Search (Derived Fields)

( Derived fields )

• copyField

• dynamicField (pass until Geospatial)

• (Default Field)

• ( Field Transformers )

000-DTSE-Search-7449-60-DM-5 © DataStax, All Rights Reserved. Confidential.

copyField: Its own object, ALTER SEARCH INDEX .. ADD copyField..

Use cases:

– Need multiple treatments (different analyzers) for

a given field (multiValued=false okay)

– Group multiple query attributes to a single

location (ease of use, a default field)

• multiValued = false // Attractive, but ..

• multiValued = true // Required for M:1

– Other

Source fields not stored in index. (No source fields are

stored in index.)

Destination field not stored in DSE table proper. (No

key column data is stored in the table proper.)

000-DTSE-Search-7449-60-DM-6 © DataStax, All Rights Reserved. Confidential.

End to End

Example:

copyField

000-DTSE-Search-7449-60-DM-7 © DataStax, All Rights Reserved. Confidential.

copyField example .. page 1 of 10

DROP KEYSPACE ks_7449; CREATE KEYSPACE ks_7449 WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}; CREATE SEARCH INDEX ON t6 WITH USE ks_7449; COLUMNS col1, CREATE TABLE t6 * { excluded : true }; ( col1 TEXT, col2 TEXT, col3 TEXT, col4 TEXT, col5 TEXT, col6 TEXT, col7 TEXT, col8 TEXT, col9 TEXT, col0 TEXT, PRIMARY KEY ((col1, col2)) );

000-DTSE-Search-7449-60-DM-8 © DataStax, All Rights Reserved. Confidential.

copyField example .. page 2 of 10

INSERT INTO t6 (col1, col2, col3, col4, col5, col6, col7, col8, col9, col0) VALUES ( 'aaa ', 'aaa', 'StarBucks ', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa');

VALUES ( 'bbb ', 'bbb', 'bbb', 'Chuck ', 'David ', 'Todd ', 'bbb', 'bbb', 'bbb', 'bbb');

VALUES ( 'ccc ', 'ccc', 'ccc', 'Chuck ', 'Mary ', 'Lincoln ', 'ccc', 'ccc', 'ccc', 'ccc');

VALUES ( 'ddd ', 'ddd', 'ddd', 'David ', 'Chuck ', 'Todd ', 'ddd', 'ddd', 'ddd', 'ddd');

000-DTSE-Search-7449-60-DM-9 © DataStax, All Rights Reserved. Confidential.

copyField example .. page 3 of 10

ALTER SEARCH INDEX SCHEMA ON t6 ADD fields.field[@name='col3', @type= 'StrField ', @indexed='false' , @multiValued='false', @stored='false'];

ALTER SEARCH INDEX SCHEMA ON t6 indexed=false ADD fieldType[@name= 'TextField71 ', @class= 'solr.TextField '] WITH '{"analyzer":{"tokenizer":{"class": "solr. KeywordTokenize rFactory"}, "filter":[{"class":"solr .LowerCaseFilter Factory"}]}}';

ALTER SEARCH INDEX SCHEMA ON t6 ADD fieldType[@name= 'TextField72 ', @class='solr. TextField '] WITH '{"analyzer":{"tokenizer":{"class": "solr. KeywordTokenizer Factory"}, "filter":[{"class":"solr. BeiderMorse FilterFactory"}]}}';

000-DTSE-Search-7449-60-DM-10 © DataStax, All Rights Reserved. Confidential.

copyField example .. page 4 of 10

ALTER SEARCH INDEX SCHEMA ON t6 ADD fields.field[@name= 'col71 ', @type= 'TextField71 ', @indexed='true', @ multiValued='false' , @stored=‘false’]; ALTER SEARCH INDEX SCHEMA ON t6 ADD fields.field[@name= 'col72 ', @type= 'TextField72 ', @indexed='true', @ multiValued='false' , @stored=‘false'];

ALTER SEARCH INDEX SCHEMA ON t6 ADD copyField [@ source='col3 ', @ dest='col71 ']; ALTER SEARCH INDEX SCHEMA ON t6 ADD copyField [@ source='col3 ', @ dest='col72 '];

RELOAD SEARCH INDEX ON t6; REBUILD SEARCH INDEX ON t6;

000-DTSE-Search-7449-60-DM-11 © DataStax, All Rights Reserved. Confidential.

copyField example .. page 5 of 10

SELECT col1, col3 FROM t6 WHERE col1 = 'aaa' ;

why ? // Fails, no index on col3 SELECT col1, col3 FROM t6 WHERE col3 = 'StarBucks';

// Fails, field not in table, needs solr_query predicate SELECT col1, col3 FROM t6 WHERE col71 = 'StarBucks';

SELECT col1, col3 FROM t6 WHERE solr_query = '{ "q" : "col71:starbucks"}';

SELECT col1, col3 FROM t6 WHERE solr_query = '{ "q" : "col72:starbux"}';

000-DTSE-Search-7449-60-DM-12 © DataStax, All Rights Reserved. Confidential.

copyField example .. page 6 of 10

ALTER SEARCH INDEX SCHEMA ON t6 ADD fields.field[@name= 'col4 ', @type='StrField', @indexed='false' , @multiValued='false', @stored='false']; ALTER SEARCH INDEX SCHEMA ON t6 ADD fields.field[@name= 'col5 ', @type='StrField', @indexed='false' , @multiValued='false', @stored='false']; ALTER SEARCH INDEX SCHEMA ON t6 ADD fields.field[@name= 'col6 ', @type='StrField', @indexed='false' , @multiValued='false', @stored='false'];

ALTER SEARCH INDEX SCHEMA ON t6 ADD fields.field[@name= 'col73 ', @type='StrField', @indexed='true', @ multiValued='false' , @stored=false']; sortable ? ALTER SEARCH INDEX SCHEMA ON t6 ADD fields.field[@name= 'col74 ', @type='StrField', @indexed='true', @ multiValued='true' , @stored=‘false'];

000-DTSE-Search-7449-60-DM-13 © DataStax, All Rights Reserved. Confidential.

copyField example .. page 7 of 10

ALTER SEARCH INDEX SCHEMA ON t6 ADD copyField[@source='col4', @dest='col73', @stored='false']; ALTER SEARCH INDEX SCHEMA ON t6 ADD copyField[@source='col5', @dest='col73', @stored='false']; ALTER SEARCH INDEX SCHEMA ON t6 ADD copyField[@source='col6', @dest='col73', @stored='false'];

ALTER SEARCH INDEX SCHEMA ON t6 ADD copyField[@source='col4', @dest='col74', @stored='false']; ALTER SEARCH INDEX SCHEMA ON t6 ADD copyField[@source='col5', @dest='col74', @stored='false']; ALTER SEARCH INDEX SCHEMA ON t6 ADD copyField[@source='col6', @dest='col74', @stored='false'];

RELOAD SEARCH INDEX ON t6; REBUILD SEARCH INDEX ON t6;

000-DTSE-Search-7449-60-DM-14 © DataStax, All Rights Reserved. Confidential.

copyField example .. page 8 of 10

SELECT col1, col4, col5, col6 FROM t6 WHERE solr_query = '{ "q" : "col73:(Chuck David Todd)"}';

col1 | col4 | col5 | col6 ------+-------+-------+--------- ddd | David | Chuck | Todd bbb | Chuck | David | Todd ccc | Chuck | Mary | Lincoln

Hint: Could have a SELECT col1, col4, col5, col6 FROM t6 perfect 1.0 score WHERE solr_query = '{ "q" : "col74:(Chuck David Todd)"}';

col1 | col4 | col5 | col6 ------+-------+-------+--------- ddd | David | Chuck | Todd bbb | Chuck | David | Todd ccc | Chuck | Mary | Lincoln

000-DTSE-Search-7449-60-DM-15 © DataStax, All Rights Reserved. Confidential.

copyField example .. page 9 of 10

SELECT col1, col4, col5, col6 FROM t6 WHERE solr_query = '{ "q" : "col73:(+Chuck +David +Todd)"}'; SELECT col1, col4, col5, col6 FROM t6 WHERE solr_query = '{ "q" : "col74:(+Chuck +David +Todd)"}';

col1 | col4 | col5 | col6 why ? ------+-------+-------+------ ddd | David | Chuck | Todd bbb | Chuck | David | Todd

000-DTSE-Search-7449-60-DM-16 © DataStax, All Rights Reserved. Confidential.

copyField example .. page 10 of 10

// Finds no rows SELECT col1, col4, col5, col6 FROM t6 WHERE solr_query = 'col73:"Chuck David Todd"'; why ? SELECT col1, col4, col5, col6 FROM t6 WHERE solr_query = 'col74:"Chuck David Todd"';

https://docs.datastax.com/en/dse/5.1/dse-dev/datastax_enterprise/search/queryTerms.html

https://docs.datastax.com/en/dse/5.1/dse-dev/datastax_enterprise/search/advancedTerms.html

000-DTSE-Search-7449-60-DM-17 © DataStax, All Rights Reserved. Confidential.

End to End

Example:

Review copyField,

000-DTSE-Search-7449-60-DM-18 © DataStax, All Rights Reserved. Confidential.

dynamicField: Also its Use cases:

own object – Geospatial/spatial, definitely

• Minimally; take a Lat/Lon pair, split, and

allow for a two dimensional index

• Pass for now-

– Dynamic schemas ?? (Not with DSE)

Source: https://docs.datastax.com/en/dse/5.1/dse-dev/datastax_enterprise/search/usingDynamicFields.html

https://docs.datastax.com/en/dse/6.0/dse-dev/datastax_enterprise/search/unsupportedSearchFeatures.html

000-DTSE-Search-7449-60-DM-19 © DataStax, All Rights Reserved. Confidential.

Default Field:

Use cases:

– Handy ?

edismax.uf ??

– Word proximity; some predicate

expressions are hard without presence

of a default field

– Config property, not schema

property/object

000-DTSE-Search-7449-60-DM-20 © DataStax, All Rights Reserved. Confidential.

End to End

Example:

(Default Field), and Word

Proximity

000-DTSE-Search-7449-60-DM-21 © DataStax, All Rights Reserved. Confidential.

Default Field Example .. page 1 of 5

DROP KEYSPACE IF EXISTS ks_7449;

CREATE KEYSPACE ks_7449 WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE ks_7449;

CREATE TABLE t7 ( col1 TEXT PRIMARY KEY, col2 TEXT, col3 TEXT );

000-DTSE-Search-7449-60-DM-22 © DataStax, All Rights Reserved. Confidential.

Default Field Example .. page 2 of 5

INSERT INTO t7 (col1, col2, col3) VALUES ('aaa', 'test space ' , 'test'); INSERT INTO t7 (col1, col2, col3) VALUES ('bbb', 'space test ' , 'test'); INSERT INTO t7 (col1, col2, col3) VALUES ('ccc', 'test one two space ' , 'test'); INSERT INTO t7 (col1, col2, col3) VALUES ('ddd', 'test one two three space ' , 'test'); INSERT INTO t7 (col1, col2, col3) VALUES ('eee', 'test one two three four space ', 'test');

CREATE SEARCH INDEX ON t7 WITH COLUMNS col1, * { excluded : true };

000-DTSE-Search-7449-60-DM-23 © DataStax, All Rights Reserved. Confidential.

Default Field Example .. page 3 of 5

// KeywordTokenizer does not work here; need tokens

ALTER SEARCH INDEX SCHEMA ON t7 ADD fieldType[@name='TextField81', @class='solr.TextField'] WITH Can we ever sort on col2 ? '{"analyzer":{"tokenizer": {"class":"solr. StandardTokenizer Factory"} }}'; What is the (default) sort ?

ALTER SEARCH INDEX SCHEMA ON t7 ADD fields.field[@name='col2', @type='TextField81', @default='true'];

RELOAD SEARCH INDEX ON t7; REBUILD SEARCH INDEX ON t7;

000-DTSE-Search-7449-60-DM-24 © DataStax, All Rights Reserved. Confidential.

Default Field Example .. page 4 of 5

SELECT * FROM t7 WHERE solr_query='col2:"test space"~10';

col1 | col2 | col3 | solr_query ------+-------------------------------+------+------------ aaa | test space | test | null bbb | space test | test | null ccc | test one two space | test | null ddd | test one two three space | test | null eee | test one two three four space | test | null

SELECT * FROM t7 WHERE solr_query='col2:"test space"~2';

aaa | test space | test | null bbb | space test | test | null ccc | test one two space | test | null

SELECT * FROM t7 WHERE solr_query='col2:"test space"~1';

aaa | test space | test | null

000-DTSE-Search-7449-60-DM-25 © DataStax, All Rights Reserved. Confidential.

Default Field Example .. page 5 of 5

// Fails with a, // InvalidRequest: Error from server: code=2200 [Invalid query] // message="no field name specified in query and no default specified SELECT * FROM t7 WHERE solr_query='"test space"~2';

ALTER SEARCH INDEX CONFIG ON t7 SET defaultQueryField = 'col2' ;

RELOAD SEARCH INDEX ON t7; REBUILD SEARCH INDEX ON t7;

Or, at least you know SELECT * FROM t7 WHERE solr_query='"test space"~2'; why this predicate

works-

000-DTSE-Search-7449-60-DM-26 © DataStax, All Rights Reserved. Confidential.

End to End

Example:

(Default Field), and Word

Review Proximity,

000-DTSE-Search-7449-60-DM-27 © DataStax, All Rights Reserved. Confidential.

Field Transformers: Current landscape

https:// www.datastax.com/dev/blog/dse-field-tran sformers • An eleven page article written using Java and Maven, this article walks you through the complete set of steps to design and implement. • In effect, take a value, store it in a DSE ETL/ELT table, and upon insert/update (and delete), apply a (custom parser), pick out the specific and distinct data elements, and DSE Search index them. Newly created data stored in index, not in • There are only two Java classes you DSE table columns proper. have to extend, FieldInputTransformer, But, still super handy. and FieldOutputTransformer. Standard Java, and much of this Java code is boilerplate.

000-DTSE-Search-7449-60-DM-28 © DataStax, All Rights Reserved. Confidential.

0.16 .314

DSE Search Text

Query Parsing, 0

1.0

Scoring • Text, score (relevancy)

• Geospatial, geodist()

• Spatial, dist(), other

• Scalars (none, sort)

000-DTSE-Search-7449-60-DM-29 © DataStax, All Rights Reserved. Confidential.

Database Server Backends: Stages

Parser

What do you know Q Optimizer right now ?

Why are parser and Q Processor

(scoring) related ?

(Run time)

Client Server

000-DTSE-Search-7449-60-DM-30 © DataStax, All Rights Reserved. Confidential.

DSE Search (Lucene) Scoring Model, Part 1 of 2

• Until Lucene 4, only Vector • tf, Term Frequency. Count per doc, Space Model (Tf-Idf) higher == higher score • “Lucene Scoring Model”, the • idf, Inverse Doc Freq. Count of term default; combination of VSM and across all docs. Denominator in

Boolean (AND, OR) equation tf / (x), lower == higher

score

• coord, Coordinator Factor. Higher • Post Lucene 4- count of distinct terms found in given (Scoring Model is pluggable) doc == higher score Okapi BM (not common) • fieldNorm, Field Length. More terms Language Model (Which words are per doc == lower score common/rare in this language) Divergence from Randomness (fraud, Source: http://www.solrtutorial.com/solr-search-relevancy.html security) Information-based (Sentiment)

000-DTSE-Search-7449-60-DM-31 © DataStax, All Rights Reserved. Confidential.

Pro:

DSE Search • Simple model based on linear algebra • Term weights not binary (Lucene) Scoring • Allows computing a continuous degree of similarity between queries and documents Model, Part 2 of 2 • Allows ranking documents according to their possible

relevance • Allows partial matching • Scores not meaningful Con: • Long documents are poorly represented because they across queries have poor similarity values (a small scalar product and a • Score normalized; always large dimensionality) between 0 and 1 • Search keywords must precisely match document terms; • Fast, hides complexity word substrings might result in a "false positive match • "Semantic sensitivity; documents with similar context but

different term vocabulary won't be associated, resulting in a "false negative match“ • The order in which the terms appear in the document is lost in the vector space representation • Theoretically assumes terms are statistically independent Source: https://en.wikipedia.org/wiki/Vector_space_model • Weighting is intuitive but not very formal

000-DTSE-Search-7449-60-DM-32 © DataStax, All Rights Reserved. Confidential.

Score: Example, Part 1 of 2

Solr Admin UI

-> Core

-> Query TAB

-> fl = * , score

-> debugQuery=true

000-DTSE-Search-7449-60-DM-33 © DataStax, All Rights Reserved. Confidential.

Score: Example, Part 2 of 2

"ddd": "0.7590632 = weight(col2:three in 4) [], result of: 0.7590632 = score (doc=4,freq=1.0 = termFreq=1.0), product of: 0.87546873 = idf(docFreq=2, docCount=5)

0.86703634 = tfNorm, computed from: 1.0 = termFreq=1.0 1.2 = parameter k1

0.75 = parameter b 3.8 = avgFieldLength 5.2244897 = fieldLength“

"eee": "0.6454073 = weight(col2:three in 0) [], result of: 0.6454073 = score (doc=0,freq=1.0 = termFreq=1.0), product of: 0.87546873 = idf(docFreq=2, docCount=5)

0.73721343 = tfNorm, computed from: 1.0 = termFreq=1.0 1.2 = parameter k1

0.75 = parameter b 3.8 = avgFieldLength 7.111111 = fieldLength"

Solr Admin UI

-> Core

-> Query TAB

-> fl = * , score

-> debugQuery=true

000-DTSE-Search-7449-60-DM-34 © DataStax, All Rights Reserved. Confidential.

Scoring: q and fq (fq, not covered yet)

• Most queries thus far (JSON) have

been “q”, query predicate

• “fq” are a further set of predicates

applied to the results of “q”

- Not a correlated subquery or similar,

(no new columns, rows)

- Just further (filtering)

• fq filter activity does not affect score

000-DTSE-Search-7449-60-DM-35 © DataStax, All Rights Reserved. Confidential.

Boosting: Index and Query, • Index time, No (Solr, Yes)

Positive and Negative • Query time, Yes

• Using boost, omitNorms=false

• (Not boost, save space, = true) • Caret; pos value , alter the score for

the given predicate (Only Lucene supports col4 | col5 | col5 neg boost; Solr and thus DSE doesn’t) -------+-------+------- David | Chuck | Chuck • Tilde (unrelated to boost) How many Chuck | Mary | Mary character misspellings Chuck | David | David aaa | aaa | aaa (Low numbers only.)

SELECT * FROM t6

WHERE solr_query =

'{ "q" : "(col73:%huck^8 OR

col74:chuck~1)" }' ;

000-DTSE-Search-7449-60-DM-36 © DataStax, All Rights Reserved. Confidential.

Remainder of

Field Type, Field

Attributes

000-DTSE-Search-7449-60-DM-37 © DataStax, All Rights Reserved. Confidential.

Discussion Lab:

Matching pairs – Match the field

type and field properties on the

right with the correct term on the

left

000-DTSE-Search-7449-60-DM-38 © DataStax, All Rights Reserved. Confidential.

Field Type, Field, Attributes: Covered

Field Type Field

Name Name

Type Class

000-DTSE-Search-7449-60-DM-39 © DataStax, All Rights Reserved. Confidential.

Field Type, Field, indexed=true

Attributes: Covered indexed=false

stored=t|f

Word Proximity docValues=t|f

multiValued=true Boosting, false=Y multiValued=false

default= str Highlighting, false=N

precisionStep=n

(Irrelevant, ignored) positionIncrementGap=n

termVectors=t|f (Space savings) termPositions=t|f

termOffsets=t|f multiValued

omitNorms=t|f

000-DTSE-Search-7449-60-DM-40 © DataStax, All Rights Reserved. Confidential.

Field Type, Field, Attributes: indexed=true

Covered indexed=false

stored=t|f

docValues=t|f

multiValued=true copyField M:1

multiValued=false

copyField 1:1 default= str

precisionStep=n

Collection positionIncrementGap=n

termVectors=t|f Non-collection termPositions=t|f

termOffsets=t|f

omitNorms=t|f

000-DTSE-Search-7449-60-DM-41 © DataStax, All Rights Reserved. Confidential.

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

000-DTSE-Search-7449-60-DM-42 © DataStax, All Rights Reserved. Confidential.

Field Type, Field,

Attributes: Covered

StrField

KeywordTokenizer

TextField

StandardTokenizer

TrieDoubleField

docValues Word Proximity

docValues

000-DTSE-Search-7449-60-DM-43 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7449-60-DM-44 © DataStax, All Rights Reserved. Confidential.

Field Type, Field, Attributes: Not (Yet) Covered

• autoGeneratePhraseQueries, For text fields. If true, Solr automatically generates phrase

queries for adjacent terms. If false, terms must be enclosed in double-quotes to be treated

as phrases.

• enableGraphQueries, (needs graph query parser, not common)

• docValuesFormat, (not common)

• postingsFormat, (not common)

• sortMissingFirst sortMissingLast, Control the placement of documents when a sort field is

not present

000-DTSE-Search-7449-60-DM-45 © DataStax, All Rights Reserved. Confidential.

Field Type, Field, Attributes: Not (Yet) Covered

• omitTermFreqAndPositions, (related to omitForms), If true, omits term frequency,

positions, and payloads from postings for this field. This can be a performance boost for

fields that don’t require that information.

• omitPositions, (related to omitNorms), Similar to omitTermFreqAndPositions but preserves

term frequency information.

• termPayloads. (related to other term*)

• useDocValuesAsStored, (related to stored, not relevant)

• large, (related to stored, not relevant)

• default (related to stored, not relevant)

000-DTSE-Search-7449-60-DM-46 © DataStax, All Rights Reserved. Confidential.

Limits,

Unsupported

Features

000-DTSE-Search-7449-60-DM-47 © DataStax, All Rights Reserved. Confidential.

Unsupported Features/Limits: C* <-> DSE <-> Solr

Source: https://docs.datastax.com/en/dse/6.0/dse-dev/datastax_enterprise/search/unsupportedSearchFeatures.html

000-DTSE-Search-7449-60-DM-48 © DataStax, All Rights Reserved. Confidential.

Unsupported Features/Limits: C* <-> DSE <-> Solr

Source: https://docs.datastax.com/en/dse/6.0/dse-dev/datastax_enterprise/search/unsupportedSearchFeatures.html

000-DTSE-Search-7449-60-DM-49 © DataStax, All Rights Reserved. Confidential.

Unsupported Features/Limits: C* <-> DSE <-> Solr

Source: https://docs.datastax.com/en/dse/6.0/dse-dev/datastax_enterprise/search/unsupportedSearchFeatures.html

000-DTSE-Search-7449-60-DM-50 © DataStax, All Rights Reserved. Confidential.

Unsupported Features/Limits: C* <-> DSE <-> Solr

Source: https://docs.datastax.com/en/dse/6.0/dse-dev/datastax_enterprise/search/unsupportedSearchFeatures.html

000-DTSE-Search-7449-60-DM-51 © DataStax, All Rights Reserved. Confidential.

Unsupported Features/Limits: C* <-> DSE <-> Solr

Source: https://docs.datastax.com/en/dse/6.0/dse-dev/datastax_enterprise/search/unsupportedSearchFeatures.html

000-DTSE-Search-7449-60-DM-52 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7449-60-DM-53

Additional Content:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7449-60-DM-54

Analyzer: index or ALTER SEARCH INDEX SCHEMA ON t6 ADD fieldType[@name='TextFieldB1', query @class='solr.TextField'] WITH '{"analyzer":{ "type" : "index" , "tokenizer": {"class":"solr.KeywordTokenizerFactory"}, "filter":[{"class":"solr.LowerCaseFilterFactory"}]}}'; The analyzer attribute to set

ALTER SEARCH INDEX SCHEMA ON t6 an analyzer as index-only, ... or query-only; the default is '{"analyzer": {"type" : “query" , "tokenizer": both. {"class":"solr.KeywordTokenizerFactory"}, ...

SELECT col1, col4 FROM t6 WHERE solr_query = '{ "q" : "col4:david"}';

col1 | col4 ------+------- ddd | David

000-DTSE-Search-7449-60-DM-55 © DataStax, All Rights Reserved. Confidential.

Phonetic Matching

Phonetic matching algorithms may be used to encode tokens so that two

different spellings that are pronounced similarly will match.

• For overviews of and comparisons between algorithms, see

http://en.wikipedia.org/wiki/Phonetic_algorithm

http://ntz-develop.blogspot.com/2011/03/phonetic-algorithms.html

• Algorithms this category are:

Beider-Morse Phonetic Matching (BMPM)

Daitch-Mokotoff Soundex

Double Metaphone, Metaphone

SoundexRefined Soundex

Caverphone

Kölner Phonetik a.k.a. Cologne Phonetic

NYSIIS

000-DTSE-Search-7449-60-DM-56 © DataStax, All Rights Reserved. Confidential.
