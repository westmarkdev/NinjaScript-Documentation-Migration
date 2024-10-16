---
title: "Moving Average - Mesa Adaptive (MAMA)"
pathName: /docs/desktop/moving_average_-_mesa_adaptive
---

## Description

The MESA Adaptive Moving Average (MAMA) adapts to price movement in an entirely new and unique way. The adaptation is based on the rate change of phase as measured by the Hilbert Transform Discriminator. The advantage of this method of adaptation is that it features a fast attack average and a slow decay average so that composite average rapidly ratchets behind price changes and holds the average value until the next ratchet occurs.

## Syntax

```csharp
MAMA(double fastLimit, double slowLimit)
MAMA(ISeries<double> input, double fastLimit, double slowLimit)

Returns MAMA value
MAMA(double fastLimit, double slowLimit)[int barsAgo]
MAMA(ISeries<double> input, double fastLimit, double slowLimit)[int barsAgo]

Returns Fama (Following Adaptive Moving Average) value
MAMA(double fastLimit, double slowLimit).Fama[int barsAgo]
MAMA(ISeries<double> input, double fastLimit, double slowLimit).Fama[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| fastLimit | Upper limit of the alpha value |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| slowLimit | Lower limit of the alpha value |

## Examples

```csharp
// Prints the current value of a 20 period MAMA using default price type
double value = MAMA(0.5, 0.05).Default[0];
Print("The current MAMA value is " + value.ToString());
// Prints the current value of a 20 period Fama using high price type
double value = MAMA(High, 0.5, 0.05).Fama[0];
Print("The current Fama value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
