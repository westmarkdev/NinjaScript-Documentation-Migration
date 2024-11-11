---
title: Ticks
pathName: ticks
parent: tradecollection
section: references
status: imported
---

## Definition

Returns a **TradesPerformanceValues** object in ticks.

## Property Value

A **TradesPerformanceValues** object that is represented in ticks.

## Syntax

<`tradecollection`>.TradesPerformance.**Ticks**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the avg. profit of all trades in ticks
     Print("Average profit: " + SystemPerformance.AllTrades.TradesPerformance.Ticks.AverageProfit);
}
```
