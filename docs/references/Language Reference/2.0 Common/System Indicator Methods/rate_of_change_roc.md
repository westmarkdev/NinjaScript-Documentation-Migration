---
section: references
title: Rate of Change (ROC)
pathName: rate_of_change_roc
parent: system_indicator_methods
status: review
---

## Description

The Rate of Change (ROC) indicator is a very simple yet effective momentum oscillator that measures the percent change in price from one period to the next. The ROC calculation compares the current price with the price n periods ago.

... Courtesy of [StockCharts](stockcharts)

## Syntax

**ROC(int period)**  
**ROC(ISeries`<double>` input, int period)**

Returns default value  
**ROC[int period](int barsAgo)**  
**ROC[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double**; Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

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
Prints the current value of a 20 period ROC using default price type
double value = ROC[20](0);
Print("The current ROC value is " + value.ToString());

// Prints the current value of a 20 period ROC using high price type
double value = ROC[High, 20](0);
Print("The current ROC value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
