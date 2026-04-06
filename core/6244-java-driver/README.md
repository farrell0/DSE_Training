# DSE Core: Java Driver

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Core curriculum and need help with java driver. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Core track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around java driver.

## Downloads

- [PDF slides](./6244-java-driver.pdf)
- [Original PowerPoint](../000-DTSE-ClientProgramming-6244-DU-60%2C%20Java%20Driver.pptx)

## Converted Slides

## Discussion Unit:

Introduce the DSE Java Driver, a Primer

• Compile and run a DSE Java client Discussion Unit: • Introduce some of the capabilities of the

driver DSE Java Driver; Use,

Key Concepts • Load balancing policies

• Failures: Retry, Reconnect

• Using Connections, Sessions,

Statements, (other) ...

• This Discussion Unit gives focus to

programming against DSE Core

0000-DTSE-Core-6244-DU-60-1 © DataStax, All Rights Reserved, Confidential

Discussion Lab:

Matching pairs – Match the

attributes on the right with the DSE areas on the left Java Driver

0000-DTSE-Core-6244-DU-60-2 © DataStax, All Rights Reserved, Confidential

Discussion Lab: Attributes Declarative

Fluent

JDBC (JCA compliant)

Asynchronous

Fault Tolerant

Connection Pools

DSE Query Builder Java Driver

Transactions

0000-DTSE-Core-6244-DU-60-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

0000-DTSE-Core-6244-DU-60-4 © DataStax, All Rights Reserved, Confidential

[ All ] DSE Client Side Drivers-

Consistent set of features across languages

• Asynchronous execution

• Automatic cluster mapping

• Connection pools, auto reconnect

• Load balancing

• Fault tolerant

Consistent terminology

DseCluster -> DseSession -> (Statement) -> ResultSet (or) Future

(The above displays the very simplest path.)

0000-DTSE-Core-6244-DU-60-5 © DataStax, All Rights Reserved, Confidential

DSE Java Driver-

• Connect to DSE cluster DseCluster my_cluster = null;

• Similar to JDBC/SQL my_cluster = DseCluster.builder()

• Not JCA compliant . addContactPoint ("127.0.0.1")

. build ();

DseSession my_session = my_cluster. connect() ;

Row my_row = my_session. execute(

"select * from system.local"). one() ;

int col1 = my_row.getInt("col2")

0000-DTSE-Core-6244-DU-60-6 © DataStax, All Rights Reserved, Confidential

DSA 420 Java Programming: 2 Days

Part 1- The Driver

• Base cluster object

• Configuration options

Part 2- Execution

• Executing CQL

• Statements, how/when

Part 3- Annotations, Mapping

• Simple object mapping

• JPA like interface

Part 4- (Other)

• Time series

• Tombstones

• Transactions

0000-DTSE-Core-6244-DU-60-7 © DataStax, All Rights Reserved, Confidential

DSE Java Driver: DseCluster object

1:m 1:m 1:m 1:m Connection Request Pool Cluster Session

(optional)

• Load balancing

• Failover

• Connection pooling

• (other)

0000-DTSE-Core-6244-DU-60-8 © DataStax, All Rights Reserved, Confidential

DseCluster.builder: Fluent Interface

DseCluster my_cluster = DseCluster.builder()

