---
status: double_check
pathName: volume_moving_average_volma
title: Volume Moving Average (VOLMA)
parent: system_indicator_methods
section: references
lg2m: true
---

## Description

The Volume Moving Average indicator is an indicator on indicator implementation. It calculates and returns the value of an [exponential moving average](moving_average_-_exponential_e) of [volume](volume.md).

## Syntax

**VOLMA(int period)**  
**VOLMA(ISeries<`double`> input, int period)**

### Returns default value  

**VOLMA[int period](int barsAgo)**  
**VOLMA[ISeries<`double`> input, int period](int barsAgo)**

## Return Value

**double**; Accessing this method via an index value [int barsAgo] returns the indicator value of the referenced bar.

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

## Example

```csharp
// Evaluates if the current volume is greater than the 20 period EMA of volume  
if (Volume[0] > VOLMA(20)[0])  
  Print("Volume has risen above its 20 period average");
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
