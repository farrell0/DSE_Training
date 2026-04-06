# DSE Analytics: DSE Analytics, Machine Learning

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><strong>DSE Analytics</strong></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Analytics curriculum and need help with dse analytics, machine learning. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Analytics track introduces the runtime model and practical usage patterns. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse analytics, machine learning.

## Downloads

- [PDF slides](./7602-dse-analytics-machine-learning.pdf)
- [Original PowerPoint](../000-DTSE-Analytics-7602-DU-60%2C%20DSE%20Analytics%2C%20Machine%20Learning.pptx)

## Converted Slides

## Discussion Unit:

• Define Machine Learning (ML)

• Overview MLlib/ML libraries Discussion Unit:

• ML process, design pattern/flow DSE Analytics

Machine Learning • Upsell, customers who bought (x)

bought (y)

• Predict customer churn

000-DTSE-Analytics-7602-60-DU-1 © DataStax, All Rights Reserved, Confidential

DSE Analytics; Business Intelligence

(BI), versus Machine Learning (ML),

Which is which

And (AI) Discussion Lab:

Matching pairs – Match the

attributes on the right with

the areas on the left

000-DTSE-Analytics-7602-60-DU-2 © DataStax, All Rights Reserved, Confidential

DSE Analytics: BI Shelf high/low, per product, per geo,

per season versus ML

Which paid search traffic brings the

most qualified registrants?

Will this customer churn ?

Which web page has the most first

time visitors?

What is the bounce rate on a given

page?

Should we issue this loan?

Online recommendations

Should we set price higher/lower ?

000-DTSE-Analytics-7602-60-DU-3 © DataStax, All Rights Reserved, Confidential

DSE Analytics: BI, ML, AI An algorithm whose accuracy

increases with the amount of data it

receives

Device that perceives its environment

and takes actions that maximize its

chance of successfully achieving its

goals

Frequent pattern matching

Historical, current and predictive

views of business operations

Statistics: begin with a statistical

population or a statistical model

process to be studied

000-DTSE-Analytics-7602-60-DU-4 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

000-DTSE-Analytics-7602-60-DU-5 © DataStax, All Rights Reserved, Confidential

DSE Analytics: 5 Major Functional Areas

DataFrames ML Pipelines

Spark Spark SQL Mllib/ML GraphX Streaming

Spark Core

Image Source: DataBricks.com

000-DTSE-Analytics-7602-60-DU-6 © DataStax, All Rights Reserved, Confidential

DSE Analytics: ML Use Cases-

• Spam Detection/Filtering

• Anomaly/Outlier Detection

• Credit Card Fraud Detection

• Voice Recognition

• Digit/character recognition

• Internet of Things

• Gaming Analytics

• Face Detection

• Product Recommendation

• Stock Trading

• Churn

000-DTSE-Analytics-7602-60-DU-7 © DataStax, All Rights Reserved, Confidential

DSE Analytics: ML Use Cases, Emerging-

• Privacy Preserving Data Mining

• Author Name Disambiguation

• Recommendation Systems

• Text Mining (e.g. plagiarism)

• Sentiment Analysis

• Speech Understanding

Why ? Application ?

000-DTSE-Analytics-7602-60-DU-8 © DataStax, All Rights Reserved, Confidential

DSE Analytics: ML Enablers-

Though machine learning has been around for a while, lately there has been a

surge in the need and use of machine learning

• Big data, creating a superabundance of data to analyze

• Ability for distributed systems like Spark to allow commodity computing

systems to work together, instead of legacy, pricier systems

• Changes in processing power, price of RAM, allow machines to crunch through

their algorithms in a reasonable amount of time

Starting with Spark 2.0, Machine Learning updated to utilize spark.ml/DataFrame

libraries instead of the spark.mllib/RDD based libraries

000-DTSE-Analytics-7602-60-DU-9 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Libraries, MLlib/RDD, ML/DataFrame

• Java, Scala, Python (Spark 0.9), R

(Spark 1.5)

• Fully Parallel/Performant

• Was RDD; Spark 2.0, in maint. mode

(now DF)

