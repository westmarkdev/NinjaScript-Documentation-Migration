---
title: LongestFlatPeriod
pathName: longestflatperiod
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the longest duration of being flat.

## Property Value

A TimeSpan value that represents the longest duration of being flat.

## Syntax

<`tradecollection`>.TradesPerformance.**LongestFlatPeriod**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the longest duration of being flat
     Print("Longest flat period: " + SystemPerformance.AllTrades.TradesPerformance.LongestFlatPeriod);
}
```
