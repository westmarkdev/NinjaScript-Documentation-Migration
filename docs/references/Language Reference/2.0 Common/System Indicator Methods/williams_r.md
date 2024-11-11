---
status: double_check
title: Williams %R
pathName: williams_r
parent: system_indicator_methods
section: references
lg2m: true
---

## Description

Developed by Larry Williams, Williams %R is a momentum indicator that works much like the [Stochastic Oscillator](stochastics). It is especially popular for measuring overbought and oversold levels. The scale ranges from 0 to -100 with readings from 0 to -20 considered overbought, and readings from -80 to -100 considered oversold.

... Courtesy of [StockCharts](https://school.stockcharts.com/doku.php?id=technical_indicators:williams_r)

## Syntax

**WilliamsR(int period)**  

**WilliamsR(ISeries<`double`> input, int period)**

### Returns default value  

**WilliamsR(int period)[int barsAgo]**  

**WilliamsR(ISeries<`double`> input, int period)[int barsAgo]**

## Return Value

**double**; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

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

{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period WilliamsR using default price type  
double value = WilliamsR(20)[0];  
Print("The current WilliamsR value is " + value.ToString());  
   
// Prints the current value of a 20 period WilliamsR using high price type  
double value = WilliamsR(High, 20)[0];  
Print("The current WilliamsR value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
