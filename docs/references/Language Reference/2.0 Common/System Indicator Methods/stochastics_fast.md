---
section: references
title: Stochastics Fast
pathName: stochastics_fast
parent: system_indicator_methods
status: review
---

## Description

Developed by George C. Lane in the late 1950s, the Stochastic Oscillator is a momentum indicator that shows the location of the current close relative to the high/low range over a set number of periods. Closing levels that are consistently near the top of the range indicate accumulation (buying pressure) and those near the bottom of the range indicate distribution (selling pressure).

... Courtesy of [StockCharts](stockcharts)

## Syntax

**StochasticsFast(int periodD, int periodK)**  

**StochasticsFast(ISeries`<double>` input, int periodD, int periodK)**

Returns %D value  

**StochasticsFast(int periodD, int periodK).D[int barsAgo]**  

**StochasticsFast(ISeries`<double>` input, int periodD, int periodK).D[int barsAgo]**

Returns %K value  

**StochasticsFast(int periodD, int periodK).K[int barsAgo]**  

**StochasticsFast(ISeries`<double>` input, int periodD, int periodK).K[int barsAgo]**

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

* periodD
* The period for the moving average of periodD

---

* periodK
* The period for the moving average of periodK
{% /table %}

## Examples

```csharp
// Prints the current %D value
double value = StochasticsFast(3, 14).D[0];
Print("The current StochasticsFast %D value is " + value.ToString());

// Prints the current %K value
double value = StochasticsFast(3, 14).K[0];
Print("The current StochasticsFast %K value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
