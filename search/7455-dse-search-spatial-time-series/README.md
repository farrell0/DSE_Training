# DSE Search: DSE Search, Spatial, Time Series

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Discussion Module

**Customer:** I am working through the DSE Search curriculum and need help with dse search, spatial, time series. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This discussion module in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, spatial, time series.

## Downloads

- [PDF slides](./7455-dse-search-spatial-time-series.pdf)
- [Original PowerPoint](../000-DTSE-Search-7455-DM-60%2C%20DSE%20Search%2C%20Spatial%2C%20Time%20Series.pptx)

## Converted Slides

## Discussion

Learn to deliver DSE spatial queries,

including time series. For example: Discussion

Module: • Did the pizza driver pass a given

point ? (Where’s my pizza ?) Spatial (not geospatial), • Is there hotel room availability for a Time Series given date ?

Prerequisites to this Discussion Module:

• That you are comfortable with

making and using DSE Search

geospatial objects and queries.

000-DTSE-Search-7455-60-DM-1 © DataStax, All Rights Reserved. Confidential.

Next page: Describe/offer business

use cases-

Discussion Lab:

Open Probe Open Probe

000-DTSE-Search-7455-60-DM-2 © DataStax, All Rights Reserved. Confidential.

Discuss: Spatial, and Time-

Describe business use cases for:

• Knowing that a driver passed

through a given location ?

• Or didn’t pass though a given

location ?

• Is in a location ?

• A resource is/is-not available on a

given date ?

How is a Lat/Lon pair similar to a span

of time ?

000-DTSE-Search-7455-60-DM-3 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7455-60-DM-4 © DataStax, All Rights Reserved. Confidential.

DSE Search, Spatial, Time Series

• Use RPT, geo=‘false’

• Set; worldBounds, maxDistErr,

distErrPct

• Casting; POINT, LINESTRING

• Operators; IsWithin, Intersects, []

(Range)

000-DTSE-Search-7455-60-DM-5 © DataStax, All Rights Reserved. Confidential.

Working with routes-

End to End

Example:

IsWithin, Intersects, POINT,

LINESTRING

000-DTSE-Search-7455-60-DM-6 © DataStax, All Rights Reserved. Confidential.

IsWithin, Intersects, CREATE KEYSPACE

DROP KEYSPACE IF EXISTS ks_7455;

CREATE KEYSPACE ks_7455 WITH

REPLICATION =

{'class': 'SimpleStrategy',

'replication_factor': 1};

USE ks_7455;

000-DTSE-Search-7455-60-DM-7 © DataStax, All Rights Reserved. Confidential.

IsWithin, Intersects, CREATE TABLE

CREATE TABLE t1

(

col1 TEXT,

my_point ' PointType ',

my_line ' LineStringType ',

PRIMARY KEY ((col1))

); Or TEXT-

There really aren’t

sane/usable assumptions

for these, to allow default

generation

000-DTSE-Search-7455-60-DM-8 © DataStax, All Rights Reserved. Confidential.

IsWithin, Intersects, Add Data

INSERT INTO t1 (col1, my_point, my_line)

VALUES ('1', ' POINT (10 10)',

' LINESTRING (10 10, 10 20, 10 30, 20 30, 20 20)' );

VALUES ('2', 'POINT(10 10)',

'LINESTRING(10 10, 10 20, 10 30, 20 30, 20 20, 20 10, 20 0)' );

VALUES ('3', 'POINT(30 30)',

'LINESTRING(30 30, 30 40, 20 40, 20 30, 20 20, 10 20, 10 30, 20 30)' );

VALUES ('4', 'POINT(20 30)',

'LINESTRING(20 30, 20 20, 10 20, 0 20)' );

000-DTSE-Search-7455-60-DM-9 © DataStax, All Rights Reserved. Confidential.

Same Data, Plotted, Page 1 of 2

40 40

30 30

20 20

10 10 X X

10 20 30 40 10 20 30 40

000-DTSE-Search-7455-60-DM-10 © DataStax, All Rights Reserved. Confidential.

Same Data, Plotted, Page 2 of 2

40 40

X 30 30 X

20 20

10 10

10 20 30 40 10 20 30 40

000-DTSE-Search-7455-60-DM-11 © DataStax, All Rights Reserved. Confidential.

LINESTRING data can not-

40

30 X

InvalidRequest: Error from server: code=2200 [Invalid query] message="Unable to make LineStringType from 20 'LINESTRING(30 30, 30 40, 20 40, 20 30, 20 20, 20 10, 30 10, 30 20, 20 20, 20 10, 20 0)' 'LINESTRING (30 30, 30 40, 20 40, 20 30, 20 20, 20 10, 30 10, 30 20, 20 20, 20 10, 20 0)' is not Points and edges cannot self-intersect simple. ." 10

10 20 30 40

