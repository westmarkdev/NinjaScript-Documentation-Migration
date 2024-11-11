---
title: CountIf()
pathName: countif
parent: analytical
section: references
status: review
---

## Definition

Counts the number of instances the test condition occurs over the look-back period expressed in bars.

{% callout type="note" %}

This method does NOT work on **multi-series** strategies and indicators.

{% /callout %}

## Method Return Value

An **int** value representing the number of occurrences found.

## Syntax

CountIf(**Func<`bool`>** condition, **int** period)

## Parameters

{% table %}

---

* **condition**
* A true/false expression

---

* **period**
* Number of bars to check for the test condition
{% /table %}

{% callout type="note" %}

Tip: The syntax for the "condition" parameter uses [lambda expression](http://msdn.microsoft.com/en-us/library/bb397687.aspx) syntax.

{% /callout %}

## Examples

```csharp
// If in the last 10 bars we have had 8 up bars then go long
if (CountIf(() => Close[0] > Open[0], 10) > 8)
     EnterLong();
```
