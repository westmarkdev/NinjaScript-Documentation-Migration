---
title: AverageExitEfficiency
pathName: averageexitefficiency
parent: tradesperformance
section: references
status: imported
---

## Definition

Returns the average exit efficiency.

## Property Value

A **double** value that represents the average exit efficiency.

## Syntax

**TradesPerformance.AverageExitEfficiency**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the average exit efficiency
     Print("Average exit efficiency is: " + SystemPerformance.AllTrades.TradesPerformance.AverageExitEfficiency);
}
```
