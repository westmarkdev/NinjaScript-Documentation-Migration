---
title: Forecast Oscillator (FOSC)
pathName: forecast_oscillator_fosc
parent: system_indicator_methods
section: references
status: review
---

## Description

The Forecast Oscillator calculates the percentage difference between the actual price and the Time Series Forecast (the endpoint of a linear regression line). When the price and the forecast are equal, the Oscillator is zero. When the price is greater than the forecast, the Oscillator is greater than zero. When the price is less than the forecast, the Oscillator is less than zero.

... Courtesy of [FM Labs](http://www.fmlabs.com/reference/default.htm?url=ForecastOscillator.htm)

## Syntax

**FOSC(int period)**  
**FOSC(ISeries`<double>` input, int period)**

Returns default value  
**FOSC[int period](int barsAgo)**  
**FOSC[ISeries`<double>` input, int period**](int barsAgo)

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* **input**
* Indicator source data ([Series<`T`>](seriest))

---

* **period**
* Number of bars used in the calculation
{% /table %}

## Examples

```csharp
// Evaluates if the current bar **FOSC** is above zero
if (FOSC[14](0) > 0)
   Print("FOSC is above zero indicating prices may rise");
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
