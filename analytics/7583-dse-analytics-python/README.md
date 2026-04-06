# DSE Analytics: DSE Analytics, Python

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, python. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, python.

## Downloads

- [PDF slides](./7583-dse-analytics-python.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7583-PL-60%2C%20DSE%20Analytics%2C%20Python.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Unit 7578, where most of

the objects we create in this lab

were introduced.

• In this Practice Lab, we use the DSE Analytics, Python

Python Shell to run some of the

earlier DSE Analytics statements we

detailed

• Run a Python client program against

DSE Analytics

000-DTSE-Analytics-7583-PL-60-1 © DataStax, All Rights Reserved, Confidential

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

000-DTSE-Analytics-7583-PL-60-2 © DataStax, All Rights Reserved, Confidential

Challenge 1: Spark Python REPL

From the command line:

• (Exist all other REPL shells)

• dse pyspark Python is whitespace

sensitive. Do not

indent. row = spark.sql("select * from ks_7579.customer")

row.show()

exit()

• Run more from prior Spark/SQL Practice Labs.

000-DTSE-Analytics-7583-PL-60-3 © DataStax, All Rights Reserved, Confidential

Challenge 2 (Optional): Python Client

• pip install dse-client # optional, see notes

pip install dse-driver

python –m pip install

• Edit an ASCII text file containing code; (See notes

page for sample program)

• This file needs to be readable from an absolute

pathname with no spaces. E.g., /opt/file_name.py

• To run, dse spark-submit /opt/file_name.py

• Edit the file above, add more from prior Spark/SQL

Practice Labs.

000-DTSE-Analytics-7583-PL-60-4 © DataStax, All Rights Reserved, Confidential

Lessons Learned

000-DTSE-Analytics-7583-PL-60-5 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7583-PL-60-6 © DataStax, All Rights Reserved, Confidential
