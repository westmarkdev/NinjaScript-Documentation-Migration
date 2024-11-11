---
title: MoveAnchorX()
pathName: moveanchorx
parent: chartanchor
status: imported
section: references
---

## Definition

Moves an anchor's x value from start point by a delta point amount.

## Method Return Value

This method does not return a value.

## Syntax

**`<chartanchor>`.MoveAnchorX(Point startPoint, Point deltaPoint, ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale)**

## Method Parameters

{% table %}

---

* **startPoint**
* The chart anchor's original starting point value

---

* **deltaPoint**
* The chart anchor's new point value to be updated

---

* **chartControl**
* A ChartControl representing the x-axis

---

* **chartScale**
* A ChartScale representing the y-axis
{% /table %}

## Examples

```csharp
//move only the chart anchors x (bar/time) value
MyAnchor.MoveAnchorX(lastPoint, newPoint, chartControl, chartScale);
```
