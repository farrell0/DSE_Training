# DSE Core: Provisioning Tools

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Core curriculum and need help with provisioning tools. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Core track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around provisioning tools.

## Downloads

- [PDF slides](./6260-provisioning-tools.pdf)
- [Original PowerPoint](../000-DTSE-Cloud-6260-DU-60%2C%20Provisioning%20Tools.pptx)

## Converted Slides

## Discussion Unit:

Introduce the tools/vendors available for Discussion Unit: provisioning larger DSE environments

Provisioning, (Cloud

Providers)

0000-DTSE-Cloud-6260-DU-60-1 © DataStax, All Rights Reserved, Confidential

Discussion Lab:

What is ? (Define the term)

Source: http://blogs.bmc.com/wp-content/uploads/2017/09/iaas-paas-saas-comparison-1024x759.jpg

0000-DTSE-Cloud-6260-DU-60-2 © DataStax, All Rights Reserved, Confidential

Cloud, Why: Discuss-

• What changes in technology enabled

the rise of cloud computing ?

• What are the benefits of cloud

computing ?

• What are (n) essential characteristics

of a cloud service ?

• Define and state the benefits of:

-- IaaS

-- PaaS

-- SaaS

Source: https://idobi.com/idobi/new-xtremebitz-podcast-24/

0000-DTSE-Cloud-6260-DU-60-3 0000-DTSE-Cloud-6260-DU-60-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

0000-DTSE-Cloud-6260-DU-60-4 © DataStax, All Rights Reserved, Confidential

Available to You:

PowerTools / EBDSE • GCE, AWS, Azure

• RightScale

-- 3 party tool rd CTool -- Multi-cloud provider

-- Give you (empty) VMs

-- Azure coming RightScale • CTool

-- Internal tool

-- Uses RightScale

-- Gives you DSE clusters

• PowerTools/EBDSE

-- "Engine Block for DSE"

-- Apps, data

0000-DTSE-Cloud-6260-DU-60-5 0000-DTSE-Cloud-6260-DU-60-5 0000-DTSE-Cloud-6260-DU-60-5 © DataStax, All Rights Reserved, Confidential

Just RightScale:

0000-DTSE-Cloud-6260-DU-60-6 0000-DTSE-Cloud-6260-DU-60-6 0000-DTSE-Cloud-6260-DU-60-6 © DataStax, All Rights Reserved, Confidential

RightScale Overview:

• Management layer for per person

usage tracking

• Two layers of access, RightScale

console and RightScale “Self Service”

• Highlevel instance / Cluster /

Deployment dashboards

• Deploys on GCE or AWS

• Various teams have built some

templates to utilize

-- The workshop template is an

example of one

0000-DTSE-Cloud-6260-DU-60-7 0000-DTSE-Cloud-6260-DU-60-7 0000-DTSE-Cloud-6260-DU-60-7 © DataStax, All Rights Reserved, Confidential

Logging in to RightScale:

Current as of 2018/06/30- • You should have automatically been given a RightScale account and been notified of same via email at time of hire. See image at right- • If not, perhaps try, nicko.garibay@datastax.com • If not, consult your manager

• RightScale login Url,

https://login.rightscale.com/login/sessi on/new

0000-DTSE-Cloud-6260-DU-60-8 0000-DTSE-Cloud-6260-DU-60-8 0000-DTSE-Cloud-6260-DU-60-8 © DataStax, All Rights Reserved, Confidential

‘Bill-to’ modal dialog:

• After username password pair verification,

you will receive a modal display asking you

to select one of possibly several cost

centers to bill your activity to.

• The display on the left displays only one

such option.

• Click the correct account listing to proceed.

0000-DTSE-Cloud-6260-DU-60-9 0000-DTSE-Cloud-6260-DU-60-9 0000-DTSE-Cloud-6260-DU-60-9 © DataStax, All Rights Reserved, Confidential

So again ..

• There are other installations you can create, via

other methods. Using brute force (and brief time

and energy), we are proceeding to create a 5

node CentOS version 7 Linux cluster in one

hosted AWS availability zone.

