---
title: AverageEtd
pathName: averageetd
parent: tradesperformancevalues
section: references
status: imported
---

## Definition

Returns the average ETD (end trade draw down) of the collection.

## Property Value

A **double** value that represents the average ETD of the collection.

## Syntax

**TradesCollection.TradesPerformance.TradesPerformanceValues.AverageEtd**

## Examples

{% callout type="note" %}

The following example prints out the average ETD of all trades in currency.

{% /callout %}

```csharp
protected override void OnBarUpdate()
{
     // Print out the average ETD of all trades in currency
     Print("Average ETD of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.AverageEtd);
}
```
