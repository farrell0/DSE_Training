# DSE Core: Ops Center

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Core curriculum and need help with ops center. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Core track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around ops center.

## Downloads

- [PDF slides](./6250-ops-center.pdf)
- [Original PowerPoint](../000-DTSE-OpsCenter-6250-DU-60%2C%20Ops%20Center.pptx)

## Converted Slides

## Discussion Unit:

Introduce the DSE Operations Center Discussion Unit:

• Adding and expanding clusters

DSE Ops Center • Configuring nodes

• Viewing performance metrics

• Correcting issues

• Monitoring cluster health

• Configure security

• Backup and recovery

• Other

0000-DTSE-OpsCenter-6250-DU-60-1 © DataStax, All Rights Reserved, Confidential

DSE, DSE Ops Center

Communication

Protocols/Architecture

Discussion Lab:

Refrigerator Magnets - Match

the terms on the right with the

boxes on the left

0000-DTSE-OpsCenter-6250-DU-60-2 © DataStax, All Rights Reserved, Confidential

DSE, Ops Center: Communication Protocols/Arch

Ops Center agent Server • node JMX C: 0 • ODBC A:

• Http

• Stomp

• Sec-28, Sub-D B: B: DSE Cluster

A: • CQL/Native

node agent node 2 1 agent E:

C: Browser

D:

0000-DTSE-OpsCenter-6250-DU-60-3 0000-DTSE-OpsCenter-6250-DU-60-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

0000-DTSE-OpsCenter-6250-DU-60-4 © DataStax, All Rights Reserved, Confidential

Ops Center Communication Architecture

Ops Center agent Server CQL/Native node 0 Http

Stomp

DSE Cluster Stomp Http

node agent node 2 1 agent

CQL/Native Browser JMX

0000-DTSE-OpsCenter-6250-DU-60-5 0000-DTSE-OpsCenter-6250-DU-60-5 0000-DTSE-OpsCenter-6250-DU-60-5 © DataStax, All Rights Reserved, Confidential

Ops Center Install Methods

Ops Center installation methods include the

following:

• Tar ball install (Practice Lab 6251 to follow)

• Docker install

• Linux Yum/APT-GET

0000-DTSE-OpsCenter-6250-DU-60-6 © DataStax, All Rights Reserved, Confidential

Ops Center: Cluster Ops Ops Center capabilities relative to

clusters include:

• Add an existing cluster, or create a

new cluster

• Disconnecting an existing cluster

form Ops Center and Lifecycle

Manager

• Rebalancing a cluster

• Restarting a cluster

• Generating diagnostic data for a

cluster

• Other

0000-DTSE-OpsCenter-6250-DU-60-7 © DataStax, All Rights Reserved, Confidential

Ops Center: Keyspace Ops

Ops Center capabilities

relative to keyspaces

include:

• View/change keyspace

settings

• Delete keyspaces

• Other

0000-DTSE-OpsCenter-6250-DU-60-8 © DataStax, All Rights Reserved, Confidential

Ops Center: Table Ops

Ops Center

capabilities relative

to tables include:

• View table

metrics

• Delete a table

• Truncate a table

• Other

0000-DTSE-OpsCenter-6250-DU-60-9 © DataStax, All Rights Reserved, Confidential

Ops Center: Agent Ops

Ops Center capabilities

relative to agents

include:

• View agent status

• Install/upgrade agents

• Other

0000-DTSE-OpsCenter-6250-DU-60-10 © DataStax, All Rights Reserved, Confidential

Ops Center: Alerts/Events

Ops Center capabilities relative to

alerts/events include:

• Set logging level per; 0/Debug thru

Alert/5.

• Specify SNMP alert parameters

• Specify SMTP alert parameters

• Specify Http/POST alert parameters

• Other

0000-DTSE-OpsCenter-6250-DU-60-11 © DataStax, All Rights Reserved, Confidential

Ops Center capabilities relative to

Ops Center: performance metrics include:

Performance

• Cluster wide performance metrics (metrics Metrics aggregated atop nodes)

• Pending task metrics; compactions, other

• Table performance metrics

• Tiered storage performance metrics

• Message latency metrics

• Search performance metrics

• Graph metrics

• Nodesync metrics

• Thread pool metrics

• Dropped messages metrics

• OS performance metrics

• Alert metrics

0000-DTSE-OpsCenter-6250-DU-60-12 © DataStax, All Rights Reserved, Confidential

Ops Center: Management Services

0000-DTSE-OpsCenter-6250-DU-60-13 © DataStax, All Rights Reserved, Confidential

Ops Center: Best Practice Rules Reference

Easily 40+ Rules; Examples ..

• Checks that the default cassandra superuser and

password has been changed from the default.

• Checks that you are not using SimpleStrategy for

any keyspaces in a multi-datacenter

environment.

• Checks to make sure SimpleSnitch isn't used in

production.

• Checks for secondary indexes with too many Maury Atwater, President of Atwater's distinct values.

• Others

0000-DTSE-OpsCenter-6250-DU-60-14 © DataStax, All Rights Reserved, Confidential

Ops Center: Lifecycle Manager (LCM)

0000-DTSE-OpsCenter-6250-DU-60-15 © DataStax, All Rights Reserved, Confidential

Ops Center: Agent API

Edit the agent

address.yaml

swagger_eabled:

true

Restart agent

localhost:61621/ui

0000-DTSE-OpsCenter-6250-DU-60-16 © DataStax, All Rights Reserved, Confidential

0000-DTSE-OpsCenter-6250-DU-60-17 © DataStax, All Rights Reserved, Confidential