• 6 steps, and they are-

0000-DTSE-Cloud-6260-DU-60-10 0000-DTSE-Cloud-6260-DU-60-10 0000-DTSE-Cloud-6260-DU-60-10 © DataStax, All Rights Reserved, Confidential

Step 1: Deployments +New

• From the Menu Bar select,

Manage ->

(Deployments) +New

0000-DTSE-Cloud-6260-DU-60-11 0000-DTSE-Cloud-6260-DU-60-11 0000-DTSE-Cloud-6260-DU-60-11 © DataStax, All Rights Reserved, Confidential

Step 2: Identify this deployment

• Enter a Nickname that includes

your DataStax identifying

information, optionally a

Description, and Click, Save.

• Why enter your name ? So that you

are more likely to be contacted

before someone else blows this

deployment away.

0000-DTSE-Cloud-6260-DU-60-12 0000-DTSE-Cloud-6260-DU-60-12 0000-DTSE-Cloud-6260-DU-60-12 © DataStax, All Rights Reserved, Confidential

RightScale terminology: Deployment

• RightScale is a multi-cloud provider, with which you can deploy nodes (virtual

machines, servers) across AWS, GCE, Azure, others. We’re not completing this type of

deployment today.

• As such, however, RightScale uses terminology different and abstract from any cloud

provider.

• A RightScale Deployment is an logical construct consisting of:

• A number of individual servers, each possibly with a different hardware profile.

• A number of arrays of servers. Each server array member will have the same

hardware profile. Each single array will reside in one (cloud provider availability

zone).

• And a mix and/or match of individual and arrays of servers.

• Today we are creating one array of five servers.

0000-DTSE-Cloud-6260-DU-60-13 0000-DTSE-Cloud-6260-DU-60-13 0000-DTSE-Cloud-6260-DU-60-13 © DataStax, All Rights Reserved, Confidential

Step 3: Create an array of servers deployment

• Click, +Array

• In the dialog bock that is produced,

Select “AWS US – Oregon”

• And Click, Continue

• Do I have to use AWS US – Oregon ? No. However, there are combinations of location, hardware profile, storage options, and related that you can choose that ultimately will not work. The path we are detailing here works. Even in one AWS region we can emulate global network latencies and such using Linux trickery.

0000-DTSE-Cloud-6260-DU-60-14 0000-DTSE-Cloud-6260-DU-60-14 0000-DTSE-Cloud-6260-DU-60-14 © DataStax, All Rights Reserved, Confidential

RightScale terminology: Server Template

• A RightScale Server Template is another abstraction.

• If we refer to a given virtual machine image as an OVF, OVA, or VMDK set of files,

each cloud provider has specific and differing sets of (rules, requirements, limitation,

whatever) before you can load or make use of same.

• RightScale uses Server Templates to try and aid you in this task.

• Net/net, you can use RightScale Server Templates, even customize them, or use brute

force. We prefer brute force.

• After we instantiate a given server, if we find we need a given version of Python or

whatever on that machine, we’ll just script that update or related.

0000-DTSE-Cloud-6260-DU-60-15 0000-DTSE-Cloud-6260-DU-60-15 0000-DTSE-Cloud-6260-DU-60-15 © DataStax, All Rights Reserved, Confidential

Step 4: Select a server template type

• Select the RightScale Server

Template titled, Base Server

Template for Linux (RSB)

(v14.1.1)

• Then Click, Server Details

• Why use this server template ? Because it has worked for us before, providing us the features we desire on the next and subsequent screens.

0000-DTSE-Cloud-6260-DU-60-16 0000-DTSE-Cloud-6260-DU-60-16 0000-DTSE-Cloud-6260-DU-60-16 © DataStax, All Rights Reserved, Confidential

Step 5: Server Details

We call to make a number of changes

here:

• Edit the (Server) Array Name, to

include your personal identifier.

• MultiCloud Image, and Instance

Type, see next slide-

0000-DTSE-Cloud-6260-DU-60-17 0000-DTSE-Cloud-6260-DU-60-17 0000-DTSE-Cloud-6260-DU-60-17 © DataStax, All Rights Reserved, Confidential

