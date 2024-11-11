---
title: ShowTransparentPlotsInDataBox
pathName: showtransparentplotsindatabox
parent: indicator
section: references
status: imported
---

## Definition

Determines if plot(s) values which are set to a **Transparent** brush display in the chart data box. The default behavior is to hide any plots which have been configured as a **Transparent** brush, however this behavior can be changed by setting **ShowTransparentPlotsInDataBox** to true on the indicator.

## Property Value

This property returns true if transparent indicator plot(s) values display in the chart data box; otherwise, false. Default set to false.

{% callout type="warning" %}

This property should ONLY be set from the **OnStateChange()** method during **State.SetDefaults** or **State.Configure**.

{% /callout %}

## Syntax

**ShowTransparentPlotsInDataBox**

## Examples

```csharp
protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         ShowTransparentPlotsInDataBox = true;   
         AddPlot(Brushes.Transparent, "MyPlot");
     }
}
```
