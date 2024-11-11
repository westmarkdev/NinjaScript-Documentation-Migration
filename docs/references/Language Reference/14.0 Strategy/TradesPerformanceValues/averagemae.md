---
section: references
status: review
parent: tradesperformancevalues
title: AverageMae
pathName: averagemae
---

## Definition

Returns the average MAE (max adverse excursion) of the collection.

## Property Value

A **double** value that represents the average MAE of the collection.

## Syntax

tradecollection.TradesPerformance.tradesperformancevalues.**AverageMae**

## Examples

{% callout type="note" %}

The following example shows how to print out the average MAE of all trades in currency.

{% /callout %}

```csharp
protected override void OnBarUpdate()
{
     // Print out the average MAE of all trades in currency
     Print("Average MAE of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.AverageMae);
}
```
