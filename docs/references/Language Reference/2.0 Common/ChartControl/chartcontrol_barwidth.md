---
title: BarWidth
pathName: barwidth
parent: chartcontrol
section: references
status: review
---

## Definition

Measures the value of the **bar width** set for the primary Bars object on the chart.

{% callout type="note" %}

This property value is not stated in pixels. To obtain the pixel-width of bars on the chart, use **GetBarPaintWidth()** instead.

{% /callout %}

## Property Value

A double representing the value of the bar width.

## Syntax

**<`chartcontrol`>.BarWidth**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    double barWidth = chartControl.BarWidth;

    // Prints the width of bars on the chart
    Print(barWidth);
}
```

Based on the image below, BarWidth reveals that the bars on the chart are 4.02 pixels wide.

![ChartControl_BarWidth](chartcontrol_barwidth.png)
