# DSE Analytics: Scala REPL to Scala program

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with scala repl to scala program. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around scala repl to scala program.

## Downloads

- [PDF slides](./7548-scala-repl-to-scala-program.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7548-DU-60%2C%20Scala%20REPL%20to%20Scala%20program.pptx)

## Converted Slides

## Discussion Unit:

Migrate a set of DSE Analytics REPL

statements, to a (true) Scala program

• Command line first, then IDE;

(Discussion Unit/Exercise 7556/7557) DSE Analytics Scala

REPL statements

• Software versions migrated to program

• Install Scala, Maven

• Generate a pom.xml, change

• Generate an App.scala, change

• Submit as Spark job

• This Discussion Unit is dependent on

Discussion Unit 7544/7545.

000-DTSE-Analytics-7458-DU-60-1 © DataStax, All Rights Reserved, Confidential

DSE

Java Driver

Discussion Lab:

Matching pairs – Match the

attributes on the right with the

DSE areas on the left Spark Cassandra

Connector

000-DTSE-Analytics-7458-DU-60-2 © DataStax, All Rights Reserved, Confidential

Discussion Lab: Attributes

REPL

Faster to develop (True)

Program Deploy to production

More memory (laptop ?)

Less memory (laptop ?)

Client uses different IDE

Access to client network Command

Line DSE Spark client

DSE Java client IDE

000-DTSE-Analytics-7458-DU-60-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7458-DU-60-4 © DataStax, All Rights Reserved, Confidential

[ What ] is interacting There are JDBC, ODBC, Parquet, (other)

connectors built into Spark, but there is not a with DSE ? (Cassandra) one

Java, Java Driver DataStax provides 2 drivers that work

interactively DSE • DSE Java Driver (See Discussion Unit,

6244/6245) (not Spark)

• Spark Cassandra Connector (Spark)

-- Open source, AND enterprise license DSE Spark Cassandra features Connector DSE -- Spark objects, activities

Spark These allow you to connect to DSE directly from

Spark, like using a JDBC driver, more

000-DTSE-Analytics-7548-60-DU-5 © DataStax, All Rights Reserved, Confidential

Versions:

They

Matter

DSE 6.0, 6.0.1

Java 8

Spark 2.2.1.2

Scala 2.11, 2.12

000-DTSE-Analytics-7458-DU-60-6 © DataStax, All Rights Reserved, Confidential

Installing Scala:

Can already run Spark Scala via REPL,

dse spark

Or, installing Scala,

Check for Java JDK 1.8

javac -version

Then,

wget http://downloads.typesafe.com/scala/2.11.8/scala-2.11.8.rpm

yum install *.rpm

000-DTSE-Analytics-7458-DU-60-7 © DataStax, All Rights Reserved, Confidential

Apache Maven: What is it ?

Apache Maven is "build automation

software". Think yum(C), or apt-get(C),

(iTunes), but for Java programs.

-- Will create your project filesystem

structure, compile, deploy, other.

-- Will find, download, version, and

manage all of your Java/Scala

dependencies.

-- And, do all of this in about 4

total commands.

-- Supports Java, Scala, Ruby, C/C++

others

000-DTSE-Studio-6240-DU-60-8 © DataStax, All Rights Reserved, Confidential

Apache Maven: How to install

• Already installed ? "mvn --version"

• If not, Tar ball; unzip, place in PATH

-- https://maven.apache.org/download.cgi

-- https://maven.apache.org/install.html

-- Version 3.5.4, 8MB in size

-- Is a Java app, requires Java 8 (v 3.5.4)

Run all commands in -- mvn --version this unit inside a Linux terminal window.

000-DTSE-Studio-6240-DU-60-9 © DataStax, All Rights Reserved, Confidential

Previously (6244/6245) when using Java-

Will be the Java Package name (as • cd /opt (cd anywhere) generated)

• mvn archetype:generate \

-DgroupId= com.datastax.enablement.bootcamp \

-DartifactId= my-app \

-Dversion=1.0 \

-DinteractiveMode=false \

-DarchetypeArtifactId= maven-archetype-quickstart Project name (logical only)

Specific to Java

000-DTSE-Analytics-7458-DU-60-10 © DataStax, All Rights Reserved, Confidential

When using Scala- • cd /opt (cd anywhere)

• mvn archetype:generate \

-DgroupId=com.datastax.enablement.bootcamp \

-DartifactId=my-app \ Different, calling for a -Dversion=1.0 \ Scala project -DinteractiveMode=false \

-DarchetypeArtifactId= scala-archetype-simple \ Specific to Scala

-DarchetypeGroupId=org.scala-tools.archetypes \

-DremoteRepositories=http://scala-tools.org/repo-releases

