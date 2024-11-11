---
title: ConvertToHorizontalPixels
pathName: converttohorizontalpixels
parent: chartingextensions
section: references
status: review
---

## Definition

Converts an x-axis pixel coordinate from application pixels to device pixels.

{% callout type="note" %}

For more information concerning the differences between application pixels and device pixels, please see the [Working with Pixel Coordinates](working_with_pixel_coordinates).

{% /callout %}

## Method Return Value

An int representing an x-coordinate value in terms of device pixels.

## Syntax

**ChartingExtensions.ConvertToHorizontalPixels**(this double x, **PresentationSource** target)  

**<`double>**.ConvertToHorizontalPixels(**PresentationSource** target)

## Parameters

{% table %}

---

* **x**
* The horizontal double coordinates in application pixels to convert

---

* **target**
* The [PresenationSource](https://msdn.microsoft.com/en-us/library/system.windows.presentationsource(v=vs.110).aspx) representing the display surface used for the conversion.  
Note: For Charts, see [ChartControl.PresentationSource](presentationsource).
{% /table %}

## Examples

```csharp
int devicePixelX;

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // Obtain the device-pixel coordinate corresponding to an application pixel X-value of 500
    devicePixelX = ChartingExtensions.ConvertToHorizontalPixels(500, ChartControl.PresentationSource);
}
```
