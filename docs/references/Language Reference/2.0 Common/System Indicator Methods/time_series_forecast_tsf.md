---
section: references
title: Time Series Forecast (TSF)
pathName: time_series_forecast_tsf
parent: system_indicator_methods
status: review
---

## Description

The Time Series Forecast function displays the statistical trend of a security's price over a specified time period based on linear regression analysis. Instead of a straight linear regression trendline, the Time Series Forecast plots the last point of multiple linear regression trendlines. This is why this indicator may sometimes be referred to as the "moving linear regression" indicator or the "regression oscillator."

## Syntax

**TSF(int forecast, int period)**  

**TSF(ISeries`<double>` input, int forecast, int period)**

Returns default value  

**TSF[int forecast, int period](int barsAgo)**  

**TSF[ISeries`<double>` input, int forecast, int period](int barsAgo)**

## Return Value

**double**; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* **forecast**
* Forecast period

---

* **input**
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))

---

* **period**
* Number of bars used in the calculation
{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period TSF using default price type
double value = TSF(3, 20)[0];
Print("The current TSF value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
