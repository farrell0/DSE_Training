# DSE Core: Studio, Install, config, and first steps

<table>
  <tr>
    <td><strong>DSE Core</strong></td><td><a href="../../search/README.md"><strong>DSE Search</strong></a></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Core curriculum and need help with studio, install, config, and first steps. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Core track explains the installation and configuration workflow. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around studio, install, config, and first steps.

## Downloads

- [PDF slides](./6211-studio-install-config-and-first-steps.pdf)
- [Original PowerPoint](../000-DTSE-Studio-6211-PL-60%2C%20Studio%2C%20Install%2C%20config%2C%20and%20first%20steps.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Unit 6210, where most of the

objects we create in this lab were Practice Lab: introduced.

DSE Studio, Install, • In this Practice Lab, we install DSE

Configure, First Steps Studio from Tar ball, configure it, and run

a basic install verification; create a table,

add data, query same.

0000-DTSE-Studio-6211-DU-60-1 © DataStax, All Rights Reserved, Confidential

Challenge 1: Install, Configure, run DSE Studio

Prerequisites:

• Instructions are provided for Linux

• We will operate below recommended

settings; 1 OS node only, minimum 8

GB RAM, 12 GB RAM preferred

• That you have an operating single

node DSE Core cluster (anything

more likely wont fit; DSE Core plus

Studio on 8 GB RAM)

• All work done as ‘root’

0000-DTSE-Studio-6211-DU-60-2 © DataStax, All Rights Reserved, Confidential

Challenge 1: Files, Directories

• Download Studio from Academy,

https://academy.datastax.com/downloads • Unpack the DSE Studio Tar ball

in /opt/studio

0000-DTSE-Studio-6211-DU-60-3 © DataStax, All Rights Reserved, Confidential

Challenge 1: Configure

• cd /opt/studio/conf

• ls –l

• (Edit configuration.yaml)

-- Optional step, as no changes

are required

-- We changed

userData:

baseDirectory: /opt/studio_data

-- Make sure directory above

exists

0000-DTSE-Studio-6211-DU-60-4 © DataStax, All Rights Reserved, Confidential

Challenge 1: Start Studio (Web client server)

cd /opt/studio/bin

./server.sh

In Web browser,

localhost:9091

Next Page

0000-DTSE-Studio-6211-DU-60-5 © DataStax, All Rights Reserved, Confidential

Challenge 1: Install verify

In Studio Web UI:

• Click the large PLUS symbol

• This action produces a modal dialog

box titled, CREATE NOTEBOOK

• Enter data as shown at right

• Click -> Create

0000-DTSE-Studio-6211-DU-60-6 © DataStax, All Rights Reserved, Confidential

Challenge 1: Make

Keyspace, table, data, select

• Enter CQL to CREATE

KEYSPACE

• Click the (Run button)

(CL.ONE is a reference to

consistency level one)

• Add a new Cell; Click the

small grey plus symbol on

the bottom-line/middle of

any existing cell

• In the new Cell, chose a

target keyspace

• Add and run CQL to

CREATE TABLE, ..

• Run

0000-DTSE-Studio-6211-DU-60-7 © DataStax, All Rights Reserved, Confidential

Challenge 2: Export/drop Notebook

1 In Studio Web UI:

• Click the left most icon in the Toolbar

(balloon help titles this icon, Main

Menu).

• Select -> Export

• Follow prompts to save (file, a Tar

ball) to the Desktop.

2 • Then, follow prompts to "Delete this

Notebook"

3

0000-DTSE-Studio-6211-DU-60-8 © DataStax, All Rights Reserved, Confidential

Challenge 2: Import a Notebook

In Studio Web UI:

• Drag and Drop the

previously exported

Notebook from the

Desktop to the Studio

(canvas)

• You will need to reselect

Keyspaces on imported

Notebooks

0000-DTSE-Studio-6211-DU-60-9 © DataStax, All Rights Reserved, Confidential

Go Father:

(Optional)

Vasco Núñez de Balboa was a Spanish explorer (or conquistador) who saw and claimed the Pacific Ocean for Spain. He was born in 1475 in a poor region of Spain known as Extremadura, which was also the home of conquistadors Hernán Cortés, Francisco Pizarro, Hernando de Soto, and Francisco de Orellana.

Source: http://mrnussbaum.com/explorers/famous-explorers/

0000-DTSE-Studio-6211-DU-60-10 © DataStax, All Rights Reserved, Confidential

Challenge 3 (Optional): Run Spark/SQL

From the command line:

• Shutdown down your single node

DSE Core

• Edit the dse.yaml. Change

alwayson_sql_options:

enabled: true

(With proper indentation)

• Restart DSE. Add a –k option on the

command line

• Restart the DSE Studio daemon (see

Notes)

0000-DTSE-Studio-6211-DU-60-11 © DataStax, All Rights Reserved, Confidential

Challenge 3 (Optional): Spurious error

0000-DTSE-Studio-6211-DU-60-12 © DataStax, All Rights Reserved, Confidential

Challenge 3 (Optional): Success

0000-DTSE-Studio-6211-DU-60-13 © DataStax, All Rights Reserved, Confidential

Challenge 3 (Optional): Definite Error (Resource)

0000-DTSE-Studio-6211-DU-60-14 © DataStax, All Rights Reserved, Confidential

Lessons Learned

0000-DTSE-Studio-6211-DU-60-15 © DataStax, All Rights Reserved, Confidential

0000-DTSE-Studio-6211-DU-60-16 © DataStax, All Rights Reserved, Confidential
