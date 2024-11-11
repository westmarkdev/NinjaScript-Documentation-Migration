---
title: GetTime()
pathName: gettime
parent: bars
section: references
status: review
---

## Definition

Returns the time stamp at the current bar index value.

{% callout type="note" %}

This method will return what is displayed in the chart's data box. For formatting purposes, the value returned is NOT guaranteed to be equal to the **[TimeSeries](timeseries)** value. If you are using daily bars and need the session end time, you should use **[Bars.GetSessionEndTime()](getsessionendtime)** instead.

{% /callout %}

## Method Return Value

A DateTime structure that represents the time stamp at the desired bar index.

## Syntax

**Bars.GetTime(int index)**

## Parameters

{% table %}

* Parameter
* Description

---

* index
* An int representing an absolute bar index value
{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    base.OnRender(chartControl, chartScale);
    // loop through only the rendered bars on the chart
    for(int barIndex = ChartBars.FromIndex; barIndex <= ChartBars.ToIndex; barIndex++)
    {
        // get the time stamp at the selected bar index value
        DateTime timeValue = Bars.GetTime(barIndex);
        Print("Bar #" + barIndex + " time stamp is " + timeValue);
    }
}
```
