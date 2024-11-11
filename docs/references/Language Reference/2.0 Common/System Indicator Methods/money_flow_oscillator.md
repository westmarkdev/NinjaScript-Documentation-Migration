---
title: Money Flow Oscillator
pathName: money_flow_oscillator
parent: system_indicator_methods
section: references
status: review
---

## Description

The Money Flow Oscillator measures the amount of money flow volume over a specific period. A move into positive territory indicates buying pressure while a move into negative territory indicates selling pressure.

## Syntax

**MoneyFlowOscillator**(int period)

**MoneyFlowOscillator**(**ISeries`<double>`** input, int period)

## Return Value

**double;** Accessing this method via an index value **int barsAgo** returns the indicator value of the referenced bar.

## Parameters

{% table %}

* Parameter

* Description

---

* input

* Indicator source data ([**valid_input_data_for_indicator**](valid_input_data_for_indicator.md))

---

* period

* Number of bars used in the calculation

---

{% /table %}

## Examples

```csharp
// Prints the current value of a 10 period Money Flow Oscillator
double value = MoneyFlowOscillator(10)[0];
Print("The current Money Flow Oscillator value is " + value.ToString());
```
