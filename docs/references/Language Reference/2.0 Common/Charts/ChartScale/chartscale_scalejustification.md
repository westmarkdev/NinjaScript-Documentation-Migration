---
title: ScaleJustification
pathName: scalejustification
parent: chartscale
section: references
status: review
---

## Definition

Indicates the location of the chart scale relative to the chart control.

## Property Value

A **ScaleJustification** enum. Possible values are:

* **Right**
* **Left**
* **Overlay**

## Syntax

**ScaleJustification**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if (chartScale.ScaleJustification == ScaleJustification.Right)
   {
     // do something
   }

}
```
