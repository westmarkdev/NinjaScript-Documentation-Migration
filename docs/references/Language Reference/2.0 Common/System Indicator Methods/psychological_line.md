---
title: Psychological Line
pathName: psychological_line
parent: system_indicator_methods
section: references
status: review
---

## Description

The Psychological Line is the ratio of the number of rising bars over the specified number of bars.

## Syntax

**PsychologicalLine(int period)**

**PsychologicalLine(ISeries`<double>` input, int period)**

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
// Prints the current value of a 10 period Psychological Line
double value = PsychologicalLine[10](0);
Print("The current Psychological Line value is " + value.ToString());
```
