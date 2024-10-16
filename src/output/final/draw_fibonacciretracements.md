---
title: "Draw.FibonacciRetracements()"
pathName: /docs/desktop/draw_fibonacciretracements
---

## Definition

Draws a Fibonacci retracement.

## Method Return Value

A [FibonacciRetracements](/docs/desktop/fibonacciretracements) object that represents the draw object.

## Syntax

```csharp
Draw.FibonacciRetracements(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int endBarsAgo, double endY)  
```

```csharp
Draw.FibonacciRetracements(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime endTime, double endY)  
```

```csharp
Draw.FibonacciRetracements(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime endTime, double endY, bool isGlobal, string templateName)  
```

```csharp
Draw.FibonacciRetracements(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int endBarsAgo, double endY, bool isGlobal, string templateName)  
```

## Parameters

|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method.<br>Typically will be the object which is calling the draw method (e.g., "this") |
| tag | A user defined unique id used to reference the draw object.<br>For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| isAutoScale | Determines if the draw object will be included in the y-axis scale. Default value is false. |
| startBarsAgo | The starting bar (x axis coordinate) where the draw object will be drawn. For example, a value of 10 would paint the draw object 10 bars back. |
| startTime | The starting time where the draw object will be drawn. |
| startY | The starting y value coordinate where the draw object will be drawn. |
| endBarsAgo | The end bar (x axis coordinate) where the draw object will terminate. |
| endTime | The end time where the draw object will terminate. |
| endY | The end y value coordinate where the draw object will terminate. |
| isGlobal | Determines if the draw object will be global across all charts which match the instrument. |
| templateName | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead). |

## Examples

```csharp
// Draws a Fibonacci retracement
Draw.FibonacciRetracements(this, "tag1", true, 10, Low[10], 0, High[0]);
```