• Most examples still MLlib/RDD, not

ML/DF

• Main doc page Url on Notes Page

000-DTSE-Analytics-7602-60-DU-10 © DataStax, All Rights Reserved, Confidential

DSE Analytics: • Use known sample data to build a model,

Process training phase (batch)

• Apply model to achieve business goal,

scoring phase (streaming, live)

• Each ML routine can have a different model;

a single array of terms, a K/V array, other,

but always structured

• Data quality of the training dataset is key

• Data selection; often make assumptions on

data as you build your process, be sure to

note and go back to validate assumptions

later

• Data munging; preprocessing,

transformation

000-DTSE-Analytics-7602-60-DU-11 © DataStax, All Rights Reserved, Confidential

DSE Analytics: Process

Image Source: https://mapr.com/blog/churn-prediction-sparkml/

000-DTSE-Analytics-7602-60-DU-12 © DataStax, All Rights Reserved, Confidential

+ =?

• Training phase may be computationally

intensive (CI), or not DSE Analytics:

• Generally, a routine with CI training phase, Process has a relatively computationally efficient (CE)

scoring phase

[ ] ?

000-DTSE-Analytics-7602-60-DU-13 © DataStax, All Rights Reserved, Confidential

DSE Analytics:

MLLib/ML categories

Supervised; known/labeled columns • Case 1; Classification, Nominal values

(T|F, reptile|fish|amphib, ..) • Case 2: Regression, Infinite numeric values • Example case 1; frequency pattern

matching • Knn; (seminal use case/example, bird identification)

Unsupervised; unlabeled columns • Generate clusters of data • Often used for discovery, to gain discovery, find outliers

000-DTSE-Analytics-7602-60-DU-14 © DataStax, All Rights Reserved, Confidential

Sample: Supervised, Classification/Regression, Knn

• Attribution, graphing

• x, y, (z ?), .. input, "features"

• Real world; normally 70-90% overlapping

in first attempts

• Outliers, patterns, more

• Next step: add/remove columns

• Ask for more/fewer groups, "labels"

• Example; find relationship between

columns involved in churn- What should

you be looking for out of 100+ enterprise

database columns

000-DTSE-Analytics-7602-60-DU-15 © DataStax, All Rights Reserved, Confidential

Machine

Learning:

Upselling / Customers who

bought (x) also bought (y),

using the Apriori Algorithm

000-DTSE-Analytics-7602-60-DU-16 © DataStax, All Rights Reserved, Confidential

Machine Learning: Apriori Algorithm

Tx num Items sold

---------- ---------------------------------------- Item Set 0 soy milk , lettuce

1 lettuce, diapers , wine, chard

2 soy milk , diapers , wine, OJ

3 lettuce, soy milk , diapers , wine

4 lettuce, soy milk , diapers , OJ Item Set

Order Set

000-DTSE-Analytics-7602-60-DU-17 © DataStax, All Rights Reserved, Confidential

Apriori • Support : percentage of dataset that contains given item set.

Soy-milk/diapers is 3 (item set) /5 (dataset).

• Confidence : support (A/B) / support (A)

(diapers, soy-milk) / (diapers) == ( 3/5) / (4/5) == 75%

Low support ? We just don't have frequent data,

not a good candidate for this type of analysis ? Some similarity across, but Confidence, with good support, useful each ML routine may have

its own (vocabulary)

• A dataset with N items can generate 2 ^ N -1 (power of) possible item sets

2 ^ 100 -1 == 1267650600228229401496703205375

Items

• We need to prune/optimize

000-DTSE-Analytics-7602-60-DU-18 © DataStax, All Rights Reserved, Confidential

• How-

• Generate a list of all unique items (singles) Apriori • Generate a list of all unique (item pairs, and higher)

soy -> lettuce (tx 0)

soy -> diapers (tx 2)

soy -> diapers, wine (tx 2)

soy -> diapers, wine, OJ (tx 2)

...

Calculate support and confidence for each

• Apriori-

• If A/B is (in)frequent, then A/B/C, A/B/D, and A/B/C/D are also (in)frequent (so

discard them)

