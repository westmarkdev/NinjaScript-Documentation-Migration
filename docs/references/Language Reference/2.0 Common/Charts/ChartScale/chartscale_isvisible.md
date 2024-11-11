---
title: IsVisible
pathName: isvisible
parent: chartscale
section: references
status: review
---

## Definition

Indicates if the chart scale is viewable on the UI. If the bar series, indicator, or strategy which uses the chart scale is not in view, the chart scale **IsVisible** property will return false.

## Property Value

A bool value, which when true the series used to build the scale is viewable; otherwise false. This property is read-only.

## Syntax

**<`chartscale`>.IsVisible**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{         
   // do not process render info chart scale is not visible
   if(!chartScale.IsVisible)
     return;
}
```
