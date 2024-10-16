---
title: "Moving Average - Triangular (TMA)"
pathName: /docs/desktop/moving_average_-_triangular_tm
---

## Description

The Triangular Moving Average is a form of [Weighted Moving Average](/docs/desktop/moving_average_-_weighted_wma) wherein the weights are assigned in a triangular pattern. For example, the weights for a 7 period Triangular Moving Average would be 1, 2, 3, 4, 3, 2, 1. This gives more weight to the middle of the time series and less weight to the oldest and newest data.

## Syntax

```csharp
TMA(int period)  
TMA(ISeries<double> input, int period)  
```

Returns default value
```csharp
TMA(int period)[int barsAgo]  
TMA(ISeries<double> input, int period)[int barsAgo]  
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Examples

```csharp
// Prints the current value of a 20 period TMA using default price type
double value = TMA(20)[0];
Print("The current TMA value is " + value.ToString());
// Prints the current value of a 20 period TMA using high price type
double value = TMA(High, 20)[0];
Print("The current TMA value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

