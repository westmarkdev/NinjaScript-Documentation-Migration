---
title: LastTimePainted
pathName: lasttimepainted
parent: chartcontrol
section: references
status: review
---

## Definition

Indicates the time of the most recently painted bar on the primary **Bars** object configured on the chart.

## Property Value

A **DateTime** object corresponding to the slot index of the most recently painted bar.

## Syntax

<chartcontrol`>.LastTimePainted

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   DateTime lastSlotTime = chartControl.LastTimePainted;

   // Print the index of the last slot painted on the chart
   Print(lastSlotTime);
}
```

In the image below, LastTimePainted reveals that the last index painted on the chart corresponds to 8/12/17 at 2:10:00 PM.

![ChartControl_LastTimePainted](chartcontrol_lasttimepainted.png)
