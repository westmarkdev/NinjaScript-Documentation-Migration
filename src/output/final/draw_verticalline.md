---
title: "Draw.VerticalLine()"
pathName: /docs/desktop/draw_verticalline
---

## Definition

Draws a vertical line.

## Method Return Value

A [VerticalLine](/docs/desktop/verticalline) object that represents the draw object.

## Syntax

```csharp
Draw.VerticalLine(NinjaScriptBase owner, string tag, DateTime time, Brush brush)  
Draw.VerticalLine(NinjaScriptBase owner, string tag, DateTime time, Brush brush, DashStyleHelper dashStyle, int width, bool drawOnPricePanel)  
Draw.VerticalLine(NinjaScriptBase owner, string tag, int barsAgo, Brush brush)  
Draw.VerticalLine(NinjaScriptBase owner, string tag, int barsAgo, Brush brush, DashStyleHelper dashStyle, int width, bool drawOnPricePanel)  
Draw.VerticalLine(NinjaScriptBase owner, string tag, int barsAgo, bool isGlobal, string templateName)  
Draw.VerticalLine(NinjaScriptBase owner, string tag, DateTime time, bool isGlobal, string templateName)  
```

## Parameters

|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method. Typically will be the object which is calling the draw method (e.g., "this") |
| tag | A user defined unique id used to reference the draw object. For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| barsAgo | The bar the object will be drawn at. A value of 10 would be 10 bars ago. |
| time | The time the object will be drawn at. |
| brush | The brush used to color draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)) |
| dashStyle | DashStyleHelper.Dash{% <br> %} DashStyleHelper.DashDot{% <br> %} DashStyleHelper.DashDotDot{% <br> %} DashStyleHelper.Dot{% <br> %} DashStyleHelper.Solid{% <br> %} Note: Fancier DashStyles like DashDotDot will require more resources than simple DashStyles like Solid. |
| width | The width of the draw object |
| drawOnPricePanel | Determines if the draw-object should be on the price panel or a separate panel |
| isGlobal | Determines if the draw object will be global across all charts which match the instrument |
| templateName | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead) |

## Examples

```csharp
// Draws a vertical line
Draw.VerticalLine(this, "tag1", 10, Brushes.Black);
```
