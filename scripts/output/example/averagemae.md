---

title: averagemae
pathName: averagemae
created: Thursday, October 3rd 2024, 11:24:29 am
updated: Thursday, October 3rd 2024, 12:16:53 pm
---

## Definition

Returns the average MAE (max adverse excursion) of the collection.  

## Property Value

A double value that represents the average MAE of the collection.

## Syntax

```plaintext
<tradecollection>.TradesPerformance.<tradesperformancevalues>.AverageMae
```

## Examples

```csharp
protected override void OnBarUpdate()
{
    // Print out the average MAE of all trades in currency
    Print("Average MAE of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.AverageMae);
}
```

{% callout type="note" %}  
This example demonstrates how to access the AverageMae property within the context of the OnBarUpdate method for trade performance.  
{% /callout %}
