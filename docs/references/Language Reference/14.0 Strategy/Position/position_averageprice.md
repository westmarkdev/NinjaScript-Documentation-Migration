---
title: AveragePrice
pathName: averageprice
parent: position
section: references
status: review
---

## Definition

Gets the average price of a strategy position.

## Property Value

A **double** value representing the position's average price per unit.

## Syntax

**Position.AveragePrice**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Raise stop loss to breakeven when there is at least 10 ticks in profit
     if (Close[0] >= Position.AveragePrice + 10 * TickSize)
         ExitLongStopMarket(Position.Quantity, Position.AveragePrice);
}
```
