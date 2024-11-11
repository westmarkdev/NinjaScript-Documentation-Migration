---
status: double_check
title: Triangle
parent: draw_triangle
pathName: triangle
section: references
lg2m: true
---

## Definition

Represents an interface that exposes information regarding a Triangle [IDrawingTool](source_files/idrawingtool.md).

## Methods and Properties

{% table %}

* Parameter

* Description

---

* StartAnchor

* An [IDrawingTool's ChartAnchor](source_files/idrawingtool.md#chartanchor) representing the starting point of the drawing object

---

* MiddleAnchor

* An [IDrawingTool's ChartAnchor](source_files/idrawingtool.md#chartanchor) representing the middle point of the drawing object

---

* EndAnchor

* An [IDrawingTool's ChartAnchor](source_files/idrawingtool.md#chartanchor) representing the end point of the drawing object

---

* AreaBrush

* A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) class representing the fill color of the draw object

---

* AreaOpacity

* An int value representing the opacity of the area color

---

* OutlineStroke

* The [Stroke](stroke_class) object used to draw the object's outline

---

{% /table %}

## Example

```csharp
// Instantiate a Triangle object  
Triangle myTri = Draw.Triangle(this, "tag1", 4, Low[4], 3, High[3], 1, Low[1], Brushes.Blue);              
   
// Change the object's AreaOpacity  
myTri.AreaOpacity = 100;
```
