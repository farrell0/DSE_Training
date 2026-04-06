# DSE Search: DSE Search, Synonym, Case Insensitive, More

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Search curriculum and need help with dse search, synonym, case insensitive, more. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, synonym, case insensitive, more.

## Downloads

- [PDF slides](./7444-dse-search-synonym-case-insensitive-more.pdf)
- [Original PowerPoint](../000-DTSE-Search-7444-PL-60%2C%20DSE%20Search%2C%20Synonym%2C%20Case%20Insensitive%2C%20More.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Module 7443, where most of Practice Lab: the objects we create in this lab were

introduced. DSE Search, Create

Synonym, Case • This Practice Lab requires a working DSE Insensitive system, with DSE Search enabled, and

with ability to execute CQL DDL.

• Because of the dependency on the

dsetool utility, this Practice Lab requires a

ssh(C) prompt on at least one node

operating DSE Search. All other

commands are run from CQLSH, or DSE

Studio.

000-DTSE-Search-7444-60-PL-1 © DataStax, All Rights Reserved. Confidential.

Challenge 1: Execute all of the following below

• Discussion Module 7443 details each

of the commands entered on the notes

page below.

• The dsetool command must be run

directly on one of the DSE nodes

running DSE Search, in an ssh(C)

command window. All other commands

may be run in CQLSH, or DSE Studio.

• Execute all of the instructions on the

notes page below-

000-DTSE-Search-7444-60-PL-2 © DataStax, All Rights Reserved. Confidential.

Challenge 1: Test via CQL SELECT / DSE Studio

• Test your results using the three CQL

SELECT statements entered on the notes

page below.

• The first two queries return data, the last

query does not.

000-DTSE-Search-7444-60-PL-3 © DataStax, All Rights Reserved. Confidential.

Go Farther:

(Optional)

Vasco da Gama (1460-1524) First European to reach India by sea.

Source: http://totallyhistory.com/biography/famous-explorers/

000-DTSE-Search-7444-60-PL-4 © DataStax, All Rights Reserved. Confidential.

Challenge 2 (Optional): Syntax to harvest from-

ALTER SEARCH INDEX SCHEMA ON t2

ADD fieldType[@name='TextField44',class='solr.TextField‘]

WITH '{"analyzer":{"tokenizer": Case insensitive example {"class":"solr.StandardTokenizerFactory"},

"filter":{"class":"solr.LowerCaseFilterFactory"}}}';

ALTER SEARCH INDEX SCHEMA ON t2

Stemming example, two ADD fieldType[@name='TextField41',class='solr.TextField']

filter example WITH '{"analyzer":{"tokenizer": {"class":"solr.StandardTokenizerFactory"},

"filter":[{"class":"solr.LowerCaseFilterFactory"},

{"class":"solr.EnglishMinimalStemFilterFactory"}]}}';

000-DTSE-Search-7444-60-PL-5 © DataStax, All Rights Reserved. Confidential.

Challenge 2 (Optional): Goals

• Leave col1, col2, and col3 alone. Alter col4, col5, ..

as needed.

• Create col4, just case insensitive.

• Create col5, case insensitive, and stemming.

• Create col6, case insensitive, synonym.

• Experiment with forms of,

SELECT * FROM t1 WHERE col3 LIKE 'D%' ; Leif Ericson (970-1020) Considered the first European to reach North America.

Source: http://totallyhistory.com/biography/famous- explorers/

000-DTSE-Search-7444-60-PL-6 © DataStax, All Rights Reserved. Confidential.

Lessons learned

000-DTSE-Search-7444-60-DM-7 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7444-60-DM-8
