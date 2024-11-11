---
title: Chaikin Volatility
pathName: chaikin_volatility
parent: system_indicator_methods
status: review
section: references
---

## Description

The Chaikin Volatility Indicator is the difference between two moving averages of a volume weighted accumulation-distribution line. By comparing the spread between a security's high and low prices, it quantifies volatility as a widening of the range between the high and the low price.

## Syntax

**ChaikinVolatility(int mAPeriod, int rOCPeriod)**  

**ChaikinVolatility(ISeries`<double>` input, int mAPeriod, int rOCPeriod)**  

Returns default value  

**ChaikinVolatility**[int mAPeriod, int rOCPeriod](int barsAgo)  

**ChaikinVolatility**[ISeries`<double>` input, int mAPeriod, int rOCPeriod](int barsAgo)

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* input
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))

---

* mAPeriod
* Number of bars used in the moving average calculation

---

* rOCPeriod
* Number of bars used in the rate of change calculation
{% /table %}

## Examples

```csharp
// Prints the current value of the 20 period Chaikin Volatility
double value = ChaikinVolatility(20, 20)[0];
Print("The current Chaikin Volatility value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
