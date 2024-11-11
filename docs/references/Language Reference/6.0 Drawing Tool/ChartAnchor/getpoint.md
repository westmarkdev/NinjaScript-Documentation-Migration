---
title: GetPoint()
pathName: getpoint
parent: chartanchor
status: imported
section: references
---

## Definition

Returns a chart anchor's data point in device pixels

## Method Return Value

A **Point** structure; a point value in device pixels for a chart's given panel & scale

## Syntax

**`<chartanchor>`.GetPoint(ChartControl chartControl, ChartPanel chartPanel, ChartScale, bool pixelAlign)**

## Method Parameters

{% table %}

---

* **chartControl**
* A [ChartControl](chartcontrol) representing the x-axis

---

* **chartPanel**
* A [ChartPanel](chartpanel) representing a panel of the chart

---

* **chartScale**
* A [ChartScale](chartscale) representing the y-axis

---

* **pixelAlign**
* An optional bool determining if the data point should be rounded to the closest .5 pixel point
{% /table %}

## Examples

```csharp
//gets the chart anchor's data points
Point anchorPoint = MyAnchor.GetPoint(chartControl, chartPanel, chartScale);
```
