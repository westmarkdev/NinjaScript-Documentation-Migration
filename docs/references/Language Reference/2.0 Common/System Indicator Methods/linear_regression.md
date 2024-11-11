---
title: Linear Regression
pathName: linear_regression
parent: system_indicator_methods
section: references
status: review
---

## Description

The Linear Regression Indicator plots the trend of a security's price over time. That trend is determined by calculating a Linear Regression Trendline using the least squares method. This ensures the minimum distance between the data points and a Linear Regression Trendline.

## Syntax

**LinReg(int period)**  

**LinReg(ISeries`<double>` input, int period)**

Returns default value  

**LinReg[int period](int barsAgo)**  

**LinReg[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* input
* Indicator source data ([valid_input_data_for_indicator](valid_input_data_for_indicator.md))

---

* period
* Number of bars used in the calculation

---
{% /table %}

## Examples

```csharp

// Prints the current value of a 20 period LinReg using default price type
double value = LinReg[20](0);
Print("The current LinReg value is " + value.ToString());

// Prints the current value of a 20 period LinReg using high price type
double value = LinReg[High, 20](0);
Print("The current LinReg value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
