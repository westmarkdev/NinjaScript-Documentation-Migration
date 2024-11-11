---
title: Quantity
pathName: quantity
parent: strategy
section: references
status: imported
---

## Definition

Gets the strategy's current position size.

## Property Value

An **int** value representing the position size.

## Syntax

**Position.Quantity**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Prints out the current market position
     Print(Position.MarketPosition.ToString() + " " + Position.Quantity.ToString());
}
```