• cd my-app

rm -r ./src/test/scala/samples/*

Generated tests: Will error on compile unless corrected

000-DTSE-Analytics-7458-DU-60-11 © DataStax, All Rights Reserved, Confidential

mvn generate: What just happened ?

-DgroupId= com.datastax.enablement.bootcamp

scala

App.scala

000-DTSE-ClientProgramming-6240-DU-60-12 © DataStax, All Rights Reserved, Confidential

What is a pom.xml ?

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchem a-instance" • xml xsi:schemaLocation="http://maven.apache.or • "project object model" g/POM/4.0.0 http://maven.apache.org/maven- • Each project has one v4_0_0.xsd"> <modelVersion>4.0.0</modelVersion>

• Tells Maven how to compile, <groupId>com.datastax.enablement.bootcamp< etc, your project /groupId> <artifactId>my-app</artifactId> <version>1.0</version> • Edit once and done ? <name>${project.artifactId}</name> <description>My wonderfull scala

... (Lines deleted)

000-DTSE-ClientProgramming-6240-DU-60-13 © DataStax, All Rights Reserved, Confidential

What's in App.scala ?

package com.datastax.enablement.bootcamp

/** * @author ${user.name} • Stub */ • It runs (it's Hello World) object App {

def foo(x : Array[String]) = • Add DSE client code; x.foldLeft("")((a,b) => a + b) structure

def main(args : Array[String]) { println( "Hello World!" ) println("concat arguments = " + foo(args)) }

}

000-DTSE-ClientProgramming-6240-DU-60-14 © DataStax, All Rights Reserved, Confidential

Did Maven know about DSE/Spark ?

• No. (And versions.)

• Get a correct pom

from DataStax

• Url on Notes page

000-DTSE-Analytics-7458-DU-60-15 © DataStax, All Rights Reserved, Confidential

To compile and run a Java (Scala, kind of) program-

• From the "project directory"

cd /opt/my-app -DgroupId= com.datastax.enablement.bootcamp

-DartifactId= my-app • # compiles

mvn package

• # generates the Java CLASSPATH

mvn dependency:build-classpath -Dmdep.outputFile=cp.txt

Left single • # call to run the program (one line below) apostrophes

java -cp target/my-app-1.0.jar :`cat cp.txt`

com.datastax.enablement.bootcamp.App

000-DTSE-ClientProgramming-6240-DU-60-16 © DataStax, All Rights Reserved, Confidential

The better sequence for DSE/Spark/Scala: Next steps

• Edit, compile, test, (repeat)

From the parent directory of the project; from ( ./my-app/ )

mvn package

dse spark-submit --class \

com.datastax.enablement.bootcamp.App target/my-app-1.0.jar

New/odd Jars ? Put them in the pom.xml

000-DTSE-ClientProgramming-6240-DU-60-17 © DataStax, All Rights Reserved, Confidential

• For brevity, this example does not

display the two additional/derived

columns.

• End to end example; imports, DSE DSE Spark Scala: Analytics (Spark) Session object,

other

Example, end to end

000-DTSE-Analytics-7458-DU-60-18 © DataStax, All Rights Reserved, Confidential

// Run this CQLSH block first, before running this program. // // DROP KEYSPACE IF EXISTS ks_7545; Just customer: // CREATE KEYSPACE ks_7545 WITH REPLICATION = // {'class': 'SimpleStrategy', end to end // 'replication_factor': 1}; // USE ks_7545; example- // // CREATE TABLE customer_plus_derived // ( // customer_num INT PRIMARY KEY, // fname TEXT, // ... lines deleted // phone TEXT, // company_upshift TEXT, // This column not in CSV input file // ew_flag TEXT // This column not in CSV input file // );

000-DTSE-Analytics-7458-DU-60-19 © DataStax, All Rights Reserved, Confidential

Just customer:

end to end

package com.datastax.enablement.bootcamp example-

import com.datastax.spark.connector._ // import com.datastax.spark.connector.cql.CassandraConnector // import org.apache.spark.sql.{SaveMode, SparkSession} import org.apache.spark.sql.cassandra._ // import org.apache.spark.sql.types._

000-DTSE-Analytics-7458-DU-60-20 © DataStax, All Rights Reserved, Confidential

Just customer: end

to end example-