Step 5: continued

• For MultiCloud Image we choose,

RightImage CentOS 7 x64 v14.2 HVM

Why ? Because we wanted CentOS version 7. Why HVM ? Largely because HVM (versus EBS) gives us exactly what we need for an ephemeral DSE system. Be advised that HVM or EBS, some AWS machine types are not compatible with both HVM or EBS. • For (AWS) Instance Type we choose,

m3.2xlarge

Why ? The AWS EC2 machine types are listed here, https://aws.amazon.com/ec2/instance-types/ m3.2xlarge gives us 8 (count) vCPUs, 30 GB RAM, and 2 (count) 80GB SSDs, and its HVM compatible.

Be aware you may need to script formatting, mounting and naming any drives, yadda, after your virtual machine is created.

0000-DTSE-Cloud-6260-DU-60-18 0000-DTSE-Cloud-6260-DU-60-18 0000-DTSE-Cloud-6260-DU-60-18 © DataStax, All Rights Reserved, Confidential

Step 5: continued, continued

• We’ve never had success using Automatic instance store mapping , so we’ll skip this

feature.

• Datacenter / Subsets

• If you want a DSE system to honestly test RAC placement, DC placement or similar, you will have to make multiple server arrays, each in a different (cloud provider host location, aka availability zone). We are not doing that type of work today, and will leave this entry Checked as, Any.

• SSH Key

• We need to generate an SSH Key so that we may later login to any of these boxes remotely and safely. • Click, (SSH Key) New, give the key a name, and Click, Save. This drop down list box will then

automatically populate.

0000-DTSE-Cloud-6260-DU-60-19 0000-DTSE-Cloud-6260-DU-60-19 0000-DTSE-Cloud-6260-DU-60-19 © DataStax, All Rights Reserved, Confidential

RightScale terminology: Security Group

• A RightScale Security Group determines the firewall rules your virtual machine will be

created with.

• Previously, someone at DataStax created the “automaton (default)” Security Group

which meets our needs. (In effect, all of the ports are open.)

0000-DTSE-Cloud-6260-DU-60-20 0000-DTSE-Cloud-6260-DU-60-20 0000-DTSE-Cloud-6260-DU-60-20 © DataStax, All Rights Reserved, Confidential

Step 5: final

• In the drop down list box for Security Groups, Select, ‘automaton (default)’.

• Leave the Checkbox titled, “Associate Ephemeral Public IP Address” checked.

• And Click, Array Details.

0000-DTSE-Cloud-6260-DU-60-21 0000-DTSE-Cloud-6260-DU-60-21 0000-DTSE-Cloud-6260-DU-60-21 © DataStax, All Rights Reserved, Confidential

Step 6: Number of servers, and more.

• Change the drop down list box titled,

Status, to Enabled.

If set to Disabled, your virtual machines

will not be provisioned.

• Set the Min and Max Count(s) to 5,

because we want 5 servers.

• Set Decision Threshold to 10%.

A rounding error in how this software works; if this number is too high, we have seen where the last server is not provisioned. • Set Resize calm time to 3 minutes.

• And Click, Confirm -> Finish -> Launch.

(Launch will be below the toolbar.)

0000-DTSE-Cloud-6260-DU-60-22 0000-DTSE-Cloud-6260-DU-60-22 0000-DTSE-Cloud-6260-DU-60-22 © DataStax, All Rights Reserved, Confidential

Result of Step 6,

and getting around:

• This screen is produced as the result of our previous

step, Step 6. You can return to this screen at any time

via the Info button.

• The ‘Status enabled|disabled’ selection will have to

be changed to disabled before we can destroy this

server array.

• The ‘Primary Security Groups automaton’ link shows

us our firewall rules, as displayed in the next slide.

• The Instances button takes us to our server array

status screen, as displayed in 2 slides.

0000-DTSE-Cloud-6260-DU-60-23 0000-DTSE-Cloud-6260-DU-60-23 0000-DTSE-Cloud-6260-DU-60-23 © DataStax, All Rights Reserved, Confidential

