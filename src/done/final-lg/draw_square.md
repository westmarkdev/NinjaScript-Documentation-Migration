---
title: "Draw.Square()"
pathName: draw_square
---

## Definition

Draws a square.

## Method Return Value

A [Square](square) object that represents the draw object.

## Syntax

```csharp
Draw.Square(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime time, double y, Brush brush)
Draw.Square(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y, Brush brush)
Draw.Square(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime time, double y, Brush brush, bool drawOnPricePanel)
Draw.Square(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y, Brush brush, bool drawOnPricePanel)
Draw.Square(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime time, double y, bool isGlobal, string templateName)
Draw.Square(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y, bool isGlobal, string templateName)
```

## Parameters

| Parameter      | Description                                                                                                                                                       |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| owner          | The hosting NinjaScript object which is calling the draw method. Typically will be the object which is calling the draw method (e.g., "this").                  |
| tag            | A user-defined unique ID used to reference the draw object. For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| isAutoScale    | Determines if the draw object will be included in the y-axis scale.                                                                                            |
| barsAgo        | The bar the object will be drawn at. A value of 10 would be 10 bars ago.                                                                                      |
| time           | The time the object will be drawn at.                                                                                                                          |
| y              | The y value.                                                                                                                                                    |
| brush          | The brush used to color the draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)).            |
| drawOnPricePanel | Determines if the draw object should be on the price panel or a separate panel.                                                                               |
| isGlobal       | Determines if the draw object will be global across all charts which match the instrument.                                                                    |
| templateName   | The name of the drawing tool template the object will use to determine various visual properties (an empty string could be used to just use the UI default visuals). |

{% callout type="tip" %}
The size of the square is tied to the chart's BarWidth and thus will scale automatically as the chart is resized.
{% /callout %}

## Examples

```csharp
// Paints a red square on the current bar 1 tick below the low
Draw.Square(this, "tag1", true, 0, Low[0] - TickSize, Brushes.Red);
```