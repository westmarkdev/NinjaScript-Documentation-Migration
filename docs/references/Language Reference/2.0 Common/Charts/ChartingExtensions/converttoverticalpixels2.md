---
title: ConvertToVerticalPixels
pathName: converttoverticalpixels
parent: chartingextensions
section: references
status: review
---

## Definition

Converts a y-axis pixel coordinate from application pixels to device pixels.

{% callout type="note" %}

For more information concerning the differences between application pixels and device pixels, please see the [Working with Pixel Coordinates](working_with_pixel_coordinates).

{% /callout %}

## Method Return Value

An int representing a y-coordinate value in terms of device pixels.

## Syntax

**ChartingExtensions.ConvertToVerticalPixels**(this double x, **PresentationSource** target)  

**double.ConvertToVerticalPixels**(**PresentationSource** target)

## Parameters

{% table %}

* x
* target

---

* The vertical double coordinates in application pixels to convert
* The [PresenationSource](https://msdn.microsoft.com/en-us/library/system.windows.presentationsource(v=vs.110).aspx) representing the display surface used for the conversion. Note: For Charts, see [ChartControl.PresentationSource](presentationsource).
{% /table %}

## Examples

```csharp
int devicePixelY;

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // Obtain the device-pixel coordinate corresponding to an application-pixel Y value of 500
    devicePixelY = ChartingExtensions.ConvertToVerticalPixels(500, ChartControl.PresentationSource);
}
```
