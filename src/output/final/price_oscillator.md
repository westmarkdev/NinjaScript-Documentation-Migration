---
title: "Price Oscillator"
pathName: /docs/desktop/price_oscillator
---

## Description

The Price Oscillator is an indicator based on the difference between two [Moving Averages](/docs/desktop/moving_average_-_exponential_e), and is expressed as either a percentage or in absolute terms.

... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_priceOscillator.html)

## Syntax

```csharp
PriceOscillator(int fast, int slow, int smooth)  
PriceOscillator(ISeries<double> input, int fast, int slow, int smooth)  
PriceOscillator(int fast, int slow, int smooth)[int barsAgo]  
PriceOscillator(ISeries<double> input, int fast, int slow, int smooth)[int barsAgo]  
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| fast | The number of bars to calculate the fast [EMA](/docs/desktop/moving_average_-_exponential_e) |
| input | Indicator source data ([?](/docs/desktop/valid_input_data_for_indicator)) |
| slow | The number of bars to calculate the slow [EMA](/docs/desktop/moving_average_-_exponential_e) |
| smooth | The number of bars to calculate the [EMA](/docs/desktop/moving_average_-_exponential_e) signal line |

## Example

```csharp
// Prints the current value of a 20 period PriceOscillator using default price type
double value = PriceOscillator(12, 26, 9)[0];
Print("The current PriceOscillator value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
