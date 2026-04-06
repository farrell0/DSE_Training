# DSE Search: DSE Search, Geo-Spatial

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Search curriculum and need help with dse search, geo-spatial. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, geo-spatial.

## Downloads

- [PDF slides](./7454-dse-search-geo-spatial.pdf)
- [Original PowerPoint](../000-DTSE-Search-7454-PL-60%2C%20DSE%20Search%2C%20Geo-Spatial.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on Discussion

Module 7453, where most of the objects we

create in this lab were introduced. Practice Lab:

• This Practice Lab requires a working DSE DSE Search, Geospatial system, with DSE Search enabled, and with

ability to execute CQL DDL.

• If running the optional portions of this lab, this

Practice Lab requires a ssh(C) prompt on all

nodes operating DSE Search. A node reboot

is required.

• All commands are run from CQLSH, or DSE

Studio. CQLSH is required to COPY data into

(a table).

000-DTSE-Search-7454-60-PL-1 © DataStax, All Rights Reserved. Confidential.

Challenge 1: Closest Starbucks, USA

• 2017; 17,000 Starbucks locations

USA

• Github downloaded data; 6000 US

Starbucks locations, 10 years old ?

• Create the runtime to support

the query; Where is my closest

Starbucks ?

000-DTSE-Search-7454-60-PL-2 © DataStax, All Rights Reserved. Confidential.

Challenge 1: Create basic runtime, Load Data-

• Given file; 7454_my_mapdata.small.csv

• CREAT KEYSPACE ...

• CREATE TABLE ...

• Load data;

COPY my_mapdata

(

md_pk,

...

md_type

)

FROM '7454_my_mapdata.small.csv'

WITH HEADER = TRUE ;

Execute all of the instructions on

the notes page below-

000-DTSE-Search-7454-60-PL-3 © DataStax, All Rights Reserved. Confidential.

Challenge 1: The Query-

• Use LatLonType

• Write the (Radius from point), geofilt

query-

• Write the bbox query-

000-DTSE-Search-7454-60-PL-4 © DataStax, All Rights Reserved. Confidential.

Go Farther:

(Optional)

A navigator and explorer of African ancestry, Pedro Alonso Nino traveled with Christopher Columbus’ first expedition to the New World in 1492. Pedro Nino was the pilot of Columbus’ ship the “Santa Maria.” http://legacysunfoldingjourney.blogspot.com/2013/07/african- explorers-and-settlers-of-new.html

000-DTSE-Search-7454-60-PL-5 © DataStax, All Rights Reserved. Confidential.

Challenge 2 (Optional): Extend (Copy) Challenge 1-

Add polygon support- • Download JTS from,

http://central.maven.org/maven2/com/vivid

solutions/jts/1.13/DSE

• Copy Jar into, ./resources/solr/lib (from

parent directory of DSE).

• Restart DSE

• Add a polygon query;

Intersects/POLYGON

• Use, SpatialRecursivePrefixTreeFieldType

• To save time, you can do all of this work

on new tables, etcetera.

000-DTSE-Search-7454-60-PL-6 © DataStax, All Rights Reserved. Confidential.

Lessons learned

000-DTSE-Search-7454-60-DM-7 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7454-60-DM-8
