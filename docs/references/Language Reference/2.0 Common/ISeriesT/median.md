---
title: Median
pathName: median
parent: iseriest
section: references
status: review
---

## Definition

A collection of historical bar median prices. Median price = (High + Low) / 2.

## Property Value

An **ISeries`<double>`** type object. Accessing this property via an index value **int barsAgo** returns A **double** value representing the price of the referenced bar.

## Syntax

**Median**  

**Median[int barsAgo]**

## Examples

```csharp

//Current bar median price
double barMedianPrice = Median[0];

//  Median price of 10 bars ago
double barMedianPrice = Median[10];

// Current bar value of a 20 period exponential moving average of median prices
double value = EMA[Median, 20](0);
```
