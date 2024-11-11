---
title: Disparity Index
pathName: disparity_index
parent: system_indicator_methods
section: references
status: review
---

## Description

The Disparity Index that measures the difference between the price and an exponential moving average. A value greater could suggest bullish momentum, while a value less than zero could suggest bearish momentum.

## Syntax

**DisparityIndex(int period)**

**DisparityIndex(ISeries`<double>` input, int period)**

## Return Value

**double;** Accessing this method via an index value **int barsAgo** returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* input
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))

---

* period
* Number of bars used in the calculation

---

{% /table %}

## Examples

```csharp
// Prints the current value of a 15 period Disparity Index
double value = DisparityIndex(15)[0];
Print("The current Disparity Index value is " + value.ToString());
```
