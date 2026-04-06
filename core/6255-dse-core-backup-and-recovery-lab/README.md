# DSE Core: DSE Core, Backup and Recovery Lab

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Core curriculum and need help with dse core, backup and recovery lab. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Core track walks through a hands-on lab. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse core, backup and recovery lab.

## Downloads

- [PDF slides](./6255-dse-core-backup-and-recovery-lab.pdf)
- [Original PowerPoint](../000-DTSE-Core-6255-PL-60%2C%20DSE%20Core%2C%20Backup%20and%20Recovery%20Lab.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Unit 6254, where most of Practice Lab: the objects we create in this lab

were introduced. DSE Core Backup and

Recovery • In this Practice Lab, we create a

table, add data, snapshot, delete the

table's contents, then restore.

0000-DTSE-Core-6255-DU-60-1 © DataStax, All Rights Reserved, Confidential

Challenge 1: Backup, then Restore

Prerequisites:

• Instructions are provided for a single

node DSE Core cluster.

• There are additional steps for a multi-

node cluster, that we overviewed in

the Discussion Unit.

• Instructions are provided for the

command prompt using CQLSH,

nodetool, other.

• All work done as ‘root’

0000-DTSE-Core-6255-DU-60-2 © DataStax, All Rights Reserved, Confidential

Challenge 1: Using instructions from Discussion Backup, then Unit 6254, complete the following:

Restore

• Make a keyspace and table, add

data

• Snapshot the above

• Truncate said table

• Check for data

• Copy the data files back to the

proper location

• nodetool refresh

• Check for data

• nodetool clearsnapshot --all

0000-DTSE-Core-6255-DU-60-3 © DataStax, All Rights Reserved, Confidential

Lessons Learned

0000-DTSE-Core-6255-DU-60-4 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Core-6255-DU-60-5 © DataStax, All Rights Reserved, Confidential
