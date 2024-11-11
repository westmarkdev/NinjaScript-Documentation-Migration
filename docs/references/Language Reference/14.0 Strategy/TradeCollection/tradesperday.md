---
title: TradesPerDay
pathName: tradesperday
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the average number of trades per day.

## Property Value

An **int** value that represents the average number of trades per day.

## Syntax

<`tradecollection>.TradesPerformance.**TradesPerDay**

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the average number of trades per day of all trades
    Print("Average # of trades per day is: " + SystemPerformance.AllTrades.TradesPerformance.TradesPerDay);
}
```
