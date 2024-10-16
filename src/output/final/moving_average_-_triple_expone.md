---
title: "Moving Average - Triple Exponential (TEMA)"
pathName: /docs/desktop/moving_average_-_triple_expone
---

## Description

The TEMA is a smoothing indicator. It was developed by Patrick Mulloy and is described in his article in the January, 1994 issue of Technical Analysis of Stocks and Commodities magazine.

## Syntax

```csharp
TEMA(int period)
TEMA(ISeries<double> input, int period)
```

```csharp
TEMA(int period)[int barsAgo]
TEMA(ISeries<double> input, int period)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([valid input data for indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period | Number of bars used in the calculation |

## Examples

```csharp
// Prints the current value of a 20 period TEMA using default price type
double value = TEMA(20)[0];
Print("The current TEMA value is " + value.ToString());
// Prints the current value of a 20 period TEMA using high price type
double value = TEMA(High, 20)[0];
Print("The current TEMA value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

