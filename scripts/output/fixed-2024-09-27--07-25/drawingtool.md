---
path: drawingtool
title: DrawingTool
---

## Definition

The DrawingTool object which owns a chart anchor.

## Property Value

A IDrawingTool object representing the owner of the chart anchor

## Syntax

`<chartanchor>.DrawingTool
=========================`

## Examples

```csharp
protected override void OnStateChange()
{
if (State == State.SetDefaults)
{
Name = "SampleDrawingTool";
MyAnchor = new ChartAnchor();
MyAnchor.DrawingTool = this; //NinjaTrader.NinjaScript.DrawingTools.SampleDrawingTool
}
else if (State == State.Configure)
{

}
}
```
