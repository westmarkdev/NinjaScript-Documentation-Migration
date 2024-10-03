---
path: averagemae
title: AverageMae
---

## Definition

Returns the average MAE (max adverse excursion) of the collection.

## Property Value

A double value that represents the average MAE of the collection.

## Syntax

`## <tradecollection>.TradesPerformance.<tradesperformancevalues>.AverageMae`

## Examples

```csharp
protected override void OnBarUpdate()
{
// Print out the average MAE of all trades in currency
Print("Average MAE of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.AverageMae);
}
```
