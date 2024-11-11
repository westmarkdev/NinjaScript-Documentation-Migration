---
title: Moving Average - Double Exponential (DEMA)
pathName: moving_average_double_exponential_dema
parent: system_indicator_methods
section: references
status: review
---

## Description

The Double Exponential Moving Average (DEMA) is a combination of a single exponential moving average and a double exponential moving average. The advantage is that gives a reduced amount of lag time than either of the two separate moving averages alone.

## Syntax

**DEMA(int period)**  

**DEMA(ISeries`<double>` input, int period)**

Returns default value  

**DEMA[int period](int barsAgo)**  

**DEMA[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* **input**
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))

---

* **period**
* Number of bars used in the calculation
{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period DEMA using default price type**
double value = DEMA(20)[0];
Print("The current DEMA value is " + value.ToString());
// Prints the current value of a 20 period DEMA using high price type**
double value = DEMA(High, 20)[0];
Print("The current DEMA value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
