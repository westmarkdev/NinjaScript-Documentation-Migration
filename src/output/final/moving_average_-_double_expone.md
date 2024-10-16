---
title: "Moving Average - Double Exponential (DEMA)"
pathName: /docs/desktop/moving_average_-_double_exponential
---

## Description

The Double Exponential Moving Average (DEMA) is a combination of a single exponential moving average and a double exponential moving average. The advantage is that it provides a reduced amount of lag time compared to either of the two separate moving averages alone.

## Syntax

```csharp
DEMA(int period)  
DEMA(ISeries<double> input, int period)  
```

```csharp
// Returns default value
DEMA(int period)[int barsAgo]  
DEMA(ISeries<double> input, int period)[int barsAgo]  
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Examples

```csharp
// Prints the current value of a 20 period DEMA using default price type
double value = DEMA(20)[0];
Print("The current DEMA value is " + value.ToString());

// Prints the current value of a 20 period DEMA using high price type
double value = DEMA(High, 20)[0];
Print("The current DEMA value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

