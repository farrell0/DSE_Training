# DSE Analytics: DSE Analytics, GraphX, GraphFrames

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Discussion Module

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, graphx, graphframes. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This discussion module in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, graphx, graphframes.

## Downloads

- [PDF slides](./7628-dse-analytics-graph-x-graph-frames.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7628-DM-60%2C%20DSE%20Analytics%2C%20GraphX%2C%20GraphFrames.pptx)

## Converted Slides

## Discussion

Discussion/Information Only-

Module: • Covered in detail when we cover DSE

Graph DSE Analytics, GraphX,

GraphFrames

000-DTSE-Analytics-7628-60-DM-1 © DataStax, All Rights Reserved. Confidential.

DSE Analytics: GraphX, GraphFrames

Allows Spark to natively manage graphs

• In general we don’t address the GraphX APIs, but instead integrate with

GraphFrames; GraphFrames is not GraphX

• GraphX is to RDDs as GraphFrames are to DataFrames

• GraphX extends the Spark RDD, GraphFrames extends Sparks DataFrames

• Developed by DataBricks in conjunction with UC Berkeley and MIT

• GraphFrames fully integrate with GraphX via conversions between the two

representations, without any data loss

• If a GraphX API is more useful, you are free to convert back and forth

• With DSE Graph integration with GraphFrames, seamless integration of DSE Graph

with Spark

• Allows for certain type of graph jobs to run more efficiently in Spark

• Spark GraphFrames API uses familiar terms to the Tinkerpop API making transition

easier

000-DTSE-Analytics-7628-60-DM-2

DSE Analytics: GraphX, GraphFrames

DseGraphFrames:

• DSE Graph data using native Spark mechanisms

• Execute bulk type processing on DSE Graph data

• Combine DSE Graph and non Graph data

• Access DSE Graph through SQL like APIs

• Analytic jobs on graphs

Mimics TinkerPop3 traversal language

• API’s in; Scala, Java, (some Python)

• Implicit conversions from GraphFrame to DseGraphFrame and back

• GraphFrame filtering and TinkerPop methods could be mixed

000-DTSE-Analytics-7628-60-DM-3

DSE Analytics: GraphX, GraphFrames, Exercise

• In Studio load the graph studio worksheet from,

https://github.com/riptano/enablement/tree/master/boot-camp-dse/studio

• Graph name can be whatever

• Create the schema

• Following the next line of instructions from the worksheet using the spark

shell

• Download data

• Import data through spark using GraphFrames

• Simple queries

• Once in studio

• Try to replicate the query using GraphFrames

• Try to get a sense on how they are different

• Export the graph in DSEFS using parquet

000-DTSE-Analytics-7628-60-DM-4

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Analytics-7628-60-DM-5
