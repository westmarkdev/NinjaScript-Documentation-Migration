---
status: double_check
title: TriangleDown
parent: draw_triangledown
pathName: triangledown
section: references
lg2m: true
---

## Definition

Represents an interface that exposes information regarding a Triangle Down [IDrawingTool](source_files/idrawingtool.md).

## Methods and Properties

{% table %}

* Parameter

* Description

---

* Anchor

* An [IDrawingTool's ChartAnchor](source_files/idrawingtool.md#chartanchor) representing the point of the drawing object

---

* AreaBrush

* A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) class representing the fill color of the draw object

---

* OutlineBrush

* A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) class representing the outline color of the draw object

---

{% /table %}

## Example

```csharp
// Instantiate a TriangleDown object  
TriangleDown myTri = Draw.TriangleDown(this, "tag1", true, 0, Low[0] - TickSize, Brushes.Red);              
   
// Change the object's AreaBrush  
myTri.AreaBrush = Brushes.Beige;
```
