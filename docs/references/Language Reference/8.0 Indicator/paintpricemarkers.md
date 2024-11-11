---
title: PaintPriceMarkers
pathName: paintpricemarkers
parent: indicator
section: references
status: imported
---

## Definition

If true, any indicator plot values display price markers in the y-axis.

## Property Value

This property returns true if the indicator plot values display in the y-axis; otherwise, false. Default set to true.

{% callout type="warning" %}

Warning: This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

**PaintPriceMarkers**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         PaintPriceMarkers = true; // Indicator plots values display in the y-axis
         AddPlot(Brushes.Orange, "SMA");
     }
}
```
