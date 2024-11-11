---
title: CreateAnchor()
pathName: createanchor
parent: drawing_tools
section: references
status: review
---

## Definition

Used to create a new chart anchor at a specified mouse point.

## Method Return Value

A new **ChartAnchor** at a specified point in device pixels.

## Syntax

**CreateAnchor(Point point, ChartControl chartControl, ChartScale chartScale)**

## Method Parameters

{% table %}

---

* **point**
* A Point in device pixels representing the current mouse cursor position

---

* **chartControl**
* A ChartControl representing the x-axis

---

* **chartScale**
* A ChartScale representing the y-axis
{% /table %}

## Examples

```csharp
public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)**
{
   // get the point where the mouse was clicked
   Point myPoint = dataPoint.GetPoint(chartControl, chartPanel, chartScale);

   // create an anchor at that point
   ChartAnchor MyAnchor = CreateAnchor(myPoint, chartControl, chartScale);

   Print(MyAnchor.Time); // 3/16/2015 8:18:48 AM
}
```
