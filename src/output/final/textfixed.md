---
title: "TextFixed"
pathName: /docs/desktop/textfixed
---

## Definition

Represents an interface that exposes information regarding a Text Fixed [IDrawingTool](/docs/desktop/idrawingtool).

## Methods and Properties

|  |  |
| --- | --- |
| Anchor | An [IDrawingTool's ChartAnchor](/docs/desktop/idrawingtool#chartanchor) representing the point of the drawing object |
| YPixelOffset | An `int` value representing the offset value in pixels from within the text box area |
| Alignment | Possible values are: {% <br> %} &bull; TextAlignment.Center{% <br> %} &bull; TextAlignment.Far{% <br> %} &bull; TextAlignment.Near{% <br> %} &bull; TextAlignment.Justify{% <br> %} (see the [reference](https://msdn.microsoft.com/en-us/library/system.windows.textalignment%28v=vs.110%29.aspx))  |
| AreaOpacity | An `int` value representing the opacity of the area color |
| AreaBrush | A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) class representing the fill color of the text box |
| DisplayText | A `string` value representing the text to be drawn |
| TextBrush | A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) class representing the color of the text |
| Font | A [Font](/docs/desktop/simplefont_class) object representing the font for the text |
| OutlineStroke | The [Stroke](/docs/desktop/stroke_class) object used to outline the text box |
| TextPosition | Possible values are: {% <br> %} &bull; TextPosition.BottomLeft{% <br> %} &bull; TextPosition.BottomRight{% <br> %} &bull; TextPosition.Center{% <br> %} &bull; TextPosition.TopLeft{% <br> %} &bull; TextPosition.TopRight |

## Example

```csharp
// Instantiate a TextFixed object
TextFixed myTF = Draw.TextFixed(this, "tag1", "Text to draw", TextPosition.TopRight);
// Change the object's TextPosition
myTF.TextPosition = TextPosition.Center;
```
