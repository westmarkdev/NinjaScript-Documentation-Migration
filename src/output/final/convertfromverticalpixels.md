---
title: "ConvertFromVerticalPixels"
pathName: /docs/desktop/convertfromverticalpixels
---

## Definition

Converts a y-axis pixel coordinate from device pixels to application pixels.

{% callout type="note" %}
For more information concerning the differences between application pixels and device pixels, please see the [Working with Pixel Coordinates](/docs/desktop/working_with_pixel_coordinates) educational resource.
{% /callout %}

## Method Return Value

A double representing a y-coordinate value in terms of application pixels.

## Syntax

```csharp
ChartingExtensions.ConvertFromVerticalPixels(this int x, PresentationSource target)
<int>.ConvertFromVerticalPixels(PresentationSource target)
```

## Parameters

|  |  |
| --- | --- |
| x | The vertical int coordinates in device pixels to convert. |
| target | The [PresentationSource](https://msdn.microsoft.com/en-us/library/system.windows.presentationsource(v=vs.110).aspx) representing the display surface used for the conversion. {% <br> %} Note: For Charts, see [ChartControl.PresentationSource](/docs/desktop/presentationsource). |

## Example

```csharp
int applicationPixelY;
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // Obtain the application-pixel coordinate corresponding to a device-pixel Y value of 500
    applicationPixelY = ChartingExtensions.ConvertFromVerticalPixels(500, ChartControl.PresentationSource);
}
```
