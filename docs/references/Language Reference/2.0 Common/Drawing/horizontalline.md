---
title: HorizontalLine
pathName: horizontalline
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding a Horizontal Line **IDrawingTool**.

## Methods and Properties

{% table %}

* StartAnchor
* Stroke

---

* An **IDrawingTool's ChartAnchor** representing the starting point of the drawing object
* A **Stroke** object used to draw the object
{% /table %}

## Examples

```csharp
// Instantiate a HorizontalLine object
HorizontalLine myLine = Draw.HorizontalLine(this, "tag1", 1000, Brushes.Black);

// Set a new Stroke for the object
myLine.Stroke = new Stroke(Brushes.Green, DashStyleHelper.Dash, 5);
```
