---
title: "Average True Range (ATR)"
pathName: /docs/desktop/average_true_range_atr
---

## Description

A measure of volatility introduced by Welles Wilder in his book: New Concepts in Technical Trading Systems.

The True Range indicator is the greatest of the following:

- current high less the current low.
- the absolute value of the current high less the previous close.
- the absolute value of the current low less the previous close.

The Average True Range is a moving average (generally 14-days) of the True Ranges.

... Courtesy of [Investopedia](http://www.investopedia.com/terms/a/atr.asp)

The original Wilder formula for an exponential moving average with a smoothing constant (k = 1/Period) is used to calculate the ATR.

## Syntax

```csharp
ATR(int period)  
ATR(ISeries<double> input, int period)  
```

Returns default value

```csharp
ATR(int period)[int barsAgo]  
ATR(ISeries<double> input, int period)[int barsAgo]  
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([?](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Example

```csharp
// Prints the current value of a 20 period ATR using default price type
double value = ATR(20)[0];
Print("The current ATR value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.