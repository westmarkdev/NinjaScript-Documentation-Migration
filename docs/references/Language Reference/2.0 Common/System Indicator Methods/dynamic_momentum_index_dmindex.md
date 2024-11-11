---
title: Dynamic Momentum Index (DMIndex)
pathName: dynamic_momentum_index_dmindex
parent: system_indicator_methods
section: references
status: review
---

## Description

An indicator used in technical analysis that determines overbought and oversold conditions of a particular asset. This indicator is very similar to the relative strength index (**RSI**). The main difference between the two is that the **RSI** uses a fixed number of time periods (usually 14), while the dynamic momentum index uses different time periods as volatility changes.

... Courtesy of [Investopedia](http://www.investopedia.com/terms/d/dynamicmomentumindex.asp)

## Syntax

**DMIndex**(**int smooth**)  
**DMIndex**(**ISeries`<double>` input**, **int smooth**)

Returns default value  
**DMIndex**[**int period**](**int barsAgo**)  
**DMIndex**[**ISeries`<double>` input**, **int smooth**](**int barsAgo**)

## Return Value

**double**; Accessing this method via an index value [**int barsAgo**] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* input
* smooth

---

* Indicator source data ([?](valid_input_data_for_indicator.htm))
* The number of bars to include in the calculation
{% /table %}

## Examples

```csharp
// Prints the current value of DMIndex using default price type
double value = DMIndex[3](0);
Print("The current DMIndex value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > **NinjaScript** Editor > Indicators within the **NinjaTrader** Control Center window.