Security Group (firewall rules): checking

Viewing our specified firewall

rules-

• We get to this screen via

the Info button, Primary

Security Groups link.

• icmp will give us ping into

these boxes.

• Otherwise we are wide

open for all inbound and

outbound TCP/IP.

0000-DTSE-Cloud-6260-DU-60-24 0000-DTSE-Cloud-6260-DU-60-24 0000-DTSE-Cloud-6260-DU-60-24 © DataStax, All Rights Reserved, Confidential

Server array status screen:

• We arrive at this screen via the Instances button. 5 servers, we have cut the displayed image to afford higher image resolution. • We see that our boxes are operational. It takes several minutes to move from Launch to Operational. • Minimally here we need to grab the ‘public IP address’ for each of the 5 servers. This address is in the Tags column for each server.

0000-DTSE-Cloud-6260-DU-60-25 0000-DTSE-Cloud-6260-DU-60-25 0000-DTSE-Cloud-6260-DU-60-25 © DataStax, All Rights Reserved, Confidential

Status, next steps:

• Thus far we have created a single array of 5 servers. As a single array, these 5 boxes

are all of one machine type and reside in one (cloud provider availability zone).

• Next, we need to login into any or all of these boxes to perform our expected work;

install and operate DSE or similar.

• We will need a copy of our SSH Key.

• We will need the public IP address of each of these boxes.

• We are going to login using ssh(C) from our laptop into these boxes.

0000-DTSE-Cloud-6260-DU-60-26 0000-DTSE-Cloud-6260-DU-60-26 0000-DTSE-Cloud-6260-DU-60-26 © DataStax, All Rights Reserved, Confidential

Logging into box 1: Getting the SSH Key

• In Step 5 earlier we generated an

SSH Key.

• We can retrieve this value from a,

Menu Bar -> Clouds -> (our cloud) -

> SSH Keys

• Click, SSH Keys, then Click the

named key we created.

0000-DTSE-Cloud-6260-DU-60-27 0000-DTSE-Cloud-6260-DU-60-27 0000-DTSE-Cloud-6260-DU-60-27 © DataStax, All Rights Reserved, Confidential

Logging into box 1: Copying the key value

• Copy all of the text including the

BEGIN RSA and END RSA lines.

• Open any text editor, paste, and save

as a named file of your choosing.

A .key suffix is optional, but standard.

We called our file, zzz.key

0000-DTSE-Cloud-6260-DU-60-28 0000-DTSE-Cloud-6260-DU-60-28 0000-DTSE-Cloud-6260-DU-60-28 © DataStax, All Rights Reserved, Confidential

Logging into box 1: Get the public IP address

• Recall that our server array public IP

addresses are available under, Manage ->

Deployments -> (your server array name) ->

(your server array name) -> Instances -> Tags -

> server:public_ip

• Capture this IP address.

0000-DTSE-Cloud-6260-DU-60-29 0000-DTSE-Cloud-6260-DU-60-29 0000-DTSE-Cloud-6260-DU-60-29 © DataStax, All Rights Reserved, Confidential

Logging into box 1: ssh

• From a command window on your

laptop, we will need to run ssh, the

secure/encrypted shell. On Mac or

Linux, this command should be pre-

installed.

• The key file you created previously must

not be publicly readable. On Mac or

Linux we change permissions using a

chmod 400 command, as displayed at

right.

• Then we perform a,

ssh –i zzz.key root@34.208.128.8

Assuming our public IP address is

34.208.128.8

0000-DTSE-Cloud-6260-DU-60-30 0000-DTSE-Cloud-6260-DU-60-30 0000-DTSE-Cloud-6260-DU-60-30 © DataStax, All Rights Reserved, Confidential

Go forth and prosper-

• Now you’re ready to do whatever you

came to do; install DSE, break DSE,

yadda.

• As largely empty server boxes, most

folks create a single script that

automates all of the settings they prefer:

• Download, configure and boot DSE

• Install any client drivers you prefer

• Other

