---
title: GetTimeByX()
pathName: gettimebyx
parent: chartcontrol
section: references
status: review
---

## Definition

Returns a time value related to the primary **Bars** slot index at a specified x-coordinate relative to the **ChartControl**.

{% callout type="note" %}

Since the time is based upon a coordinate of the chart canvas, the value returned by **GetTimeByX()** can be expected to change as new bars are painted on the chart, or as the chart is scrolled backward or forward on the x-axis.

{% /callout %}

## Method Return Value

A **DateTime** object corresponding to a slot index at a specified x-coordinate.

## Syntax

**<`chartcontrol`>.GetTimeByX(int x)**

## Method Parameters

{% table %}

---

* x
* The x-coordinate used to find a time value
{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Find the timestamp of the bar at x-coordinate 100
   DateTime slotTime = chartControl.GetTimeByX(100);
 
   // Print the date of slotTime
   Print(slotTime);
}
```
