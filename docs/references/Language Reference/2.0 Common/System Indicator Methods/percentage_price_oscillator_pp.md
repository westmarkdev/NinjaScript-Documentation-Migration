---
section: references
title: Percentage Price Oscillator (PPO)
pathName: percentage_price_oscillator_pp
parent: system_indicator_methods
status: review
---

## Description

The Percentage Price Oscillator shows the percentage difference between two **exponential moving averages**.

## Syntax

**PPO(int fast, int slow, int smooth)**  

**PPO(ISeries`<double>` input, int fast, int slow, int smooth)**

Returns default value  

**PPO[int fast, int slow, int smooth](int barsAgo)**  

**PPO[ISeries`<double>` input, int fast, int slow, int smooth](int barsAgo)**

Returns smoothed value  

**PPO(int fast, int slow, int smooth).Smoothed[int barsAgo]**  

**PPO(ISeries`<double>` input, int fast, int slow, int smooth).Smoothed[int barsAgo]**

## Return Value

**double;** Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

## Parameters

{% table %}

* fast
* The number of bars to calculate the fast EMA

---

* input
* Indicator source data (**[?](valid_input_data_for_indicator.md)**)

---

* slow
* The number of bars to calculate the slow EMA

---

* smooth
* The number of bars to calculate the EMA signal line
{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period Percentage Price Oscillator
double value = PPO(12, 26, 9)[0];
Print("The current Percentage Price Oscillator value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
