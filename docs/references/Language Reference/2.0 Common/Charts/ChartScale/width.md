---
status: double_check
title: Width
pathName: width
parent: chartscale
section: references
lg2m: true
---

## Definition

Indicates the overall distance (from left to right) of the chart scale.

{% callout type="note" %}

Width does not return its value in terms of device pixels. However, using Width.ConvertToVerticalPixels or Width.ConvertToHorizontalPixels will convert the Width value to device pixels. Alternatively, RenderTarget.PixelSize.Width or ChartPanel.W will also provide the width in terms of device pixels.

{% /callout %}

## Property Value

A double value representing the width of the chart scale.

## Syntax

<`chartScale`>.Width

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)  
{  
  // the width of the entire chart scale  
  double   width       = chartScale.Width;  
  Print("the width of the chart scale is: " + Width);    
}
```

In the image below, the entire of width of the chart scale is represented by the blue line which is calculated at 450 pixels.

![Width](https://cdn.sanity.io/images/1hlwceal/production/6f2dd3610b9b325c2775878a32954655b7cacff9-535x433.png)
