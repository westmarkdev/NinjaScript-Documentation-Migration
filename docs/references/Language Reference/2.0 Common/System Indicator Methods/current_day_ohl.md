---
title: Current Day OHL
pathName: current_day_ohl
parent: system_indicator_methods
section: references
status: review
---

## Description

The current day (session) open, high and low values.

{% callout type="note" %}

Only use this indicator on intraday series.

{% /callout %}

## Syntax

**CurrentDayOHL()**  

**CurrentDayOHL(ISeries`<double>` input)**

## Returns current session open value  

**CurrentDayOHL().CurrentOpen[int barsAgo]**  

**CurrentDayOHL(ISeries`<double>` input).CurrentOpen[int barsAgo]**

## Returns current session high value  

**CurrentDayOHL().CurrentHigh[int barsAgo]**  

**CurrentDayOHL(ISeries`<double>` input).CurrentHigh[int barsAgo]**

## Returns current session low value  

**CurrentDayOHL().CurrentLow[int barsAgo]**  

**CurrentDayOHL(ISeries`<double>` input).CurrentLow[int barsAgo]**

## Return Value

**double;** Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

## Parameters

{% table %}

* input
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))
{% /table %}

## Examples

```csharp
// Prints the current value of the session low
double value = CurrentDayOHL().CurrentLow[0];
Print("The current session low value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
