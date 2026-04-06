# DSE Core: DSE Core, Keyspaces

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Core curriculum and need help with dse core, keyspaces. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Core track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse core, keyspaces.

## Downloads

- [PDF slides](./6207-dse-core-keyspaces.pdf)
- [Original PowerPoint](../000-DTSE-Core-6207-PL-60%2C%20DSE%20Core%2C%20Keyspaces.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab has no specific preceding

Discussion Unit. A 101-level expertise is

required on given terms; data center,

keyspace, (and others, as listed on the Notes

page below).

DSE Core, alter, create, and • This Practice Lab is meant to address two examine keyspaces issues:

-- After you create a new DSE cluster, a

number of the system keyspaces exist

with SimpleStrategy, and should be

altered to NetworkTopologyStrategy.

-- If you inherit a cluster with down nodes,

and seek to repair same, how to

determine if data is at risk.

000-DTSE-Core-6207-60-PL-1 © DataStax, All Rights Reserved, Confidential

Challenge 1: Create a 2 DC, 1 Node per DC Cluster

Prerequisites:

• Instructions are provided for Linux

• We will operate below recommended

settings; 1 OS node only, minimum 8

GB RAM, 12 GB RAM preferred

• That you have downloaded a DSE Tar

ball

• That you are familiar with a DSE Tar

ball install; cassandra.yaml, and

similar

• All prior DSE software is shut down,

resources reclaimed

• All work done as ‘root’

000-DTSE-Core-6207-60-PL-2 © DataStax, All Rights Reserved, Confidential

Challenge 1: Files, directories

• Unpack the DSE Tar ball in /opt/node0

• Copy these contents into

/opt/node1 # aka “node1”

/opt/node2 # aka “node2”

• Under node1, node2, make a ./data

folder

• Under each ./data, make the folders

./cdc_raw

./commitlog

./data # results in ./data/data

./hints

./saved_caches

000-DTSE-Core-6207-60-PL-3 © DataStax, All Rights Reserved, Confidential

Challenge 1: cassandra.yaml

In the cassandra.yaml in each of node1/node2,

change:

• cluster_name: 'my_cluster' • endpoint_snitch:

org.apache.cassandra.locator.GossipingProperty

FileSnitch • - seeds: "127.0.0.1, 127.0.0.2"

(above, properly indented, same on both) DseSimpleSnitch PropertyFileSnitch • listen_address: 127.0.0.1 # node 1 GossipingPropertyFileSnitch • listen_address: 127.0.0.2 # node 2

• native_transport_address: 127.0.0.1 # node 1 • native_transport_address: 127.0.0.2 # node 2

000-DTSE-Core-6207-60-PL-4 © DataStax, All Rights Reserved, Confidential

Challenge 1: cassandra.yaml

In the cassandra.yaml in each of node1/node2, change:

• commitlog_directory: /opt/dse/node1/data/commitlog # node 1 • commitlog_directory: /opt/dse/node2/data/commitlog # node 2

(Each below different for node1 , node2 )

• cdc_raw_directory: /opt/dse/ node1 /data/cdc_raw • hints_directory: /opt/dse/ node1 /data/hints • saved_caches_directory: /opt/dse/ node1 /data/saved_caches

• data_file_directories:

- /opt/dse/ node1 /data/data

000-DTSE-Core-6207-60-PL-5 © DataStax, All Rights Reserved, Confidential

Challenge 1: cassandra-env.sh

In the cassandra-env.sh in each of node1/node2,

change:

• The first two will be commented, uncomment and set

to,

MAX_HEAP_SIZE="2048M" # Same both nodes

HEAP_NEWSIZE="200M" # Same both nodes

• JMX_PORT="7199" # Node 1 • JMX_PORT="7299" # Node 2

000-DTSE-Core-6207-60-PL-6 © DataStax, All Rights Reserved, Confidential

Challenge 1: logback.xml

In the logback.xml in each of node1/node2,

[ globally ] change:

${cassandra.logdir}

to

/opt/dse/node1/ # node 1

/opt/dse/node2/ # node 2

Generally, this change is made 8 times.

000-DTSE-Core-6207-60-PL-7 © DataStax, All Rights Reserved, Confidential

Challenge 1: cassandra-rackdc.properties

The node 1 (rackdc) properties file is fine.

You only need to edit this file on node 2.

• Make this change-

dc=dc2

000-DTSE-Core-6207-60-PL-8 © DataStax, All Rights Reserved, Confidential

Challenge 1: Boot both DSE nodes

• 3 Linux terminal windows-

• In window 1, cd /opt/dse/node1/bin

• In window 2, cd /opt/dse/node2/bin

• In both windows above,

./dse cassandra –f -R

• In window 3,

cd /opt/dse/node1/bin

nodetool ring # repeat this command

000-DTSE-Core-6207-60-PL-9 © DataStax, All Rights Reserved, Confidential

Challenge 1: Success

A successful exercise outputs-

# ./nodetool ring

Datacenter: dc1 ========== Address Rack Status State Load Owns Token

127.0.0.1 rack1 Up Normal

87.99 KiB ? 6676891273543202389

Datacenter: dc2 ========== Address Rack Status State Load Owns Token

127.0.0.2 rack1 Up Normal

40.39 KiB ? -3406290366391324992

000-DTSE-Core-6207-60-PL-10 © DataStax, All Rights Reserved, Confidential

> Note: Non-system keyspaces don't have the same replication settings, effective

ownership information is meaningless

Challenge 2: Changing system keyspaces

# cqlsh

Connected to my_cluster at 127.0.0.1:9042.

[cqlsh 5.0.1 | Cassandra 4.0.0.2284 | DSE 6.0.0 |

CQL spec 3.4.5 | DSE protocol v2]

Use HELP for help.

cqlsh> use system_schema;

cqlsh:system_schema> describe tables;

tables triggers views keyspaces dropped_columns

functions aggregates indexes types columns

cqlsh:system_schema> select * from keyspaces;

000-DTSE-Core-6207-60-PL-11 © DataStax, All Rights Reserved, Confidential

Challenge 2: Which keyspaces need change ?

cqlsh:system_schema> select * from keyspaces;

keyspace_name | ... | replication --------------------+ ... +------------------------------------------------------------------------------------- system_auth | ... | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1'} system_schema | ... | {'class': 'org.apache.cassandra.locator.LocalStrategy'} dse_system_local | ... | {'class': 'org.apache.cassandra.locator.LocalStrategy'} dse_system | ... | {'class': 'org.apache.cassandra.locator.EverywhereStrategy'} dse_leases | ... | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1'} solr_admin | ... | {'class': 'org.apache.cassandra.locator.EverywhereStrategy'} system_distributed | ... | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'} system | ... | {'class': 'org.apache.cassandra.locator.LocalStrategy'} dse_perf | ... | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1'} system_traces | ... | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '2'} dse_security | ... | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1'}

