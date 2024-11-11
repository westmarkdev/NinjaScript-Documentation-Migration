---
title: UpdateFromPoint()
pathName: updatefrompoint
parent: chartanchor
section: references
status: imported
---

## Definition

Updates an anchor's x and y values from a given point (in device pixels).

## Method Return Value

This method does not return a value.

## Syntax

**`ChartAnchor`>.UpdateFromPoint(Point point, ChartControl chartControl, ChartScale chartScale)**

## Method Parameters

{% table %}

* Name
* Description

---

* point
* The chart anchor's point value to be updated

___

* chartControl
* A ChartControl representing the x-axis

---

* chartScale
* A ChartScale representing the y-axis

---

{% /table %}

## Examples

```cs
//set the chart anchors x point value

MyAnchor.UpdateXFromPoint(point, chartControl, chartScale);
```