• Association rules: antecedent -> consequent

diapers -> chard (1/5 diapers-chard) / (4/5 diapers) = 25%

chard -> diapers (1/5 diapers-chard) / (1/5 chard) = 100%

Is it statistically significant

Created from 2 or more items

000-DTSE-Analytics-7602-60-DU-19 © DataStax, All Rights Reserved, Confidential

Working Goal:

From: Maury_Atwater To: DSE_HOTSHOT

Subject: Need this now !!!

We need to start upselling ! CSV file; 10k orders, 43k items sold, 170 unique items,

4.4 items per transaction.

We need a set of association rules to apply on the Web site ! Maury Atwater, President of Atwater's -MA

000-DTSE-Analytics-7544-60-DU-20 © DataStax, All Rights Reserved, Confidential

Apriori: New data set

000-DTSE-Analytics-7602-60-DU-21 © DataStax, All Rights Reserved, Confidential

Apriori: If you hand coded in Python, other

• All manual Python code,

809 lines

• Large data set, killed it after

1 hour

• Using Spark/Python

libraries, 54 lines of code

• Large data set, laptop/VM, 2

cores, 20 seconds

000-DTSE-Analytics-7602-60-DU-22 © DataStax, All Rights Reserved, Confidential

Coding the

Apriori

Customers who bought (x)

bought (y)

000-DTSE-Analytics-7602-60-DU-23 © DataStax, All Rights Reserved, Confidential

Apriori: In Python,

Pg 1 of 2

from pyspark.mllib.fpm import FPGrowth

from pyspark import SparkContext

sc = SparkContext()

l_datafile = sc.textFile("10_grocery.csv") What is the 0.01 here ? l_orders = l_datafile.map(lambda line: line.strip().split(','))

l_model = FPGrowth. train (l_orders, minSupport=0.01, numPartitions=1)

l_results = l_model. freqItemsets ().collect()

# l_results is of type: <class 'collections.FreqItemset'>

000-DTSE-Analytics-7602-60-DU-24 © DataStax, All Rights Reserved, Confidential

Apriori: In Python,

Pg 2 of 2

for l_result in l_results:

print str( l_result[0] ) + " " + str(float( l_result[1] ) / 100)

# From Spark,

# [u'whole milk'] 0.2513

# [u'other vegetables'] 0.1903

# [u'rolls/buns'] 0.1809 0 == (label) # 1 == (support) # From pure Python,

# frozenset(['whole milk']) 0.255516014235 Python currently: You have # frozenset(['other vegetables']) 0.193492628368 to calculate confidence and # frozenset(['rolls/buns']) 0.183934926284 association rules yourself.

Not awful, but ..

000-DTSE-Analytics-7602-60-DU-25 © DataStax, All Rights Reserved, Confidential

Apriori: In Scala, 1/6

package com.datastax.enablement.bootcamp

import org.apache.spark.{SparkConf, SparkContext}

import org.apache.spark.mllib.fpm.FPGrowth

import org.apache.spark.rdd.RDD

import org.apache.spark.mllib.fpm.AssociationRules

And others if you

expand scope

000-DTSE-Analytics-7602-60-DU-26 © DataStax, All Rights Reserved, Confidential

Apriori: In Scala, 2/6

