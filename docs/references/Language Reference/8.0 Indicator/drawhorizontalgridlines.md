---
title: DrawHorizontalGridLines
pathName: drawhorizontalgridlines
parent: indicator
section: references
status: imported
---

## Definition

Plots horizontal grid lines on the indicator panel.

{% callout type="note" %}

The indicator panel's parent chart has a similar option 'Grid line - horizontal' which if Visible property set to false, will override the indicator's local setting if true.

{% /callout %}

## Property Value

This property returns true if horizontal grid lines are plotted on the indicator panel; otherwise, false. Default set to true.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during State.SetDefaults or State.Configure.

{% /callout %}

## Syntax

**DrawHorizontalGridLines**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         DrawHorizontalGridLines = false; // Horizontal grid lines will not plot on the indicator panel     
         AddPlot(Brushes.Orange, "SMA");
     }
}
```
