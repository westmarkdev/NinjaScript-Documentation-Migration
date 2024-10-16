---
title: "Draw.GannFan()"
pathName: /docs/desktop/draw_gannfan
---

## Definition

Draws a Gann Fan.

## Method Return Value

A [GannFan](/docs/desktop/gannfan) object that represents the draw object.

## Syntax

```csharp
Draw.GannFan(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y)  
Draw.GannFan(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime time, double y)  
Draw.GannFan(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y, bool isGlobal, string templateName)
```

## Parameters

|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method. Typically will be the object which is calling the draw method (e.g., "this"). |
| tag | A user defined unique id used to reference the draw object. For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| isAutoScale | Determines if the draw object will be included in the y-axis scale. |
| barsAgo | The bar the object will be drawn at. A value of 10 would be 10 bars ago. |
| time | The time the object will be drawn at. |
| y | The y value. |
| isGlobal | Determines if the draw object will be global across all charts which match the instrument. |
| templateName | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead). |

## Examples

```csharp
// Draws a Gann Fan at the current bar low
Draw.GannFan(this, "tag1", true, 0, Low[0]);
```

