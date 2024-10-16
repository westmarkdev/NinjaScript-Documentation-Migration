---
title: "Moving Average - Variable (VMA)"
pathName: /docs/desktop/moving_average_-_variable_vma
---

## Description

A Variable Moving Average is an exponential moving average that automatically adjusts its smoothing percentage based on market volatility. Giving more weight to the current data increases sensitivity thus making it a better signal indicator for short and long term markets.

## Syntax

```csharp
VMA(int period, int volatilityPeriod)
```

```csharp
VMA(ISeries<double> input, int period, int volatilityPeriod)
```

```csharp
VMA(int period, int volatilityPeriod)[int barsAgo]
```

```csharp
VMA(ISeries<double> input, int period, int volatilityPeriod)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|                      |                                                                                  |
|----------------------|----------------------------------------------------------------------------------|
| input                | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| period               | Number of bars used in the calculation                                           |
| volatilityPeriod     | The number of bars used to calculate the [CMO](/docs/desktop/chande_momentum_oscillator_cmo) based volatility index |

## Examples

```csharp
// OnBarUpdate method of a strategy
protected override void OnBarUpdate()
{
    // Print out the VMA value of lows 3 bars ago for fun
    double value = VMA(Low, 9, 9)[3];
    Print("The value is " + value.ToString());
    
    // Go long if price closes above the current VMA value
    if (Close[0] > VMA(9, 9)[0])
        EnterLong();
}
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

