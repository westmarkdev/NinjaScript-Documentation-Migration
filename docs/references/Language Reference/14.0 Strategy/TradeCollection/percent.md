---
title: Percent
pathName: percent
parent: tradecollection
section: references
status: imported
---

## Definition

Returns a **TradesPerformanceValues** object in percent.

## Property Value

A **TradesPerformanceValues** object that is represented in percent.

## Syntax

**<`tradecollection`>.TradesPerformance.Percent**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the avg. profit of all trades in percent
     Print("Average profit: " + SystemPerformance.AllTrades.TradesPerformance.Percent.AverageProfit);
}
```
