---
title: ArrowDown
pathName: arrowdown
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding an Arrow Down IDrawingTool.

## Methods and Properties

{% table %}

* Anchor
* An IDrawingTool's ChartAnchor representing the point of the drawing object

---

* AreaBrush
* A Brush object representing the fill color of the draw object

---

* OutlineBrush
* A Brush object representing the color of the draw object's outline
{% /table %}

## Example

```csharp
// Instantiate an ArrowDown object
ArrowDown myArrow = Draw.ArrowDown(this, "tag1", true, Time[0], High[0] + (2 * TickSize), Brushes.Green);

// Set the outline color of the Arrow
myArrow.OutlineBrush = Brushes.Black;
```