0000-DTSE-Cloud-6260-DU-60-31 0000-DTSE-Cloud-6260-DU-60-31 0000-DTSE-Cloud-6260-DU-60-31 © DataStax, All Rights Reserved, Confidential

Shutting this all down:

By the nature of the work we perform, it

is generally expected that you will un-

provision any boxes you created once

your work is complete.

• Go to the Info TAB and ensure that

Status is disabled, else RightScale

will be configured to resurrect your

boxes when you try to terminate

them.

• Then go to Instances -> Terminate All.

There is a safety prompt, then you’re

committed.

• Like provisioning, the terminate step

may take a few minutes.

0000-DTSE-Cloud-6260-DU-60-32 0000-DTSE-Cloud-6260-DU-60-32 0000-DTSE-Cloud-6260-DU-60-32 © DataStax, All Rights Reserved, Confidential

Shutting this all down: Confirming

• If you wish to be hyper-safe, we

actually go back and delete the now

empty (un-provisioned) server array.

0000-DTSE-Cloud-6260-DU-60-33 0000-DTSE-Cloud-6260-DU-60-33 0000-DTSE-Cloud-6260-DU-60-33 © DataStax, All Rights Reserved, Confidential

Just CTool:

0000-DTSE-Cloud-6260-DU-60-34 0000-DTSE-Cloud-6260-DU-60-34 0000-DTSE-Cloud-6260-DU-60-34 © DataStax, All Rights Reserved, Confidential

CTool

• Datastax built automation

• Test Engineering “Toolkit”

• Command Line with

granular control of

environment

• Ability to reset

environment for repetitive

testing

0000-DTSE-Cloud-6260-DU-60-35 0000-DTSE-Cloud-6260-DU-60-35 0000-DTSE-Cloud-6260-DU-60-35 © DataStax, All Rights Reserved, Confidential

CTOOL (cont)

● Tool to automate the setup of clusters

○ Originally created and used by the test team

Open to the wider company ○

● Riptano repository

https://github.com/riptano/ctool ○

■ what you should be using now

● Pull down to install

Make sure to view the readme file ○

For full documentation see: ○

■ https://datastax.jira.com/wiki/display/QA/CTOOL+DOCUMENTATION

■ https://datastax.jira.com/wiki/display/QA/CTOOL+New+Repo

0000-DTSE-Cloud-6260-DU-60-36 0000-DTSE-Cloud-6260-DU-60-36 0000-DTSE-Cloud-6260-DU-60-36 © DataStax, All Rights Reserved, Confidential

CTOOL Requirements

● Python 2.7.5 +

● On mac use homebrew to install

http://www.howtogeek.com/211541/homebrewforosxeasilyinstallsdeskt ○ opappsandterminalutilities/

https://coolestguidesontheplanet.com/installinghomebrewonosxelcapit ○ an1011packagemanagerforunixapps/

● DO NOT use mac installed python

● Homebrew install will install pip

● If get errors when first running ctool may need to install additional modules with

pip

○ Pip install pythonnovaclient pythonkeystoneclient funcsigs wrapt

netifaces==0.10.3 positional monotonic

0000-DTSE-Cloud-6260-DU-60-37 0000-DTSE-Cloud-6260-DU-60-37 0000-DTSE-Cloud-6260-DU-60-37 © DataStax, All Rights Reserved, Confidential

Create .automaton.conf in Your Home Directory

[cluster]provider = rightscale

[rightscale] # for the private key: login to RightScale, download SSH private key from: https://us4.rightscale.com/global/users/ssh#ssh , # save it locally, then set the local path here user_email = <rightscaleemail> user_pass = <rightscalepassword> private_key = /Users/example/bin/keys/example_rightscale_private_key_rsa

# supported cloud providers: ec2, gce cloud_provider = gce

# account_id as seen in your RightScale url: https://us4.rightscale.com/acct/<account_id>/ account_id = 00000

[logging] # log file location must be a full path ("~" not allowed) level = INFO file = /Users/example/tmp/automaton.log