object App {

// If this case class is not outside the main, // we can get a compiler error, case class My_Record ( customer_num : Int, fname : String, lname : String, company : String, address1 : String, address2 : String, city : String, state : String, zipcode : String, phone : String )

000-DTSE-Analytics-7458-DU-60-21 © DataStax, All Rights Reserved, Confidential

Just customer:

end to end def main(args : Array[String]) {

example- val spark = SparkSession.builder .appName("My App") .getOrCreate() val sc = spark.sparkContext

// You will need this line eventually // // import spark.implicits._

// ------------------------------

000-DTSE-Analytics-7458-DU-60-22 © DataStax, All Rights Reserved, Confidential

Just customer:

end to end

example-

// Reading from a DSE table // // val rows10 = spark.sparkContext.cassandraTable( // "system", "local").select("dse_version")

val rows10 = sc.cassandraTable("system", "local"). select("dse_version")

rows10.collect().foreach(println) println()

// ------------------------------

000-DTSE-Analytics-7458-DU-60-23 © DataStax, All Rights Reserved, Confidential

// Reading a CSV, but as a text file; List of Strings // val rows20 = sc.textFile("file:///opt/stores_db/customer.csv") rows20.collect().foreach(println) Just println()

customer: // split returns an array // end to end val rows21 = rows20.map ( line => line.split (","))

example- // map the array elements (by position) into our record // val rows22 = rows21.map ( p => My_Record ( p(0).toInt, p(1).toString, p(2).toString, p(3).toString, p(4).toString, p(5).toString, p(6).toString, p(7).toString, p(8).toString, p(9).toString )) rows22.collect().foreach(println) println()

000-DTSE-Analytics-7458-DU-60-24 © DataStax, All Rights Reserved, Confidential

Just customer:

end to end

example-

rows22.saveToCassandra("ks_7545", "customer", SomeColumns( "customer_num" , "fname", "lname" , "company" , "address1" , "address2" , "city" , "state" , "zipcode" , "phone" ))

// ------------------------------

000-DTSE-Analytics-7458-DU-60-25 © DataStax, All Rights Reserved, Confidential

// The above is subject to error; positional array reading // // Reading directly into a StructType; can't use a case class // with the read.schema below- // Just val My_Schema = StructType(Array( StructField("customer_num" , IntType, true), customer: StructField("fname" , StringType, true), StructField("lname" , StringType, true), end to end StructField("company" , StringType, true), StructField("address1" , StringType, true), example- StructField("address2" , StringType, true), StructField("city" , StringType, true), StructField("state" , StringType, true), StructField("zipcode" , StringType, true), StructField("phone" , StringType, true) ))

000-DTSE-Analytics-7458-DU-60-26 © DataStax, All Rights Reserved, Confidential

// Reading the CSV into a StructType actually returns a DataFrame // // . Reading a CSV requires a schema (which gets us into DataFrame // territory) // . That is cheating at this point // // . Reading as a text file, and parsing this string with confidence // is a lot of code we want to avoid. // val rows30 = spark.read.schema(My_Schema).csv( Just customer: "file:///opt/stores_db/customer.csv")

end to end // Convert the DataFrame to RDD // example- val rows31 = rows30.rdd rows31.collect().foreach(println) println()

000-DTSE-Analytics-7458-DU-60-27 © DataStax, All Rights Reserved, Confidential

Just customer:

end to end // ks_7545.customer must exist // example- rows31.saveToCassandra("ks_7545", "customer", SomeColumns( "customer_num" , "fname", "lname" , "company" , "address1" , "address2" , "city" , "state" , "zipcode" , "phone" ))

// ------------------------------

// We need these lines in order to terminate the program // spark.stop() sys.exit(0)

} }

000-DTSE-Analytics-7458-DU-60-28 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7458-DU-60-29 © DataStax, All Rights Reserved, Confidential

Additional Detail:

000-DTSE-Analytics-7458-DU-60-30 © DataStax, All Rights Reserved, Confidential

DSE Java Driver-

On top of the open source driver sits the DSE Driver-

• Specific extensions for DSE

-- Authenticator implementations that use the authentication

scheme negotiation in the server-side DseAuthenticator

-- Value classes for geospatial types, and type codecs that

integrate them seamlessly

-- Continuous Paging

-- DSE graph integration

-- https://github.com/datastax/java-dse-driver

• Only allowed to use if you have a valid DSE License

000-DTSE-Analytics-7548-60-DU-31 © DataStax, All Rights Reserved, Confidential

DSE Spark (Cassandra) Connector-

• Exposes (Cassandra) tables as Spark RDDs, DataFrames, Datasets

• Read, write, and more

• Execute arbitrary CQL queries in your Spark applications

• Used with the Cassandra Java Driver

• Open Source Apache 2.0 license

• DataStax Github Repository, https://

github.com/datastax/spark-cassandra-connector

Use cases:

• Streaming data into DSE

• Analyzing the data in place

• Migrating from bad data model

000-DTSE-Analytics-7548-60-DU-32 © DataStax, All Rights Reserved, Confidential
