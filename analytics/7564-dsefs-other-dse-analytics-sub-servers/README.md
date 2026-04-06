# DSE Analytics: DSEFS Other DSE Analytics sub-servers

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dsefs other dse analytics sub-servers. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dsefs other dse analytics sub-servers.

## Downloads

- [PDF slides](./7564-dsefs-other-dse-analytics-sub-servers.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7564-DU-60%2C%20DSEFS%20Other%20DSE%20Analytics%20sub-servers.pptx)

## Converted Slides

## Discussion Unit:

• DSE Analytics History Server

DSE Analytics • DSE Analytics Spark Job Server

Other (sub-servers)

Not: DSE Always-on SQL (another unit)

000-DTSE-Analytics-7564-60-DU-1 © DataStax, All Rights Reserved, Confidential

DSE Analytics; Process Architecture,

and reporting on same

Discussion Lab:

Matching pairs – Match the

attributes on the right with the

areas on the left

000-DTSE-Analytics-7564-60-DU-2 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Process Architecture

Has most info about your app Master

Persistent Logger

Goes away Executor

Some-Host:7080 Driver

Some-Host:4040 Worker

000-DTSE-Analytics-7564-60-DU-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7564-60-DU-4 © DataStax, All Rights Reserved, Confidential

While a DSE Analytics App is Running:

000-DTSE-Analytics-7564-60-DU-5 © DataStax, All Rights Reserved, Confidential

After a DSE Analytics

App is Complete:

000-DTSE-Analytics-7564-60-DU-6 © DataStax, All Rights Reserved, Confidential

After a DSE

Analytics App is

Complete:

000-DTSE-Analytics-7564-60-DU-7 © DataStax, All Rights Reserved, Confidential

After a

DSE

Analytics

App is

Complete:

000-DTSE-Analytics-7564-60-DU-8 © DataStax, All Rights Reserved, Confidential

DSE Analytics History Server:

000-DTSE-Analytics-7564-60-DU-9 © DataStax, All Rights Reserved, Confidential

DSE

Analytics

History

Server:

000-DTSE-Analytics-7564-60-DU-10 © DataStax, All Rights Reserved, Confidential

DSE Analytics

History Server:

000-DTSE-Analytics-7564-60-DU-11 © DataStax, All Rights Reserved, Confidential

DSE

Analytics

History

Server:

000-DTSE-Analytics-7564-60-DU-12 © DataStax, All Rights Reserved, Confidential

DSE Analytics History Server: How to

DSEFS

• mkdir –p spark/history_server

spark-defaults.conf (40 lines, below are adds)

• spark.eventLog.dir dsefs:///spark/history_server

• spark.eventLog.enabled true

• spark.history.fs.logDirectory dsefs:///spark/history_server

dse spark-history-server start|stop

localhost:18080

000-DTSE-Analytics-7564-60-DU-13 © DataStax, All Rights Reserved, Confidential

DSE Analytics History Server: Maintenance

spark-defaults.conf (more adds)

• spark.history.fs.cleaner.enabled true

• spark.history.fs.cleaner.interval 1d

• spark.history.fs.cleaner.maxAge 7d

000-DTSE-Analytics-7564-60-DU-14 © DataStax, All Rights Reserved, Confidential

On DSEFS: (JSON formatted), avail from Web UI

dsefs dsefs://127.0.0.1:5598/spark/history_server/ > ls -l Type Permission Owner Group Length Modified Name file rwxrwx--- none none 98468 2018-07-19 22:04:14-0600 app-20180719220355-0000

000-DTSE-Analytics-7564-60-DU-15 © DataStax, All Rights Reserved, Confidential

DSE Analytics

Spark Job

Server

000-DTSE-Analytics-7564-60-DU-16 © DataStax, All Rights Reserved, Confidential

DSE Analytics Spark Job Server:

How you run (applications) now:

• One of the REPLs

• "dse spark-submit ... "

How OSS Spark also runs applications:

• Spark REST Server

• Deprecated in DSE 5.1

DSE Analytics Spark Job Server-

• REST, Curl (no Bash required)

• Faster/easier than spark-submit .. (Re-uses SparkContext)

• Developers only, no HA

000-DTSE-Analytics-7564-60-DU-17 © DataStax, All Rights Reserved, Confidential

DSE Analytics Spark Job Server:

• Simple Web UI, port 8090

• Submit jobs via Curl

• Query status, results via Curl

• Query job history via Curl

• Can cache/share RDDs across jobs

000-DTSE-Analytics-7564-60-DU-18 © DataStax, All Rights Reserved, Confidential

DSE Analytics Spark Job Server: Configuring

• ./resources/spark/spark-jobserver/

./dse.conf

./settings.sh

• dse spark-jobserver start|stop

• Tutorial on GitHub, Url on Notes page

000-DTSE-Analytics-7564-60-DU-19 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7564-60-DU-20 © DataStax, All Rights Reserved, Confidential
