---
section: references
title: ArrowUp
pathName: arrowup
parent: drawing
status: review
---

## Definition

Represents an interface that exposes information regarding an Arrow Up [IDrawingTool](idrawingtool).

## Methods and Properties

{% table %}

* Anchor
* An [IDrawingTool's ChartAnchor](idrawingtool.md#chartanchor) representing the point of the drawing object

---

* AreaBrush
* A **Brush** object representing the fill color of the draw object

---

* OutlineBrush
* A **Brush** object representing the color of the draw object's outline
{% /table %}

## Example

```csharp
// Instantiate an ArrowDown object
ArrowUp myArrow = Draw.ArrowUp(this, "tag1", true, Time[0], Low[0] - (2 * TickSize), Brushes.Green);

// Set the outline color of the Arrow
myArrow.OutlineBrush = Brushes.Black;
```
