---
section: references
title: Ray
pathName: ray
parent: drawing
status: review
---

## Definition

Represents an interface that exposes information regarding a Ray **IDrawingTool**.

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
// Instantiate a Ray object
Ray myRay = Draw.Ray(this, "tag1", 10, 1000, 0, 1001, Brushes.LimeGreen);
 
// Set a new Stroke for the object
myRay.Stroke = new Stroke(Brushes.Green, DashStyleHelper.DashDot, 3);
```
