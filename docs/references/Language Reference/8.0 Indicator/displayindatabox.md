---
title: DisplayInDataBox
pathName: displayindatabox
parent: indicator
section: references
status: imported
---

## Definition

Determines if plot(s) display in the chart data box.

## Property Value

This property returns true if the indicator plot(s) values display in the chart data box; otherwise, false. Default set to true.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

**DisplayInDataBox**

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        DisplayInDataBox = false;   
        AddPlot(Brushes.Orange, "SMA");
    }
}
```
