---
title: Parabolic SAR
pathName: parabolic_sar
parent: system_indicator_methods
section: references
status: review
---

## Description

The parabolic SAR is a technical indicator that is used by many traders to determine the direction of an asset's momentum and the point in time when this momentum has a higher-than-normal probability of switching directions.

... Courtesy of [Investopedia](http://www.investopedia.com/articles/technical/02/042202.asp)

## Syntax

**ParabolicSAR(double acceleration, double accelerationMax, double accelerationStep)**

**ParabolicSAR(ISeries`<double>` input, double acceleration, double accelerationMax, double accelerationStep)**

Returns default value  

**ParabolicSAR[double acceleration, double accelerationMax, double accelerationStep](int barsAgo)**  

**ParabolicSAR[ISeries`<double>` input, double acceleration, double accelerationStep, double accelerationMax](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* **acceleration**
* Acceleration value

---

* **accelerationStep**
* Step value used to increment acceleration value

---

* **accelerationMax**
* Max acceleration value

---

* **input**
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))
{% /table %}

## Examples

```csharp
// Prints the current value of ParabolicSAR using default price type
double value = ParabolicSAR(0.02, 0.2, 0.02)[0];
Print("The current ParabolicSAR value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
