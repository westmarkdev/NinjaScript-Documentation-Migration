---
title: MonthlyUlcer
pathName: monthlyulcer
parent: tradecollection
section: references
status: imported
---

## Definition

Returns the monthly Ulcer index.

## Property Value

A **double** value that represents the monthly Ulcer index.

## Syntax

<`tradecollection`>.TradesPerformance.**MonthlyUlcer**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Print out the monthly Ulcer index
     Print("Monthly Ulcer index is: " + SystemPerformance.AllTrades.TradesPerformance.MonthlyUlcer);
}
```
