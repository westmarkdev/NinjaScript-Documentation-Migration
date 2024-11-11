---
title: High
pathName: high
parent: iseriest
section: references
status: review
---

## Definition

A collection of historical bar high prices.

## Property Value

An **ISeries`<double>`** type object. Accessing this property via an index value **int barsAgo** returns A **double** value representing the price of the referenced bar.

## Syntax

**High**  

**High[int barsAgo]**

## Examples

```csharp
// OnBarUpdate method
protected override void OnBarUpdate()
{
     // Make sure we have at least 20 bars
     if (CurrentBar < 20)
         return;

     // Evaluates for higher highs
     if (High[0] > High[1] && High[1] > High[2])
         Print("Two successive higher highs");

     // Gets the current value of a 20 period SMA of high prices
     double value = SMA(High, 20)[0];
     Print("The value is " + value.ToString());
}
```

\
