---
title: Adaptive Price Zone (APZ)
pathName: adaptive_price_zone_apz
parent: system_indicator_methods
section: references
status: review
---

## Description

The Adaptive Price Zone indicator from the S&C, September 2006 article "Trading With An Adpative Price Zone" by Lee Leibfarth is a set of bands based on a short term double smooth exponential moving average. The bands form a channel that surrounds the average price and tracks price fluctuations quickly, especially in volatile markets. As price crosses above the zone it can signal an opportunity to sell in anticipation of a reversal. As price crosses below the zone it can signal an opportunity to buy in anticipation of a reversal.

## Syntax

**APZ(double bandPct, int period)**

**APZ(ISeries<`double`> input, double bandPct, int period)**

Returns upper band value

**APZ(double bandPct, int period).Upper[int barsAgo]**

**APZ(ISeries<`double`> input, double bandPct, int period).Upper[int barsAgo]**

Returns lower band value

**APZ(double bandPct, int period).Lower[int barsAgo]**

**APZ(ISeries<`double`> input, double bandPct, int period).Lower[int barsAgo]**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* bandPct
* The number of standard deviations

---

* input
* Indicator source data

---

* period
* Number of bars used in the calculation

---

{% /table %}

## Example

```csharp
// Prints the current upper band value of a 20 period APZ
double upperValue = APZ(2, 20).Upper[0];
Print("The current APZ upper value is " + upperValue.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
