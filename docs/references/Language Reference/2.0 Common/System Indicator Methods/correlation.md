---
title: Correlation
pathName: correlation
parent: system_indicator_methods
section: references
status: review
---

## Description

The correlation indicator will plot the correlation of the data series to a desired instrument. Values close to 1 indicate movement in the same direction. Values close to -1 indicate movement in opposite directions. Values near 0 indicate no correlation.

## Syntax

**Correlation(int period, string correlationSeries)**  

**string correlationSeies(ISeries`<double>` input, int period, string correlationSeies)**

## Return Value

**double**; Accessing this method via an index value **int barsAgo** returns the indicator value of the referenced bar.

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

* correlationSeries
* The data series to compare to

---

{% /table %}

## Examples

```csharp

// The correlation data series must be added to OnStateChange() as this indicator runs off the correlation data series data
else if (State == State.Configure)
{
   AddDataSeries("SPY");
}

// Checks the bars in progress and prints the current correlation to the SPY
if (BarsInProgress == 0)
{
   double value = Correlation[20, "SPY"](0);
   Print("The current correlation to the SPY is " + value.ToString());
}
```

{% callout type="note" %}

If the correlation series does not plot during a time the input series plots, a value of zero would plot in the above example. You may consider ignoring zero values.

{% /callout %}

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
