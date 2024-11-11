---
title: GetVolume()
pathName: getvolume
parent: bars
section: references
status: review
---

## Definition

Returns the volume at the selected bar index value.

## Method Return Value

A long value represents the volume at the desired bar index.

## Syntax

**Bars.GetVolume(int index)**

## Parameters

{% table %}

* index
* An int representing an absolute bar index value
{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
   // loop through all the rendered bars on the chart
   for(int barIndex = ChartBars.FromIndex; barIndex &lt;= ChartBars.ToIndex; barIndex++)
   {
     // get the volume value at the selected bar index value
     long volumeValue = Bars.GetVolume(barIndex);
     Print("Bar #" + barIndex + " volume value is " + volumeValue);
   }
}
```
