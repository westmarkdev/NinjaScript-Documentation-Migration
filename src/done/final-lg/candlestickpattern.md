---
title: "CandleStickPattern"
path: candlestickpattern
---

## Description

Detects the specified candle stick pattern.

## Syntax

```csharp
CandleStickPattern(ChartPattern pattern, int trendStrength)
CandleStickPattern(ISeries<double> input, ChartPattern pattern, int trendStrength)

CandleStickPattern(ChartPattern pattern, int trendStrength)[int barsAgo]
CandleStickPattern(ISeries<double> input, ChartPattern pattern, int trendStrength)[int barsAgo]
```

## Return Value

A double value representing pattern found. Returns a value of 1 if the pattern is found; returns a value of 0 if no pattern was found.

Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

| Parameter | Description |
| --- | --- |
| input | Indicator source data ([?](valid_input_data_for_indicator)) |
| pattern | Possible values are: <br> ChartPattern.BearishBeltHold <br> ChartPattern.BearishEngulfing <br> ChartPattern.BearishHarami <br> ChartPattern.BearishHaramiCross <br> ChartPattern.BullishBeltHold <br> ChartPattern.BullishEngulfing <br> ChartPattern.BullishHarami <br> ChartPattern.BullishHaramiCross <br> ChartPattern.DarkCloudCover <br> ChartPattern.Doji <br> ChartPattern.DownsideTasukiGap <br> ChartPattern.EveningStar <br> ChartPattern.FallingThreeMethods <br> ChartPattern.Hammer <br> ChartPattern.HangingMan <br> ChartPattern.InvertedHammer <br> ChartPattern.MorningStart <br> ChartPattern.PiercingLine <br> ChartPattern.RisingThreeMethods <br> ChartPattern.ShootingStar <br> ChartPattern.StickSandwich <br> ChartPattern.ThreeBlackCrows <br> ChartPattern.ThreeWhiteSoldiers <br> ChartPattern.UpsideGapTwoCrows <br> ChartPattern.UpsideTasukiGap |
| trendStrength | The number of required bars to the left and right of the swing point used to determine trend. A value of zero will exclude the requirement of a trend and only detect based on the candles themselves. |

## Example

```csharp
// Go long if the current bar is a bullish engulfing pattern
if (CandlestickPattern(ChartPattern.BullishEngulfing, 4)[0] == 1)
    EnterLong();
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
