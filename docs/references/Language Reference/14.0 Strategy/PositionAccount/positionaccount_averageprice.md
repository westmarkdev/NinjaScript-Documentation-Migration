---
title: AveragePrice
pathName: averageprice
parent: positionaccount
section: references
status: imported
---

## Definition

Gets the average price of an account position.

## Property Value

A **double** value representing the account position's average price per unit.

## Syntax

**PositionAccount.AveragePrice**

## Examples

```csharp
protected override void OnBarUpdate()
// Raise stop loss to breakeven when there is at least 10 ticks in profit
if (Close[0] >= PositionAccount.AveragePrice + 10 * TickSize)
    ExitLongStopMarket(PositionAccount.Quantity, PositionAccount.AveragePrice);
```
