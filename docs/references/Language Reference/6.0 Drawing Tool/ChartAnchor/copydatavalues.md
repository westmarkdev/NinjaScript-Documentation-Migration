---
title: CopyDataValues()
pathName: copydatavalues
parent: chartanchor
status: imported
section: references
---

## Definition  

Copies the **ChartAnchor** time and price values from one anchor to another. This includes the **BarsAgo**, **SlotIndex**, **Time**, **Price**, and **DrawnOnBar** values. This method is useful for updating a chart anchor to a recent data point when the user interacts with the drawing chart anchor.  

## Method Return Value

This method does not return a value.

## Syntax

`<chartanchor>`.CopyDataValues(ChartAnchor toAnchor)

## Method Parameters

{% table %}

---

* toAnchor
* The ChartAnchor to copy
{% /table %}

## Examples

```csharp

public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   // if the user is moving the draw object, copy the most recent dataPoint to MyAnchor
   if (DrawingState == DrawingState.Moving)
     dataPoint.CopyDataValues(Anchor);
```