[credentials] github_private_key_path = /Users/example/bin/keys/ctool_private_key_rsa artifactory_user = qaautomaton artifactory_pass = [REDACTED_API_KEY]

[install] repo_username = <DSA user name (not email)> repo_password = <DSA password> 0000-DTSE-Cloud-6260-DU-60-38 0000-DTSE-Cloud-6260-DU-60-38 0000-DTSE-Cloud-6260-DU-60-38 © DataStax, All Rights Reserved, Confidential

Basic CTOOL Use

ctool launch p ubuntu MyCluster i m3.2xlarge 2

ctool install b "5.0.0rc2" k 1 s 1 \

MyCluster enterprise enablegraph

ctool start MyCluster enterprise

0000-DTSE-Cloud-6260-DU-60-39 0000-DTSE-Cloud-6260-DU-60-39 0000-DTSE-Cloud-6260-DU-60-39 © DataStax, All Rights Reserved, Confidential

ctool list Getting Info

ctool info murphyEAP

0000-DTSE-Cloud-6260-DU-60-40 0000-DTSE-Cloud-6260-DU-60-40 0000-DTSE-Cloud-6260-DU-60-40 © DataStax, All Rights Reserved, Confidential

Cluster ‘type’

● You can specify what parts of DSE to turn on when defining your cluster

e PERCENT_SEARCH

g PERCENT_ANALYTICS

k PERCENT_SPARK

-- PERCENT_* Must be a valid decimal number between 0.0 and 1.0

-- Where 0 is off and 1.0 is 100%

● To turn on graph simply use

enablegraph

● To enable DSEFS

enabledsefs

0000-DTSE-Cloud-6260-DU-60-41 0000-DTSE-Cloud-6260-DU-60-41 0000-DTSE-Cloud-6260-DU-60-41 © DataStax, All Rights Reserved, Confidential

Adding Complexity

● Datacenter fun:

ctool launch multiregion 2 "ec2:uswest1:1 ec2:useast1:1”

● Security:

-- ctool secure kdc –k

-- https://datastax.jira.com/wiki/display/QA/CTOOL+Secure

● Park/Unpark (Currently park works on EC2 using the "rightscale" cluster

provider.)

-- ctool park superCluster

-- ctool unpark

-- https://datastax.jira.com/wiki/pages/viewpage.action?pageId=81592724

0000-DTSE-Cloud-6260-DU-60-42 0000-DTSE-Cloud-6260-DU-60-42 0000-DTSE-Cloud-6260-DU-60-42 © DataStax, All Rights Reserved, Confidential

Accessing your Servers

You can access your nodes in a couple of ways

• Via ctool directly

ctool ssh exampleEAP 0 • Or using the ssh key to ssh directly as user automaton --You will need to put your key into a file with read only permissions for user

ssh i myClusterKey automaton@<external ip>

-- This is the same method used if accessing any cloud based server though

the name may change depending on the template

• To retrieve your ID ssh key use

ctool dump_key MyClusterName

0000-DTSE-Cloud-6260-DU-60-43 0000-DTSE-Cloud-6260-DU-60-43 0000-DTSE-Cloud-6260-DU-60-43 © DataStax, All Rights Reserved, Confidential

Command Line

You can execute command line actions using ctool to any and all nodes in your cluster

ctool run MyCluster all 'sudo mv /home/automaton /mnt1 && \

sudo ln s /mnt1/automaton /home/’

ctool run MyCluster all 'sudo sed i s/"^authenticator: .*$"/"authenticator: com.datastax.bdp.cassandra.auth .DseAuthenticator"/ /etc/dse/cassandra/cassandra.yaml'

0000-DTSE-Cloud-6260-DU-60-44 0000-DTSE-Cloud-6260-DU-60-44 0000-DTSE-Cloud-6260-DU-60-44 © DataStax, All Rights Reserved, Confidential

Building environments quickly

With CTOOL you can

• SCP

• SSH

• EXEC

• JAVA_INSTALL

• RESET (!!!)

• START/STOP AGENTS

• UPGRADE

• ETC

