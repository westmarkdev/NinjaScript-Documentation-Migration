---
title: n Bars Down
pathName: n_bars_down
parent: system_indicator_methods
section: references
status: review
---

## Description

Evaluates for n number of consecutive lower closes. Returns a value of 1 when the condition is true or 0 when false.

## Syntax

**NBarsDown(int barCount, bool barDown, bool lowerHigh, bool lowerLow)**  

**NBarsDown(ISeries`<double>` input, int barCount, bool barDown, bool lowerHigh, bool lowerLow)**

Returns default value  

**NBarsDown[int barCount, bool barDown, bool lowerHigh, bool lowerLow](int barsAgo)**  

**NBarsDown[ISeries`<double>` input, bool barCount, int barDown, bool lowerHigh, bool lowerLow](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* input
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))

---

* barCount
* The number of required consecutive lower closes

---

* barDown
* Each bar's open must be less than the close; true or false

---

* lowerHigh
* Consecutive lower highs required; true or false

---

* lowerLow
* Consecutive lower lows required; true or false
{% /table %}

## Examples

```csharp
// OnBarUpdate method
protected override void OnBarUpdate()
{
   // Evaluates if we have 3 consecutive lower closes
   double value = NBarsDown(3, true, true, true)[0];
 
   if (value == 1)
       Print("We have three consecutive lower closes");
}
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
