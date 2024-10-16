---
title: "Ease of Movement"
pathName: /docs/desktop/ease_of_movement
---

## Description

The Ease of Movement indicator was designed to illustrate the relationship between volume and price change. It shows how much volume is required to move prices.

High Ease of Movement values occur when prices are moving upward with light volume. Low values occur when prices are moving downward on light volume. If prices are not moving or if heavy volume is required to move prices, then the indicator will read near zero. A buy signal is produced when it crosses above zero. A sell signal is produced when the indicator crosses below zero (prices are moving downward more easily).

## Syntax

```csharp
EaseOfMovement(int smoothing, int volumeDivisor)  
EaseOfMovement(ISeries<double> input, int smoothing, int volumeDivisor)  
```

Returns default value

```csharp
EaseOfMovement(int smoothing, int volumeDivisor)[int barsAgo]  
EaseOfMovement(ISeries<double> input, int smoothing, int volumeDivisor)[int barsAgo]  
```

## Return Value

`double`; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| smoothing | The number of bars used to smooth the signal |
| volumeDivisor | The value used to calculate the box ratio |

## Example

```csharp
// Prints the current value of Ease of Movement using default price type
double value = EaseOfMovement(14, 10000)[0];
Print("The current Ease of Movement value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu **New > NinjaScript Editor > Indicators** within the NinjaTrader Control Center window.
