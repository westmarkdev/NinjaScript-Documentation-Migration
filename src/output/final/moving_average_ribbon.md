---
title: "Moving Average Ribbon"
pathName: /docs/moving_average_ribbon
---

## Description

The Moving Average Ribbon is a series of incrementing moving averages.

## Syntax

```csharp
MovingAverageRibbon(RibbonMAType movingAverage, int basePeriod, int incrementalPeriod)

MovingAverageRibbon(ISeries<double> input, RibbonMAType movingAverage, int basePeriod, int incrementalPeriod)

Returns the MovingAverage1 value (Replace the 1 with the desired moving average you want the value to return)

MovingAverageRibbon(RibbonMAType movingAverage, int basePeriod, int incrementalPeriod).MovingAverage1[int barsAgo]

MovingAverageRibbon(ISeries<double> input, RibbonMAType movingAverage, int basePeriod, int incrementalPeriod).MovingAverage1[int barsAgo]
```

## Return Value

`double`; Accessing this method via an index value `[int barsAgo]` returns the indicator value of the referenced bar.

## Parameters

|  |  |
| --- | --- |
| input | Indicator source data ([Valid Input Data for Indicator](/docs/desktop/valid_input_data_for_indicator)) |
| RibbonMAType | Moving average to use for calculations |
| basePeriod | Number of bars used in the calculation for the fastest moving average |
| incrementalPeriod | Number of bars to increase for the calculation in each additional moving average |

## Examples

```csharp
// Prints the current value of the 3rd moving average
double value = MovingAverageRibbon(RibbonMAType.Exponential, 10, 10).MovingAverage3[0];
Print("The current 3rd moving average's value is " + value.ToString());
```
