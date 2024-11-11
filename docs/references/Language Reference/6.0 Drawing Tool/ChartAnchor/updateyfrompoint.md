---
title: UpdateYFromPoint()
pathName: updateyfrompoint
parent: chartanchor
section: references
status: imported
---

## Definition

Updates an anchor's Y value from a given point (in device pixels).

## Method Return Value

This method does not return a value.

## Syntax

**<`ChartAnchor`>.UpdateYFromPoint(Point point, ChartScale chartScale)**

## Method Parameters

{% table %}

* Name
* Description

---

* point
* The chart anchor's point value to be updated

---

* chartScale
* A ChartScale representing the y-axis

---

{% /table %}

## Examples

```csharp
//set the chart anchors x point value

MyAnchor.UpdateYFromPoint(point, chartScale);
```