object App {

Any ML yet ? def main(args: Array[String]) {

val sc = new SparkContext(new SparkConf().

setAppName("My App"))

val data = sc.textFile("file:///opt/dse_ml/10_grocery.csv")

val transactions : RDD[Array[String]] = data.

map(s => s.trim.split(','))

// Sample data lines from CSV

// citrus fruit,semi-finished bread,margarine,ready soups

// tropical fruit,yogurt,coffee

000-DTSE-Analytics-7602-60-DU-27 © DataStax, All Rights Reserved, Confidential

Apriori: In Scala, 3/6

val fpg = new FPGrowth() .setMinSupport(0.01).

setNumPartitions(1)

val model = fpg. run ( transactions )

Python was model. freqItemsets .collect().foreach { itemset => train() ? println(itemset. items .mkString("[", ",", "]") +

", " + itemset .freq)

}

// {canned vegetables}: 106 Data from println() // {pork}: 567

//

// 99 {curd,yogurt,whole milk} The actual high/low // 2513 {whole milk}

// class org.apache.spark.mllib.fpm.FPGrowth$FreqItemset;

000-DTSE-Analytics-7602-60-DU-28 © DataStax, All Rights Reserved, Confidential

Apriori: In Scala, 4/6

val minConfidence = 0.8

model. generateAssociationRules (minConfidence).

collect().foreach { rule =>

println(

rule. antecedent .mkString("[", ",", "]")

+ " => " + rule. consequent .mkString("[", ",", "]")

+ ", " + rule. confidence

)

}

Difference between this page and the next page ?

000-DTSE-Analytics-7602-60-DU-29 © DataStax, All Rights Reserved, Confidential

Apriori: In Scala, 5/6

println("")

println("")

val ar = new AssociationRules().setMinConfidence(0.1)

val results = ar.run(model.freqItemsets)

results.collect().foreach { rule =>

println("[" + rule.antecedent.mkString(",")

+ "=>"

+ rule.consequent.mkString(",") + "]," +

rule.confidence

)

}

000-DTSE-Analytics-7602-60-DU-30 © DataStax, All Rights Reserved, Confidential

Apriori: In Scala, 6/6

sc.stop()

sys.exit(0)

}

}

// High low,

// 0.10074626865671642 {root vegetables} => {pastry} // 0.10167910447761194 {root vegetables} => {margarine} // ... // 0.5845410628019324 {tropical fruit,root vegetables} => {other vegetables} // 0.5862068965517241 {citrus fruit,root vegetables} => {other vegetables} // // class org.apache.spark.mllib.fpm.AssociationRules$Rule

000-DTSE-Analytics-7602-60-DU-31 © DataStax, All Rights Reserved, Confidential

Apriori: Application

000-DTSE-Analytics-7602-60-DU-32 © DataStax, All Rights Reserved, Confidential

How would you

know this

• Url on Notes page

• And this example

000-DTSE-Analytics-7602-60-DU-33 © DataStax, All Rights Reserved, Confidential

How would

you know this

No Python TAB ?

000-DTSE-Analytics-7602-60-DU-34 © DataStax, All Rights Reserved, Confidential

Apriori: Summary

• order set, item set • FPGrowth.run() • support • FPGrowth.train() • confidence freqItemsets • association rules (0 == label, 1 == confidence) • antecedent, consequent freqItemsets.items • C1, candidate item set of freqItemsets.freq size 1 • AssociationRules.run() • C2, .. antecedent • L2, frequent item set consequent (scored, size 2) confidence

000-DTSE-Analytics-7602-60-DU-35 © DataStax, All Rights Reserved, Confidential

Machine

Learning:

Predicting Customer Churn

using Decision Tree

Classifier

000-DTSE-Analytics-7602-60-DU-36 © DataStax, All Rights Reserved, Confidential

Customer Churn/Attrition

Banks, telephone service companies, Internet

service providers, pay TV companies,

insurance firms, and alarm monitoring

services, often use customer attrition analysis

and customer attrition rates as one of their

key business metrics (along with cash flow,

EBITDA, etc.) because the cost of retaining

an existing customer is far less than acquiring

a new one.

Companies from these sectors often have

customer service branches which attempt to

win back defecting clients, ...

Reference Url:https://en.wikipedia.org/wiki/Customer_attrition

000-DTSE-Analytics-7602-60-DU-37 © DataStax, All Rights Reserved, Confidential

Churn: Data required

In order to understand the customer, a number of factors can be

analyzed, such as:

• Customer demographic data (age, marital status, etc.)

• Sentiment analysis of social media

• Customer usage patterns and geographical usage trends

• Calling-circle data

• Browsing behavior from clickstream logs

• Support call center statistics

• Historical data that show patterns of behavior that suggest churn

000-DTSE-Analytics-7602-60-DU-38 © DataStax, All Rights Reserved, Confidential

Churn Example: USA, Dish Network

• Customer/360 (Need the data)

