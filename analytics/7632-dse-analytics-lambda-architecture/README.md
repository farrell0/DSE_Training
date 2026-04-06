# DSE Analytics: DSE Analytics, Lambda architecture

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, lambda architecture. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, lambda architecture.

## Downloads

- [PDF slides](./7632-dse-analytics-lambda-architecture.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7632-DU-60%2C%20DSE%20Analytics%2C%20Lambda%20architecture.pptx)

## Converted Slides

## Discussion Unit:

• Discuss Lamdba architecture as it DSE Analytics, relates to DSE, DSE Analytics

Lambda

Architecture

000-DTSE-Analytics-7632-60-DU-1 © DataStax, All Rights Reserved, Confidential

Architectures of years past and

present-

Discussion Lab:

Matching pairs – Match the

attributes on the right with the

areas on the left

000-DTSE-Analytics-7632-60-DU-2 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Architectures of years past

Data Mart

Data Warehouse

Enterprise Data

Warehouse/Layer

Data Lake

Excel Spreadsheet

000-DTSE-Analytics-7632-60-DU-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7632-60-DU-4 © DataStax, All Rights Reserved, Confidential

Wikipedia: Lambda Architecture

Lambda architecture is a data-processing architecture designed to handle massive quantities of data by taking advantage of both batch and stream-processing methods . This approach to architecture attempts to balance latency, throughput, and fault-tolerance by using batch processing to provide comprehensive and accurate views of batch data, while simultaneously using real-time stream processing to provide views of online data . The two view outputs may be joined before presentation. The rise of lambda architecture is correlated with the growth of big data, real-time analytics, and the drive to mitigate the latencies of map-reduce.

Lambda architecture depends on a data model with an append-only, immutable data source that serves as a system of record. Source: https://en.wikipedia.org/wiki/Lambda_architecture

It is intended for ingesting and processing times tamped events that are appended to existing events rather than overwriting them. State is determined from the natural time-based ordering of the data.

000-DTSE-Analytics-7632-60-DU-5 © DataStax, All Rights Reserved, Confidential

Review: The 4 Primary Functional Areas to DSE

• All 4 primary functional areas

provide query processing The Why

• DSE Analytics Query -- Parallel Query Processing processing Horizontal scaling

Index and High Speed

query -- Batch, Streaming,

processing Iterative, Interactive

000-DTSE-Analytics-7632-60-DU-6 © DataStax, All Rights Reserved, Confidential

Review: DSE Analytics, 5 Major Functional Areas

Image Source: DataBricks.com

000-DTSE-Analytics-7632-60-DU-7 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Lambda Architecture

DSE Analytics is part of a Lambda Architecture

• The idea and original term Lambda Architecture was first introduced in

Book https://www.manning.com/books/big-data , by Nathan Marz (2012)

• Lambda has become an overloaded phrase; buzzword and marking material

without necessarily tying back to the original intent

• True Lambda architectural design in your enterprise applications is considered

a key part of an enterprise ready system, making the idea of saying your design

is part of Lambda appealing

• Lambda architecture is a data-processing architecture designed to handle

massive quantities of data by taking advantage of both batch- and stream-

processing methods

000-DTSE-Analytics-7632-60-DU-8 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Lambda Architecture

The lambda architecture is

an attempt to solve the

problem of computing

arbitrary functions on

arbitrary data in real time

000-DTSE-Analytics-7632-60-DU-9 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Lambda Architecture

The promise of Lambda:

• Analysis happens on streaming ingest allowing for

time sensitive value to be captured

• Batch layer re-calculates fast analytics and corrects

accuracy

• Serving layer accesses both layers and treats

batch layer as authoritative for conflicts

Three layers:

• Streaming/Speed

• Batch

• Serving

000-DTSE-Analytics-7632-60-DU-10 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Lambda Architecture

Ingest flow - double writes into queue and DSE

Ingest Flow Write

Elastic Application Tier

Event Sourcing

Publish

Queue / Message Bus

000-DTSE-Analytics-7632-60-DU-11 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Lambda Architecture

Batch Layer - DSE batch aggregations

Ingest Flow Write

Elastic application Tier

Batch Layer

000-DTSE-Analytics-7632-60-DU-12 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Lambda Architecture

Server Layer - Batch wins for accuracy

Serving Layer

Elastic application Tier

Read Read

Ingest Flow Write

Elastic application Tier

Event Sourcing Speed Layer + Batch Layer

Publish Streaming Ingest

Queue / Message Bus

000-DTSE-Analytics-7632-60-DU-13 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Lambda Architecture

Decompose the problem into three layers:

• Batch layer

-- Stores immutable Master Data Set

-- Computes Arbitrary Views - functions on data

• Serving layer

-- Random Access to Batch Views

-- Updated by batch layer

• Streaming/speed layer

-- Compensates for high latency of update to serving layer

-- Fast incremental Algorithms

• Batch layer eventually overrides speed layer

-- Batch layer looks at all data

-- Streaming/speed layer for incremental updates

000-DTSE-Analytics-7632-60-DU-14 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Lambda Architecture, How DSE fits

HDFS Hive and SparkSQL BI Tools Spark or MapR me R ark educe Flu in Spark Sp eam g Str Data Science Events Kafk Analytic Workflows a CQL Writes Results Direct Read from in Real CQL Rollup Tables Realtim Sensors Dashboar Spark e Time Stream ds CQL Rea in g Transaction Runs ds Replicati in An s alytic on s DC Search Analytic Replication Applicatio s Solr Reads (CQL & ns HTTP) Spark Rollups and Data Science

000-DTSE-Analytics-7632-60-DU-15 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7632-60-DU-16 © DataStax, All Rights Reserved, Confidential
