---
title: Height
pathName: height
parent: chartscale
section: references
status: review
---

## Definition

Indicates the overall distance (from top to bottom) of the chart scale.

## Note

{% callout type="note" %}

Height does not return its value in terms of device pixels. However, using **Height.ConvertToVerticalPixels** or **Height.ConvertToHorizontalPixels** will convert the Height value to device pixels. Alternatively, **RenderTarget.PixelSize.Height** or **ChartPanel.H** will also provide the height in terms of device pixels.

{% /callout %}

## Property Value

A **double** value representing the height of the chart scale.

## Syntax

**<`chartscale`>.Height**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // the height of the entire chart scale
   double   height       = chartScale.Height;
   Print("the height of the chart scale is: " + height);  
}
```

In the image below, the entire height of the chart scale is represented by the blue line which is calculated at 300 pixels.

![Height](height.png)
