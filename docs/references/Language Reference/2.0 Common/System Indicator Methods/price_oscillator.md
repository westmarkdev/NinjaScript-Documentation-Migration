---
section: references
title: Price Oscillator
pathName: price_oscillator
parent: system_indicator_methods
status: review
---

## Description

The Price Oscillator is an indicator based on the difference between two **moving averages**, and is expressed as either a percentage or in absolute terms.

... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_priceOscillator.html)

## Syntax

**PriceOscillator(int fast, int slow, int smooth)**  
**PriceOscillator(ISeries`<double>` input, int fast, int slow, int smooth)**

Returns default value  
**PriceOscillator[int fast, int slow, int smooth](int barsAgo)**  
**PriceOscillator[ISeries`<double>` input, int fast, int slow, int smooth](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* fast
* The number of bars to calculate the fast **EMA**

---

* input
* Indicator source data (**[?](valid_input_data_for_indicator.md)**)

---

* slow
* The number of bars to calculate the slow **EMA**

---

* smooth
* The number of bars to calculate the **EMA** signal line
{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period PriceOscillator using default price type
double value = PriceOscillator(12, 26, 9)[0];
Print("The current PriceOscillator value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
