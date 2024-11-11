---
status: double_check
pathName: volume_rate_of_change_vroc
title: Volume Rate of Change (VROC)
parent: system_indicator_methods
section: references
lg2m: true
---

## Description

Volume Rate of Change is identical to [Price Rate Of Change (ROC)](source_files/rate_of_change_roc.md) indicator except that it uses volume instead of price.

## Syntax

**VROC(int period, int smooth)**  

**VROC(ISeries<`double`> input, int period, int smooth)**

### Returns default value  

**VROC[int period, int smooth](int barsAgo)**  

**VROC[ISeries<`double`> input, int period, int smooth](int barsAgo)**

## Return Value

double; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter

* Description

---

* input

* Indicator source data ([?](valid_input_data_for_indicator.md))

---

* period

* Number of bars used in the calculation

---

* smooth

* The number of bars for smoothing the signal

---

{% /table %}

## Example

```csharp
// Prints the current value of VROC  
double value = VROC(13, 3)[0];  
Print("The current VROC value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
