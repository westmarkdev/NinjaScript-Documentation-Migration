---
title: Moving Average Ribbon
pathName: moving_average_ribbon
parent: system_indicator_methods
section: references
status: review
---

## Description

The Moving Average Ribbon is a series of incrementing moving averages.

## Syntax

**MovingAverageribbon(RibbonMAType movingAverage, int basePeriod, int incrementalPeriod)**

**MovingAverageribbon(ISeries`<double>` input, RibbonMAType movingAverage, int basePeriod, int incrementalPeriod)**

**Returns the MovingAverage1 value (Replace the 1 with the desired moving average you want the value to return)**

**MovingAverageribbon(RibbonMAType movingAverage, int basePeriod, int incrementalPeriod).MovingAverage1[int barsAgo]**

**MovingAverageribbon(ISeries`<double>` input, RibbonMAType movingAverage, int basePeriod, int incrementalPeriod).MovingAverage1[int barsAgo]**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* input
* RibbonMAType
* basePeriod
* incrementalPeriod

---

* Indicator source data ([**valid_input_data_for_indicator**](valid_input_data_for_indicator.md))
* Moving average to use for calculations
* Number of bars used in the calculation for the fastest moving average
* Number of bars to increase for the calculation in each additional moving average
{% /table %}

## Examples

```csharp
// Prints the current value of the 3rd moving average
double value = MovingAverageRibbon(RibbonMAType.Exponential, 10, 10).MovingAverage3[0];
Print("The current 3rd moving average's value is " + value.ToString());
```
