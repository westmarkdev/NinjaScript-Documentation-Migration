---
title: Linear Regression Slope
pathName: linear_regression_slope
parent: system_indicator_methods
section: references
status: review
---

## Description

The Linear Regression Slope provides the slope value of the **Linear Regression** trendline.

## Syntax

**LinRegSlope(int period)**  

**LinRegSlope(ISeries`<double>` input, int period)**

Returns default value  

**LinRegSlope[int period](int barsAgo)**  

**LinRegSlope[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* input
* Indicator source data (**[?](valid_input_data_for_indicator.md)**)

---

* period
* Number of bars used in the calculation

---

{% /table %}

## Examples

```csharp

// Prints the current slope value of a 20 period LinReg using default price type
double value = LinRegSlope[20](0);
Print("The current slope value is " + value.ToString());

// Prints the current slope value of a 20 period LinReg using high price type
double value = LinRegSlope[High, 20](0);
Print("The current slope value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
