---
section: references
title: Stochastics RSI (StochRSI)
pathName: stochastics_rsi_stochrsi
parent: system_indicator_methods
status: review
---

## Description

This is an indicator on indicator implementation. It is simply a **[Stochastics](stochastics)** indicator applied on **[RSI](relative_strength_index_rsi)**.

## Syntax

**StochRSI(int period)**  

**StochRSI(ISeries`<double>` input, int period)**

Returns default value  

**StochRSI[int period](int barsAgo)**  

**StochRSI[ISeries`<double>` input, int period](int barsAgo)**

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

## Examples

```csharp
// Evaluates if the current bar StochRSI value is greater than the value one bar ago
if (StochRSI[14](0) > StochRSI[14](1))
   Print("Stochastics RSI is rising");
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
