---
title: TimePainted
pathName: timepainted
parent: chartcontrol
section: references
status: review
---

## Definition

Indicates the range of time in which bars are painted on the visible chart canvas.

## Property Value

A TimeSpan measuring the difference between the earliest and latest times at which bars are painted on the chart.

## Syntax

**<`chartcontrol`>.TimePainted**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print a message if less than three hours' worth of data is painted on the chart canvas
   if(chartControl.TimePainted.Hours < 3)
       Print(String.Format("It is recommended to view at least three hours worth of data on your chart with this indicator. You are currently viewing {0}", chartControl.TimePainted));
}
```

{% callout type="note" %}

Note: TimePainted is intended to be used when Non-Equidistant (time-based) bar spacing is enabled on the chart. Otherwise, it will have a value of 0.

{% /callout %}
