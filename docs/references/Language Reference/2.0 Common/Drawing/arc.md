---
title: Arc
pathName: arc
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding an Arc **IDrawingTool**.

## Methods and Properties

{% table %}

* Parameter

* Description

---

* StartAnchor

* An IDrawingTool's ChartAnchor representing the starting point of the drawing object

---

* EndAnchor

* An IDrawingTool's ChartAnchor representing the end point of the drawing object

---

* AreaBrush

* A Brush object representing the fill color of the draw object

---

* AreaOpacity

* An int value representing the opacity of the area color

---

* ArcStroke

* The Stroke object used to draw the arc line of the object's outline

---

* Stroke

* The Stroke object used to draw the straight line of the object's outline

---

{% /table %}

## Example

```csharp
// Draw an Arc object
Arc myArc = Draw.Arc(this, "myArc", Time[10], Close[10], Time[0], Close[0], Brushes.Blue);

// Set the opacity of the shading between the arc and the chord
myArc.AreaOpacity = 100;
```
