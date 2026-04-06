# DSE Search: DSE Search, Debugging

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Search curriculum and need help with dse search, debugging. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, debugging.

## Downloads

- [PDF slides](./7446-dse-search-debugging.pdf)
- [Original PowerPoint](../000-DTSE-Search-7446-PL-60%2C%20DSE%20Search%2C%20Debugging.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Module 7445, where most of Practice Lab: the objects we create in this lab were

introduced. DSE Search, Debugging

• This Practice Lab requires a working DSE

system, with DSE Search enabled, and

with ability to execute CQL DDL.

• Because of the dependency on the

dsetool utility, this Practice Lab requires a

ssh(C) prompt on at least one node

operating DSE Search. All other

commands are run from CQLSH, or DSE

Studio.

000-DTSE-Search-7446-60-PL-1 © DataStax, All Rights Reserved. Confidential.

Challenge 1: Reverse Engineer

<fieldType name="nametext" class="solr.TextField">

<analyzer>

<tokenizer class="solr.StandardTokenizerFactory"/>

<filter class="solr.StandardFilterFactory"/>

<filter class="solr.LowerCaseFilterFactory"/>

• What does this analyzer do ? <filter class="solr.StopFilterFactory"/>

• Is this an INDEX or QUERY <filter class="solr. EnglishMinimalStemFilterFactory"/>

analyzer ? </analyzer>

• </fieldType> What happens if a decimal

value gets placed in this field ?

000-DTSE-Search-7446-60-PL-2 © DataStax, All Rights Reserved. Confidential.

Challenge 2: • Use CQL commands to create, and Solr

Admin UI to test (query)

• Create an analyzer that returns the DSE

table column value “The Cranberries”,

when given the query predicate, “anD a

kraNBurry”.

• More than one analyzer, stage the

development incrementally-

– A 1 field with just the single tokenizer st – A 2 field with the same tokenizer and just nd first filter – A 3 field that adds a second tokenizer rd

– Be prepared to show output values for each stage.

000-DTSE-Search-7446-60-PL-3 © DataStax, All Rights Reserved. Confidential.

Challenge 3: AND, OR-Topped queries

• Use CQL commands to create, and Solr

Admin UI to test (query)

• Create a DSE table with at least two non-

primary key columns, add data

• Using these two query strings, and

debugQuery

– (col3:ddd AND col4:eee) – (col3:ddd OR col4:eee)

be prepared to discuss the differences in

the (explain plans).

000-DTSE-Search-7446-60-PL-4 © DataStax, All Rights Reserved. Confidential.

Discussion Lab:

Lessons learned

000-DTSE-Search-7446-60-PL-5 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7446-60-PL-6