000-DTSE-Search-7455-60-DM-12 © DataStax, All Rights Reserved. Confidential.

JIRA, DSP-11516

You can not smudge the values. E.g., add 0.00001 or similar

to overlapping points.

https://datastax.jira.com/browse/DSP-11516 DataStax

Internal Use

Only You have to break these LINESTRINGS in two-

000-DTSE-Search-7455-60-DM-13 © DataStax, All Rights Reserved. Confidential.

IsWithin, Intersects, CREATE SEARCH INDEX

// CREATE SEARCH INDEX ON t1

// WITH COLUMNS col1, my_point, my_line;

//

// InvalidRequest: Error from server: code=2200 [Invalid query]

// message="The search index schema could not be auto-generated

// because: Type org.apache.cassandra.db.marshal.LineStringType

// is not supported with automatic Solr schema generation.

// Specify 'lenient: true' in your resource generation options

// to ignore unsupported columns."

CREATE SEARCH INDEX ON t1

WITH COLUMNS col1, * {excluded : true } ;

000-DTSE-Search-7455-60-DM-14 © DataStax, All Rights Reserved. Confidential.

ALTER SEARCH ALTER SEARCH INDEX SCHEMA ON t1

ADD types.fieldType[@name='ft_rpt', INDEX, deploy @class='solr.SpatialRecursivePrefixTreeFieldType',

@ geo='false' ,

@ worldBounds='ENVELOPE(-1000, 1000, 1000, -1000)' ,

@ maxDistErr='0.001' , @distanceUnits='degrees'];

ALTER SEARCH INDEX SCHEMA ON t1

ADD fields.field[@name='my_point', @type='ft_rpt',

@indexed='true', @multiValued='false', @stored='true',

@docValues='true'];

ALTER SEARCH INDEX SCHEMA ON t1

ADD fields.field[@name='my_line', @type='ft_rpt',

@indexed='true', @multiValued='false', @stored='true',

@docValues='true'];

RELOAD SEARCH INDEX on t1;

REBUILD SEARCH INDEX ON t1;

000-DTSE-Search-7455-60-DM-15 © DataStax, All Rights Reserved. Confidential.

SELECT, IsWithin POINT

SELECT col1, my_point FROM t1

WHERE solr_query=

'{ "q" : "my_point : \"IsWithin(BUFFER(

POINT(30 30), 1))\"" }';

col1 | my_point

------+-------------------

3 | POINT (30.0 30.0)

000-DTSE-Search-7455-60-DM-16 © DataStax, All Rights Reserved. Confidential.

SELECT, IsWithin POINT

SELECT col1, my_point FROM t1

WHERE solr_query=

'{ "q" : "my_point : \"IsWithin(BUFFER(

POINT(20 30), 1))\"" }';

col1 | my_point

------+-------------------

4 | POINT (20.0 30.0)

000-DTSE-Search-7455-60-DM-17 © DataStax, All Rights Reserved. Confidential.

SELECT, IsWithin POINT

SELECT col1, my_point FROM t1

WHERE solr_query=

'{ "q" : "my_point : \"IsWithin(BUFFER(

POINT(20 30), 10))\"" }';

col1 | my_point

------+-------------------

4 | POINT (20.0 30.0)

3 | POINT (30.0 30.0)

000-DTSE-Search-7455-60-DM-18 © DataStax, All Rights Reserved. Confidential.

IsWithin using LINESTRING, Odd results-

SELECT * FROM t1 WHERE

solr_query= DataStax

'{ "q" : "my_line : \"IsWithin(BUFFER( Internal Use

POINT(20 30), 40))\"" }'; Only

000-DTSE-Search-7455-60-DM-19 © DataStax, All Rights Reserved. Confidential.

LINESTRING, Intersects

SELECT col1, my_line

FROM t1 WHERE

solr_query='my_line:"Intersects(

POINT(20 20))"';

col1 | my_line ------+----------------------------------------------------------------------------------------------------- 4 | LINESTRING (20.0 30.0, 20.0 20.0, 10.0 20.0, 0.0 20.0) 3 | LINESTRING (30.0 30.0, 30.0 40.0, 20.0 40.0, 20.0 30.0, 20.0 20.0, 10.0 20.0, 10.0 30.0, 20.0 30.0) 2 | LINESTRING (10.0 10.0, 10.0 20.0, 10.0 30.0, 20.0 30.0, 20.0 20.0, 20.0 10.0, 20.0 0.0) 1 | LINESTRING (10.0 10.0, 10.0 20.0, 10.0 30.0, 20.0 30.0, 20.0 20.0)

000-DTSE-Search-7455-60-DM-20 © DataStax, All Rights Reserved. Confidential.

LINESTRING, Intersects

SELECT col1, my_line FROM t1

WHERE solr_query='my_line:

"Intersects(POINT(30 40))"';

SELECT col1, my_line FROM t1

