---
title: Relative Vigor Index
pathName: relative_vigor_index
parent: system_indicator_methods
section: references
status: review
---

## Description

The Relative Vigor Index measures the strength of a trend by comparing an instruments closing price to its price range. It's based on the fact that prices tend to close higher than they open in up trends, and closer lower than they open in downtrends.

## Syntax

**RelativeVigorIndex(int period)**

**RelativeVigorIndex(ISeries`<double>` input, int period)**

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
// Prints the current value of a 10 period Relative Vigor Index
double value = RelativeVigorIndex(10)[0];
Print("The current Relative Vigor Index value is " + value.ToString());
```
