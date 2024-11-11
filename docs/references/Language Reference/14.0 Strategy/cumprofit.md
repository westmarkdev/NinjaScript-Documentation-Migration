---
title: CumProfit
pathName: cumprofit
parent: strategy
section: references
status: imported
---

## Definition

Returns the cumulative profit of the collection.

## Property Value

A **double** value that represents the cumulative profit of the collection.

## Syntax

**<`tradecollection>.TradesPerformance.<`tradesperformancevalues>.CumProfit**

## Examples

```csharp
// Print out the cumulative profit of all trades in currency
protected override void OnBarUpdate()
{
    // Print out the cumulative profit of all trades in currency
    Print("Average cumulative profit of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.CumProfit);
}
```
