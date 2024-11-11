---
title: ArrowLine
pathName: arrowline
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding an Arrow Line **IDrawingTool**.

## Methods and Properties

{% table %}

* StartAnchor
* EndAnchor
* Stroke

---

* An **IDrawingTool's ChartAnchor** representing the starting point of the drawing object
* An **IDrawingTool's ChartAnchor** representing the end point of the drawing object
* A **Stroke** object used to draw the object
{% /table %}

## Example

```csharp
// Draw an ArrowLine object
ArrowLine myArrow = Draw.ArrowLine(this, "myArrowLine", 3, High[3], 1, High[1], Brushes.Blue, DashStyleHelper.DashDot, 3);

// Disable the arrow's visibility
myArrow.IsVisible = false;
```
