---
title: "GetSessionEndTime()"
pathName: /docs/desktop/getsessionendtime
---

## Definition

Returns the daily bar session ending time stamp relative to the current bar index value.

{% callout type="note" %}
This method is ONLY intended for bars built from daily data. If called on intraday data, GetSessionEndTime() will return the [Bars.GetTime()](/docs/desktop/gettime) value.
{% /callout %}

## Method Return Value

A DateTime structure that represents the daily bars ending time stamp at the desired bar index; intraday bars will return the time stamp at the current bar index value.

## Syntax

```csharp
Bars.GetSessionEndTime(int index)
```

## Parameters

|  |  |
| --- | --- |
| index | An `int` representing an absolute bar index value |

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
}
```
