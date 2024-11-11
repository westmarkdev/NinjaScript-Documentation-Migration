---
title: TradesCount
pathName: tradescount
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the total # of trades.

## Property Value

A **double** value that represents the total # of trades.

## Syntax

<`tradecollection`>.TradesPerformance.**TradesCount**

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the total # of trades
    Print("Trades count is: " + SystemPerformance.AllTrades.TradesPerformance.TradesCount);
}
```
