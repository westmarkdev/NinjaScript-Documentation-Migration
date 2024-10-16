---
title: "Chaikin Money Flow"
pathName: /docs/desktop/chaikin_money_flow
---

## Description

The formula for Chaikin Money Flow is the cumulative total of the Accumulation/Distribution Values for 21 periods divided by the cumulative total of volume for 21 periods.

... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_ChaikinMoneyFlow1.html)

## Syntax

```csharp
ChaikinMoneyFlow(int period)
ChaikinMoneyFlow(ISeries<double> input, int period)
```

Returns default value 

```csharp
ChaikinMoneyFlow(int period)[int barsAgo]
ChaikinMoneyFlow(ISeries<double> input, int period)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Example

```csharp
// Prints the current value of a 20 period ChaikinMoneyFlow using default price type
double value = ChaikinMoneyFlow(20)[0];
Print("The current ChaikinMoneyFlow value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

