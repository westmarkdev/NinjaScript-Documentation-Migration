---
title: "ConvertFromHorizontalPixels"
pathName: /docs/desktop/convertfromhorizontalpixels
---

## Definition

Converts an x-axis pixel coordinate from device pixels to application pixels.

{% callout type="note" %}
For more information concerning the differences between application pixels and device pixels, please see the [Working with Pixel Coordinates](/docs/desktop/working_with_pixel_coordinates) educational resource.
{% /callout %}

## Method Return Value

A double representing an x-coordinate value in terms of application pixels.

## Syntax

```csharp
ChartingExtensions.ConvertFromHorizontalPixels(this int x, PresentationSource target)
<int>.ConvertFromHorizontalPixels(PresentationSource target)
```

## Parameters

|  |  |
| --- | --- |
| x | The horizontal int coordinates in device pixels to convert. |
| target | The [PresentationSource](https://msdn.microsoft.com/en-us/library/system.windows.presentationsource(v=vs.110).aspx) representing the display surface used for the conversion. {% <br> %} **Note**: For Charts, see [ChartControl.PresentationSource](/docs/desktop/presentationsource). |

## Example

```csharp
int applicationPixelX;

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // Obtain the application-pixel coordinate corresponding to a device-pixel X value of 500
    applicationPixelX = ChartingExtensions.ConvertFromHorizontalPixels(500, ChartControl.PresentationSource);
}
```
