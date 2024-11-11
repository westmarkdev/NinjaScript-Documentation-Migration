---
title: MoveAnchorY()
pathName: moveanchory
parent: chartanchor
status: imported
section: references
---

## Definition

Moves an anchor's y value from start point by a delta point amount.

## Method Return Value

This method does not return a value.

## Syntax

**`<chartanchor>`.MoveAnchorY(Point startPoint, Point deltaPoint, ChartControl chartControl, ChartScale chartScale)**

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
//move only the chart anchors Y (price) value
MyAnchor.MoveAnchorY(lastPoint, newPoint, chartControl, chartPanel, chartScale);
```
