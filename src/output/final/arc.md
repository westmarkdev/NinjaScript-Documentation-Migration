---
title: "Arc"
pathName: /docs/desktop/arc
---

## Definition

Represents an interface that exposes information regarding an Arc [IDrawingTool](/docs/desktop/idrawingtool).

## Methods and Properties

|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](/docs/desktop/idrawingtool#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](/docs/desktop/idrawingtool#chartanchor) representing the end point of the drawing object |
| AreaBrush | A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object representing the fill color of the draw object |
| AreaOpacity | An `int` value representing the opacity of the area color |
| ArcStroke | The [Stroke](/docs/desktop/stroke_class) object used to draw the arc line of the object's outline |
| Stroke | The [Stroke](/docs/desktop/stroke_class) object used to draw the straight line of the object's outline |

## Example

```csharp
// Draw an Arc object
Arc myArc = Draw.Arc(this, "myArc", Time[10], Close[10], Time[0], Close[0], Brushes.Blue);
// Set the opacity of the shading between the arc and the chord
myArc.AreaOpacity = 100;
```
