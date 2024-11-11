---
title: GrossProfit
pathName: grossprofit
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the gross profit.

## Property Value

A **double** value that represents the gross profit.

## Syntax

<`tradecollection`>.TradesPerformance.**GrossProfit**

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the gross profit of all trades
    Print("Gross profit is: " + SystemPerformance.AllTrades.TradesPerformance.GrossProfit);
}
```
