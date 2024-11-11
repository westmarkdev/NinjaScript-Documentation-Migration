---
status: double_check
pathName: verticalline
title: VerticalLine
parent: drawing
section: references
lg2m: true
---

## Definition

Represents an interface that exposes information regarding a Vertical Line [IDrawingTool](source_files/idrawingtool.md).

## Methods and Properties

{% table %}

* Parameter

* Description

---

* StartAnchor

* An [IDrawingTool's ChartAnchor](source_files/idrawingtool.md#chartanchor) representing the starting point of the drawing object

---

* EndAnchor

* An [IDrawingTool's ChartAnchor](source_files/idrawingtool.md#chartanchor) representing the end point of the drawing object

---

* Stroke

* A [Stroke](stroke_class) object used to draw the object

---

{% /table %}

## Examples

```csharp
// Instantiate a VerticalLine object  
VerticalLine myLine = Draw.VerticalLine(this, "tag1", 10, Brushes.Black);  
   
// Change the object's Stroke  
myLine.Stroke = new Stroke(Brushes.BlanchedAlmond, DashStyleHelper.Dot, 5);
```
