---
title: AverageMfe
pathName: averagemfe
parent: tradesperformancevalues
section: references
status: imported
---

## Definition

Returns the average MFE (max favorable excursion) of the collection.

## Property Value

A **double** value that represents the average MFE of the collection.

## Syntax

TradeCollection.TradesPerformance.TradesPerformanceValues.**AverageMfe**

## Examples

{% callout type="note" %}

The following example prints out the average MFE of all trades in currency.

{% /callout %}

```csharp
protected override void OnBarUpdate()
{
     // Print out the average MFE of all trades in currency
     Print("Average MFE of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.AverageMfe);
}
```
