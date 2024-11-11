---
title: ProfitPerMonth
pathName: profitpermonth
parent: tradesperformancevalues
section: references
status: imported
---

## Definition

Returns the profit per month of the collection. This value is always returned as a percentage.

## Property Value

A **double** value that represents the profit per month of the collection as a percentage.

## Syntax

<`tradecollection`>.TradesPerformance.<`tradesperformancevalues`>.**ProfitPerMonth**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the profit per month of all trades
     Print("Profit per month of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.ProfitPerMonth);
}
```
