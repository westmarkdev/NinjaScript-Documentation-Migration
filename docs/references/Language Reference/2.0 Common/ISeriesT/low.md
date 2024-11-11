---
title: Low
pathName: low
parent: iseriest
section: references
status: review
---

## Definition

A collection of historical bar low prices.

## Property Value

An **ISeries`<double>`** type object. Accessing this property via an index value **int barsAgo** returns A **double** value representing the price of the referenced bar.

## Syntax

**Low**  

**Low[int barsAgo]**

## Examples

```csharp
// Current bar low price
double barLowPrice = Low[0];

// Low price of 10 bars ago
double barLowPrice = Low[10];

// Current bar value of a 20 period exponential moving average of low prices**
double value = EMA[Low, 20](0);
```