0000-DTSE-Cloud-6260-DU-60-45 0000-DTSE-Cloud-6260-DU-60-45 0000-DTSE-Cloud-6260-DU-60-45 © DataStax, All Rights Reserved, Confidential

Getting Help-

• ‘ctool’ by itself will give you a list of commands • Once you know the commands you can then get help on them individually by using -- ctool <command name> help

-- Or ctool <command name> h • For example:

-- ctool install –help

-- ctool start –h

-- ctool list help

0000-DTSE-Cloud-6260-DU-60-46 0000-DTSE-Cloud-6260-DU-60-46 0000-DTSE-Cloud-6260-DU-60-46 © DataStax, All Rights Reserved, Confidential

Final on CTool:

CTOOL is great for doing things in house

• Test something a customer is doing

• Try something new for yourself

• General experimentation

And RightScale is the cloud provider manager behind the scenes

• Used by CTOOL

• Used by Asset Hub

• Can build clusters based on templates

But what if you want to demo for a client how to easy it is to build a cluster on the cloud

• You don't want to use our internal tools

• Because you want to demonstrate in a way they may do it themselves

0000-DTSE-Cloud-6260-DU-60-47 0000-DTSE-Cloud-6260-DU-60-47 0000-DTSE-Cloud-6260-DU-60-47 © DataStax, All Rights Reserved, Confidential

Final on CTool:

While AWS is very common some customers prefer using other providers

• Maybe do to competition with Amazon • Maybe because they want to have a hybrid cloud strategy • Maybe because of previous relations with one provider over the other

We will not do an install on all providers available but do know

• CTOOL and RightScale can provision in AWS or GCE • We have a Strong Partner with Azure • DMC currently uses Azure and AWS • DMC is looking to add either Oracle Cloud or GCE in the near future

No matter which provider you choose the DSE steps are the same and provisioning is based upon the individual console

0000-DTSE-Cloud-6260-DU-60-48 0000-DTSE-Cloud-6260-DU-60-48 0000-DTSE-Cloud-6260-DU-60-48 © DataStax, All Rights Reserved, Confidential

Just Power

Tools, EBDSE:

0000-DTSE-Cloud-6260-DU-60-49 0000-DTSE-Cloud-6260-DU-60-49 0000-DTSE-Cloud-6260-DU-60-49 © DataStax, All Rights Reserved, Confidential

Power Tools

The Vanguard group has been working on a number of tools for internal consumption • We have already spoke some about AssetHub • We next want to introduce EBDSE

-- Engine Block for DSE -- Internal tool used for testing all aspects of DSE not just the Core as per cassandrastress • Slack channel can be found at -- #ebdse • Documentation can be found at

-- https://powertools.datastax.com/intro/powertools/ -- Use academy login to access

0000-DTSE-Cloud-6260-DU-60-50 0000-DTSE-Cloud-6260-DU-60-50 0000-DTSE-Cloud-6260-DU-60-50 © DataStax, All Rights Reserved, Confidential

Introduction to EBDSE

Cassandra Stress is very useful to become familiar with • Part of toolset that comes with Open Source Cassandra • Clients may be familiar with or even already using • Thus they may have questions about it

But it doesn’t • Have user friendly data • Work well for testing Search • Hard to make useful data for Analytics tests • Can’t test DSE graph loads

So an internal tool has been developed • EBDSE

0000-DTSE-Cloud-6260-DU-60-51 0000-DTSE-Cloud-6260-DU-60-51 0000-DTSE-Cloud-6260-DU-60-51 © DataStax, All Rights Reserved, Confidential

EBDSE

Is an internal only toolset • You can’t leave a copy of it at a customer site

-- Of course you can leave the results of the test, the metrics and such, just not the tool itself • It is a carrot for sales and services to unfold our product • We want to protect ourselves from having an internal tool used against us by competitors Initially designed to enhance the sales cycle • Be able to do a quick demo • Rapidly showcase a Proof of Technology (POT)

-- SE’s may want to note that fact for their project -- Many AssetHub assets use EBDSE for testing within • Demonstrate a user experience that will scale

