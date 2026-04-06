# DSE Search: DSE Search, Query Syntax

<table>
  <tr>
    <td><a href="../../core/README.md"><strong>DSE Core</strong></a></td><td><strong>DSE Search</strong></td><td><a href="../../analytics/README.md"><strong>DSE Analytics</strong></a></td><td><a href="../../graph/README.md"><strong>DSE Graph</strong></a></td>
  </tr>
</table>


**Module Type:** Practical Lab

**Customer:** I am working through the DSE Search curriculum and need help with dse search, query syntax. What does this training module cover, and when should I use the techniques it introduces?

**Daniel:** This practical lab in the DSE Search track introduces the topic and shows how it fits into the overall platform. It is intended as a training module rather than a product reference, so the emphasis is on learning the workflow around dse search, query syntax.

## Downloads

- [PDF slides](./7452-dse-search-query-syntax.pdf)
- [Original PowerPoint](../000-DTSE-Search-7452-PL-60%2C%20DSE%20Search%2C%20Query%20Syntax.pptx)

## Converted Slides

## Practice Lab:

• This Practice Lab is dependent on

Discussion Module 7451, where most of Practice Lab: the objects we create in this lab were

introduced. DSE Search, Query

Syntax, Facets, other • This Practice Lab requires a working DSE

system, with DSE Search enabled, and

with ability to execute CQL DDL.

• No command line prompt is required.

• All commands are run from CQLSH, or

DSE Studio.

000-DTSE-Search-7452-60-PL-1 © DataStax, All Rights Reserved. Confidential.

• Challenge 1: Be Amazon Create the runtime environment to

support the query “computer mouse”,

and return a faceted set of results

similar to those in the image on the

left. (A query response is okay; no

Html required.)

• Design and create the tables, data,

indexes, and query.

• The (data model) should be generic,

so that you can also satisfy the query

“Volvo accessories”, and get an

appropriate facet response.

• You can use a non-tokenized key

value for the initial query.

000-DTSE-Search-7452-60-PL-2 © DataStax, All Rights Reserved. Confidential.

Challenge 1: Be Amazon

• The (data model) should be

generic, so that you can also

satisfy the query “Life is Good”,

and get an appropriate facet

response.

(In other words; prove that your

model works with more than once

product.)

000-DTSE-Search-7452-60-PL-3 © DataStax, All Rights Reserved. Confidential.

Go Farther:

(Optional)

Born in Shrewsbury, England, in 1831 Charles Robert Darwin embarked on a five-year survey voyage around the world on the HMS Beagle; his studies of specimens led him to formulate his theories. https://www.biography.com/people/charles-darwin-9266433

000-DTSE-Search-7452-60-PL-4 © DataStax, All Rights Reserved. Confidential.

Challenge 2 (Optional): Add a leading phrase search-

From Challenge 1-

• It was okay to use a non-tokenized key value for

the initial query.

• Change from marketing; that’s no longer okay.

The initial query should return the same results

for; “computer mouse” or “mouse computer”, “life

is good”, “good life”.

• To save time, you can do all of this work on new

tables, etcetera.

000-DTSE-Search-7452-60-PL-5 © DataStax, All Rights Reserved. Confidential.

Lessons learned

000-DTSE-Search-7452-60-DM-6 © DataStax, All Rights Reserved. Confidential.

End of Module:

© DataStax, All Rights Reserved. Confidential. 000-DTSE-Search-7452-60-DM-7
