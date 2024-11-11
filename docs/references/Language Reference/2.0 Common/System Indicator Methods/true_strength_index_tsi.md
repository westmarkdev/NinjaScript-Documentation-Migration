---
status: double_check
title: True Strength Index (TSI)
parent: system_indicator_methods
pathName: true_strength_index_tsi
section: references
lg2m: true
---

## Description

The True Strength Index (TSI) is a momentum-based indicator, developed by William Blau. Designed to determine both trend and overbought/oversold conditions, the TSI is applicable to intraday time frames as well as long term trading.

## Syntax

**TSI(int fast, int slow)**  
**TSI(ISeries<`double`> input, int fast, int slow)**

### Returns default value  

**TSI[int fast, int slow](int barsAgo)**  
**TSI[ISeries<`double`> input, int fast, int slow](int barsAgo)**

## Return Value

**double**; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter

* Description

---

* fast

* Period of the fast smoothing factor

---

* input

* Indicator source data ([?](valid_input_data_for_indicator.md))

---

* slow

* Period of the slow smoothing factor

---

{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period TSI using default price type  
double value = TSI(20, 10)[0];  
Print("The current TSI value is " + value.ToString());  
   
// Prints the current value of a 20 period TSI using high price type  
double value = TSI(High, 20, 10)[0];  
Print("The current TSI value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
