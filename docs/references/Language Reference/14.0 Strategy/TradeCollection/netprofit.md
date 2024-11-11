---
title: NetProfit
pathName: netprofit
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the net profit.

## Property Value

A **double** value that represents the net profit.

## Syntax

<`tradecollection`>.TradesPerformance.**NetProfit**

## Examples

```csharp
protected override void OnBarUpdate()
// Print out the net profit of all trades
Print("Net profit is: " + SystemPerformance.AllTrades.TradesPerformance.NetProfit);
```
