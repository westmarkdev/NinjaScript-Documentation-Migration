---
title: DefaultChartStyle
pathName: defaultchartstyle
parent: bars_type
status: imported
section: references
---

## Definition

Allows to set a default ChartStyle for usage with a NinjaTrader bars type

## Property Value

A **ChartStyleType** enum value representing the [ChartStyle](chartstyletype) to be set as default. System defaults include:

* **ChartStyleType.Box**
* **ChartStyleType.CandleStick**
* **ChartStyleType.LineOnClose**
* **ChartStyleType.OHLC**
* **ChartStyleType.PointAndFigure**
* **ChartStyleType.KagiLine**
* **ChartStyleType.OpenClose**
* **ChartStyleType.Mountain**

## Syntax

**DefaultChartStyle**

## Examples

```csharp

protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name                     = "SampleBarsType";
        BarsPeriod               = new BarsPeriod { BarsPeriodType = (BarsPeriodType) 15, BarsPeriodTypeName = "SampleBarsType(15)", Value = 1 };
        BuiltFrom                = BarsPeriodType.Minute;
        DaysToLoad               = 5;
        DefaultChartStyle        = Gui.Chart.ChartStyleType.CandleStick;
        IsIntraday               = true;
    }
}
```
