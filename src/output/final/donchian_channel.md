---
title: "Donchian Channel"
pathName: /docs/desktop/donchian_channel
---

## Description

A moving average indicator developed by Richard Donchian. It plots the highest high and lowest low over a specific period.

## Syntax

```csharp
DonchianChannel(int period)
DonchianChannel(ISeries<double> input, int period)
```

Returns mean value (middle band) at a specified bar index

```csharp
DonchianChannel(int period)[int barsAgo]
DonchianChannel(ISeries<double> input, int period)[int barsAgo]
```

Returns upper band value at a specified bar index

```csharp
DonchianChannel(int period).Upper[int barsAgo]
DonchianChannel(ISeries<double> input, int period).Upper[int barsAgo]
```

Returns lower band value at a specified bar index

```csharp
DonchianChannel(int period).Lower[int barsAgo]
DonchianChannel(ISeries<double> input, int period).Lower[int barsAgo]
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
// Prints the current upper value of a 20 period DonchianChannel using default price type
double value = DonchianChannel(20).Upper[0];
Print("The current DonchianChannel upper value is " + value.ToString());
// Note the above call with a barsAgo of 0 includes the current Upper channel in the value. If we want to check for example for a break of this value, storing the last bar's channel value would be needed.
double value = DonchianChannel(20).Upper[1];
if (High[0] > value)
    Draw.ArrowUp(this, CurrentBar.ToString(), true, 0, Low[0] - TickSize, Brushes.Blue);
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
