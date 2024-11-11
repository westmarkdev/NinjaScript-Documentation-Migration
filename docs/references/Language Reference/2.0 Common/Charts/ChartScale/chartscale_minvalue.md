---
title: MinValue
pathName: minvalue
parent: chartscale
section: references
status: review
---

## Definition

The lowest rendered value on the chart scale.

## Property Value

A **double** value representing the lowest value on the chart scale as a y value.

## Syntax

**<`chartscale>**.MinValue

## Examples

{% callout type="note" %}

In the image below, the lowest value displayed as text on the y-axis reads 2102.50, however as you can see, there are a few pixels on the chart scale below this tick. The absolute rendered MinValue on the chart scale is calculated as 2102.29.

{% /callout %}

![MinValue](minvalue.png)

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{         
   // the minimum value of the chart scale
   double minValue   = chartScale.MinValue;

   Print("minValue: " + minValue);
}
```
