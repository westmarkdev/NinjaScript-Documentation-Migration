---
section: references
title: Relative Spread Strength (RSS)
pathName: relative_spread_strength_rss
parent: system_indicator_methods
status: review
---

## Description

Developed by Ian Copsey, **Relative Spread Strength** is a variation to the [Relative Strength Index](relative_strength_index_rsi).

## Syntax

**RSS(int eMA1, int eMA2, int length)**

**RSS(ISeries`<double>` input, int eMA1, int eMA2, int length)**

Returns default value

**RSS[int eMA1, int eMA2, int length](int barsAgo)**

**RSS[ISeries`<double>` input, int eMA1, int eMA2, int length](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* eMA1
* First EMA's period

---

* eMA2
* Second EMA's period

---

* input
* Indicator source data ([?](valid_input_data_for_indicator.md))

---

* length
* Number of bars used in the calculation
{% /table %}

## Examples

```csharp
// Prints the current value of the RSS using default price type
double value = RSS[10, 40, 5](0);
Print("The current RSS value is " + value.ToString());

// Prints the current value of the RSS using high price type
double value = RSS[High, 10, 40, 5](0);
Print("The current RSS value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
