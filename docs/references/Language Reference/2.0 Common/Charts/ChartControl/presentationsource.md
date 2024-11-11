---
title: PresentationSource
pathName: presentationsource
parent: chartcontrol
section: references
status: review
---

## Definition

Provides a reference to the base window in which the chart is rendered. **PresentationSource** can be used when converting application pixels to/from device pixels via the helper methods in the [ChartingExtensions](chartingextensions) class.

## Property Value

A **PresentationSource** object representing the base window in which the chart is rendered.

## Syntax

**ChartControl.PresentationSource**

## Examples

```csharp
int devicePixelX;
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Obtain the device-pixel coordinate corresponding to an application-pixel X value of 500
   devicePixelX = ChartingExtensions.ConvertToHorizontalPixels(500, ChartControl.PresentationSource);
}
```
