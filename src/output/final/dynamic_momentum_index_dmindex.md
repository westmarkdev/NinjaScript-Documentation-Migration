---
title: "Dynamic Momentum Index (DMIndex)"
pathName: /docs/desktop/dynamic_momentum_index_dmindex
---

## Description

An indicator used in technical analysis that determines overbought and oversold conditions of a particular asset. This indicator is very similar to the [Relative Strength Index (RSI)](/docs/desktop/relative_strength_index). The main difference between the two is that the RSI uses a fixed number of time periods (usually 14), while the dynamic momentum index uses different time periods as volatility changes.

... Courtesy of [Investopedia](http://www.investopedia.com/terms/d/dynamicmomentumindex.asp)

## Syntax

```csharp
DMIndex(int smooth)
DMIndex(ISeries<double> input, int smooth)

Returns default value
DMIndex(int period)[int barsAgo]
DMIndex(ISeries<double> input, int smooth)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| smooth | The number of bars to include in the calculation |

## Example

```csharp
// Prints the current value of DMIndex using default price type
double value = DMIndex(3)[0];
Print("The current DMIndex value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

