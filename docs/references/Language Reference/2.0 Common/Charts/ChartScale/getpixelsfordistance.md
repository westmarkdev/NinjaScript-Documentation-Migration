---
title: GetPixelsForDistance()
pathName: getpixelsfordistance
parent: chartscale
section: references
status: review
---

## Definition

Returns the number of device pixels between the value passed to the method representing a series point value on the chart scale.

## Method Return Value

A float representing the number of pixels between a value.

## Syntax

**<`chartscale>**.GetPixelsForDistance(double distance)

## Method Parameters

{% table %}

---

* distance
* A **double** value representing the distance in points to be measured
{% /table %}

## Examples

```csharp

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // the number of pixels between the point value passed as a distance to the method
   float pixelForDistance = chartScale.GetPixelsForDistance(0.25);

   Print("pixelForDistance: " + pixelForDistance); //20 pixels per every 1 tick on the chart scale

}
```

In the image below, we pass a value of 1 for the distance, which tells us there are 76 pixels for every 1 point on the ES 06-15 chart scale.

![GetPixelsForDistance](getpixelsfordistance.png)
