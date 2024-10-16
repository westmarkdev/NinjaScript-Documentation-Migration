---
title: "n Bars Up"
pathName: /docs/desktop/n_bars_up
---

## Description

Evaluates for n number of consecutive higher closes. Returns a value of 1 when the condition is true or 0 when false.

## Syntax

```csharp
NBarsUp(int barCount, bool barUp, bool higherHigh, bool higherLow)
NBarsUp(ISeries<double> input, int barCount, bool barUp, bool higherHigh, bool higherLow)

Returns default value
NBarsUp(int barCount, bool barUp, bool higherHigh, bool higherLow)[int barsAgo]
NBarsUp(ISeries<double> input, int barCount, bool barUp, bool higherHigh, bool higherLow)[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| barCount | The number of required consecutive higher closes |
| barUp | Each bar's close must be higher than the open; true or false |
| higherHigh | Consecutive higher highs required; true or false |
| higherLow | Consecutive higher lows required; true or false |

## Example

```csharp
// OnBarUpdate method
protected override void OnBarUpdate()
{
    // Evaluates if we have 3 consecutive higher closes
    double value = NBarsUp(3, true, true, true)[0];
    if (value == 1)
        Print("We have three consecutive higher closes");
}
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
