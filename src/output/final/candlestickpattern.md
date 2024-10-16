---
title: "CandleStickPattern"
pathName: /docs/desktop/candlestickpattern
---

## Description

Detects the specified candlestick pattern.

## Syntax

```csharp
CandleStickPattern(ChartPattern pattern, int trendStrength)
CandleStickPattern(ISeries<double> input, ChartPattern pattern, int trendStrength)

Returns a value indicating if the specified pattern was detected

CandleStickPattern(ChartPattern pattern, int trendStrength)[int barsAgo]
CandleStickPattern(ISeries<double> input, ChartPattern pattern, int trendStrength)[int barsAgo]
```

## Return Value

A `double` value representing the pattern found. Returns a value of 1 if the pattern is found; returns a value of 0 if no pattern was found.

Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| pattern | Possible values are: {% <br> %} &bull; ChartPattern.BearishBeltHold{% <br> %} &bull; ChartPattern.BearishEngulfing{% <br> %} &bull; ChartPattern.BearishHarami{% <br> %} &bull; ChartPattern.BearishHaramiCross{% <br> %} &bull; ChartPattern.BullishBeltHold{% <br> %} &bull; ChartPattern.BullishEngulfing{% <br> %} &bull; ChartPattern.BullishHarami{% <br> %} &bull; ChartPattern.BullishHaramiCross{% <br> %} &bull; ChartPattern.DarkCloudCover{% <br> %} &bull; ChartPattern.Doji{% <br> %} &bull; ChartPattern.DownsideTasukiGap{% <br> %} &bull; ChartPattern.EveningStar{% <br> %} &bull; ChartPattern.FallingThreeMethods{% <br> %} &bull; ChartPattern.Hammer{% <br> %} &bull; ChartPattern.HangingMan{% <br> %} &bull; ChartPattern.InvertedHammer{% <br> %} &bull; ChartPattern.MorningStar{% <br> %} &bull; ChartPattern.PiercingLine{% <br> %} &bull; ChartPattern.RisingThreeMethods{% <br> %} &bull; ChartPattern.ShootingStar{% <br> %} &bull; ChartPattern.StickSandwich{% <br> %} &bull; ChartPattern.ThreeBlackCrows{% <br> %} &bull; ChartPattern.ThreeWhiteSoldiers{% <br> %} &bull; ChartPattern.UpsideGapTwoCrows{% <br> %} &bull; ChartPattern.UpsideTasukiGap |
| trendStrength | The number of required bars to the left and right of the swing point used to determine trend. A value of zero will exclude the requirement of a trend and only detect based on the candles themselves. |

## Example

```csharp
// Go long if the current bar is a bullish engulfing pattern
if (CandleStickPattern(ChartPattern.BullishEngulfing, 4)[0] == 1)
    EnterLong();
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
