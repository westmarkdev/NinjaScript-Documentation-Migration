---
title: Square
pathName: square
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding a Square **IDrawingTool**.

## Methods and Properties

{% table %}

* Parameter

* Description

---

* Anchor

* An **IDrawingTool's ChartAnchor** representing the point of the drawing object

---

* OutlineBrush

* A **Brush** used for the outline of the square

---

* AreaBrush

* A **Brush** object representing the fill color of the draw object

---

{% /table %}

## Examples

```csharp
// Instantiate a Square object
Square mySquare = Draw.Square(this, "tag1", true, 0, Low[0] - TickSize, Brushes.Red);
 
// Change the object's OutlineBrush
mySquare.OutlineBrush = Brushes.Blue;
```
