# DSE Core: Ops Center, Lab

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Core curriculum and need help with ops center, lab. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Core track walks through a hands-on lab. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around ops center, lab.

## Downloads

- [PDF slides](./6251-ops-center-lab.pdf)
- [Original PowerPoint](../000-DTSE-OpsCenter-6251-PL-60%2C%20Ops%20Center%2C%20Lab.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Unit 6250, where most of the

objects we create in this lab were

introduced. Install DSE Ops Center,

Call to Manage Existing • In this Practice Lab, we install Ops Cluster Center, the Ops Center agent, and call to

manage an existing cluster.

0000-DTSE-OpsCenter-6251-DU-60-1 © DataStax, All Rights Reserved, Confidential

Challenge: Overview

Prerequisites:

• Instructions are provided for Linux

• We will operate below recommended

settings; 1 OS node only, minimum 8

GB RAM, 12 GB RAM preferred

Challenges 1-4:

• Make a single node DSE cluster with

a real IP address

• Manually install the Ops Center agent

• Install Ops Center

• Tell Ops Center to manage the DSE

cluster above

0000-DTSE-OpsCenter-6251-DU-60-2 © DataStax, All Rights Reserved, Confidential

Challenge 1: Single node DSE with real IP addr

Edits given IP addr of 172.16.119.194

• Leverage lab instructions from cassandra.yaml 6207, Keyspace Lab - seeds: "172.16.119.194"

listen_address:

172.16.119.194 • Make certain hostname resolves native_transport_address: ping `hostname`

172.16.119.194 ifconfig (or Google how) cassandra-env.sh vi /etc/hosts MAX_HEAP_SIZE="2048M" • Ensure firewall is disabled HEAP_NEWSIZE="200M" (CentOs 7 below, or Google) JMX_PORT=" 7499 " systemctl disable firewalld

dse cassandra –f -R

0000-DTSE-OpsCenter-6251-DU-60-3 © DataStax, All Rights Reserved, Confidential

Challenge 2: Ops Center Agent (manual install)

• Ops Center can install its agent

automatically

• But, manual install today because ..

-- Run agent in foreground,

easier diagnostics

-- This is an odd install, multiple

entities may try to take

localhost/127.0.0.1, better

control via manual install

0000-DTSE-OpsCenter-6251-DU-60-4 © DataStax, All Rights Reserved, Confidential

Challenge 2: Ops Center Agent (manual install)

Create a download key

from,

https://

academy.datastax.com/

downloads

Value used on

next page

0000-DTSE-OpsCenter-6251-DU-60-5 © DataStax, All Rights Reserved, Confidential

Challenge 2: Ops Center Agent (manual install)

mkdir /opt/ops_center_agent

cd /opt/ops_center_agent

Download agent via,

curl --user your_name@aol.com:your_key -L \

ht tp://downloads.datastax.com/enterprise/datastax-agent -6.5.0 .tar.gz \

| tar xz

Wrong version (6.5.0) other ?

gzip: stdin: not in gzip format

tar: Child returned status 1

tar: Error is not recoverable: exiting now

0000-DTSE-OpsCenter-6251-DU-60-6 © DataStax, All Rights Reserved, Confidential

Challenge 2: Ops Center Agent (manual install)

The previous command outputs files-

cd /opt/ops_center_agent/conf

vi ./conf/address.yaml

stomp_interface: 127.0.0.1

use_ssl: 0

cd ../bin

./datastax-agent -f

0000-DTSE-OpsCenter-6251-DU-60-7 © DataStax, All Rights Reserved, Confidential

Challenge 3: Ops

Center install mkdir /opt/ops_center

cd /opt/ops_center

Download Ops Center 6.5.0 from,

https://academy.datastax.com/quick-downloads

(Version 6.5.0 instructions here.)

./bin/opscenter -f

http://localhost:8888/

Answers on both localhost and (actual IP addr)

0000-DTSE-OpsCenter-6251-DU-60-8 © DataStax, All Rights Reserved, Confidential

Challenge 4: Ops Center, First steps

As a first time boot of Ops

Center, you receive the

modal dialog box shown at

left-

Choose (existing), and Click,

Get Started

0000-DTSE-OpsCenter-6251-DU-60-9 © DataStax, All Rights Reserved, Confidential

Challenge 4:

Enter the IP address and

JMX port number of the

existing DSE cluster we

created in Challenge 1.

No security, leave these

Click, Next

0000-DTSE-OpsCenter-6251-DU-60-10 © DataStax, All Rights Reserved, Confidential

Challenge 4:

Check, Install Agents

Manually, then Click

Close.

0000-DTSE-OpsCenter-6251-DU-60-11 © DataStax, All Rights Reserved, Confidential

Challenges

1-4:

Success

0000-DTSE-OpsCenter-6251-DU-60-12 © DataStax, All Rights Reserved, Confidential

Lessons Learned

0000-DTSE-OpsCenter-6251-DU-60-13 © DataStax, All Rights Reserved, Confidential

0000-DTSE-OpsCenter-6251-DU-60-14 © DataStax, All Rights Reserved, Confidential
