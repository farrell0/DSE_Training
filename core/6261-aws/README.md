# DSE Core: AWS

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Core curriculum and need help with aws. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Core track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around aws.

## Downloads

- [PDF slides](./6261-aws.pdf)
- [Original PowerPoint](../000-DTSE-Cloud-6261-PL-60%2C%20AWS.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on Practice Lab: Discussion Unit 6260, where most of the

objects we create in this lab were Create a cluster using introduced. AWS

• The goal of this practice lab is to make a

cluster.

0000-DTSE-Cloud-6261-DU-60-1 © DataStax, All Rights Reserved, Confidential

Challenge 1: Create a Cluster

• Log into the the AWS web console

• Provision 3 machines

-- Type of machine is your choice though the

OS has to support DSE

-- Limit your disk space to only 100GB as we

are not going to do a lot with these

instances

0000-DTSE-Cloud-6261-DU-60-2 © DataStax, All Rights Reserved, Confidential

• Don’t forget to Challenge 1: -- Use the right security group for DSE ports

Create a Cluster o The quick is to open up ports according

to firewall guide to 0.0.0.0

o This is not optimal as not near secure

enough but works for a quick demo

o Remind clients they should do much

more in the security arena for prod

-- Download your certificate

● After the instances are up use your cert to

log into each instance to verify it is up and

you have access

After you are done leave the instances up as

we will use them for a future exercise

0000-DTSE-Cloud-6261-DU-60-3 © DataStax, All Rights Reserved, Confidential

Challenge 1: Create a Cluster

• After the instances are up use your cert to log

into each instance to verify it is up and you

have access

• After you are done leave the instances up as

we will use them for a future exercise

0000-DTSE-Cloud-6261-DU-60-4 © DataStax, All Rights Reserved, Confidential

Lessons Learned

0000-DTSE-Cloud-6261-DU-60-5 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Cloud-6261-DU-60-6 © DataStax, All Rights Reserved, Confidential
