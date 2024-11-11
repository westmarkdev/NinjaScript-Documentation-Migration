---
title: Directional Movement Index (DMI)
pathName: directional_movement_index_dmi
parent: system_indicator_methods
section: references
status: review
---

## Description

An indicator developed by J. Welles Wilder for identifying when a definable trend is present in an instrument. That is, the DMI tells whether an instrument is trending or not.

...Courtesy of [FMLabs](http://www.fmlabs.com/reference/default.htm?url=DX.htm)

## Syntax

**DMI(int period)**  

**DMI(ISeries`<double>` input, int period)**

Returns default value  

**DMI[int period](int barsAgo)**  

**DMI[ISeries`<double>` input, int period](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

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
// Prints the current value of a 20 period DMI using default price type
double value = DMI[20](0);
Print("The current DMI value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
