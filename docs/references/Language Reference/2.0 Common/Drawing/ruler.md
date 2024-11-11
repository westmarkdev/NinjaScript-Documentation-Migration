---
section: references
title: Ruler
pathName: ruler
parent: drawing
status: review
---

## Definition

Represents an interface that exposes information regarding a Ruler **IDrawingTool**.

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

* TextAnchor

* An **IDrawingTool's ChartAnchor** representing the text point of the drawing object

---

* TextColor

* A **Brush** class representing the fill color of the draw object's text area

---

* LineColor

* A **Stroke** object used to draw the object

---

{% /table %}

## Examples

```csharp
// Instantiate a Ruler object
Ruler myRuler = Draw.Ruler(this, "tag1", true, 4, Low[4], 3, High[3], 1, Low[1]);

// Change the object's text color to white
myRuler.TextColor = Brushes.White;
```
