---
title: Moving Average - Volume Weighted (VWMA)
pathName: moving_average_volume_weighted_vwma
parent: system_indicator_methods
section: references
status: review
---

## Description

The Volume Weighted Moving Average is a weighted moving average that uses the volume as the weighting factor, so that higher volume days have more weight. It is a non-cumulative moving average, in that only data within the time period is used in the calculation.

## Syntax

**VWMA(int period)**  

**VWMA(ISeries`<double>` input, int period)**

Returns default value  

**VWMA[int period](int barsAgo)**  

**VWMA[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* input
* Indicator source data ([**valid_input_data_for_indicator**](valid_input_data_for_indicator.md))

---

* period
* Number of bars used in the calculation

---

{% /table %}

## Examples

```csharp
// OnBarUpdate method
protected override void OnBarUpdate()
{
   // Evaluates for a VWMA cross over to the long side
   if (CrossAbove(VWMA(14), VWMA(40), 1))
       Print("We have a moving average cross over long");

   // Prints the current 14 period VWMA of high prices to the output window
   double value = VWMA[High, 14](0);
   Print("The current VWMA value of high prices is " + value.ToString());
}
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
