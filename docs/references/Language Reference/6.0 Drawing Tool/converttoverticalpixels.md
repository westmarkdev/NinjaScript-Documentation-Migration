---
title: ConvertToVerticalPixels()
pathName: converttoverticalpixels
parent: drawing_tools
status: imported
section: references
---

## Definition

Used to convert the cursor position (pixels) to device pixels represented on the Y axis of the chart. This method would only be needed if the value you are given is provided in WPF pixel point (such as the data point used in **OnMouseDown**), but you would need the value in the chart's rendered pixels. This is useful when handling drawing tools and charts which would have multiple chart panels.

## Method Return Value

An **int** value representing the converted value in device pixels.

## Syntax

**ConvertToVerticalPixels(ChartControl chartControl, ChartPanel chartPanel, double wpfY)**

## Method Parameters

{% table %}

---

* **chartControl**
* A **ChartControl** representing the x-axis

---

* **chartPanel**
* A **ChartPanel** representing the the panel for the chart

---

* **wpfY**
* A **double** value which needs to be converted
{% /table %}

## Examples

```csharp

public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   //get chart anchors data point when mouse is clicked
   Point myPoint = dataPoint.GetPoint(chartControl, chartPanel, chartScale);

   Print("before convert: " + myPoint.Y); //before convert: 630.5

   //convert the data point to device pixels
   double yPixel = ConvertToVerticalPixels(chartControl, chartPanel, myPoint.Y);

   Print("after convert: " + yPixel); //after convert: 1108
}
```
