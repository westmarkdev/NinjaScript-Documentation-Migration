---
title: "Draw.HorizontalLine()"
pathName: /docs/desktop/draw_horizontalline
---

## Definition

Draws a horizontal line.

## Method Return Value

A [HorizontalLine](/docs/desktop/horizontalline) object that represents the draw object.

## Syntax

```csharp
Draw.HorizontalLine(NinjaScriptBase owner, string tag, double y, Brush brush)  
```

```csharp
Draw.HorizontalLine(NinjaScriptBase owner, string tag, bool isAutoScale, double y, Brush brush, DashStyleHelper dashStyle, int width)  
```

```csharp
Draw.HorizontalLine(NinjaScriptBase owner, string tag, bool isAutoscale, double y, Brush brush, bool drawOnPricePanel)  
```

```csharp
Draw.HorizontalLine(NinjaScriptBase owner, string tag, double y, Brush brush, DashStyleHelper dashStyle, int width, bool drawOnPricePanel)  
```

```csharp
Draw.HorizontalLine(NinjaScriptBase owner, string tag, double y, bool isGlobal, string templateName)  
```

## Parameters

|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method{% <br> %} Typically will be the object which is calling the draw method (e.g., "this") |
| tag | A user defined unique id used to reference the draw object{% <br> %} For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| isAutoScale | Determines if the draw object will be included in the y-axis scale. Default value is false. |
| y | The y value |
| brush | The brush used to color draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)) |
| dashStyle | DashStyleHelper.Dash{% <br> %} DashStyleHelper.DashDot{% <br> %} DashStyleHelper.DashDotDot{% <br> %} DashStyleHelper.Dot{% <br> %} DashStyleHelper.Solid{% <br> %} Note: Fancier DashStyles like DashDotDot will require more resources than simple DashStyles like Solid. |
| width | The width of the draw object |
| isDrawOnPricePanel | Determines if the draw-object should be on the price panel or a separate panel |
| isGlobal | Determines if the draw object will be global across all charts which match the instrument |
| templateName | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead) |

## Examples

```csharp
// Draws a horizontal line
Draw.HorizontalLine(this, "tag1", 1000, Brushes.Black);
```

