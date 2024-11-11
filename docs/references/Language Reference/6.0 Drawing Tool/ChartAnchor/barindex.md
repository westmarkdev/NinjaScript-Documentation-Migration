---
title: SlotIndex
pathName: barindex
parent: chartanchor
status: imported
section: references
---

## Definition

Indicates the nearest bar slot value where anchor is drawn on a chart. In a single series chart there will always be equal number of slots and bars, however for multi-series charts there may be additional slots compared to the bar series your drawing tool resides.

## Property Value

A **double** value representing the current bar.

{% callout type="note" %}

The bar index value is represented as a double as it is possible (and likely) that a given chart anchor is drawn between bars (i.e., if a user draws the tool with snap mode disabled)
{% /callout %}

## Syntax

**ChartAnchor.SlotIndex**

## Examples

```csharp
public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   Print(MyAnchor.SlotIndex); // prints the nearest current bar value
   //4502.02734375
}
```
