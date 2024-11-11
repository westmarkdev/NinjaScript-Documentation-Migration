---
title: DrawVerticalGridLines
pathName: drawverticalgridlines
parent: indicator
section: references
status: imported
---

## Definition

Plots vertical grid lines on the indicator panel.

{% callout type="note" %}

The indicator panel's parent chart has a similar option 'Grid line - vertical' which if Visible property set to false, will override the indicator's local setting if true.

{% /callout %}

## Property Value

This property returns true if vertical grid lines are plotted on the indicator panel; otherwise, false. Default set to true.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults or State.Configure.

{% /callout %}

## Syntax

**DrawVerticalGridLines**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         DrawVerticalGridLines = false; // Vertical grid lines will not plot on the indicator panel     
         AddPlot(Brushes.Orange, "SMA");
     }
}
```
