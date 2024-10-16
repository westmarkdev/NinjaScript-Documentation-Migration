---
title: "GetTimeByX()"
pathName: /docs/desktop/gettimebyx
---

## Definition

Returns a time value related to the primary [Bars](/docs/desktop/bars)' slot index at a specified x-coordinate relative to the ChartControl.

{% callout type="note" %}
Since the time is based upon a coordinate of the chart canvas, the value returned by GetTimeByX() can be expected to change as new bars are painted on the chart, or as the chart is scrolled backward or forward on the x-axis.
{% /callout %}

## Method Return Value

A [DateTime](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx) object corresponding to a slot index at a specified x-coordinate.

## Syntax

```csharp
## <chartcontrol>.GetTimeByX(int x)
```

## Method Parameters

|  |  |
| --- | --- |
| x | The x-coordinate used to find a time value |

## Example

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // Find the timestamp of the bar at x-coordinate 100
    DateTime slotTime = chartControl.GetTimeByX(100);
    // Print the date of slotTime
    Print(slotTime);
}
```