0000-DTSE-Cloud-6260-DU-60-52 0000-DTSE-Cloud-6260-DU-60-52 0000-DTSE-Cloud-6260-DU-60-52 © DataStax, All Rights Reserved, Confidential

EBDSE

Core Assumptions around design include Our customers want to be compelled by facts and evidence, not by ideas alone. • DataStax and our Customers can't afford to spend weeks or months building a custom • testing harness for each opportunity just to establish product fit, relevancy, or scale. Establishing value should be as loweffort as we can make it. Analytic methods for establishing workload sizing are moot without data from real tests. • Given the choice, real benchmark data is preferred to estimates.

Do simple things fast! Simple things should be simple. Complex things should be possible. •

0000-DTSE-Cloud-6260-DU-60-53 0000-DTSE-Cloud-6260-DU-60-53 0000-DTSE-Cloud-6260-DU-60-53 © DataStax, All Rights Reserved, Confidential

So What is EBDSE

A single scriptable testing system that • Creates human readable data • Can validate a database design • Can provide load metrics • Test systems using CQL • Test systems using DSE graph • Because of the above two also

-- Tests out DSE Search -- Provides Data to test DSE Analytics o Does not write jobs for you • Is extensible -- Internal tool that is tracked in Jira where you can put in bug and feature requests • 90% of the time you will not have to do any scripting -- Just custom yamls that reflect your data model

0000-DTSE-Cloud-6260-DU-60-54 0000-DTSE-Cloud-6260-DU-60-54 0000-DTSE-Cloud-6260-DU-60-54 © DataStax, All Rights Reserved, Confidential

How do I get it?

EBDSE is documented at • https://powertools.datastax.com -- Uses your DataStax academy login -- Contact Academy team if you can’t get access -- Also can get help on the command line o ./ebdse help o ./ebdse advancedhelp

Has a slack channel for questions and comments • #ebdse

Download at

• https://powertools.datastax.com/assets/ • curl O https://powertools.datastax.com/assets/ebdse u <dsa account>

0000-DTSE-Cloud-6260-DU-60-55 0000-DTSE-Cloud-6260-DU-60-55 0000-DTSE-Cloud-6260-DU-60-55 © DataStax, All Rights Reserved, Confidential

Core Machinery

PowerTools Core • EngineBlock ○ Provides the core runtime ○ Docs http://docs.engineblock.io/ • VirtData ○ Provides the generation of data ○ Docs available at http://docs.virtdata.io/ • Github ○ https://github.com/riptano/ebdse ○ https://github.com/engineblock/engineblock/ ○ https://github.com/virtualdataset/virtdatajava

0000-DTSE-Cloud-6260-DU-60-56 0000-DTSE-Cloud-6260-DU-60-56 0000-DTSE-Cloud-6260-DU-60-56 © DataStax, All Rights Reserved, Confidential

How do I run?

Against default test keyspace (testks) and schema (telemetry) • Download ebdse • Execute ○ ./ebdse v run type=cql yaml=telemetry/telemetryschema.yaml host=localhost ■ This creates the keyspace and schema ○ ./ebdse v run alias=ops type=cql yaml=telemetry/telemetryops.yaml host=localhost cycles=1000 ■ This runs a test with 1000 cycles, feel free to change the numbers ○ Read the results ■ Some results on command line ■ Detailed Output in scenario*.log • https://powertools.datastax.com/book/intro/quickstart/ • Example yaml files ○ https://github.com/riptano/ebdse/tree/master/ebdse/src/main/resources/activities

0000-DTSE-Cloud-6260-DU-60-57 0000-DTSE-Cloud-6260-DU-60-57 0000-DTSE-Cloud-6260-DU-60-57 © DataStax, All Rights Reserved, Confidential

Look at the command help for cql

./ebdse help cql • Note all the options • Note the example yaml file for a custom table setup

0000-DTSE-Cloud-6260-DU-60-58 0000-DTSE-Cloud-6260-DU-60-58 0000-DTSE-Cloud-6260-DU-60-58 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Cloud-6260-DU-60-59 © DataStax, All Rights Reserved, Confidential
