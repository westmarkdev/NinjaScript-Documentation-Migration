---
title: Moving Average - Weighted (WMA)
pathName: moving_average_weighted_wma
parent: system_indicator_methods
section: references
status: review
---

## Description

The Weighted Moving Average gives the latest price more weight than prior prices. Each prior price in the period gets progressively less weight as they become older.

## Syntax

**WMA(int period)**  

**WMA(ISeries`<double>` input, int period)**

Returns default value  

**WMA[int period](int barsAgo)**  

**WMA[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* input
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))

---

* period
* Number of bars used in the calculation
{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period WMA using default price type
double value = WMA[20](0);
Print("The current WMA value is " + value.ToString());

// Prints the current value of a 20 period WMA using high price type
double value = WMA[High, 20](0);
Print("The current WMA value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
