---
section: references
title: Relative Volatility Index (RVI)
pathName: relative_volatility_index_rvi
parent: system_indicator_methods
status: review
---

## Description

Developed by Donald Dorsey, the Relative Volatility Index is the **RSI** using the standard deviation over the indicator period in place of the daily price change. The RVI measures the direction of volatility on a scale from 0 to 100. Readings below 50 indicate that the direction of volatility is to the downside and that you should be looking to sell, readings above 50 indicate that the direction of volatility is to the upside and that you should be looking to buy.

## Syntax

**RVI(int period)**  

**RVI(ISeries`<double>` input, int period)**

Returns default value  

**RVI[int period](int barsAgo)**  

**RVI[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

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
{% /table %}

## Examples

```csharp
// OnBarUpdate method
protected override void OnBarUpdate()
{
    // Check for buy condition
    if (RVI(14)[0] > 50 && CrossAbove(SMA(9), SMA(14), 1))
    {
        EnterLong();
    }
}
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