(11 rows) cqlsh:system_schema>

000-DTSE-Core-6207-60-PL-12 © DataStax, All Rights Reserved, Confidential

Challenge 2: ALTER KEYSPACE

# cqlsh

alter keyspace system_auth

with replication =

{

'class' : 'NetworkTopologyStrategy',

'dc1' : 1,

'dc2' : 1

}

and

durable_writes = 'true' ;

Warnings :

When increasing replication factor you need to run a a non-

incremental repair on all nodes to distribute the data (nodetool

repair -pr).

000-DTSE-Core-6207-60-PL-13 © DataStax, All Rights Reserved, Confidential

Challenge 2: nodetool

# nodetool -h 127.0.0.1 repair -pr repair [2018-06-23 ... ] Starting repair command #1 ... repairing keyspace dse_system with ... [2018-06-23 ... ] Repair session ... finished [2018-06-23 ... ] Repair completed successfully [2018-06-23 ... ] Repair command #1 finished in 0 seconds

[2018-06-23 ... ] Replication factor is 1. No repair is needed for keyspace 'dse_leases'

[2018-06-23 ... ] Starting repair command #2 ... repairing keyspace solr_admin with ... [2018-06-23 ... ] Repair session ... finished [2018-06-23 ... ] Repair completed successfully [2018-06-23 ... ] Repair command #2 finished in 0 seconds

[2018-06-23 ... ] Replication factor is 1. No repair is needed for keyspace 'dse_perf'

[2018-06-23 ... ] Starting repair command #3 ... repairing keyspace system_traces with ... [2018-06-23 ... ] Repair session ... finished [2018-06-23 ... ] Repair completed successfully [2018-06-23 ... ] Repair command #3 finished in 0 seconds

[2018-06-23 ... ] Replication factor is 1. No repair is needed for keyspace 'dse_security'

Starting repair command #4 ... repairing keyspace system_auth with ... [2018-06-23 ... ] [2018-06-23 ... ] Repair session ... finished [2018-06-23 ... ] Repair completed successfully [2018-06-23 ... ] Repair command #4 finished in 0 seconds

000-DTSE-Core-6207-60-PL-14 © DataStax, All Rights Reserved, Confidential

Challenge 2: Confirm change

cqlsh:system_schema> select * from keyspaces;

keyspace_name | ... | replication ---------------+-----+--------------------------------------------------------------------- system_auth | ... | {'class': 'org ... NetworkTopologyStrategy', 'dc1': '1', 'dc2': '1'} ...

000-DTSE-Core-6207-60-PL-15 © DataStax, All Rights Reserved, Confidential

Challenge 3: Will [ you ] cause data loss ? [Discuss]

nodetool decommission node down , N nodetool netstats

RF > # of down nodes Simple node down, Y

Strategy RF <= # of down nodes

RF spans DCs, At least 1 DC not affected Network

Topology RF > # of down nodes AT LEAST 1 DC Strategy

RF spans all DCs and

RF <= # of down nodes IN EACH DC

Most likely ? Restore from backup

000-DTSE-Core-6207-60-PL-16 © DataStax, All Rights Reserved, Confidential

Lessons Learned

000-DTSE-Core-6207-60-PL-17 © DataStax, All Rights Reserved, Confidential

000-DTSE-Core-6207-60-PL-18 © DataStax, All Rights Reserved, Confidential
