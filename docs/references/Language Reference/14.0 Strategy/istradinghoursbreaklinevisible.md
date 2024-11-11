---
title: IsTradingHoursBreakLineVisible
pathName: istradinghoursbreaklinevisible
parent: strategy
section: references
status: imported
---

## Definition

Plots trading hours break lines on the indicator panel.

{% callout type="note" %}

The indicator panel's parent chart has a similar property **Plot session break line** which if set to false, will override the indicator's local setting if true.

{% /callout %}

## Property Value

This property returns true if trading hours break lines are plotted on the indicator panel; otherwise, false. Default set to true.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

**IsTradingHoursBreakLineVisible**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        IsTradingHoursBreakLineVisible = true;     
        AddPlot(Brushes.Orange, "SMA");
    }
}
```
