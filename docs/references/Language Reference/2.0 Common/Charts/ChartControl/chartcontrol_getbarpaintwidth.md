---
title: GetBarPaintWidth()
pathName: getbarpaintwidth
parent: chartcontrol
section: references
status: review
---

## Definition

Returns the width of the bars in the primary Bars object on the chart, in pixels.

## Method Return Value

A double representing the pixel width of bars on the chart.

## Syntax

**<`chartcontrol`>.GetBarPaintWidth(ChartBars chartBars)**

## Method Parameters

{% table %}

---

* **chartBars**
* A [ChartBars](chartbars) object to measure
{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Use BarsArray[0] to pass in a ChartBars object representing the primary Bars object on the chart
   double barPixelWidth = chartControl.GetBarPaintWidth(chartControl.BarsArray[0]);
 
   // Print the pixel width of bars painted on the chart
   Print(String.Format("Bars on the chart are {0} pixels wide", barPixelWidth));   
}
```

In the image below, **GetBarPaintWidth()** reveals that the bars are being drawn 27 pixels wide on the chart:

![ChartControl_GetBarPaintWidth](chartcontrol_getbarpaintwidth.png)
