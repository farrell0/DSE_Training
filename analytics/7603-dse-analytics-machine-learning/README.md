# DSE Analytics: DSE Analytics, Machine Learning

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, machine learning. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Analytics track introduces the runtime model and practical usage patterns. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, machine learning.

## Downloads

- [PDF slides](./7603-dse-analytics-machine-learning.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7603-PL-60%2C%20DSE%20Analytics%2C%20Machine%20Learning.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on Discussion

Unit 7602, where most of the objects we create Practice Lab: in this lab were introduced.

• This Practice Lab is also dependent on DSE Analytics, Machine Discussion Unit 7548/7549, where we learn Learning, Apriori Algorithm how to compile, set up a Spark/Scala project

structure, other.

• This Practice Lab requires a working DSE

system, with DSE Analytics enabled.

• Because of the dependency on the "dse spark-

submit" utility, this Practice Lab requires a

ssh(C) prompt on at least one node operating

DSE Analytics.

000-DTSE-Analytics-7603-PL-60-1 © DataStax, All Rights Reserved, Confidential

Challenge 1:

Prerequisites: Prerequisites • Instructions are provided for Linux

• We will operate below recommended

settings; 1 OS node only, minimum 8

GB RAM, 12 GB RAM preferred

• That you have an operating single

node DSE Analytics cluster.

• All work done as ‘root’

• You need to complete Practice Lab

7549 first, because we are going to

re-use its project filesystem structure,

other.

000-DTSE-Analytics-7603-PL-60-2 © DataStax, All Rights Reserved, Confidential

Working Goal:

From: Maury_Atwater To: DSE_HOTSHOT

Subject: Need this now !!!

We need to start upselling ! CSV file; 10k orders, 43k items sold, 170 unique items,

4.4 items per transaction.

We need a set of association rules to apply on the Web site ! Maury Atwater, President of Atwater's -MA

000-DTSE-Analytics-7603-60-DU-3 © DataStax, All Rights Reserved, Confidential

• You are given the CSV source data file. Place Challenge 1:

this file in an easily spelled absolute Deliver Apriori pathname.

• You are given the single Scala application

source file, which is the Apriori application.

• Let's save steps and time, and re-use the

infrastructure from the 7548/7549 Practice

Lab.

• Save that original App.scala file to another

location.

• Overwrite the contents of App.scala with the

Apriori source code.

000-DTSE-Analytics-7603-PL-60-4 © DataStax, All Rights Reserved, Confidential

Challenge 1: Compile and Run

From the my-app folder:

• Compile via, mvn package

• Run via,

dse spark-submit --class com.datastax.enablement.bootcamp.App target/my-app-1.0.jar

000-DTSE-Analytics-7603-PL-60-5 © DataStax, All Rights Reserved, Confidential

Challenge 2 (Optional): Same for Customer Churn

• Save App.scala

• Replace contents of App.scala

with the single Customer Churn

application code

000-DTSE-Analytics-7603-PL-60-6 © DataStax, All Rights Reserved, Confidential

Challenge 3 (Optional): Clean Up

• Using the instructions from

Practice Lab 7549, actually

instantiate two new project parent

directories, so that we are not

(cheating, and overwriting the

contents of App.scala)

• Compile and run all 3 programs;

the original and the two new

000-DTSE-Analytics-7603-PL-60-7 © DataStax, All Rights Reserved, Confidential

Lessons Learned

000-DTSE-Analytics-7603-PL-60-8 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7603-PL-60-9 © DataStax, All Rights Reserved, Confidential
