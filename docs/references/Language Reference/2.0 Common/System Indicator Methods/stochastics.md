---
section: references
title: Stochastics
pathName: stochastics
parent: system_indicator_methods
status: review
---

## Description

Developed by George C. Lane in the late 1950s, the Stochastic Oscillator is a momentum indicator that shows the location of the current close relative to the high/low range over a set number of periods. Closing levels that are consistently near the top of the range indicate accumulation (buying pressure) and those near the bottom of the range indicate distribution (selling pressure).

... Courtesy of [StockCharts](stockcharts)

## Syntax

**Stochastics(int periodD, int periodK, int smooth)**  
**Stochastics(ISeries`<double>` input, int periodD, int periodK, int smooth)**

**Returns %D value**  
**Stochastics(int periodD, int periodK, int smooth).D[int barsAgo]**  
**Stochastics(ISeries`<double>` input, int periodD, int periodK, int smooth).D[int barsAgo]**

**Returns %K value**  
**Stochastics(int periodD, int periodK, int smooth).K[int barsAgo]**  
**Stochastics(ISeries`<double>` input, int periodD, int periodK, int smooth).K[int barsAgo]**

## Return Value

**double**; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* **input**
* Indicator source data ([?](valid_input_data_for_indicator.md))

---

* **periodD**
* The period for the moving average of periodD

---

* **periodK**
* The period for the moving average of periodK

---

* **smooth**
* The smoothing value to be used
{% /table %}

## Examples

```csharp
// Prints the current %D value
double value = Stochastics(7, 14, 3).D[0];
Print("The current Stochastics %D value is " + value.ToString());

// Prints the current %K value
double value = Stochastics(7, 14, 3).K[0];
Print("The current Stochastics %K value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
