---
title: "On Balance Volume (OBV)"
pathName: /docs/desktop/on_balance_volume_obv
---

## Description

OBV is a simple indicator that adds a period's volume when the close is up and subtracts the period's volume when the close is down. A cumulative total of the volume additions and subtractions forms the OBV line. This line can then be compared with the price chart of the underlying security to look for divergences or confirmation.

... Courtesy of [StockCharts](/docs/desktop/http://stockcharts.com/education/IndicatorAnalysis/indic-obv)

## Syntax

```csharp
OBV()
OBV(ISeries<double> input)

Returns default value
OBV()[int barsAgo]
OBV(ISeries<double> input)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([valid input data for indicator](/docs/desktop/valid_input_data_for_indicator)) |

## Example

```csharp
// Prints the current value of OBV
double value = OBV()[0];
Print("The current OBV value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
