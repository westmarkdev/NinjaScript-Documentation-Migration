---
section: references
title: Polygon
pathName: polygon
parent: drawing
status: review
---

## Definition

Represents an interface that exposes information regarding a **Polygon** **IDrawingTool**.

## Methods and Properties

{% table %}

* Parameter

* Description

---

* StartAnchor

* An **IDrawingTool's ChartAnchor** representing the starting point of the drawing object

---

* EndAnchor

* An **IDrawingTool's ChartAnchor** representing the end point of the drawing object

---

* Stroke

* A **Stroke** object used to draw the object

---

{% /table %}

## Examples

```csharp
// Instantiate a Polygon object
Polygon myPolygon = Draw.Polygon(this, "tag1", false, 20, 194, 10, 184, 13, 176, 25, 182);

// Set a new area brush for the object
myPolygon.AreaBrush = Brushes.Green;
```
