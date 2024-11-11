---
title: MouseDownPoint
pathName: mousedownpoint
parent: chartcontrol
section: references
status: review
---

## Definition

Indicates the WPF x- and y-coordinates of the mouse cursor at the most recent **OnMouseDown()** event.

## Property Value

A [Point](https://msdn.microsoft.com/en-us/library/system.drawing.point(v=vs.110).aspx) object containing x- and y-coordinates of the mouse cursor when the left mouse button is clicked or held.

## Syntax

**<`chartcontrol`>.MouseDownPoint**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   Point cursorPoint = chartControl.MouseDownPoint;
 
   // Print the x- and y-coordinates of the mouse cursor when clicked
   Print(String.Format("Mouse clicked at coordinates {0},{1}", cursorPoint.X, cursorPoint.Y));
}
```
