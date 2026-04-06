# DSE Analytics: DSE Analytics, Persistence

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, persistence. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, persistence.

## Downloads

- [PDF slides](./7574-dse-analytics-persistence.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7574-DU-60%2C%20DSE%20Analytics%2C%20Persistence.pptx)

## Converted Slides

## Discussion Unit:

role of persistence • Understand the

DSE Analytics, when using DSE Analytics

Persistence

000-DTSE-Analytics-7574-60-DU-1 © DataStax, All Rights Reserved, Confidential

DSE Analytics; Optimization (thus far)

Discussion Lab:

Discuss-

000-DTSE-Analytics-7574-60-DU-2 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Optimization (thus far) ..

Based on what you know

right now; How can you

make your Spark Job

faster, more efficient ?

Source: https://www.amazon.com/gp/product/0060929510

000-DTSE-Analytics-7574-60-DU-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7574-60-DU-4 © DataStax, All Rights Reserved, Confidential

Why we persist- (And recovery from failure)

Image From: DSA-320

000-DTSE-Analytics-7574-60-DU-5 © DataStax, All Rights Reserved, Confidential

Why we persist- (And recovery from failure)

Image From: DSA-320

000-DTSE-Analytics-7574-60-DU-6 © DataStax, All Rights Reserved, Confidential

RDD/DataFrame/DataSet: Persistence API-

Transform Description

Persists source RDD According to storage level (sl) persist(sl) specified. Default is MEMORY_ONLY, which persists RDD

element as deserialized Java objects in the JVM.

cache() Same as persist(StorgageLevel.MEMORY_ONLY)

unpersist() Optional; Spark automatically manages this.

000-DTSE-Analytics-7574-60-DU-7 © DataStax, All Rights Reserved, Confidential

Storage Levels

Storage Level Description

MEMORY_ONLY Deserialized, or Serialized, Java objects in the JVM. MEMORY_ONLY_SER Partitions that do not fit are not stored, and are recalculated

MEMORY_AND_DISK Same as above; partitions not fitting in memory are stored to MEMORY_AND_DISK_SER disk

DISK_ONLY Persisting to disk only.

MEMORY_ONLY_2 Same as above; replication to two nodes MEMORY_AND_DISK_2

Serialized in-memory using Tachyon; a memory-centric OFF_HEAP distributed storage system

** Serialized: more space efficient, more CPU intensive

000-DTSE-Analytics-7574-60-DU-8 © DataStax, All Rights Reserved, Confidential

val c_rows = sc.cassandraTable("ks_7571", "customer"). Example: When select("customer_num", "state"). A as((customer_num:Int, state:String) => to apply (customer_num, (state)))

val o_rows = sc.cassandraTable("ks_7571", "orders"). select("customer_num", "order_num", "paid_date"). • Persist ? What level ? B as((customer_num:Int, order_num:Int, paid_date:String) => (customer_num, (order_num, paid_date)))

C val j_rows1 = o_rows.join(c_rows)

val j_rows2 = o_rows.leftOuterJoin(c_rows). D filter{case (pk, (row_o, row_c)) => row_c.isDefined} Outer, and isDefined ?

val j_rows3 = o_rows.leftOuterJoin(c_rows). filter{case (pk, (row_o, row_c)) => row_c.isDefined}. E map{r => ( r._1, Option(r._2._1._2), r._2._1._1, r._2._2 )}. map{r => ( r._1, r._2.getOrElse("N/A"), r._3, r._4.get )}

j_rows4.saveToCassandra("ks_7571", "customer_orders", F SomeColumns("customer_num", "paid_date", "order_num", "state"))

000-DTSE-Analytics-7574-60-DU-9 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7574-60-DU-10 © DataStax, All Rights Reserved, Confidential
