---
title: DrawOnPricePanel
pathName: drawonpricepanel
parent: indicator
section: references
status: imported
---

## Definition

Determines the chart panel the draw objects renders

## Property Value

This property returns true if the indicator paints draw objects on the price panel; otherwise when false, draw objects are painted on the actual indicator panel itself. Default set to true.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults**. Dynamically using **DrawOnPricePanel** in an indicator outside of **State.SetDefaults** may show issues when working with that indicator through a hosting strategy via **AddChartIndicator()**.

{% /callout %}

## Syntax

**DrawOnPricePanel**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
          DrawOnPricePanel = false; // Draw objects now paint on the indicator panel itself     
          AddPlot(Brushes.Orange, "SMA");
     }
}
```
