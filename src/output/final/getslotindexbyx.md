---
title: "GetSlotIndexByX()"
pathName: /docs/desktop/getslotindexbyx
---

## Definition

Returns the slot index relative to the chart control corresponding to a specified x-coordinate.

{% callout type="note" %}
&bull; A "Slot" is used in Equidistant [bar spacing](/docs/desktop/barspacingtype) and represents a position on the chart canvas background which may or may not contain a bar. The concept of "Slots" does NOT exist on a Time-Based bar spacing type.  
&bull; If you are looking for information on a bar series, please see [ChartBars.GetBarIdxByX()](/docs/desktop/chartbars_getbaridxbyx).  
&bull; Since the slot index is based on the chart canvas, the value returned by GetSlotIndexByX() can be expected to change as new bars are painted, or as the chart is scrolled backward or forward on the x-axis.
{% /callout %}

## Method Return Value

A double representing a slot index; returns -1 on a time based bar spacing type.

### Syntax

```csharp
## <chartcontrol>.GetSlotIndexByX(int x)
```

## Method Parameters

|  |  |
| --- | --- |
| x | An `int` used to determine a slot index. |

## Example

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // Find the index of the bar painted at x-coordinate 35
    double slotIndex = chartControl.GetSlotIndexByX(35);
    // Print the slot index of the specified time
    Print(slotIndex);
}
```
