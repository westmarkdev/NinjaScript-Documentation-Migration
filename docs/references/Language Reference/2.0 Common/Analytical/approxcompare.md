---
title: ApproxCompare()
pathName: approxcompare
parent: analytical
section: references
status: review
---

## Definition

Compares two double or float values for equality or being greater than / less than the compared to value.

{% callout type="note" %}

Comparing for being greater than / less is done using an epsilon value of 1E19

{% /callout %}

## Method Return Value

An **int** value representing the outcome of the comparison. Returns 0 if values are equal, 1 if value1 is greater than value2. -1 if value1 is less than value2.

## Syntax

**this.ApproxCompare(this double double1, double double2)**
**this.ApproxCompare(this float float1, double float2)**

## Parameters

{% table %}

* Parameter
* Description

---

* double1 / float1
* First value to compare against (not actually passed in)

---

* double2 / float2
* Second passed in value to compare against

---

{% callout type="note" %}

Main use would be using it for equality comparisons to circumvent running into floating point considerations, value compares for < or > could be usually done more straightforward directly.

{% /callout %}

## Examples

```csharp
// Build the High / Low difference and if 0 sets the indicator main Value series to 0
if ((High[0] - Low[0]).ApproxCompare(0) == 0)
   Value[0] = 0;
```
