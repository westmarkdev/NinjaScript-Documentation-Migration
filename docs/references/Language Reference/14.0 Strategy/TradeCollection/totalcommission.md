---
title: TotalCommission
pathName: totalcommission
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the total commission.

## Property Value

A **double** value that represents the total commission.

## Syntax

<`tradecollection`>.TradesPerformance.**TotalCommission**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the total commission of all trades
     Print("Total commission is: " + SystemPerformance.AllTrades.TradesPerformance.TotalCommission);
}
```
