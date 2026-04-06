# DSE Search: DSE Search, Text Part 2

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Search curriculum and need help with dse search, text part 2. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, text part 2.

## Downloads

- [PDF slides](./7450-dse-search-text-part-2.pdf)
- [Original PowerPoint](../000-DTSE-Search-7450-PL-60%2C%20DSE%20Search%2C%20Text%20Part%202.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Module 7449, where most of Practice Lab: the objects we create in this lab were

introduced. DSE Search, Text Part 2

• This Practice Lab requires a working DSE

system, with DSE Search enabled, and

with ability to execute CQL DDL.

• All other commands are run from CQLSH,

DSE Studio, or the Solr Admin UI.

000-DTSE-Search-7450-60-PL-1 © DataStax, All Rights Reserved. Confidential.

Challenge 1: Score using Solr Admin UI

.. VALUES ('aaa', 'test space ‘ , 'test'); .. VALUES ('bbb', 'space test ‘ , 'test'); .. VALUES ('ccc', 'test one two space ‘ , 'test'); • Use CQL to CREATE TABLE, .. VALUES ('ddd', 'test one two three space ‘ , 'test'); .. VALUES ('eee', 'test one two three four space ‘ , 'test'); CREATE | ALTER SEARCH

INDEX, INSERT (data)

• Use Solr Admin UI to observe Tf-

Idf scoring as outlined in module

7449.

000-DTSE-Search-7450-60-PL-2 © DataStax, All Rights Reserved. Confidential.

Challenge 1: Score using Solr Admin UI

You are done when

you have produced

screens similar to

these, and

understand score,

and Tf-Idf values- "ddd": "0.7590632 = weight(col2:three in 4) [], result of: 0.7590632 = score (doc=4,freq=1.0 = termFreq=1.0), product of: 0.87546873 = idf(docFreq=2, docCount=5)

0.86703634 = tfNorm, computed from: 1.0 = termFreq=1.0 1.2 = parameter k1

0.75 = parameter b 3.8 = avgFieldLength 5.2244897 = fieldLength“

"eee": "0.6454073 = weight(col2:three in 0) [], result of: 0.6454073 = score (doc=0,freq=1.0 = termFreq=1.0), product of: 0.87546873 = idf(docFreq=2, docCount=5)

0.73721343 = tfNorm, computed from: 1.0 = termFreq=1.0 1.2 = parameter k1

0.75 = parameter b 3.8 = avgFieldLength 7.111111 = fieldLength"

000-DTSE-Search-7450-60-PL-3 © DataStax, All Rights Reserved. Confidential.

Challenge 2: Boosting Query-

• Create two columns; one straight

index, one sounds like.

• Create an OR query with the

straight index boosted higher than

the sounds like.

• Test to ensure exact match

columns return higher

000-DTSE-Search-7450-60-PL-4 © DataStax, All Rights Reserved. Confidential.

Challenge 3: Experiment with Fuzzy Search

• Create two columns; both

straight index

• Create an OR query with the

straight index boosted higher

than the fuzzy search.

• Test to ensure exact match

columns return higher

SELECT * FROM t6

WHERE solr_query =

'{ "q" : "(col73:%huck^8 OR

col74:chuck~1)" }' ;

000-DTSE-Search-7450-60-PL-5 © DataStax, All Rights Reserved. Confidential.

Discussion Lab:

Lessons learned

000-DTSE-Search-7450-60-PL-6 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7450-60-PL-7
