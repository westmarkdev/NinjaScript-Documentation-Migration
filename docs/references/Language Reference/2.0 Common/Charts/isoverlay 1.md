---
title: IsOverlay
pathName: isoverlay
parent: charts
section: references
status: review
---

## Definition

Determines if indicator plot(s) are drawn on the chart panel over top of price. Setting this value to true will also allow an Indicator to be used as a [SuperDOM Indicator](working_with_indicators_superdom).

## Property Value

This property returns true if any indicator plot(s) are drawn on the chart panel; otherwise, false. Default set to false.

{% callout type="warning" %}
This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults**.
{% /callout %}

## Syntax

**IsOverlay**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        IsOverlay = true; // Indicator plots are drawn on the chart panel on top of price     
        AddPlot(Brushes.Orange, "SMA");
    }
}
```
