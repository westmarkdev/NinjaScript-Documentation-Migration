---
title: BarsPeriod
pathName: chartcontrol_barsperiod
parent: chartcontrol
section: references
status: double_check
lg2m: true
---

## Definition

Provides the period (interval) used for the primary **Bars** object on the chart.

## Property Value

A **NinjaTrader.Data.BarsPeriod** object containing information on the period used by the **Bars** object on the chart.

## Syntax

**<`chartcontrol`>.BarsPeriod**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale) 
{
   BarsPeriod period = chartControl.BarsPeriod;
 
   // Print the period (interval) of the Bars object on the chart
   Print(period);
}
```

Based on the image below, **BarsPeriod** confirms that the primary **Bars** object on the chart is configured to a 5-minute interval.

![ChartControl_BarsPeriod](chartcontrol_barsperiod.png)
