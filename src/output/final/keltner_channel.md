---
title: "Keltner Channel"
pathName: /docs/desktop/keltner_channel
---

## Description

Keltner Channel indicator is based on volatility using a pair of values placed as an "envelope" around the data field.

## Syntax

```csharp
KeltnerChannel(double offsetMultiplier, int period)
KeltnerChannel(ISeries<double> input, double offsetMultiplier, int period)
```

Returns midline value

```csharp
KeltnerChannel(double offsetMultiplier, int period)[int barsAgo]
KeltnerChannel(ISeries<double> input, double offsetMultiplier, int period)[int barsAgo]
```

Returns upper band value

```csharp
KeltnerChannel(double offsetMultiplier, int period).Upper[int barsAgo]
KeltnerChannel(ISeries<double> input, double offsetMultiplier, int period).Upper[int barsAgo]
```

Returns lower band value

```csharp
KeltnerChannel(double offsetMultiplier, int period).Lower[int barsAgo]
KeltnerChannel(ISeries<double> input, double offsetMultiplier, int period).Lower[int barsAgo]
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
// Prints the current upper value of a 20 period KeltnerChannel using default price type
double value = KeltnerChannel(1.5, 20).Upper[0];
Print("The current KeltnerChannel upper value is " + value.ToString());
// Prints the current lower value of a 20 period KeltnerChannel using high price type
double value = KeltnerChannel(High, 1.5, 20).Lower[0];
Print("The current KeltnerChannel lower value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
