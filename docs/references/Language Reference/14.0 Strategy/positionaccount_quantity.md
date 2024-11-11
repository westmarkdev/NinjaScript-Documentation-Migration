---
title: Quantity
pathName: quantity
parent: strategy
section: references
status: imported
---

## Definition

Gets the current account's position size.

## Property Value

An **int** value representing the account's position size.

## Syntax

**PositionAccount.Quantity**

## Examples

```csharp
protected override void OnBarUpdate()
{ 
    // Prints out the current market position
    Print(PositionAccount.MarketPosition.ToString() + " " + PositionAccount.Quantity.ToString());
}
```
