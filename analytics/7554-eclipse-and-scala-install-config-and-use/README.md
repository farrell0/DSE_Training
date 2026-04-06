# DSE Analytics: Eclipse and Scala, Install, config and use

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Analytics curriculum and need help with eclipse and scala, install, config and use. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Analytics track explains the installation and configuration workflow. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around eclipse and scala, install, config and use.

## Downloads

- [PDF slides](./7554-eclipse-and-scala-install-config-and-use.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7554-PL-60%2C%20Eclipse%20and%20Scala%2C%20Install%2C%20config%20and%20use.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab has as a prerequisite, Practice

Lab 6241, where we install and configure Eclipse

Photon on MacOS including a Scala plugin.

• This Practice Lab also has a prerequisite, Practice Lab: Discussion Units 7544/7545 and 7548/7549, where

we make the DSE Analytics client we run here.

Edit and Compile using

• In this Practice Lab, we edit, compile, and run a Eclipse with Scala DSE Analytics client program. As such, this lab

expects an operating DSE cluster with DSE

Analytics be accessible.

• Instructions in this practice lab are written for

MacOS, but should function for most Linux distros.

• This Practice Lab will require reasonable Internet

access.

000-DTSE-Analytics-7554-PL-60-1 © DataStax, All Rights Reserved, Confidential

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

000-DTSE-Analytics-7554-PL-60-2 © DataStax, All Rights Reserved, Confidential

Eclipse: How to Install

• Reference Practice Lab 6241, where

we installed Eclipse, and an Eclipse

plugin specific to Scala.

• Launch Eclipse, and then ..

Instructions in Practice Lab 6241.

000-DTSE-Analytics-7554-PL-60-3 © DataStax, All Rights Reserved, Confidential

After Practice

Lab 6241-

• Configured for DSE

Java clients

• Eclipse Scala plugin

installed

000-DTSE-Analytics-7554-PL-60-4 © DataStax, All Rights Reserved, Confidential

From the Eclipse

Menu Bar-

• File -> New -> Other

000-DTSE-Analytics-7554-PL-60-5 © DataStax, All Rights Reserved, Confidential

Don't use this-

• Simple Scala programs only

• Not a Maven project, no

pom.xml

• Better off using the DSE Spark

REPL

000-DTSE-Analytics-7554-PL-60-6 © DataStax, All Rights Reserved, Confidential

In the, Select a wizard,

modal dialog box

• Maven -> Maven Project

• This option gives us support for a

pom.xml, which will automatically

pull all of our (DSE and Spark)

dependencies

000-DTSE-Analytics-7554-PL-60-7 © DataStax, All Rights Reserved, Confidential

Just click through

this dialog box-

• There's nothing we need

on this dialog box-

• Click, Next

000-DTSE-Analytics-7554-PL-60-8 © DataStax, All Rights Reserved, Confidential

Maven Archetypes

• Maven Archetypes, a project

templating device; filesystem

structure, other

• The default is the same we used in

Discussion Unit 6240, the default

Java client archetype

• We want Scala

• Click, Configure

000-DTSE-Analytics-7554-PL-60-9 © DataStax, All Rights Reserved, Confidential

Online (Remote) Maven Archetype Repository

• Enter the value as shown

in the text entry field titled,

Catalog File

• Optionally Click, Verify

• And Click, OK

000-DTSE-Analytics-7554-PL-60-10 © DataStax, All Rights Reserved, Confidential

Archetype

Catalog added-

• After the addition of our

Archetype Catalog,

Click, Apply and Close

000-DTSE-Analytics-7554-PL-60-11 © DataStax, All Rights Reserved, Confidential

Picking a given

Archetype

• Manage the display as

shown on the right-

• Specifically enter a Filter

of, scala-archetype-

simple, to reduce the

number of options

• When your dialog box

matches that as shown,

Click, Next

000-DTSE-Analytics-7554-PL-60-12 © DataStax, All Rights Reserved, Confidential

The Project

Proper-

• Enter a GroupId,

ArtifactId, and

Version as shown

• Click, Finish

000-DTSE-Analytics-7554-PL-60-13 © DataStax, All Rights Reserved, Confidential

As generated, a

number of things

are broken-

• We'll fix these; not here

000-DTSE-Analytics-7554-PL-60-14 © DataStax, All Rights Reserved, Confidential

Delete the generated/stub,

test code

• In the Project Explorer view, navigate

to, my-app/scala -> src/test/scala ->

samples

• Shift-Click all entries, Right-Click, and

Delete

• These are stub test units and do not

compile

000-DTSE-Analytics-7554-PL-60-15 © DataStax, All Rights Reserved, Confidential

Setting Java Compiler version to 1.8-

000-DTSE-Analytics-7554-PL-60-16 © DataStax, All Rights Reserved, Confidential

Maven knows, Eclipse

doesn't know

• While Maven knows we want a Scala

project, Eclipse does not

• In the Project Explorer view, Right-

Click the project, and select;

Configure -> Add Scala Nature

000-DTSE-Analytics-7554-PL-60-17 © DataStax, All Rights Reserved, Confidential

Fix the pom.xml-

• Edit the pom.xml file as

detailed on the Notes

page.

• Save

• From the Menu Bar;

Project -> Clean

• (Clean can take a bit of

time.)

000-DTSE-Analytics-7554-PL-60-18 © DataStax, All Rights Reserved, Confidential

What is a pom.xml ? <project xmlns="http://maven.apache.or ... xsi:schemaLocation="http://mav ... <modelVersion>4.0.0</modelVersion>

<groupId>com.datastax.enablement.bootcamp< • xml /groupId> • "project object model" <artifactId>my-app</artifactId> • Each project has one <packaging>jar</packaging> <version>1.0-SNAPSHOT</version> <name>my-app</name> • Tells Maven how to compile, <url>http://maven.apache.org</url> etc, your project <dependencies> <dependency> <groupId>junit</groupId> • Edit once and done ? <artifactId>junit</artifactId> <version>3.8.1</version> <scope>test</scope> </dependency> </dependencies> </project>

000-DTSE-Analytics-7554-PL-60-19 © DataStax, All Rights Reserved, Confidential

Run the generated

App.scala

• Time for a test-

• In the Project Explorer view, find

and open (Double-Click)

App.scala

• From the Eclipse Toolbar, click

the Run icon (Run is context

sensitive, and App.scala must be

current.)

• Successful output as shown in

the Console view

000-DTSE-Analytics-7554-PL-60-20 © DataStax, All Rights Reserved, Confidential

That was the default generated App.scala-

• From Discussion Unit

7548/7549, and 7554, grab the

very same pom.xml, and

App.scala you created and ran

there.

• Copy and paste the above files

into the same pom.xml and

App.scala you just generated

and ran. Be certain to Save.

• Do a, Project -> Clean, and Run

000-DTSE-Analytics-7554-PL-60-21 © DataStax, All Rights Reserved, Confidential

You are done when-

000-DTSE-Analytics-7554-PL-60-22 © DataStax, All Rights Reserved, Confidential

Lessons Learned

000-DTSE-Analytics-7554-PL-60-23 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7554-PL-60-24 © DataStax, All Rights Reserved, Confidential

Additional Detail:

000-DTSE-Analytics-7554-PL-60-25 © DataStax, All Rights Reserved, Confidential

More Help

Finding

Archetypes:

The Notes page lists a Url

to a StackOverflow article

on finding Maven Scala

archetypes-

000-DTSE-Analytics-7554-PL-60-26 © DataStax, All Rights Reserved, Confidential

Eclipse Sluggish ?

• Eclipse is a Java app

• Tune the JVM settings

as shown; specifically

Xmx

• 1G default is common,

4G if you have room

• Url on Notes page

000-DTSE-Analytics-7554-PL-60-27 © DataStax, All Rights Reserved, Confidential
