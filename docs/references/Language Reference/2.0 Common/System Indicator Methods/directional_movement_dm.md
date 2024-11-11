---
title: Directional Movement (DM)
pathName: directional_movement_dm
parent: system_indicator_methods
section: references
status: review
---

## Description

Same as the **ADX** indicator with the addition of the +DI and -DI values.

... Courtesy of [Investopedia](http://www.investopedia.com/terms/d/dmi.asp)

## Syntax

**DM(int period)**  
**DM(ISeries`<double>` input, int period)**

Returns default ADX value  

**DM[int period](int barsAgo)**  
**DM[ISeries`<double>` input, int period](int barsAgo)**

Returns +DI value  

**DM(int period).DiPlus[int barsAgo]**  
**DM(ISeries`<double>` input, int period).DiPlus[int barsAgo]**

Returns -DI value  

**DM(int period).DiMinus[int barsAgo]**  
**DM(ISeries`<double>` input, int period).DiMinus[int barsAgo]**

## Return Value

**double;** Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* input
* Indicator source data ([?](valid_input_data_for_indicator.md))

---

* period
* Number of bars used in the calculation
{% /table %}

## Examples

```csharp
// Prints the current value of a 20 period +DI using default price type
double value = DM(20).DiPlus[0];
Print("The current +DI value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
