---
title: Commodity Channel Index (CCI)
pathName: commodity_channel_index_cci
parent: system_indicator_methods
section: references
status: review
---

## Description

Developed by Donald Lambert, the Commodity Channel Index (CCI) was designed to identify cyclical turns in commodities. The assumption behind the indicator is that commodities (or stocks or bonds) move in cycles, with highs and lows coming at periodic intervals.

... Courtesy of [StockCharts](http://stockcharts.com/education/IndicatorAnalysis/indic_CCI.html)

## Syntax

**CCI(int period)**  

**CCI(ISeries`<double>` input, int period)**

Returns default value  

**CCI[int period](int barsAgo)**  

**CCI[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* **input**
* Indicator source data ([?](valid_input_data_for_indicator.htm))

---

* **period**
* Number of bars used in the calculation
{% /table %}

## Examples

```csharp

// Prints the current value of a 20 period CCI using default price type
double value = CCI[20](0);
Print("The current CCI value is " + value.ToString());

// Prints the current value of a 20 period CCI using high price type
double value = CCI[High, 20](0);
Print("The current CCI value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
