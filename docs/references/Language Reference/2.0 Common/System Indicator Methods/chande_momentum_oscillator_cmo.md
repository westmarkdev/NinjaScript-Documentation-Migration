---
title: Chande Momentum Oscillator (CMO)
pathName: chande_momentum_oscillator_cmo
parent: system_indicator_methods
section: references
status: review
---

## Description

The Chande Momentum Oscillator was developed by Tushar S. Chande and is described in the 1994 book The New Technical Trader by Tushar S. Chande and Stanley Kroll. This indicator is a modified **RSI**. Where the **RSI** divides the upward movement by the net movement (up / (up + down)), the **CMO** divides the total movement by the net movement ((up - down) / (up + down)). Values under -50 indicate oversold conditions while values over 50 indicate overbought conditions.

## Syntax

**CMO(int period)**  

**CMO(ISeries`<double>` input, int period)**

Returns default value  

**CMO[int period](int barsAgo)**  

**CMO[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* input
* Indicator source data ([**?**](valid_input_data_for_indicator.htm))

---

* period
* The number of bars to include in the calculation
{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period CMO using default price type
double value = CMO(20)[0];
Print("The current CMO value is " + value.ToString());
```

```csharp
// Prints the current value of a 20 period CMO using high price type
double value = CMO(High, 20)[0];
Print("The current CMO value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
