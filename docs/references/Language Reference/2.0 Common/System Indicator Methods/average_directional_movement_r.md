---
title: Average Directional Movement Rating (ADXR)
pathName: average_directional_movement_rating_adxr
parent: system_indicator_methods
section: references
status: review
---

## Description

The ADXR is equal to the current [ADX](average_directional_index_adx) plus the ADX from n bars ago divided by two.

## Syntax

**ADXR(int interval, int period)**

**ADXR(ISeries<`double`> input, int interval, int period)**

Returns default value

**ADXR[int interval, int period](int barsAgo)**

**ADXR[ISeries<`double`> input, int interval, int period](int barsAgo)**

## Return Value

**double**; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

## Parameters

{% table %}

* input
* Indicator source data

---

* interval
* The interval between the first ADX value and the current ADX value

---

* period
* Number of bars used in the calculation
{% /table %}

## Example

```csharp
// Prints the current value of a 20 period ADXR using default price type
double value = ADXR(10, 20)[0];
Print("The current ADXR value is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