• You rebooted your modem twice that morning DataStax • You accessed the pricing page on the Web site Internal Use • You queried "cancel service" on the Web page Only

• Now you're in the VRU/800-number

• Which of 30,000 CSRs do we route you to ?

000-DTSE-Analytics-7602-60-DU-39 © DataStax, All Rights Reserved, Confidential

Churn: Atwater's data CREATE TABLE orders

order_num

order_date

customer_num CREATE TABLE customer

customer_num ship_instruct

fname backlog

lname po_num

ship_date company

ship_weight address1

address2 ship_charge

city paid_date

CREATE TABLE items state

item_num zipcode

phone order_num

stock_num

manu_code

quantity

total_price

000-DTSE-Analytics-7602-60-DU-40 © DataStax, All Rights Reserved, Confidential

Churn

• Yearly contest, specifically 2009, focus was Churn

• "The challenge (was) to beat the in-house system developed by

Orange Labs." A.k.a, Orange Telecomm ( https://

www.orange.com/en/home)

• 3000+ real data rows (customer ID cleansed)

• 262 lines of Scala

• Will this customer churn ?

000-DTSE-Analytics-7602-60-DU-41 © DataStax, All Rights Reserved, Confidential

Churn: Data model, telecomm

State Total eve calls

Account length Total eve charge

Area code Total night minutes

International plan Total night calls

Voice mail plan Total night charge

Number vmail messages Total intl minutes

Total day minutes Total intl calls

Total day calls Total intl charge

Total day charge Customer service calls

Total eve minutes Churn (Did they churn (label): T|F)

LA,117,408,No,No,0,184.5,97,31.37,351.6,80,29.89,215.8,90,9.71,8.7,4,2.35,1,False

IN,65,415,No,No,0,129.1,137,21.95,228.5,83,19.42,208.8,111,9.4,12.7,6,3.43,4,True

000-DTSE-Analytics-7602-60-DU-42 © DataStax, All Rights Reserved, Confidential

Coding the

Decision Tree

Classifier

Will this customer churn ?

000-DTSE-Analytics-7602-60-DU-43 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 1 of 14

package com.datastax.enablement.bootcamp

import org.apache.spark.sql.SparkSession import org.apache.spark.sql.functions._ import org.apache.spark.sql.types._ import org.apache.spark.sql.Dataset import org.apache.spark.ml.Pipeline import org.apache.spark.ml.classification.DecisionTreeClassifier import org.apache.spark.ml.classification.DecisionTreeClassificationModel import org.apache.spark.mllib.evaluation.BinaryClassificationMetrics import org.apache.spark.ml.evaluation.BinaryClassificationEvaluator import org.apache.spark.ml.feature.StringIndexer import org.apache.spark.ml.tuning.ParamGridBuilder import org.apache.spark.ml.tuning.CrossValidator import org.apache.spark.ml.feature.VectorAssembler

000-DTSE-Analytics-7602-60-DU-44 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 2 of 14

