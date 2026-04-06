# DSE Core: Maven, Install, config and use

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Core curriculum and need help with maven, install, config and use. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Core track explains the installation and configuration workflow. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around maven, install, config and use.

## Downloads

- [PDF slides](./6240-maven-install-config-and-use.pdf)
- [Original PowerPoint](../000-DTSE-ClientProgramming-6240-PL-60%2C%20Maven%2C%20Install%2C%20config%20and%20use.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab has no specific preceding

Discussion Unit.

• In this Practice Lab we install, configure and Practice Lab: use Maven, so that you can edit, compile and

run Java client programs that target the DSE Install, configure and use database server. As such, this lab expects an

Maven operating DSE cluster be accessible.

• Instructions in this practice lab are written for

CentOS 7 using the command line, but

should function for most Linux distros.

• Maven is an 8MB download, but any Java

program compiles you perform will require

reasonable Internet access.

0000-DTSE-ClientProgramming-6240-DU-60-1 © DataStax, All Rights Reserved, Confidential

Apache Maven: What is it ?

Apache Maven is "build automation

software". Think yum(C), or apt-get(C),

(iTunes), but for Java programs.

-- Will create your project filesystem

structure, compile, deploy, other.

-- Will find, download, version, and

manage all of your Java

dependencies.

-- And, do all of this in about 4

total commands.

-- Supports Java, Scala, Ruby, C/C++

others

0000-DTSE-ClientProgramming-6240-DU-60-2 © DataStax, All Rights Reserved, Confidential

Apache Maven: How to install

• Already installed ? "mvn --version"

• If not, Tar ball; unzip, place in PATH

-- https://maven.apache.org/download.cgi

-- https://maven.apache.org/install.html

-- Version 3.5.4, 8MB in size

-- Is a Java app, requires Java 8 (v 3.5.4)

Run all commands in -- mvn --version this unit inside a Linux terminal window.

0000-DTSE-ClientProgramming-6240-DU-60-3 © DataStax, All Rights Reserved, Confidential

Command 1: Initialize a new Java/DSE client project

Will be the Java • cd /opt (cd anywhere) Package name (as generated)

• mvn archetype:generate

-DgroupId= com.datastax.enablement.bootcamp

-DarchetypeArtifactId=maven-archetype-quickstart

-DinteractiveMode=false

-DartifactId= my-app

Project name (logical only)

0000-DTSE-ClientProgramming-6240-DU-60-4 © DataStax, All Rights Reserved, Confidential

Command 1: What just happened ?

-DgroupId= com.datastax.enablement.bootcamp

0000-DTSE-ClientProgramming-6240-DU-60-5 © DataStax, All Rights Reserved, Confidential

What is a pom.xml ? <project xmlns="http://maven.apache.or ... xsi:schemaLocation="http://mav ... <modelVersion>4.0.0</modelVersion>

<groupId>com.datastax.enablement.bootcamp< • xml /groupId> • "project object model" <artifactId>my-app</artifactId> • Each project has one <packaging>jar</packaging> <version>1.0-SNAPSHOT</version> <name>my-app</name> • Tells Maven how to compile, <url>http://maven.apache.org</url> etc, your project <dependencies> <dependency> <groupId>junit</groupId> • Edit once and done ? <artifactId>junit</artifactId> <version>3.8.1</version> <scope>test</scope> </dependency> </dependencies> </project>

0000-DTSE-ClientProgramming-6240-DU-60-6 © DataStax, All Rights Reserved, Confidential

What's in App.java ?

package com.datastax.enablement.bootcamp;

/** * Hello world! • Stub * • It runs (it's Hello World) */ public class App { • Add DSE client code; public static void main( String[] args ) structure { System.out.println( "Hello World!" ); } }

0000-DTSE-ClientProgramming-6240-DU-60-7 © DataStax, All Rights Reserved, Confidential

To compile and run the program-

• From the "project directory"

cd /opt/my-app -DgroupId= com.datastax.enablement.bootcamp

-DartifactId= my-app • # compiles

mvn package

• # generates the Java CLASSPATH Left single apostrophes mvn dependency:build-classpath -Dmdep.outputFile=cp.txt

• # call to run the program (one line below)

java -cp target/my-app-1.0-SNAPSHOT.jar :`cat cp.txt`

com.datastax.enablement.bootcamp.App

0000-DTSE-ClientProgramming-6240-DU-60-8 © DataStax, All Rights Reserved, Confidential

• Full/complete POM A POM that supports pasted below on Notes DSE/Java- page

• But in effect, only need

<dependencies> this/additional <dependency> "dependency" block <groupId> com.datastax.dse </groupId> <artifactId> dse-java-driver-core </artifactId> • Jar files pulled, by <version>1.6.7</version> </dependency> default, from an online </dependencies? Maven repository

• Also pulls whatever Jars

these Jars need, etc

• This repository can be

(should be) internal for

real/production apps

0000-DTSE-ClientProgramming-6240-DU-60-9 © DataStax, All Rights Reserved, Confidential

package com.datastax.enablement.bootcamp; An App.java that import com.datastax.driver.dse.DseCluster; import com.datastax.driver.dse.DseSession; accesses DSE import com.datastax.driver.core.Row; public class App { public static void main( String[] args ) { DseCluster my_cluster = null; try { my_cluster = DseCluster.builder() .addContactPoint("127.0.0.1") .build(); DseSession my_session = my_cluster.connect(); Row my_row = my_session.execute("select * from system.local").one(); System.out.println("DSE release version: " + my_row.getString("dse_version") ); } finally { if (my_cluster != null) my_cluster.close(); } } }

0000-DTSE-ClientProgramming-6240-DU-60-10 © DataStax, All Rights Reserved, Confidential

Next steps-

• Edit, compile, test, (repeat)

mvn package

mvn dependency:build-classpath -Dmdep.outputFile=cp.txt

java -cp target/my-app-1.0-SNAPSHOT.jar:`cat cp.txt`

com.datastax.enablement.bootcamp.App

0000-DTSE-ClientProgramming-6240-DU-60-11 © DataStax, All Rights Reserved, Confidential

Lessons Learned

0000-DTSE-ClientProgramming-6240-DU-60-12 © DataStax, All Rights Reserved, Confidential

0000-DTSE-ClientProgramming-6240-DU-60-13 © DataStax, All Rights Reserved, Confidential
