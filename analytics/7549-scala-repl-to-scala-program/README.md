# DSE Analytics: Scala REPL to Scala program

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Analytics curriculum and need help with scala repl to scala program. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around scala repl to scala program.

## Downloads

- [PDF slides](./7549-scala-repl-to-scala-program.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7549-PL-60%2C%20Scala%20REPL%20to%20Scala%20program.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Unit 7548, where most of

the objects we create in this lab

were introduced.

• In this Practice Lab, we migrate a DSE Scala REPL to Scala

Program number of [ your ] DSE Spark Scala

statements (runnable in the Scala

REPL, created in Practice Lab

7545), to a true Scala/Spark

program.

000-DTSE-Analytics-7549-PL-60-1 © DataStax, All Rights Reserved, Confidential

Challenge 1: Prerequisites

Prerequisites:

• Instructions are provided for Linux

• We will operate below recommended

settings; 1 OS node only, minimum 8

GB RAM, 12 GB RAM preferred

• That you have an operating single

node DSE Core cluster with DSE

Analytics enabled.

• All work done as ‘root’

000-DTSE-Analytics-7549-PL-60-2 © DataStax, All Rights Reserved, Confidential

Challenge 1: Prerequisites

• Confirm or install the Scala compiler,

as outlined in Discussion Unit 7548.

• Confirm or install the Maven utility, as

outlined in Discussion Unit 7548.

000-DTSE-Analytics-7549-PL-60-3 © DataStax, All Rights Reserved, Confidential

Challenge 1: Scala REPL to Scala Program

• cd /opt (cd anywhere)

• mvn archetype:generate \

-DgroupId=com.datastax.enablement.bootcamp \

-DartifactId=my-app \

-Dversion=1.0 \

-DinteractiveMode=false \

-DarchetypeArtifactId= scala-archetype-simple \

-DarchetypeGroupId=org.scala-tools.archetypes \

-DremoteRepositories=http://scala-tools.org/repo-releases

• cd my-app

rm -r ./src/test/scala/samples/*

Generated tests: Will error on compile unless corrected

000-DTSE-Analytics-7549-PL-60-4 © DataStax, All Rights Reserved, Confidential

Challenge 1: Scala REPL to Scala Program

• Copy in (replace) with a correct

pom.xml

• Copy in a final, or stub App.scala

• Both above supplied by the instructor

000-DTSE-Analytics-7549-PL-60-5 © DataStax, All Rights Reserved, Confidential

Challenge 1: You are done when-

• Your Scala program compiles and runs, loads data from CSV into

DSE

• mvn package

• dse spark-submit --class \

com.datastax.enablement.bootcamp.App \

target/my-app-1.0.jar

000-DTSE-Analytics-7549-PL-60-6 © DataStax, All Rights Reserved, Confidential

Lessons Learned

000-DTSE-Analytics-7549-PL-60-7 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7549-PL-60-8 © DataStax, All Rights Reserved, Confidential
