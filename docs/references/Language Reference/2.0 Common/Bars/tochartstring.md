---
title: ToChartString()
pathName: tochartstring
parent: bars
section: references
status: review
---

## Definition

Returns the bars series as a formatted string, including the **Instrument.FullName**, **BarsPeriod** Value, and **BarsPeriodType** name.

{% callout type="note" %}

Note: To obtain a return value which matches the user configured **ChartBars Label property**, please see the **ChartBars.ToChartString()** method.

{% /callout %}

## Syntax

**Bars.ToChartString()**

## Return Value

A **string** value that represents the bars series.

## Parameters

This method does not accept any parameters.

## Examples

```csharp
protected override void OnBarUpdate()
{
   // print the chart string on start up
   if(CurrentBar == 0)
     Print(Bars.ToChartString()); // ES 09-15 (60 Minute)      
}
```
