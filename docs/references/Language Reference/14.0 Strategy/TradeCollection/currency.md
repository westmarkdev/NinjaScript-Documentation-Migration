---
title: Currency
pathName: currency
parent: tradecollection
section: references
status: imported
---

## Definition

Returns a **TradesPerformanceValues** object in currency.

## Property Value

A **TradesPerformanceValues** object that is represented in currency.

## Syntax

<`tradecollection`>.TradesPerformance.**Currency**

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the avg. profit of all trades in currency
    Print("Average profit: " + SystemPerformance.AllTrades.TradesPerformance.Currency.AverageProfit);
}
```
