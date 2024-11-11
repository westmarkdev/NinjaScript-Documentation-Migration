---
title: RSquared
pathName: rsquared
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the trade performance R-Squared value.

## Property Value

A **double** value that represents the R-Squared (R2)

## Syntax

<`tradecollection`>.TradesPerformance.**RSquared**

## Examples

```csharp
protected override void OnBarUpdate()
// Print out the R2 value of all trades
Print("R-Squared is: " + SystemPerformance.AllTrades.TradesPerformance.RSquared);
```
