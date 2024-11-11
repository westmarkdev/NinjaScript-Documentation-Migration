---
title: ToChartString()
pathName: tochartstring
parent: chartbars
section: references
status: review
---

## Definition

Returns a formatted string representing the **ChartBars.Properties.Label** property, **BarsPeriod** Value, and **BarsPeriodType** name.

{% callout type="note" %}

The property returned is dependent on a user configured **Data Series** property, and results may return differently than expected. See also **Bars.ToChartString()** for a return value which is not subject to user-defined variables.

{% /callout %}

## Syntax

**ChartBars.ToChartString()**

## Return Value

A **string** value that represents the ChartBars label and configured bars period.

## Parameters

This method does not accept any parameters.

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if (ChartBars != null)
     Print(ChartBars.ToChartString()); // My Favorite Instrument (1 Minute)
}
```
