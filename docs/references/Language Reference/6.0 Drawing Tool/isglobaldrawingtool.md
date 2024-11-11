---
title: IsGlobalDrawingTool
pathName: isglobaldrawingtool
parent: drawing_tools
status: imported
section: references
---

## Definition

Indicates if the drawing tool is currently set as a Global Drawing object. Global draw objects display on any chart which matches the parent chart's underlying instrument.

## Property Value

A bool value which returns true if the drawing tool is currently attached as a global drawing object; otherwise false.

## Syntax

**IsGlobalDrawingTool**

## Examples

```csharp
public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   // do not interact if attached to global chart
   if (IsGlobalDrawingTool)
     return;
}
```
