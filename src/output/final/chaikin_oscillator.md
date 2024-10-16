---
title: "Chaikin Oscillator"
pathName: /docs/desktop/chaikin_oscillator
---

## Description

The Chaikin Oscillator is simply the Moving Average Convergence Divergence indicator (MACD) applied to the Accumulation/Distribution Line. The formula is the difference between the 3-day exponential moving average and the 10-day exponential moving average of the Accumulation/Distribution Line. Just as the MACD-Histogram is an indicator to predict moving average crossovers in MACD, the Chaikin Oscillator is an indicator to predict changes in the Accumulation/Distribution Line.

... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_ChaikinOscillator.html)

## Syntax

```csharp
ChaikinOscillator(int fast, int slow)
ChaikinOscillator(ISeries<double> input, int fast, int slow)

Returns default value
ChaikinOscillator(int fast, int slow)[int barsAgo]
ChaikinOscillator(ISeries<double> input, int fast, int slow)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| fast | The number of bars to calculate the fast [EMA](/docs/desktop/moving_average_-_exponential_e) |
| input | Indicator source data ([?](/docs/desktop/valid_input_data_for_indicator)) |
| slow | The number of bars to calculate the slow EMA |

## Example

```csharp
// Prints the current value of a ChaikinOscillator using default price type
double value = ChaikinOscillator(3, 10)[0];
Print("The current ChaikinOscillator value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