object App {

tncalls: Double, case class Account tncharge: Double, ( timins: Double, state: String, ticalls: Double, len: Integer, ticharge: Double, acode: String, numcs: Double, intlplan: String, churn: String vplan: String, ) numvmail: Double, tdmins: Double, tdcalls: Double, tdcharge: Double, temins: Double, tecalls: Double, techarge: Double, tnmins: Double,

000-DTSE-Analytics-7602-60-DU-45 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 3 of 14

val schema = StructType(Array( StructField ("state", StringType, true), StructField("len", IntegerType, true), StructField("acode", StringType, true), StructField("intlplan", StringType, true), StructField("vplan", StringType, true), StructField("numvmail", DoubleType, true), StructField("tdmins", DoubleType, true), ... StructField("tncharge", DoubleType, true), StructField("timins", DoubleType, true), StructField("ticalls", DoubleType, true), StructField("ticharge", DoubleType, true), StructField("numcs", DoubleType, true), StructField("churn", StringType, true) ))

000-DTSE-Analytics-7602-60-DU-46 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 4 of 14 def main(args: Array[String]) {

val spark: SparkSession = SparkSession.builder(). appName("churn").getOrCreate()

import spark.implicits._

val train: Dataset[Account] = spark.read.option( "inferSchema", "false"). schema(schema).csv( "file:///opt/dse_ml/churn-bigml-80.csv"). as[Account] train.take(1) train.cache // println(train.count)

000-DTSE-Analytics-7602-60-DU-47 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 5 of 14

val test: Dataset[Account] = spark.read.option( "inferSchema", "false"). schema(schema).csv( "file:///opt/dse_ml/churn-bigml-20.csv"). as[Account] test.take(2) println(test.count) // test.cache

train.printSchema() train.show

train.createOrReplaceTempView("account") spark.catalog.cacheTable("account")

train.groupBy("churn").count.show

000-DTSE-Analytics-7602-60-DU-48 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 6 of 14

val fractions = Map("False" -> .17, "True" -> 1.0)

// Here we're keeping all instances of the Churn=True class, // but downsampling the Churn=False class to a fraction of 388/2278. val strain = train.stat.sampleBy("churn", fractions, 36L) // strain.groupBy("churn").count.show val ntrain = strain.drop("state").drop("acode"). drop("vplan").drop("tdcharge").drop("techarge") println(ntrain.count) ntrain.show

000-DTSE-Analytics-7602-60-DU-49 © DataStax, All Rights Reserved, Confidential

Description: Returns a stratified sample without replacement based on the fraction given on each stratum. Spark: sampleBy() Usage: sampleBy(x, col, fractions, seed)

// S4 method for signature 'SparkDataFrame,character,list,numeric' sampleBy(x, col, fractions, seed)

Arguments: x A SparkDataFrame col column that defines strata fractions A named list giving sampling fraction for each stratum. If a stratum is not specified, we treat its fraction as zero. seed random seed

Value: A new SparkDataFrame that represents the stratified sample

000-DTSE-Analytics-7602-60-DU-50 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 7 of 14

val ipindexer = new StringIndexer() . setInputCol("intlplan"). setOutputCol("iplanIndex") val labelindexer = new StringIndexer(). setInputCol("churn"). setOutputCol("label") val featureCols = Array("len", "iplanIndex", "numvmail", "tdmins", "tdcalls", "temins", "tecalls", "tnmins", "tncalls", "timins", "ticalls", "numcs")

val assembler = new VectorAssembler() . setInputCols(featureCols). setOutputCol("features")

val dTree = new DecisionTreeClassifier(). setLabelCol("label"). setFeaturesCol("features")

000-DTSE-Analytics-7602-60-DU-51 © DataStax, All Rights Reserved, Confidential

Spark: StringIndexer()

"The ML package needs data to be put in a (label: Double, features: Vector) DataFrame format with correspondingly named fields. We set up a pipeline to pass the data through 3 transformers in order to extract the features: 2 StringIndexers and a VectorAssembler. We use the StringIndexers to convert the String Categorial feature intlplan and label into number indices. Indexing categorical features allows decision trees to treat categorical features appropriately, improving performance.

000-DTSE-Analytics-7602-60-DU-52 © DataStax, All Rights Reserved, Confidential

Spark: VectorAssembler()

VectorAssembler is a transformer that combines a given list of columns into a single vector column. It is useful for combining raw features and features generated by different feature transformers into a single feature vector, in order to train ML models like logistic regression and decision trees. VectorAssembler accepts the following input column types: all numeric types, boolean type, and vector type. In each row, the values of the input columns will be concatenated into a vector in the specified order.

000-DTSE-Analytics-7602-60-DU-53 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 8 of 14

// Chain indexers and tree in a Pipeline. val pipeline = new Pipeline() . setStages(Array(ipindexer, labelindexer, assembler, dTree))

// Search through decision tree's maxDepth // parameter for best model val paramGrid = new ParamGridBuilder(). addGrid(dTree.maxDepth, Array(2, 3, 4, 5, 6, 7)).build()

val evaluator = new BinaryClassificationEvaluator(). setLabelCol("label"). setRawPredictionCol("prediction")

000-DTSE-Analytics-7602-60-DU-54 © DataStax, All Rights Reserved, Confidential

Spark: Pipeline()

The ML Pipelines is a High-Level API for MLlib that lives under the “spark.ml” package. A pipeline consists of a sequence of stages. There are two basic types of pipeline stages: Transformer and Estimator. A Transformer takes a dataset as input and produces an augmented dataset as output. E.g., a tokenizer is a Transformer that transforms a dataset with text into an dataset with tokenized words. An Estimator must be first fit on the input dataset to produce a model, which is a Transformer that transforms the input dataset. E.g., logistic regression is an Estimator that trains on a dataset with labels and features and produces a logistic regression model.

000-DTSE-Analytics-7602-60-DU-55 © DataStax, All Rights Reserved, Confidential

Spark: (Many)

• ParamGridBuilder() • BinaryClassificationBuilder() • CrossValidator()

000-DTSE-Analytics-7602-60-DU-56 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 9 of 14

// Set up 3-fold cross validation val crossval = new CrossValidator(). setEstimator(pipeline). setEvaluator(evaluator). setEstimatorParamMaps(paramGrid). setNumFolds(3)

val cvModel = crossval.fit(ntrain)

val bestModel = cvModel.bestModel println("The Best Model and Parameters:\n--------------------") println(bestModel.asInstanceOf[ org.apache.spark.ml.PipelineModel].stages(3)) // bestModel.asInstanceOf[org.apache.spark.ml.PipelineModel]. stages(3). extractParamMap

000-DTSE-Analytics-7602-60-DU-57 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 10 of 14

val treeModel = bestModel.asInstanceOf[ org.apache.spark.ml.PipelineModel]. stages(3).asInstanceOf[ DecisionTreeClassificationModel] println("Learned classification tree model:\n" + treeModel.toDebugString)

val predictions = cvModel.transform(test) val accuracy = evaluator.evaluate(predictions) evaluator.explainParams()

000-DTSE-Analytics-7602-60-DU-58 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 11 of 14

val predictionAndLabels = predictions.select( "prediction", "label"). rdd.map(x => (x(0).asInstanceOf[Double], x(1).asInstanceOf[Double])) val metrics = new BinaryClassificationMetrics(predictionAndLabels) println("area under the precision-recall curve: " + metrics.areaUnderPR) println("area under the receiver operating characteristic (ROC) curve : " + metrics.areaUnderROC)

println(metrics.fMeasureByThreshold())

val result = predictions.select("label", "prediction", "probability") result.show

000-DTSE-Analytics-7602-60-DU-59 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 12 of 14

val lp = predictions.select("label", "prediction") val counttotal = predictions.count() val correct = lp.filter($"label" === $"prediction").count() val wrong = lp.filter(not($"label" === $"prediction")).count() val ratioWrong = wrong.toDouble / counttotal.toDouble val ratioCorrect = correct.toDouble / counttotal.toDouble val truep = lp.filter($"prediction" === 0.0).filter( $"label" === $"prediction").count() / counttotal.toDouble val truen = lp.filter($"prediction" === 1.0).filter( $"label" === $"prediction").count() / counttotal.toDouble val falsep = lp.filter($"prediction" === 1.0).filter(not( $"label" === $"prediction")).count() / counttotal.toDouble val falsen = lp.filter($"prediction" === 0.0).filter(not( $"label" === $"prediction")).count() / counttotal.toDouble

000-DTSE-Analytics-7602-60-DU-60 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 13 of 14

println("counttotal : " + counttotal) println("correct : " + correct) println("wrong: " + wrong) println("ratio wrong: " + ratioWrong) println("ratio correct: " + ratioCorrect) println("ratio true positive : " + truep) println("ratio false positive : " + falsep) println("ratio true negative : " + truen) println("ratio false negative : " + falsen)

println("wrong: " + wrong)

000-DTSE-Analytics-7602-60-DU-61 © DataStax, All Rights Reserved, Confidential

Churn: In Scala 14 of 14

val equalp = predictions.selectExpr( "double(round(prediction)) as prediction", "label", """CASE double(round(prediction)) = label WHEN true then 1 ELSE 0 END as equal""" )

equalp.show

spark.stop() sys.exit(0)

}

}

