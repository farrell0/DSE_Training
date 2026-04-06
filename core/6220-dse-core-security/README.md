# DSE Core: DSE Core, Security

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Demonstration Unit

**Customer:** I am working through the DSE Core curriculum and need help with dse core, security. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This demonstration unit in the DSE Core track covers the security model and the administrative steps needed to apply it. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse core, security.

## Downloads

- [PDF slides](./6220-dse-core-security.pdf)
- [Original PowerPoint](../000-DTSE-Core-6220-DU-60%2C%20DSE%20Core%2C%20Security.pptx)

## Converted Slides

## Discussion Unit:

Introduce DSE Security

• Large topic, necessary for the enterprise

• CSO or similar ? Get help

• Multiple Levels DSE Core (and more),

-- OS (Pre DSE) Security

-- DSE

-- Database connections (end

user)

-- Inter-nodal communication

-- Data in flight

-- Data at rest

-- Files, (config, temp)

-- (Other)

0000-DTSE-Core-6220-DU-60-1 © DataStax, All Rights Reserved, Confidential

Discussion Lab:

What is ? (Define the term)

Source: https://www.youtube.com/watch?v=5NhZXDU9FMo

0000-DTSE-Core-6220-DU-60-2 © DataStax, All Rights Reserved, Confidential

Define the term: What is ? Authentication

Authorization

Separation of Roles

Encryption at rest

Encryption in flight

RBAC

RLAC

TLAC

Auditing

“The forecast average loss

for a breach of 1,000 records

is generally over $$ (2015)

Source:https://www.verizonenterprise.com/verizon-insights-lab/dbir/

0000-DTSE-Core-6220-DU-60-3 © DataStax, All Rights Reserved, Confidential

End of

Discussion Lab:

0000-DTSE-Core-6220-DU-60-4 © DataStax, All Rights Reserved, Confidential

DSE 6 Security: Overview

Feature Core Search Analytics Graph

Yes Partial Yes Yes Authenticate, LDAP or Internal

Yes Yes Yes Yes Authenticate, Kerberos (Extern)

Yes Partial Yes Partial Authorize (RBAC)

Yes No Yes Row Level perm (RLAC) No

Yes Yes Yes Client-to-node encryption Yes

Yes Yes Yes Node-to-node encryption Yes

Yes Yes Transparent data encryption No Yes

Data auditing Yes Yes Partial Yes

0000-DTSE-Core-6220-DU-60-5 © DataStax, All Rights Reserved, Confidential

DSE Security: Authentication "DSE Unified

Authentication",

database Inter-nodal (gossip, other) connections only -- SSL certificates

Database connections (client to node, tools and apps)

-- Internal, credentials by DSE

-- LDAP (including Active Directory) Practice Lab to follow

-- Kerberos

PKI (Public key infrastructure)

KMIP (Key management interoperability protocol)

-- And encrypt data in flight (client to node SSL)

0000-DTSE-Core-6220-DU-60-6 © DataStax, All Rights Reserved, Confidential

DSE Security: Authorization

Role based access control (RBAC)

-- Only if authentication is enabled

Internal (credentials by DSE)

-- 1:1 mapping of user name to roles

LDAP Unbreakable -- 1:M mapping, users assigned roles that Source: https://www.imdb.com/title/tt0217869

match groups in LDAP

0000-DTSE-Core-6220-DU-60-7 © DataStax, All Rights Reserved, Confidential

DSE: Encryption of Data in Flight

SSL encryption for data in-flight for the following components:

• DSE transactional nodes

• DSE Search (Apache Solr™)

• DSE Analytics (Apache Spark™)

• DSE Graph

• DSE tools

• DSE drivers

• DSE OpsCenter

0000-DTSE-Core-6220-DU-60-8 © DataStax, All Rights Reserved, Confidential

DSE: Encryption "Transparent Data Encryption (TDS)"

of Data at Rest • Entire tables (except for partition keys which are always

stored in plain text)

• SSTables containing data, including system tables (such

as system.batchlog and system.paxos)

• Search indexes

• File-based Hints (in DSE 5.0 and later)

• Commit logs

• Sensitive properties in dse.yaml and cassandra.yam

• TDE only applies to data stored in the database. DSE

does not support encrypting data that is used by Spark

and stored in DSEFS or local temporary directories.

• Graph: Cached data is not encrypted. Encryption may

slightly impact performance.

0000-DTSE-Core-6220-DU-60-9 © DataStax, All Rights Reserved, Confidential

DSE: Securing Ports, Temp directories (JNA)

(20+ more)

0000-DTSE-Core-6220-DU-60-10 © DataStax, All Rights Reserved, Confidential

DSE: RBAC (Managing Roles)

• Similar to any RDBMS

• Keyspace Filtering

cassandra.yaml

system_keyspaces_filtering: true User/role needs

DESCRIBE permission on

keyspace

0000-DTSE-Core-6220-DU-60-11 © DataStax, All Rights Reserved, Confidential

DSE: Object Hierarchy for GRANT|REVOKE

Row-level access control (RLAC) is disabled by default. To use RLAC, set allow_row_level_security parameter to true in the dse.yaml.

0000-DTSE-Core-6220-DU-60-12 © DataStax, All Rights Reserved, Confidential

DSE: Audit Secure Subsystem

• DataStax Enterprise (DSE)

supports capturing database

activity to a log file or table.

• The audit logger also captures

queries and prepared statements

submitted by DataStax drivers,

which use CQL binary protocol.

• Security-

• Separation of duties

• Tuning, Capacity planning

0000-DTSE-Core-6220-DU-60-13 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Core-6220-DU-60-14 © DataStax, All Rights Reserved, Confidential
