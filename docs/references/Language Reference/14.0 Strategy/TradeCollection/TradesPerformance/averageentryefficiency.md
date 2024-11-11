---
title: AverageEntryEfficiency
pathName: averageentryefficiency
parent: tradesperformance
section: references
status: imported
---

## Definition

Returns the average entry efficiency.

## Property Value

A **double** value that represents the average entry efficiency.

## Syntax

**TradesPerformance.AverageEntryEfficiency**

## Examples

{% callout type="note" %}

Print out the average entry efficiency

{% /callout %}

```csharp
protected override void OnBarUpdate()
{
     // Print out the average entry efficiency
     Print("Average entry efficiency is: " + SystemPerformance.AllTrades.TradesPerformance.AverageEntryEfficiency);
}
```
