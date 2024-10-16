---
title: "Stochastics"
pathName: stochastics
---

## Description

Developed by George C. Lane in the late 1950s, the Stochastic Oscillator is a momentum indicator that shows the location of the current close relative to the high/low range over a set number of periods. Closing levels that are consistently near the top of the range indicate accumulation (buying pressure) and those near the bottom of the range indicate distribution (selling pressure).

... Courtesy of [StockCharts](http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:stochastic_oscillator_fast_slow_and_full)

## Syntax

```csharp
Stochastics(int periodD, int periodK, int smooth)
```

```csharp
Stochastics(ISeries<double> input, int periodD, int periodK, int smooth)
```

Returns %D value

```csharp
Stochastics(int periodD, int periodK, int smooth).D[int barsAgo]
```

```csharp
Stochastics(ISeries<double> input, int periodD, int periodK, int smooth).D[int barsAgo]

Returns %K value

```csharp
Stochastics(int periodD, int periodK, int smooth).K[int barsAgo]
```

```csharp
Stochastics(ISeries<double> input, int periodD, int periodK, int smooth).K[int barsAgo]
```

## Return Value

double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

| Parameter | Description |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator)) |
| periodD | The period for the moving average of periodD |
| periodK | The period for the moving average of periodK |
| smooth | The smoothing value to be used |

## Examples

```csharp
// Prints the current %D value
double value = Stochastics(7, 14, 3).D[0];
Print("The current Stochastics %D value is " + value.ToString());
// Prints the current %K value
double value = Stochastics(7, 14, 3).K[0];
Print("The current Stochastics %K value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
