---
title: "Moving Average - Volume Weighted (VWMA)"
pathName: /docs/desktop/moving_average_-_volume_weight
---

## Description

The Volume Weighted Moving Average is a weighted moving average that uses the volume as the weighting factor, so that higher volume days have more weight. It is a non-cumulative moving average, in that only data within the time period is used in the calculation.

## Syntax

```csharp
VWMA(int period)  
VWMA(ISeries<double> input, int period)  
```

Returns default value

```csharp
VWMA(int period)[int barsAgo]  
VWMA(ISeries<double> input, int period)[int barsAgo]  
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
// OnBarUpdate method
protected override void OnBarUpdate()
{
    // Evaluates for a VWMA cross over to the long side
    if (CrossAbove(VWMA(14), VWMA(40), 1))
        Print("We have a moving average cross over long");

    // Prints the current 14 period VWMA of high prices to the output window
    double value = VWMA(High, 14)[0];
    Print("The current VWMA value of high prices is " + value.ToString());
}
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