.addContactPoints("127.0.0.1", ..

.withLoadBalancingPolicy( ... )

.withRetryPolicy( ... )

.withReconnectPolicy( ... ) These will default out

.withPoolingOptions( ... )

.withQueryOptions( ... )

.build()

0000-DTSE-Core-6244-DU-60-9 © DataStax, All Rights Reserved, Confidential

Load Balancers-

• Used to choose a coordinator

• Maintains pulse on node up/down/other state

• (Downed nodes excluded from query plans)

• Chainable, nestable (just like DSE Search analyzers)

• Default,

new TokenAwarePolicy(new DCAwareRoundRobinPolicy("local-dc-name") )

0000-DTSE-Core-6244-DU-60-10 © DataStax, All Rights Reserved, Confidential

Load Balancers-

Non-chainable policies (inner policies)-

• DCAwareRoundRobinPolicy (optional DC)

• RoundRobinPolicy

Chainable policies (outer policies)-

• TokenAwarePolicy

• LatencyAwarePolicy (define acceptable latencies)

• WhiteListPolicy

• HostFilterPolicy (super of WhiteListPolicy)

0000-DTSE-Core-6244-DU-60-11 © DataStax, All Rights Reserved, Confidential

DseCluster my_cluster = DseCluster.builder() Load Balancer, .withLoadBalancingPolicy(tokenAware)

.build() Examples-

DseCluster my_cluster.DseCluster.builder()

.addContactPoints("127.0.0.1", ..

.withLoadBalancingPolicy(whiteListPolicy(["127.0.0.1", .. ]))

.build();

LatencyAwarePolicy my_lap = LatencyAwarePolicy.builder(

new RoundRobinPolicy())

.withMinimum.Measurements(5)

.build()

DseCluster my_cluster = DseCluster.builder()

.withLoadBalancingPolicy(my_lap)

.build()

0000-DTSE-Core-6244-DU-60-12 © DataStax, All Rights Reserved, Confidential

Failover and Recovery; Retry, Reconnection Policies

Retry

• onReadTimeout(), onWriteTimeout(), onUnavailable()

• Whether a retry is made, what the consistency level should be

• Available policies

-- DefaultRetryPolicy

-- DowngradingConsistencyRetryPolicy

-- FallthroughRetryPolicy

-- LoggingRetryPolicy

0000-DTSE-Core-6244-DU-60-13 © DataStax, All Rights Reserved, Confidential

Failover and Recovery; Retry, Reconnection Policies

ConstantReconnectionPolicy

Constant/configurable time between each attempt

ExponentialReconnectionPolicy

Wait exponentially longer between each attempt

(up to configurable max)

0000-DTSE-Core-6244-DU-60-14 © DataStax, All Rights Reserved, Confidential

Control Host-

At driver level, special connection to single node

• Any node, will change if current goes down

• Host sends notice of; schema change, token

assignment, node health, other

Push Notifications

Driver can receive distinct notice of a node changing to

UP, other

0000-DTSE-Core-6244-DU-60-15 © DataStax, All Rights Reserved, Confidential

(Connection) Pooling-

DseCluster my_cluster = DseCluster.builder()

.addContactPoints( ... )

.withPoolingOptions(new PoolingOptions)

. setConnectionsPerHost (HostDistance.LOCAL, 1, 4)

. setMaxRequestsPerConnection (HostDistance.LOCAL, 800)

. setNewConnectionThreshold (HostDistance.LOCAL, 100))

.build()

0000-DTSE-Core-6244-DU-60-16 © DataStax, All Rights Reserved, Confidential

DseSession-

DseSession my_session = my_cluster.connect( <keyspace name> )

• Both DseCluster and DseSession are singleton objects

• One per DSE Core workload and one per DSE Search ?

• Or, tune using cassandra-stress. Increase until speed goes negative

0000-DTSE-Core-6244-DU-60-17 © DataStax, All Rights Reserved, Confidential

Now that you are

connected-

0000-DTSE-Core-6244-DU-60-18 © DataStax, All Rights Reserved, Confidential

Sourcing: O'Reilly Book (2016)

The example code that follows arrive from the

O'Reilly Book,

"Cassandra: the Definitive Guide"

and are publicly downloadable from,

https://github.com/jeffreyscarpenter/cassandra-guide

The examples here are written contiguously,

with objects referenced page over page-

0000-DTSE-Core-6244-DU-60-19 © DataStax, All Rights Reserved, Confidential

Executing CQL-

my_session.execute("SELECT * FROM t1");

Or ,statements-

SimpleStatement

BoundStatement (same as above, how variables are treated)

PreparedStatement Efficiency, compiled/cached

BatchStatement

.setConsistencyLevel()

.enableTracing()

.setFetchSize()

(others)

0000-DTSE-Core-6244-DU-60-20 © DataStax, All Rights Reserved, Confidential

Example Statements: Base runtime (CQL objects)

CREATE TABLE ks_6240.cust_orders

(

region TEXT,

cust_name TEXT,

ord_num INT,

other TEXT,

PRIMARY KEY ((region, cust_name), ord_num)

);

0000-DTSE-Core-6244-DU-60-21 © DataStax, All Rights Reserved, Confidential

Example Statements: Imports (all)

import com.datastax.driver.dse.DseCluster;

import com.datastax.driver.dse.DseSession;

//

import com.datastax.driver.core.Row;

//

import com.datastax.driver.core.Cluster;

import com.datastax.driver.core.Host;

import com.datastax.driver.core.Metadata;

//

import com.datastax.driver.core.Session;

0000-DTSE-Core-6244-DU-60-22 © DataStax, All Rights Reserved, Confidential

Example Statements: Imports (all)

import com.datastax.driver.core.QueryTrace;

import com.datastax.driver.core.ResultSet;

import com.datastax.driver.core.Row;

import com.datastax.driver.core.SimpleStatement;

//

import java.text.SimpleDateFormat;

//

import com.datastax.driver.core.BoundStatement;

import com.datastax.driver.core.PreparedStatement;

//

import com.datastax.driver.core.BatchStatement;

0000-DTSE-Core-6244-DU-60-23 © DataStax, All Rights Reserved, Confidential

Example Statements: Imports (all)

import com.datastax.driver.core.querybuilder.BuiltStatement;

import com.datastax.driver.core.querybuilder.QueryBuilder;

import static

com.datastax.driver.core.querybuilder.QueryBuilder.eq;

//

import java.util.Arrays;

import java.util.List;

0000-DTSE-Core-6244-DU-60-24 © DataStax, All Rights Reserved, Confidential

Example

DseCluster my_cluster = null; Statements-

my_cluster = DseCluster.builder()

.addContactPoint("127.0.0.1")

// .withCredentials("guest", "password")

.build();

DseSession my_session1 = my_cluster.connect();

Row my_row1 = my_session1.execute("select * from

system.local").one();

System.out.println("DSE release version: " +

my_row1.getString("dse_version") );

0000-DTSE-Core-6244-DU-60-25 © DataStax, All Rights Reserved, Confidential

Metadata my_metadata1 = my_cluster.getMetadata();

System.out.printf("Connected to cluster: %s %s\n",

my_metadata1.getClusterName(), Example

my_cluster.getClusterName()); Statements-

for (Host host : my_metadata1.getAllHosts()) {

System.out.printf("Data Center: %s; Rack: %s; Host: %s\n",

host.getDatacenter(), host.getRack(), host.getAddress());

}

System.out.printf("Protocol Version: %s\n",

my_cluster.getConfiguration()

.getProtocolOptions()

.getProtocolVersion());

0000-DTSE-Core-6244-DU-60-26 © DataStax, All Rights Reserved, Confidential

Example

Statements-

Session.State my_state = my_session1.getState();

System.out.printf("New session created for keyspace: %s\n",

my_session1.getLoggedKeyspace());

for (Host host : my_state.getConnectedHosts()) {

System.out.printf("Data Center: %s; Rack: %s; \

Host: %s; Open Connections: %s\n",

host.getDatacenter(), host.getRack(), host.getAddress(),

my_state.getOpenConnections(host));

}

0000-DTSE-Core-6244-DU-60-27 © DataStax, All Rights Reserved, Confidential

Session my_session2 = my_cluster.connect("ks_6240");

String my_str1 = "JC Penney";

SimpleStatement my_insert1 = new SimpleStatement(

"INSERT INTO cust_orders (region, cust_name, Example ord_num, other) VALUES (?, ?, ?, ?)",

"NA", my_str1, 109, "Ball, Mitt"); Statements-

ResultSet my_result1 = my_session2.execute(my_insert1);

System.out.println(my_result1);

System.out.println(my_result1.wasApplied());

System.out.println(my_result1.getExecutionInfo());

System.out.println(my_result1.getExecutionInfo().

getIncomingPayload());

0000-DTSE-Core-6244-DU-60-28 © DataStax, All Rights Reserved, Confidential

SimpleStatement my_select1 = new SimpleStatement(

"SELECT * FROM cust_orders WHERE region = ? \

AND cust_name = ?", "NA", my_str1); Example

my_select1.enableTracing(); Statements-

ResultSet my_result2 = my_session2.execute(my_select1);

System.out.println(my_result2);

System.out.println(my_result2.wasApplied());

System.out.println(my_result2.getExecutionInfo());

System.out.println(my_result2.getExecutionInfo().

getIncomingPayload());

System.out.println(my_result2.getExecutionInfo().

getQueryTrace());

0000-DTSE-Core-6244-DU-60-29 © DataStax, All Rights Reserved, Confidential

Example

Statements-

for (Row row : my_result2) {

System.out.format("region: %s, cust_name: %s, \

ord_num: %s, other: %s\n\n",

row.getString("region"), row.getString("cust_name"),

row.getInt("ord_num"), row.getString("other") );

}

SimpleDateFormat my_dateFormat = new

SimpleDateFormat("HH:mm:ss.SSS");

QueryTrace my_queryTrace1 =

my_result2.getExecutionInfo().getQueryTrace();

0000-DTSE-Core-6244-DU-60-30 © DataStax, All Rights Reserved, Confidential

Example

Statements-

System.out.printf("Trace id: %s\n\n",

my_queryTrace1.getTraceId());

System.out.printf("%-42s | %-12s | %-10s \n",

"activity", "timestamp", "source");

System.out.println("---------- ... ------------");

0000-DTSE-Core-6244-DU-60-31 © DataStax, All Rights Reserved, Confidential

Example

Statements-

for (QueryTrace.Event event : my_queryTrace1.getEvents()) {

System.out.printf("%42s | %12s | %10s\n",

event.getDescription(),

my_dateFormat.format((event.getTimestamp())),

event.getSource());

}

0000-DTSE-Core-6244-DU-60-32 © DataStax, All Rights Reserved, Confidential

Example

Statements-

String my_str2 ="Woolworth's";

PreparedStatement my_prepared1 = my_session2.prepare(

"INSERT INTO cust_orders (region, cust_name,

ord_num, other) VALUES (?, ?, ?, ?)");

BoundStatement my_bound1 = my_prepared1.bind(

"NA", my_str2, 110, "Robot, Car");

ResultSet my_result3 = my_session2.execute(my_bound1);

0000-DTSE-Core-6244-DU-60-33 © DataStax, All Rights Reserved, Confidential

Example

Statements-

System.out.println(my_result3);

System.out.println(my_result3.wasApplied());

System.out.println(my_result3.getExecutionInfo());

System.out.println(my_result3.getExecutionInfo().

getIncomingPayload());

0000-DTSE-Core-6244-DU-60-34 © DataStax, All Rights Reserved, Confidential

Example

Statements-

PreparedStatement my_prepared2 = my_session2.prepare(

"SELECT * FROM cust_orders WHERE region = ? \

AND cust_name = ?");

BoundStatement my_bound2 = my_prepared2.bind(

"NA", "SEARS");

ResultSet my_result4 = my_session2.execute(my_bound2);

0000-DTSE-Core-6244-DU-60-35 © DataStax, All Rights Reserved, Confidential

Example

Statements-

ResultSet my_result4 = my_session2.execute(my_bound2);

System.out.println(my_result4);

System.out.println(my_result4.wasApplied());

System.out.println(my_result4.getExecutionInfo());

System.out.println(my_result4.getExecutionInfo().

getIncomingPayload());

0000-DTSE-Core-6244-DU-60-36 © DataStax, All Rights Reserved, Confidential

Example

Statements-

for (Row row : my_result4) {

System.out.format("region: %s, cust_name: %s, \

ord_num: %s, other: %s\n",

row.getString("region"), row.getString("cust_name"),

row.getInt("ord_num"), row.getString("other"));

}

0000-DTSE-Core-6244-DU-60-37 © DataStax, All Rights Reserved, Confidential

Example

Statements-

SimpleStatement my_delete1 = new SimpleStatement(

"DELETE FROM cust_orders WHERE region = ? \

AND cust_name= ?", "NA", my_str2);

ResultSet my_result5 = my_session2.execute(my_delete1);

System.out.println(my_result5);

System.out.println(my_result5.wasApplied());

System.out.println(my_result5.getExecutionInfo());

System.out.println("num results: " +

my_result5.all().size());

0000-DTSE-Core-6244-DU-60-38 © DataStax, All Rights Reserved, Confidential

Example

Statements-

for (Row row : my_result5) {

System.out.format("region: %s, cust_name: %s, \

ord_num: %s, other: %s\n",

row.getString("region"), row.getString("cust_name"),

row.getInt("ord_num"), row.getString("other"));

}

0000-DTSE-Core-6244-DU-60-39 © DataStax, All Rights Reserved, Confidential

Example

Statements-

SimpleStatement my_insert2 = new SimpleStatement(

"INSERT INTO cust_orders (region, cust_name, ord_num,

other) VALUES (?, ?, ?, ?)",

"SA", "X-Store", 101, "Water, Juice");

SimpleStatement my_insert3 = new SimpleStatement(

"INSERT INTO cust_orders (region, cust_name, ord_num,

other) VALUES (?, ?, ?, ?)",

"SA", "X-Store", 102, "Water, Juice, Lemons");

0000-DTSE-Core-6244-DU-60-40 © DataStax, All Rights Reserved, Confidential

Example

Statements-

BatchStatement my_batch1 = new BatchStatement();

my_batch1.add(my_insert2);

my_batch1.add(my_insert3);

ResultSet my_result6 = my_session2.execute(my_batch1);

0000-DTSE-Core-6244-DU-60-41 © DataStax, All Rights Reserved, Confidential

Example

Statements-

System.out.println(my_result6);

System.out.println(my_result6.wasApplied());

System.out.println(my_result6.getExecutionInfo());

System.out.println(my_result6.getExecutionInfo().

getIncomingPayload());

0000-DTSE-Core-6244-DU-60-42 © DataStax, All Rights Reserved, Confidential

Example

Statements-

SimpleStatement my_insert4 = new SimpleStatement(

"INSERT INTO cust_orders (region, cust_name,

ord_num, other) VALUES (?, ?, ?, ?) IF NOT EXISTS",

"SA", "X-Store", 103, "Water, Juice, Pie");

ResultSet my_result7 = my_session2.execute(my_insert4);

0000-DTSE-Core-6244-DU-60-43 © DataStax, All Rights Reserved, Confidential

Example

Statements-

System.out.println(my_result7);

System.out.println(my_result7.wasApplied());

System.out.println(my_result7.getExecutionInfo());

System.out.println(my_result7.getExecutionInfo().

getQueryTrace());

0000-DTSE-Core-6244-DU-60-44 © DataStax, All Rights Reserved, Confidential

Example

Statements-

for (Row row : my_result7) {

System.out.format("region: %s, cust_name: %s, \

ord_num: %s, other: %s\n",

row.getString("region"), row.getString("cust_name"),

row.getInt("ord_num"), row.getString("other") );

}

0000-DTSE-Core-6244-DU-60-45 © DataStax, All Rights Reserved, Confidential

Example Statements-

Metadata my_metadata2 = my_cluster.getMetadata();

System.out.printf("Connected to cluster: %s %s\n",

my_metadata2.getClusterName(),

my_cluster.getClusterName());

System.out.println("Schema:");

System.out.println(my_metadata2.exportSchemaAsString());

System.out.println();

System.out.printf("Schema agreement : %s\n",

my_metadata2.checkSchemaAgreement());

0000-DTSE-Core-6244-DU-60-46 © DataStax, All Rights Reserved, Confidential

• Nothing new [ functionally ] over

previous content/methods

(Inherits from Statement, thus, all DSE Query options available.)

Builder • Syntactic sugar-

• Easier to read, maintain ??

0000-DTSE-Core-6244-DU-60-47 © DataStax, All Rights Reserved, Confidential

Query Builder API-

• Alternative to (manual) query strings

• Generates a Statement, per earlier

• QueryBuilder.select()

• QueryBuilder.insertInto()

• QueryBuilder.update()

• QueryBuilder.delete()

• .enableTracing()

• .isIdempotent()

• .limit()

.orderBy()

• (others)

0000-DTSE-Core-6244-DU-60-48 © DataStax, All Rights Reserved, Confidential

BuiltStatement my_built1 = Query

QueryBuilder.insertInto("cust_orders"). Builder value("region", "EMEA").

Example- value("cust_name", "Apple").

value("ord_num", 200).

value("other", "mouse");

ResultSet my_result8 = my_session2.execute(my_built1);

System.out.println(my_result8);

System.out.println(my_result8.wasApplied());

System.out.println(my_result8.getExecutionInfo());

System.out.println(my_result8.getExecutionInfo()

.getIncomingPayload());

0000-DTSE-Core-6244-DU-60-49 © DataStax, All Rights Reserved, Confidential

Query Select my_select = QueryBuilder.select()

.all() Builder

.distinct() Example- .from( "ks", "table")

.where(eq("col", "value"))

.and(eq("col", "value"))

.orderBy(asc("col")

.limit(2);

System.out.println(my_select.getQueryString());

// SELECT * FROM ..

ResultSet my_result = my_session.execute(my_select);

System.out.println(my_result.one().getString("col"));

0000-DTSE-Core-6244-DU-60-50 © DataStax, All Rights Reserved, Confidential

Delete.Where my_delete = QueryBuilder.delete()

.from("ks", "table")

.where(eq("col", "value"));

Query

my_session.execute(my_delete); Builder

Example-

0000-DTSE-Core-6244-DU-60-51 © DataStax, All Rights Reserved, Confidential

Topics Not

Covered:

0000-DTSE-Core-6244-DU-60-52 © DataStax, All Rights Reserved, Confidential

Topics Not Covered-

Futures

• DSE is inherently asynchronous

• All prior objects were wrappers for the default

asynchronous, but calling for synchronous

• Futures require Java annotations, which we

don't want to teach in this intro level unit.

• Other JCA topics-

• Other

0000-DTSE-Core-6244-DU-60-53 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Core-6244-DU-60-54 © DataStax, All Rights Reserved, Confidential
