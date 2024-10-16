---
title: "Stochastics RSI (StochRSI)"
pathName: /docs/desktop/stochastics_rsi_stochrsi
---

## Description

This is an indicator on indicator implementation. It is simply a [Stochastics](/docs/desktop/stochastics) indicator applied on [RSI](/docs/desktop/relative_strength_index_rsi).

## Syntax

```csharp
StochRSI(int period)
StochRSI(ISeries<double> input, int period)
```

Returns default value

```csharp
StochRSI(int period)[int barsAgo]
StochRSI(ISeries<double> input, int period)[int barsAgo]
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
// Evaluates if the current bar StochRSI value is greater than the value one bar ago
if (StochRSI(14)[0] > StochRSI(14)[1])
    Print("Stochastics RSI is rising");
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
