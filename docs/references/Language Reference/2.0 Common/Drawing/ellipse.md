---
title: Ellipse
pathName: ellipse
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding an Ellipse **IDrawingTool**.

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

* AreaBrush

* A **Brush** class representing the fill color of the draw object

---

* AreaOpacity

* An **int** value representing the opacity of the area color

---

* OutlineStroke

* The **Stroke** object used to draw the object's outline

---

{% /table %}

## Examples

```csharp
// Paint a red ellipse on the current bar
Ellipse myEllipse = Draw.Ellipse(this, "tag1", true, 5, Close[5], 0, Close[0], Brushes.Red, Brushes.Red, 5);

// Change the AreaOpacity of the Ellipse
myEllipse.AreaOpacity = 0;
```
