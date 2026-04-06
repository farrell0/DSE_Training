# DSE Core: DSE Core, Security

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Core curriculum and need help with dse core, security. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Core track covers the security model and the administrative steps needed to apply it. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse core, security.

## Downloads

- [PDF slides](./6221-dse-core-security.pdf)
- [Original PowerPoint](../000-DTSE-Core-6221-PL-60%2C%20DSE%20Core%2C%20Security.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Unit 6220, where most of the

objects we create in this lab were Practice Lab: introduced.

DSE Core (and more), • In this Practice Lab, we DSE initiate

Security (internal, native) Authentication, and

apply Authorization rules to a number of

database objects.

0000-DTSE-Studio-6221-DU-60-1 © DataStax, All Rights Reserved, Confidential

Challenge 1: Enable/Test DSE Security

Prerequisites:

• Instructions are provided for a single

node DSE Core cluster.

• There are additional steps for a multi-

node cluster, that we overview only.

• Instructions are provided for the

command prompt using CQLSH.

• All work done as ‘root’

0000-DTSE-Studio-6221-DU-60-2 © DataStax, All Rights Reserved, Confidential

Challenge 1: DSE

• Implementing Security, In the Real Authorization/Authentication can be World .. done without downtime

-- Clients: Roll out new client

programs with TRANSITIONAL

client side driver switch (details

on Notes page)

-- Server: change in multi-user

mode, or rolling change

• Multi-node:

-- ALTER KEYSPACE,

system_auth, dse_security

-- nodetool repair

0000-DTSE-Studio-6221-DU-60-3 © DataStax, All Rights Reserved, Confidential

DSE Security: Sample Artifacts to Secure

DROP KEYSPACE IF EXISTS ks_6221;

CREATE KEYSPACE ks_6221

WITH REPLICATION =

{'class': 'SimpleStrategy',

'replication_factor': 1};

USE ks_6221;

0000-DTSE-Studio-6221-DU-60-4 © DataStax, All Rights Reserved, Confidential

DSE Security:

Sample Artifacts to

DROP TABLE IF EXISTS cust_orders; Secure

CREATE TABLE cust_orders

(

region TEXT,

cust_name TEXT,

ord_num INT,

other TEXT,

PRIMARY KEY ((region, cust_name),

ord_num)

);

0000-DTSE-Studio-6221-DU-60-5 © DataStax, All Rights Reserved, Confidential

DSE Security:

Sample Artifacts to

Secure

INSERT INTO cust_orders

(region, cust_name, ord_num, other)

VALUES ('EMEA', 'IKEA' , 101, 'Shoes' );

...

VALUES ('NA' , 'SEARS' , 101, 'Shoes, Washer');

VALUES ('NA' , 'SEARS' , 102, 'Oranges' );

VALUES ('NA' , 'MACYS' , 101, 'Dress, Tie' );

0000-DTSE-Studio-6221-DU-60-6 © DataStax, All Rights Reserved, Confidential

DSE Security:

Sample Artifacts to DROP TABLE IF EXISTS cust_payments;

Secure

CREATE TABLE cust_payments

(

cust_name TEXT,

payment_num INT,

other TEXT,

PRIMARY KEY ((cust_name, payment_num))

);

INSERT INTO cust_payments (cust_name,

payment_num, other)

VALUES ('SEARS' , 101, '$100');

...

VALUES ('MACYS' , 101, '$200');

0000-DTSE-Studio-6221-DU-60-7 © DataStax, All Rights Reserved, Confidential

DSE Security:

Confirm or create these changes- cassandra.yaml

# default, confirm set

authenticator: com.datastax.bdp.cassandra.auth.DseAuthenticator

# default, confirm set

role_manager: com.datastax.bdp.cassandra.auth.DseRoleManager

# If doing RLAC (Yes, you are), tune

#

# Uncomment any that are commented

# permissions_cache_max_entries not present in 6.0

permissions_validity_in_ms: 2000

permissions_uddate_interval_in_ms: 2000

permissions_cache_max_entries: 1000

0000-DTSE-Studio-6221-DU-60-8 © DataStax, All Rights Reserved, Confidential

Confirm or create these changes-

DSE Security: # Uncomment all # Set, enabled: true dse.yaml # Ensure, default_scheme: internal authentication_options: enabled: true default_scheme: internal other_schemes: scheme_permissions: false allow_digest_with_kerberos: true plain_text_without_ssl: warn transitional_mode: disabled # Uncomment role_management_options: mode: internal # Uncomment # Set, enabled: true authorization_options: enabled: true transitional_mode: disabled allow_row_level_security: true

0000-DTSE-Studio-6221-DU-60-9 © DataStax, All Rights Reserved, Confidential

DSE Security: then reboot DSE

Again; not required when in

production. Easier when testing.

• Less steps

• Error messages on boot screen/log

0000-DTSE-Studio-6221-DU-60-10 © DataStax, All Rights Reserved, Confidential

DSE Security:

CREATE ROLE

DROP ROLE IF EXISTS bob ;

DROP ROLE IF EXISTS nancy ;

DROP ROLE IF EXISTS dirk ;

DROP ROLE IF EXISTS senior_operator;

DROP ROLE IF EXISTS operator ;

DROP ROLE IF EXISTS operator_na ;

CREATE ROLE bob WITH LOGIN = true AND PASSWORD = 'password';

GRANT EXECUTE on INTERNAL SCHEME to bob ;

CREATE ROLE nancy WITH LOGIN = true AND PASSWORD = 'password';

GRANT EXECUTE on INTERNAL SCHEME to nancy;

CREATE ROLE dirk WITH LOGIN = true AND PASSWORD = 'password';

GRANT EXECUTE on INTERNAL SCHEME to dirk ;

0000-DTSE-Studio-6221-DU-60-11 © DataStax, All Rights Reserved, Confidential

DSE Security: Assign/CREATE Roles

CREATE ROLE senior_operator;

// INSERT, UPDATE, DELETE and TRUNCATE rows in // any table in the specified keyspace. // ADD SELECT GRANT MODIFY, SELECT ON KEYSPACE ks_6221 TO senior_operator;

GRANT senior_operator to nancy;

CREATE ROLE operator;

GRANT MODIFY,SELECT ON TABLE ks_6221.cust_orders TO operator;

GRANT SELECT ON TABLE ks_6221.cust_payments TO operator;

GRANT operator to bob;

0000-DTSE-Studio-6221-DU-60-12 © DataStax, All Rights Reserved, Confidential

DSE Security: Review of

data/other CREATE TABLE cust_orders

(

region TEXT,

cust_name TEXT,

ord_num INT,

other TEXT,

PRIMARY KEY ((region, cust_name), ord_num)

INSERT INTO cust_orders ...

VALUES ('EMEA', 'IKEA' , 101, 'Shoes' );

VALUES (' NA ' , 'SEARS' , 101, 'Shoes, Washer' );

VALUES (' NA ' , 'SEARS' , 102, 'Oranges' );

VALUES (' NA ' , 'MACYS' , 101, 'Dress, Tie' );

INSERT INTO cust_payments ...

VALUES ('SEARS' , 101, '$100' );

VALUES ('MACYS' , 101, '$200' );

0000-DTSE-Studio-6221-DU-60-13 © DataStax, All Rights Reserved, Confidential

DSE Security:

RLAC CREATE ROLE operator_na;

// RESTRICT ROWS ON ks_6221.cust_orders USING other;

// InvalidRequest: Error from server: code=2200 [Invalid query]

// message="Restrict Rows Statement must be for a Primary Key

// or a Partition Key column"

RESTRICT ROWS ON ks_6221.cust_orders USING region;

RESTRICT ROWS ON ks_6221.cust_orders USING cust_name;

// DESCRIBE TABLE shows cust_name only

RESTRICT ROWS ON ks_6221.cust_orders USING region;

GRANT SELECT ON 'NA' ROWS IN ks_6221.cust_orders TO operator_na;

GRANT operator_na to dirk;

0000-DTSE-Studio-6221-DU-60-14 © DataStax, All Rights Reserved, Confidential

DSE Security: Testing

cqlsh -u nancy -p password

cqlsh -u bob -p password

cqlsh -u dirk -p password

use ks_6221;

select * from cust_orders;

select * from cust_payments;

Nancy, copyright Ernie Bushmiller Bob the Builder, copyright, Keith Chapman Dirk Nowitzki, by Chris Sebastian

0000-DTSE-Studio-6221-DU-60-15 © DataStax, All Rights Reserved, Confidential

Lessons Learned

0000-DTSE-Studio-6221-DU-60-16 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Studio-6221-DU-60-17 © DataStax, All Rights Reserved, Confidential
