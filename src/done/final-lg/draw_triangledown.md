---
title: "Draw.TriangleDown()"
pathName: draw_triangledown
---

## Definition

Draws a triangle pointing down.

## Method Return Value

A [TriangleDown](triangledown) object that represents the draw object.

## Syntax

```csharp
Draw.TriangleDown(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime time, double y, Brush brush)
```

```csharp
Draw.TriangleDown(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y, Brush brush)
```

```csharp
Draw.TriangleDown(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime time, double y, Brush brush, bool drawOnPricePanel)
```

```csharp
Draw.TriangleDown(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y, Brush brush, bool drawOnPricePanel)
```

```csharp
Draw.TriangleDown(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime time, double y, bool isGlobal, string templateName)
```

```csharp
Draw.TriangleDown(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y, bool isGlobal, string templateName)
```

## Parameters

| Parameter      | Description |
|----------------|-------------|
| owner          | The hosting NinjaScript object which is calling the draw method. Typically will be the object which is calling the draw method (e.g., "this"). |
| tag            | A user defined unique id used to reference the draw object. For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| isAutoScale    | Determines if the draw object will be included in the y-axis scale. |
| barsAgo        | The bar the object will be drawn at. A value of 10 would be 10 bars ago. |
| time           | The time the object will be drawn at. |
| y              | The y value. |
| brush          | The brush used to color draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)). |
| drawOnPricePanel | Determines if the draw-object should be on the price panel or a separate panel. |
| isGlobal       | Determines if the draw object will be global across all charts which match the instrument. |
| templateName   | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead). |

{% callout tip %}
The size of the triangle is tied to the chart's BarWidth and thus will scale automatically as the chart is resized.
{% /callout %}

## Examples

```csharp
// Paints a red triangle pointing down on the current bar 1 tick below the low
Draw.TriangleDown(this, "tag1", true, 0, Low[0] - TickSize, Brushes.Red);
```