000-DTSE-Analytics-7602-60-DU-62 © DataStax, All Rights Reserved, Confidential

Churn, Decision Tree:

Select Output- The Best Model and Parameters: -------------------- DecisionTreeClassificationModel (uid=dtc_d2da400284df) of depth 5 with 53 nodes Learned classification tree model: DecisionTreeClassificationModel (uid=dtc_d2da400284df) of depth 5 with 53 nodes If (feature 11 <= 3.0) If (feature 3 <= 222.4) If (feature 1 in {1.0}) If (feature 9 <= 13.1) If (feature 10 <= 2.0) Predict: 0.0 Else (feature 10 > 2.0) Predict: 1.0 Else (feature 9 > 13.1) Predict: 0.0 Else (feature 1 not in {1.0})

000-DTSE-Analytics-7602-60-DU-63 © DataStax, All Rights Reserved, Confidential

Churn, Decision Tree:

Select Output-

counttotal : 667 correct : 574 wrong: 93 ratio wrong: 0.13943028485757122 ratio correct: 0.8605697151424287 ratio true positive : 0.1184407796101949 ratio false positive : 0.0239880059970015 ratio true negative : 0.7421289355322339 ratio false negative : 0.11544227886056972

000-DTSE-Analytics-7602-60-DU-64 © DataStax, All Rights Reserved, Confidential

