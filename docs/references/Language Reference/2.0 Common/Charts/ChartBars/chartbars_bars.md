---
title: Bars
pathName: bars
parent: chartbars
section: references
status: review
---

## Definition

Represents the data returned from the historical data repository in relation to the primary **ChartBars** object configured on the chart. See also [Bars](bars).

## Property Value

A **Bars** object

## Syntax

**ChartBars.Bars**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if(ChartBars != null && ChartBars.Bars != null)
   {
     Print("The configured bars period type represented on the chart is" + ChartBars.Bars.BarsPeriod.BarsPeriodType);
   }
}
```
