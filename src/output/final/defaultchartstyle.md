---
title: "DefaultChartStyle"
pathName: /docs/desktop/defaultchartstyle
---

## Definition

Allows to set a default ChartStyle for usage with a NinjaTrader bars type.

## Property Value

A `ChartStyleType` enum value representing the [ChartStyle](/docs/desktop/chartstyletype) to be set as default. System defaults include:

&bull; ChartStyleType.Box{% <br> %}
&bull; ChartStyleType.CandleStick{% <br> %}
&bull; ChartStyleType.LineOnClose{% <br> %}
&bull; ChartStyleType.OHLC{% <br> %}
&bull; ChartStyleType.PointAndFigure{% <br> %}
&bull; ChartStyleType.KagiLine{% <br> %}
&bull; ChartStyleType.OpenClose{% <br> %}
&bull; ChartStyleType.Mountain

## Syntax

```csharp
DefaultChartStyle
```

## Examples

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "SampleBarsType";
        BarsPeriod = new BarsPeriod { BarsPeriodType = (BarsPeriodType) 15, BarsPeriodTypeName = "SampleBarsType(15)", Value = 1 };
        BuiltFrom = BarsPeriodType.Minute;
        DaysToLoad = 5;
        DefaultChartStyle = Gui.Chart.ChartStyleType.CandleStick;
        IsIntraday = true;
    }
}
```
