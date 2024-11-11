---
title: AverageTotalEfficiency
pathName: averagetotalefficiency
parent: tradesperformance
section: references
status: imported
---

## Definition

Returns the average total efficiency.

## Property Value

A **double** value that represents the average total efficiency.

## Syntax

**TradesPerformance.AverageTotalEfficiency**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the average total efficiency
     Print("Average total efficiency is: " + SystemPerformance.AllTrades.TradesPerformance.AverageTotalEfficiency);
}
```
