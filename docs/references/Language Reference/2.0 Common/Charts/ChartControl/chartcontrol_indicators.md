---
title: Indicators
pathName: chartcontrol_indicators
parent: chartcontrol
section: references
status: changed
---

## Definition

Contains a collection of indicators currently configured on the chart.

## Property Value

A ChartObjectCollection of **NinjaTrader.Gui.NinjaScript.IndicatorRenderBase** objects representing the indicators on the chart.

## Syntax

**<`chartcontrol`>.Indicators**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    // Instantiate a ChartObjectCollection to hold chartControl.Indicators
    ChartObjectCollection<NinjaTrader.Gui.NinjaScript.IndicatorRenderBase> indicatorCollection = chartControl.Indicators;

    // Print the Calculate setting for any configured indicators not using Calculate.OnBarClose
    foreach (NinjaTrader.Gui.NinjaScript.IndicatorRenderBase indicator in indicatorCollection)
    {
        if (indicator.Calculate != Calculate.OnBarClose)
            Print(String.Format("{0} is using Calculate.{1}", indicator.Name, indicator.Calculate.ToString()));
    }
}

```
