---
title: AverageTimeInMarket
pathName: averagetimeinmarket
parent: tradesperformance
section: references
status: imported
---

## Definition

Returns the average duration of a trade weighted by quantity.

## Property Value

A TimeSpan value that represents the quantity-weighted average duration of a trade.

## Syntax

**TradesPerformance.AverageTimeInMarket**

## Examples

{% callout type="note" %}

Print out the quantity-weighted average duration of all trades

{% /callout %}

```csharp
protected override void OnBarUpdate()
{
     // Print out the quantity-weighted average duration of all trades
     Print("Average time in market: " + SystemPerformance.AllTrades.TradesPerformance.AverageTimeInMarket);
}
```
