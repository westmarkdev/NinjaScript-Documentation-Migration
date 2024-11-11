---
title: GrossLoss
pathName: grossloss
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the gross loss.

## Property Value

A **double** value that represents the gross loss.

## Syntax

<`tradecollection`>.TradesPerformance.**GrossLoss**

## Examples

```csharp

protected override void OnBarUpdate()
{
     // Print out the gross loss of all trades
     Print("Gross loss is: " + SystemPerformance.AllTrades.TradesPerformance.GrossLoss);
}
```
