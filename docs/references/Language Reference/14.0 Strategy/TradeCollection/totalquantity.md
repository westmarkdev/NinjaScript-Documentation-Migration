---
title: TotalQuantity
pathName: totalquantity
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the total quantity.

## Property Value

A **double** value that represents the total quantity.

## Syntax

<`tradecollection`>.TradesPerformance.**TotalQuantity**

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the total quantity of all trades
    Print("Total quantity is: " + SystemPerformance.AllTrades.TradesPerformance.TotalQuantity);
}
```
