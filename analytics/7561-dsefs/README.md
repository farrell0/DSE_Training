# DSE Analytics: DSEFS

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Analytics curriculum and need help with dsefs. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dsefs.

## Downloads

- [PDF slides](./7561-dsefs.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7561-PL-60%2C%20DSEFS.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on Discussion

Unit 7560, where most of the objects we create

in this lab were introduced.

DSEFS, Configure and • This Practice Lab requires a working DSE use system, with DSE Analytics enabled.

• Because of the dependency on the "dse fs"

utility, this Practice Lab requires a ssh(C)

prompt on at least one node operating DSE

Analytics.

000-DTSE-Analytics-7561-PL-60-1 © DataStax, All Rights Reserved, Confidential

Challenge 1: Prerequisites

Prerequisites:

• Instructions are provided for Linux

• We will operate below recommended

settings; 1 OS node only, minimum 8

GB RAM, 12 GB RAM preferred

• That you have an operating single

node DSE Analytics cluster.

• All work done as ‘root’

000-DTSE-Analytics-7561-PL-60-2 © DataStax, All Rights Reserved, Confidential

Challenge 1: Examine and/or fix dse.yaml

dsefs_options:

enabled:

keyspace_name: dsefs

work_dir: /var/lib/dsefs

public_port: 5598

private_port: 5599

data_directories:

- dir: /var/lib/dsefs/data

storage_weight: 1.0

min_free_space: 5368709120 # Change to 1024 for dev

000-DTSE-Analytics-7561-PL-60-3 © DataStax, All Rights Reserved, Confidential

Challenge 2: Scala, Scala REPL

Using the Scala REPL:

val rows = sc.textFile(

"file:///opt/stores_db/7545_HelloWorld.csv")

rows.collect().foreach(println)

rows.saveAsTextFile(

"dsefs:///tmp/7545_HelloWorld.csv")

000-DTSE-Analytics-7561-PL-60-4 © DataStax, All Rights Reserved, Confidential

Challenge 3: "dse fs"

• Confirm the presence of the

newly created file

• Cat same

• Run other POSIX/FS

commands

000-DTSE-Analytics-7561-PL-60-5 © DataStax, All Rights Reserved, Confidential

Lessons Learned

000-DTSE-Analytics-7561-PL-60-6 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7561-PL-60-7 © DataStax, All Rights Reserved, Confidential
