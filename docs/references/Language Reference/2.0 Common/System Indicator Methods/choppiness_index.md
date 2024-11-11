---
title: Choppiness Index
pathName: choppiness_index
parent: system_indicator_methods
section: references
status: review
---

## Description

The Choppiness Index is designed to determine if the market is choppy (trading sideways) or not choppy (trading within a trend in either direction).

## Syntax

**ChoppinessIndex(int period)**

**ChoppinessIndex(ISeries`<double>` input, int period)**

## Return Value

**double;** Accessing this method via an index value **int barsAgo** returns the indicator value of the referenced bar.

## Parameters

{% table %}

---

* **input**
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))

---

* **period**
* Number of bars used in the calculation
{% /table %}

## Examples

```csharp
// Prints the current value of a 14 period Choppiness Index
double value = ChoppinessIndex(14)[0];
Print("The current Choppiness Index value is " + value.ToString());
```
