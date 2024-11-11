---
title: LargestWinner
pathName: largestwinner
parent: tradesperformancevalues
section: references
status: imported
---

## Definition

Returns the largest win amount of the collection.

## Property Value

A **double** value that represents the largest win amount of the collection.

## Syntax

<`tradecollection>.TradesPerformance.<`tradesperformancevalues>.**LargestWinner**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the largest win of all trades in currency
     Print("Largest win of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.LargestWinner);
}
```
