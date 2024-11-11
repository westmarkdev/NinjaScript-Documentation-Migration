---
title: Money Flow Index (MFI)
pathName: money_flow_index_mfi
parent: system_indicator_methods
section: references
status: review
---

## Description

The Money Flow Index (MFI) is a momentum indicator that is similar to the Relative Strength Index (RSI) in both interpretation and calculation. However, MFI is a more rigid indicator in that it is volume-weighted, and is therefore a good measure of the strength of money flowing in and out of a security.

... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_MFI.htm)

## Syntax

**MFI(int period)**  

**MFI(ISeries`<double>` input, int period)**

Returns default value  

**MFI[int period](int barsAgo)**  

**MFI[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* input
* Indicator source data ([?](valid_input_data_for_indicator.md))

---

* period
* Number of bars used in the calculation

---

{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period MFI using default price type
double value = MFI[20](0);
Print("The current MFI value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
