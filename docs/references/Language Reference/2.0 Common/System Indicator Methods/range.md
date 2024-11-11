---
section: references
title: Range
pathName: range
parent: system_indicator_methods
status: review
---

## Description

Returns the range of a bar.

## Syntax

**Range()**  
**Range(ISeries`<double>` input)**

Returns default value  
**Range()[int barsAgo]**  
**Range[ISeries`<double>` input](int barsAgo)**

## Return Value

**double;** Accessing this method via an index value **[int barsAgo]** returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter
* Description

---

* input
* Indicator source data (**[?](valid_input_data_for_indicator.md)**)

---

* period
* Number of bars used in the calculation

---

{% /table %}

## Examples

```csharp
// Prints the range of the current bar
double value = Range()[0];
Print("The current bar's range is " + value.ToString());

// Prints the 20 period simple moving average of range
double value = SMA(Range(), 20)[0];
Print("The 20 period average of range is " + value.ToString());
```

## Source Code

You can view this indicator method source code by selecting the menu New > NinjaScript Editor > Indicators within the NinjaTrader Control Center window.
