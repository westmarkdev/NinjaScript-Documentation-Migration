---
title: "MA Envelopes"
pathName: /docs/desktop/maenvelopes
---

## Description

The Moving Average Envelope consists of moving averages calculated from the underlying price, shifted up and down by a fixed percentage.

## Syntax

```csharp
MAEnvelopes(double envelopePercentage, int mAType, int period)

MAEnvelopes(ISeries<double> input, double envelopePercentage, int mAType, int period)
```

Returns upper band levels

```csharp
MAEnvelopes(double envelopePercentage, int mAType, int period).Upper[int barsAgo]

MAEnvelopes(ISeries<double> input, double envelopePercentage, int mAType, int period).Upper[int barsAgo]
```

Returns moving average value

```csharp
MAEnvelopes(double envelopePercentage, int mAType, int period).Middle[int barsAgo]

MAEnvelopes(ISeries<double> input, double envelopePercentage, int mAType, int period).Middle[int barsAgo]
```

Returns lower band levels

```csharp
MAEnvelopes(double envelopePercentage, int mAType, int period).Lower[int barsAgo]

MAEnvelopes(ISeries<double> input, double envelopePercentage, int mAType, int period).Lower[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| envelopePercentage | Percentage around MA that envelopes will be drawn |
| input | Indicator source data ([?](/docs/desktop/valid_input_data_for_indicator)) |
| mAType | Moving average type: {% <br> %} 1 = EMA{% <br> %} 2 = HMA{% <br> %} 3 = SMA{% <br> %} 4 = TMA{% <br> %} 5 = TEMA{% <br> %} 6 = WMA |
| period | Number of bars used in the calculation |

## Examples

```csharp
// Prints the current upper band value of a 20 period SMA envelope using default price type
double upperValue = MAEnvelopes(0.2, 3, 20).Upper[0];
Print("The current SMA envelope upper value is " + upperValue.ToString());

// Prints the current lower band value of a 20 period SMA envelope using low price type
double lowerValue = MAEnvelopes(Low, 0.2, 3, 20).Lower[0];
Print("The current SMA envelope lower value is " + lowerValue.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.

