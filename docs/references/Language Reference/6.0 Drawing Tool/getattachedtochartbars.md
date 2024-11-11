---
title: GetAttachedToChartBars()
pathName: getattachedtochartbars
parent: drawing_tools
status: imported
section: references
---

## Definition

Returns information which relate to the underlying bars series in which the drawing tool is attached. If the drawing tool is attached to an indicator rather than a bar series, the indicator's bars series used for input will be returned.

{% callout type="note" %}

For drawing tools made global, this method will not be returning meaningful values - since those are not attached to a specific bars series.

{% /callout %}

## Method Return Value

A **ChartBars** object

## Syntax

**GetAttachedToChartBars()**

## Method Parameters

This method does not accept any parameters.

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{   
   // get the attached chart bars
   ChartBars myBars = GetAttachedToChartBars();
   
   Print(myBars.Bars.ToChartString()); // NQ 03-15 (1 Minute)
}
```