WHERE solr_query=

'{ "q" : "my_line : \"Intersects(

POINT(30 40))\"" }';

// same for both col1 | my_line ------+----------------------------------------------------------------------------------------------------- 3 | LINESTRING (30.0 30.0, 30.0 40.0, 20.0 40.0, 20.0 30.0, 20.0 20.0, 10.0 20.0, 10.0 30.0, 20.0 30.0)

000-DTSE-Search-7455-60-DM-21 © DataStax, All Rights Reserved. Confidential.

Working with routes-

End to End

Example:

IsWithin, Intersects, POINT,

LINESTRING

REVIEW

000-DTSE-Search-7455-60-DM-22 © DataStax, All Rights Reserved. Confidential.

Working with time series-

End to End

Example:

Ranges of dates/times.

000-DTSE-Search-7455-60-DM-23 © DataStax, All Rights Reserved. Confidential.

CREATE TABLE, add CREATE TABLE t2

( data, CREATE SEARCH col1 TEXT, INDEX my_dates 'PointType',

PRIMARY KEY ((col1))

);

INSERT INTO t2 (col1, my_dates)

VALUES ('101', 'POINT(2 5)');

VALUES ('102', 'POINT(2 3)');

VALUES ('103', 'POINT(4 5)');

VALUES ('104', 'POINT(1 2)');

VALUES ('105', 'POINT(1 3)');

VALUES ('106', 'POINT(1 6)');

CREATE SEARCH INDEX ON t2

WITH COLUMNS col1, * {excluded : true } ;

000-DTSE-Search-7455-60-DM-24 © DataStax, All Rights Reserved. Confidential.

ALTER SEARCH

INDEX ALTER SEARCH INDEX SCHEMA ON t2

ADD types.fieldType[@name='ft_rpt',

@class='solr.SpatialRecursivePrefixTreeFieldType',

@geo='false', No ENVELOPE, like @ worldBounds='0 0 365 365' , earlier @ maxDistErr='1' , @ distErrPct='0' ];

ALTER SEARCH INDEX SCHEMA ON t2

ADD fields.field[@name='my_dates', @type='ft_rpt',

@indexed='true', @multiValued='false', @stored='true',

@docValues='true'];

RELOAD SEARCH INDEX on t2;

REBUILD SEARCH INDEX on t2;

000-DTSE-Search-7455-60-DM-25 © DataStax, All Rights Reserved. Confidential.

106, 1-6 Same Data, Plotted 6

103, 4-5 101, 2-5 5 End (Day) y-axis 4

105, 1-3 102, 2-3 3

2

104, 1-2

1

5 1 2 3 4 6

Start (Day), x-axis 000-DTSE-Search-7455-60-DM-26 © DataStax, All Rights Reserved. Confidential.

Contains; exclusive to range

SELECT col1, my_dates

FROM t2

WHERE solr_query=

'{ "q" : "*:*", "fq" : "my_dates:

[0,1 TO 3,365]" }';

x y y x

col1 | my_dates

------+-----------------

104 | POINT (1.0 2.0)

102 | POINT (2.0 3.0)

105 | POINT (1.0 3.0)

000-DTSE-Search-7455-60-DM-27 © DataStax, All Rights Reserved. Confidential.

Intersects; not exclusive to range

SELECT col1, my_dates

FROM t2

WHERE solr_query=

'{ "q" : "*:*", "fq" : "my_dates:

[1,0 TO 365,3]" }';

col1 | my_dates

------+-----------------

104 | POINT (1.0 2.0)

106 | POINT (1.0 6.0)

102 | POINT (2.0 3.0)

105 | POINT (1.0 3.0)

101 | POINT (2.0 5.0)

000-DTSE-Search-7455-60-DM-28 © DataStax, All Rights Reserved. Confidential.

On a given date/time

SELECT col1, my_dates

FROM t2

WHERE solr_query=

'{ "q" : "*:*",

"fq" : "my_dates:

[4,0 TO 10,4]" }';

col1 | my_dates

------+-----------------

103 | POINT (4.0 5.0)

106 | POINT (1.0 6.0)

101 | POINT (2.0 5.0)

000-DTSE-Search-7455-60-DM-29 © DataStax, All Rights Reserved. Confidential.

Not on a given date/time

SELECT col1, my_dates

FROM t2

WHERE solr_query=

'{ "q" : "*:*",

"fq" : " NOT

my_dates:[4,0 TO 10,4]" }';

col1 | my_dates

------+-----------------

104 | POINT (1.0 2.0)

102 | POINT (2.0 3.0)

105 | POINT (1.0 3.0)

000-DTSE-Search-7455-60-DM-30 © DataStax, All Rights Reserved. Confidential.

Working with time series-

End to End

Example:

Ranges of dates/times.

REVIEW

000-DTSE-Search-7455-60-DM-31 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7455-60-DM-32
