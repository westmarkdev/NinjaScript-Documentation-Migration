---
title: GetSessionEndTime()
pathName: getsessionendtime
parent: bars
section: references
status: review
---

## Definition

Returns the daily bar session ending time stamp relative to the current bar index value.

{% callout type="note" %}

This method is ONLY intended for bars built from daily data. If called on intraday data, **GetSessionEndTime()** will return the [**Bars.GetTime()**](gettime) value.

{% /callout %}

## Method Return Value

A DateTime structure that represents the daily bars ending time stamp at the desired bar index; intraday bars will return the time stamp at the current bar index value.

## Syntax

**Bars.GetSessionEndTime(int index)**

## Parameters

{% table %}

---

* **index**
* An int representing an absolute bar index value
{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
   // loop through only the rendered bars on the chart
   for (int barIndex = ChartBars.FromIndex; barIndex <= ChartBars.ToIndex; barIndex++)
   {
     // get the time stamp at the selected bar index value
     DateTime timeValue = Bars.GetSessionEndTime(barIndex);
     Print("Bar #" + barIndex + " time stamp is " + timeValue);
   }
```
