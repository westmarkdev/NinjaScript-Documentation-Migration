---
section: references
title: Rectangle
pathName: rectangle
parent: drawing
status: review
---

## Definition

Represents an interface that exposes information regarding a Rectangle **IDrawingTool**.

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

* A **Brush** object representing the fill color of the draw object

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
// Instantiate a Rectangle object
Rectangle myRec = Draw.Rectangle(this, "tag1", 10, Low[10] - TickSize, 5, High[5] + TickSize, Brushes.Blue);

// Set the object's AreaBrush to Blue
myRec.AreaBrush = Brushes.Blue;
```
