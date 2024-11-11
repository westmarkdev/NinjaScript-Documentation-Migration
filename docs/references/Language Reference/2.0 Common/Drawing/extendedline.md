---
title: ExtendedLine
pathName: extendedline
parent: drawing
section: references
status: review
---

## Definition

Represents an interface that exposes information regarding an Extended Line **IDrawingTool**.

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
// Instantiate a dotted lime green Extended Line
ExtendedLine myLine = Draw.ExtendedLine(this, "tag1", 10, Close[10], 0, Close[0], Brushes.LimeGreen, DashStyleHelper.Dot, 2);

// Make the line a Global Drawing Object
myLine.IsGlobalDrawingTool = true;
```
