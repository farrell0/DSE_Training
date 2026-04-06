# DSE Core: DSE Core, Troubleshooting Lab

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Core curriculum and need help with dse core, troubleshooting lab. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Core track walks through a hands-on lab. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse core, troubleshooting lab.

## Downloads

- [PDF slides](./6293-dse-core-troubleshooting-lab.pdf)
- [Original PowerPoint](../000-DTSE-Core-6293-PL-60%2C%20DSE%20Core%2C%20Troubleshooting%20Lab.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on Discussion

Unit 6292, but also on most other Discussion

Units we have presented. Practice Lab:

• In this Practice Lab, you are given an (n) node

DSE Troubleshooting, DSE cluster in need of attention.

• You are done when: Tuning

-- All servers are running

-- Metrics are being collected

-- Loads are balanced between nodes

-- You can answer the questions that follow

-- List all issues you found, and what/how

you had to do to fix

0000-DTSE-Core-6293-PL-60-1 © DataStax, All Rights Reserved, Confidential

The Challenge: Data (or similar) you will receive-

-----BEGIN RSA PRIVATE KEY----- Part 1 MIIEpAIBAAKC ... deqw8hD8BB1HJV++HDG3DwL1SyR ... 9Iduj4WNK4yZ ... WvlIE4yLa/OZZuG2WYRucUhQQ== -----END RSA PRIVATE KEY----- • You will be given an (n)

node cluster df, 9 instances • Ops Center will be tw, 9 instances cluster name: xyz running on one node instance type: n1-standard-2 with a public IP Node 0: • You don't have to "fix" public hostname: 35.193.183.32 public ip: 35.193.183.32 Ops Ctr private hostname: tony ... les.internal private ip: 10.240.0.24 • Any problems are with the region: Google non Ops Ctr nodes Node 1: public hostname: 35.193.152.40 public ip: 35.193.152.40 ...

0000-DTSE-Core-6293-PL-60-2 © DataStax, All Rights Reserved, Confidential

The Challenge: Part 1, Repair the cluster

• Don't just blow the cluster away.

• Look first. Many persons create more

problems initially through incorrect

assumptions. Know what and why you

are changing something.

• Use nodetool heavily; also CQLSH

• If you know exactly what to do, 20

minutes tops.

• Most persons take 2-4 hours for part 1.

0000-DTSE-Core-6293-PL-60-3 © DataStax, All Rights Reserved, Confidential

The Challenge: Part 1, Share, but be wary ..

• Share with other attendees,

certainly

• The clusters were all identical.

Then your neighbor did something

wrong, and will share details with

everyone of incorrect

assumptions/steps. Dave !

0000-DTSE-Core-6293-PL-60-4 © DataStax, All Rights Reserved, Confidential

The Challenge: Part 2, Tuning/cassandra-stress

• Monitor with Ops Center (should be running on node0 on the public ip):

-- Reads, Average reads, read timeouts

-- Writes, Average writes, write timeout

-- Disk utilization, Disk IO

-- CPU Utilization

-- Java Memory, Java Garbage collection

-- Other Metrics that you like

• Run cassandra-stress with a replication factor of 2 to each data center

-- Load at least an average of 1 GB of data per node (Approximately

10,000,000 records with default stress table)

-- Use skills gained from cassandra-stress exercise

0000-DTSE-Core-6293-PL-60-5 © DataStax, All Rights Reserved, Confidential

The Challenge: Part 2, Be Prepared to Report

• What is the fastest read speed you can get

out of the system at 90%, 95%, max ?

• What is the fastest write speed you can get

out of the system at 90%, 95%, max ?

• What is the average data size difference

between nodes, smallest dataset, largest,

the difference between the two ?

• Can you make that difference closer or even

exact ? If so how ?

• Is it worth the effort to do so ?

Hermes Greek God of Commerce, Communications and Wealth Source: https://www.majesticdragonfly.com/hermes-greek-god-statue-8220

0000-DTSE-Core-6293-PL-60-6 © DataStax, All Rights Reserved, Confidential

The Challenge: Part 2, Be Prepared to Report

• What problems did you find?

• What was the hardest part to fix?

Source: https://www.popculturecrossing.com/classics/thepaperchase1973review

0000-DTSE-Core-6293-PL-60-7 © DataStax, All Rights Reserved, Confidential

Lessons Learned

0000-DTSE-Core-6293-PL-60-8 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Core-6293-PL-60-9 © DataStax, All Rights Reserved, Confidential
