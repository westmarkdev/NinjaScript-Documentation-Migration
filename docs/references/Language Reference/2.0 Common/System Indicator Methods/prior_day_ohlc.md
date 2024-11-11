---
section: references
title: Prior Day OHLC
pathName: prior_day_ohlc
parent: system_indicator_methods
status: review
---

## Description

The prior day (session) open, high, low and close values.

{% callout type="note" %}

Only use this indicator on intraday series.

{% /callout %}

## Syntax

**PriorDayOHLC()**  

**PriorDayOHLC(ISeries`<double>` input)**

Returns prior session open value  

**PriorDayOHLC().PriorOpen[int barsAgo]**  

**PriorDayOHLC(ISeries`<double>` input).PriorOpen[int barsAgo]**

Returns prior session high value  

**PriorDayOHLC().PriorHigh[int barsAgo]**  

**PriorDayOHLC(ISeries`<double>` input).PriorHigh[int barsAgo]**

Returns prior session low value  

**PriorDayOHLC().PriorLow[int barsAgo]**  

**PriorDayOHLC(ISeries`<double>` input).PriorLow[int barsAgo]**

Returns prior session close value  

**PriorDayOHLC().PriorClose[int barsAgo]**  

**PriorDayOHLC(ISeries`<double>` input).PriorClose[int barsAgo]**

## Return Value

**double**; Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

## Parameters

{% table %}

* input
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))
{% /table %}

## Examples

```csharp
// Prints the value of the prior session low
double value = PriorDayOHLC().PriorLow[0];
Print("The prior session low value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
