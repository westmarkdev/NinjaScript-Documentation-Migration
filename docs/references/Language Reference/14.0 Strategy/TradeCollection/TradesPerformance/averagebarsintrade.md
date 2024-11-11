---
title: AverageBarsInTrade
pathName: averagebarsintrade
parent: tradesperformance
section: references
status: imported
---

## Definition

Returns the average number of bars per trade.

## Property Value

A **double** value that represents the average number of bars per trade.

## Syntax

**TradesPerformance.AverageBarsInTrade**

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the average number of bars per trade of all trades
    Print("Average # bars per trade is: " + SystemPerformance.AllTrades.TradesPerformance.AverageBarsInTrade);
}
```
