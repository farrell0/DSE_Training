# DSE Search: DSE Search, Capacity Planning and Tuning

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Discussion Module

**Customer:** I am working through the DSE Search curriculum and need help with dse search, capacity planning and tuning. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This discussion module in the DSE Search track reviews performance, sizing, and tuning considerations. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, capacity planning and tuning.

## Downloads

- [PDF slides](./7459-dse-search-capacity-planning-and-tuning.pdf)
- [Original PowerPoint](../000-DTSE-Search-7459-DM-60%2C%20DSE%20Search%2C%20Capacity%20Planning%20and%20Tuning.pptx)

## Converted Slides

## Discussion

Discussion/Information Only-

Anything less than (n) nodes and (mGB) data can Module: produce spurious results. A capacity planning and

tuning lab exists in the advanced class; 14 + Capacity Planning and nodes, plus driver nodes, production sized data,

other. Tuning

• Topics related to capacity planning

• Topics related to tuning

• DSE Search specific only

000-DTSE-Search-7459-60-DM-1 © DataStax, All Rights Reserved. Confidential.

Discussion Lab:

Discuss

000-DTSE-Search-7459-60-DM-2 © DataStax, All Rights Reserved. Confidential.

• Background: Fictitious company operates out of Miami,

with stand alone production servers/data

centers in all/most countries in S.America

and LATAM.

• Shared development/test server; 24 cores,

84 TB disk

• Explosive growth over 7-10 years-

– Production servers in Brazil, Mexico become 12x to 48x larger than development/test

– No real HA disaster planning/test. Best estimate is to serve a (failed) country out of an adjacent country/server

– Highly spikey system load; imagine pay per view on World Cup Soccer style events

• Too much unplanned downtime

000-DTSE-Search-7459-60-DM-3 © DataStax, All Rights Reserved. Confidential.

Vendor <- -> Customer

When I give you this patch, what is your level of comfort that this will solve the production problem ?

Zero, In fact, you’ve given us patches before that have brought production down, and that can’t happen again.

The last time you did (recovery procedure x); How long did that take ?

We haven’t done that in 6-8 years. Since that time production volumes have gone up 48x. This can’t take more than (n) www.snoopy.com time, and it can’t affect production.

000-DTSE-Search-7459-60-DM-4 © DataStax, All Rights Reserved. Confidential.

Best / Not-Best Practice ?

Testing on

representative hardware

Testing/developing on

production sized data

Having a

ready/representative

test (query) harness

Having a Rabbit’s Foot

http://knowyourmeme.com/photos/1080551

000-DTSE-Search-7459-60-DM-5 © DataStax, All Rights Reserved. Confidential.

End of

Discussion Lab:

000-DTSE-Search-7459-60-DM-6 © DataStax, All Rights Reserved. Confidential.

DSE Search: Cap Planning,

Tuning-

System tuning

Statement tuning (queries)

• Prod sized data, repeatable

test harness, isolation

• Frequency, concurrency,

spread

• One variable; rinse, repeat

http://www.classicgaming.cc/classics/frogger/about

000-DTSE-Search-7459-60-DM-7 © DataStax, All Rights Reserved. Confidential.

Common

SDLC, and

Issues

000-DTSE-Search-7459-60-DM-8 © DataStax, All Rights Reserved. Confidential.

DSE Search: DCs, Read/Write, Load isolation

Data Center 1 Data Center 2 DB Network DB DB Interruption

DB

DB DB DB DB

App App

Clients

Clients

000-DTSE-Search-7459-60-DM-9 © DataStax, All Rights Reserved. Confidential.

If you don’t have the Query Harness-

1 • CQL Slow Log (dse.yaml. perm)

– enabled • Developers

– threshhold_ms – This is something someone 2 should have – ttl_seconds created/maintained – async_writers – Reverse engineering is not • dsetool perf cqlslowlog enable (temp) forecasting, signing your

• dsetool perf cqlslowlog 1000 name to something

• SELECT * FROM

dse_perf,node_slow_log;

000-DTSE-Search-7459-60-DM-10 © DataStax, All Rights Reserved. Confidential.

• Solr Slow Sub-query Log If you don’t have the

– dsetool perf solrslowlog enable Query Harness- 4 – dsetool perf solrindexstats enable

– dsetool perf solrcachestats enable

– dsetool perf solrlatencysnapshots enable • _

– SELECT * FROM

dse_perf.solr_slow_sub_query_log;

– SELECT (8-10 others)

• DSE Ops Center • DSE Audit Secure subsystem

– Search requests, latencies, – https://docs.datastax.com/en/dse/6.0/dse-admin/ timeouts, errors datastax_enterprise/security/secAuditEnable.html

– Index size 3

000-DTSE-Search-7459-60-DM-11 © DataStax, All Rights Reserved. Confidential.

Start working the (graph) • Not cost effective to fix every query;

Pick the top n% that you have time

for

• Index only necessary columns

Duration – CREATE SEARCH INDEX ON t1;

– First graph vertex predicate

– Is it a better DSE Core index or DSE

Search index application-

Frequency of Query

000-DTSE-Search-7459-60-DM-12 © DataStax, All Rights Reserved. Confidential.

Start working the (graph)

• CQLSH (driver); tracing on • Query Metrics Mbean

• Solr Admin UI screen – jmxterm, other

– com.datastax.bdp -> search -> (core name) ->

• QueryMetrics • CQL statement tuning • IndexPool – (Everything/most you know from SQL) • CommitMetrics – Leading wildcards, complex expressions • UpdateMetrics – Index negation statements; OR topped – Latency counts, latency percentile, average latency – Unnecessary sorts

– Read path phases; coordinate, execute, retrieve – Casting

– If it doesn’t reduce network comm, move to the client tier

000-DTSE-Search-7459-60-DM-13 © DataStax, All Rights Reserved. Confidential.

“q” and “fq”

• filtercache

– Easiest/most-common means to OOM

– dse.yaml – ramBufferSizeMB, ram_buffer_heap_space_in_mb

– solrconfig.xml, highWaterMarkMB=“256”, lowWaterMarkMB=“128”

• dse.yaml (pre 6.0) –

max_solr_concurrency_per_core,

back_pressure_theshhold_per_core

000-DTSE-Search-7459-60-DM-14 © DataStax, All Rights Reserved. Confidential.

Call to Action-

• We’ve outlined the knobs-

• It’s about changing one variable at a

time; careful testing

• Invest in the query harness

– Remember the incremental issue versus overnight ? Two very different problems.

http://picsnook.com/sunset-desert-minimal-4k-hd-wallpaper/

000-DTSE-Search-7459-60-DM-15 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7459-60-DM-16
