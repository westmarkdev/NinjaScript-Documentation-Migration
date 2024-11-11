---
title: Moving Average - Kaufman's Adaptive (KAMA)
pathName: moving_average_kaufmans_adaptive
parent: system_indicator_methods
section: references
status: review
---

## Description

Developed by Perry Kaufman, this indicator is an EMA using an Efficiency Ratio to modify the smoothing constant, which ranges from a minimum of Fast Length to a maximum of Slow Length.

## Syntax

**KAMA**(int fast, int period, int slow)  
**KAMA**(ISeries`<double>` input, int fast, int period, int slow)

Returns default value  
**KAMA**[int fast, int period, int slow](int barsAgo)  
**KAMA**[ISeries`<double>` input, int fast, int period, int slow](int barsAgo)

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* **fast**
* Fast length

---

* **input**
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))

---

* **period**
* Number of bars used in the calculation

---

* **slow**
* Slow length
{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period KAMA using default price type
double value = KAMA[2, 20, 30](0);
Print("The current KAMA value is " + value.ToString());

// Prints the current value of a 20 period KAMA using high price type
double value = KAMA[High, 2, 20, 30](0);
Print("The current KAMA value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
