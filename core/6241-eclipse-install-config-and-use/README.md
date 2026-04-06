# DSE Core: Eclipse, Install, config and use

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Core curriculum and need help with eclipse, install, config and use. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Core track explains the installation and configuration workflow. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around eclipse, install, config and use.

## Downloads

- [PDF slides](./6241-eclipse-install-config-and-use.pdf)
- [Original PowerPoint](../000-DTSE-ClientProgramming-6241-PL-60%2C%20Eclipse%2C%20Install%2C%20config%20and%20use.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab has no specific preceding

Discussion Unit.

• In this Practice Lab we install, configure and Practice Lab:

use Eclipse, so that you can edit, compile and

run Java client programs that target the DSE Install, configure and use database server. As such, this lab expects an Eclipse operating DSE cluster be accessible.

• Instructions in this practice lab are written for

MacOS, but should function for most Linux

distros.

• This Practice Lab will require reasonable

Internet access.

0000-DTSE-ClientProgramming-6241-PL-60-1 © DataStax, All Rights Reserved, Confidential

Eclipse IDE: What is it ?

Open source integrated developer's

workbench (IDE)

• From 1984's Visual Age, a similar IBM

program

• Not apache, is Eclipse Public License

(ECL)

• Releases with science related names

• June/2018 release is Photon

• Many/many development languages

supported

• Extensible (Vi plugin !)

0000-DTSE-ClientProgramming-6241-PL-60-2 © DataStax, All Rights Reserved, Confidential

Eclipse: How to Install

• Installer program, 49MB,

http://www.eclipse.org/downloads/

• Tar ball, yields DMG file

• Double-Click the DMG

• Choose, "Eclipse IDE for Java EE

Developers" Instructions that follow • And Click, Install are for MacOS, and Eclipse Photon

0000-DTSE-ClientProgramming-6241-PL-60-3 © DataStax, All Rights Reserved, Confidential

Eclipse Install: Spurious Errors

0000-DTSE-ClientProgramming-6241-PL-60-4 © DataStax, All Rights Reserved, Confidential

Eclipse Install: Accept Licenses

0000-DTSE-ClientProgramming-6241-PL-60-5 © DataStax, All Rights Reserved, Confidential

Eclipse: Launch, and Workspace

0000-DTSE-ClientProgramming-6241-PL-60-6 © DataStax, All Rights Reserved, Confidential

Eclipse: Install Scala plugin

0000-DTSE-ClientProgramming-6241-PL-60-7 © DataStax, All Rights Reserved, Confidential

Eclipse: Adding Scala IDE 4.7.x

0000-DTSE-ClientProgramming-6241-PL-60-8 © DataStax, All Rights Reserved, Confidential

Eclipse Install: Accept Licenses

0000-DTSE-ClientProgramming-6241-PL-60-9 © DataStax, All Rights Reserved, Confidential

Eclipse: First Steps

• Close the Welcome View (and

uncheck that you want to see

this view next time)

• In the upper left, Click to make

current the "Project Explorer"

view

• Right-Click on whitespace in

this view, and select New ->

Other

• This action produces the modal

dialog box on the right.

• Select Maven -> Maven Project

-> Next

0000-DTSE-ClientProgramming-6241-PL-60-10 © DataStax, All Rights Reserved, Confidential

Eclipse: New Maven Project

0000-DTSE-ClientProgramming-6241-PL-60-11 © DataStax, All Rights Reserved, Confidential

Eclipse: Maven

(Project type)

• Maven archetypes are

essentially (project

templates)

• Select " .. QuickStart",

and Click, Next

0000-DTSE-ClientProgramming-6241-PL-60-12 © DataStax, All Rights Reserved, Confidential

0000-DTSE-ClientProgramming-6241-PL-60-13 © DataStax, All Rights Reserved, Confidential

Eclipse: What just happened ?

Group id= com.datastax.enablement.bootcamp

0000-DTSE-ClientProgramming-6241-PL-60-14 © DataStax, All Rights Reserved, Confidential

Eclipse: Problem w/ Compiler Version

0000-DTSE-ClientProgramming-6241-PL-60-15 © DataStax, All Rights Reserved, Confidential

Eclipse: Changing

Compiler Version-

• In the Project Explorer view, Right-

Click the project name (my-app)

• And select, Properties

0000-DTSE-ClientProgramming-6241-PL-60-16 © DataStax, All Rights Reserved, Confidential

Eclipse:

Version 1.8

JDK

0000-DTSE-ClientProgramming-6241-PL-60-17 © DataStax, All Rights Reserved, Confidential

Eclipse: Clean, and (clean)

0000-DTSE-ClientProgramming-6241-PL-60-18 © DataStax, All Rights Reserved, Confidential

Ready to

Program Java

and a DSE Client

0000-DTSE-ClientProgramming-6241-PL-60-19 © DataStax, All Rights Reserved, Confidential

Project

Explorer

view,

pom.xml

0000-DTSE-ClientProgramming-6241-PL-60-20 © DataStax, All Rights Reserved, Confidential

What is a pom.xml ? <project xmlns="http://maven.apache.or ... xsi:schemaLocation="http://mav ... <modelVersion>4.0.0</modelVersion>

<groupId>com.datastax.enablement.bootcamp< • xml /groupId> • "project object model" <artifactId>my-app</artifactId> • Each project has one <packaging>jar</packaging> <version>1.0-SNAPSHOT</version> <name>my-app</name> • Tells Maven how to compile, <url>http://maven.apache.org</url> etc, your project <dependencies> <dependency> <groupId>junit</groupId> • Edit once and done ? <artifactId>junit</artifactId> <version>3.8.1</version> <scope>test</scope> </dependency> </dependencies> </project>

0000-DTSE-ClientProgramming-6241-PL-60-21 © DataStax, All Rights Reserved, Confidential

• Full/complete POM A POM that pasted below on Notes supports page

DSE/Java- • But in effect, only need

<dependencies> this/additional <dependency> "dependency" block <groupId> com.datastax.dse </groupId> <artifactId> dse-java-driver-core </artifactId> • Jar files pulled, by <version>1.6.7</version> </dependency> default, from an online </dependencies? Maven repository

• Also pulls whatever Jars

these Jars need, etc

• This repository can be

(should be) internal for

real/production apps

0000-DTSE-ClientProgramming-6241-PL-60-22 © DataStax, All Rights Reserved, Confidential

Changing App.java

• In the Project Explorer view,

navigate to App.java, and

Double-Click to open this file in

the Editor view

0000-DTSE-ClientProgramming-6241-PL-60-23 © DataStax, All Rights Reserved, Confidential

Changing

App.java

• In the Editor view,

change App.java to equal

the source code pasted

on the Notes page below.

0000-DTSE-ClientProgramming-6241-PL-60-24 © DataStax, All Rights Reserved, Confidential

Eclipse: Compile

and Run

• Anywhere in the Editor view (in

App.java), Right-Click and

select, Run As -> Java

Application

• You will be prompted to save the

changes you made to pom.xml,

and App.java, so save

0000-DTSE-ClientProgramming-6241-PL-60-25 © DataStax, All Rights Reserved, Confidential

Eclipse: Success

0000-DTSE-ClientProgramming-6241-PL-60-26 © DataStax, All Rights Reserved, Confidential

Lessons Learned

0000-DTSE-ClientProgramming-6241-PL-60-27 © DataStax, All Rights Reserved, Confidential

End of Unit:

0000-DTSE-ClientProgramming-6241-PL-60-28 © DataStax, All Rights Reserved, Confidential