Churn, Decision Tree:

Select Output-

area under the precision-recall curve: 0.9747578698231796 area under the receiver operating characteristic (ROC) curve :

0.8484817813765183 MapPartitionsRDD[1233] at map at BinaryClassificationMetrics.scala:214 +-----+----------+--------------------+ |label|prediction| probability| +-----+----------+--------------------+ | 1.0| 1.0|[0.10676156583629...| | 0.0| 0.0|[0.91666666666666...| | 0.0| 0.0| [1.0,0.0]| | 1.0| 1.0|[0.10676156583629...| | 1.0| 1.0|[0.10676156583629...| | 1.0| 1.0| [0.1,0.9]| | 1.0| 1.0|[0.27027027027027...| ...

000-DTSE-Analytics-7602-60-DU-65 © DataStax, All Rights Reserved, Confidential

How would you

know this

• Url on Notes page

• And this example

000-DTSE-Analytics-7602-60-DU-66 © DataStax, All Rights Reserved, Confidential

End of Unit:

000-DTSE-Analytics-7602-60-DU-67 © DataStax, All Rights Reserved, Confidential

Additional Detail:

000-DTSE-Analytics-7602-60-DU-68 © DataStax, All Rights Reserved, Confidential

Machine Learning: A

Must Read ?

• Older, Amazon

• Python

• Most examples also coded by

hand; great for deep

understanding

• Yes, Apriori

• No, Decision Tree Classifier

000-DTSE-Analytics-7602-60-DU-69 © DataStax, All Rights Reserved, Confidential

Machine Learning: A

Must Read ?

• Amazon

• Python, Scala

• Newer

• Complete , if you already have

some sense of the material

• No, Apriori

• No, Decision Tree Classifier

• Yes, others

• Yes, basics like pipelining

000-DTSE-Analytics-7602-60-DU-70 © DataStax, All Rights Reserved, Confidential

Apriori Algorithm: Source

Spark-ML overview-

Parallel compute engine, storage in DataStax Based on simple math (algebra, some calculus, some set operands) DataFrames (typed RDDs), and better parallelism to routines Rakesh Agrawal, MIT/Purdue Machine learning: an algorithm that provides better results given more data

Apriori algorithm- Used for recommendation engines (customer who bought x also ..) 1994, Latin ‘ from before ’ ..

Ramakrishnan Srikant, UW-Madison, Google Fellow

000-DTSE-Analytics-7602-60-DU-71 © DataStax, All Rights Reserved, Confidential

Apriori

You put this in

your shopping

cart, then ..

Apriori

And after you

chose a washer

in stock,

16 straight

washers, no

other options
