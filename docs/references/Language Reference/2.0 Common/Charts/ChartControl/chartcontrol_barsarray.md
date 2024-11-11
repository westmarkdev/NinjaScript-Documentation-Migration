---
title: BarsArray
pathName: barsarray
parent: chartcontrol
section: references
status: review
---

## Definition

Provides a collection of **ChartBars** objects currently configured on the chart.

## Property Value

An **ObservableCollection** of **ChartBars** objects.

## Syntax

**<`chartcontrol`>.BarsArray**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Instantiate a new <chartcontrol`>.BarsArray collection
   System.Collections.ObjectModel.ObservableCollection<chartbars> myChartBars = chartControl.BarsArray;
 
   // Print the number of bars in each Bars object within the <chartcontrol`>.BarsArray collection
   foreach(ChartBars bars in myChartBars)
   {
       Print(bars.Bars.Count);
   }
}
```
