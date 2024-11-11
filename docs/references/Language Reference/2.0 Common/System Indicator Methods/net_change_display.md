---
title: Net Change Display
pathName: net_change_display
parent: system_indicator_methods
section: references
status: review
---

## Description

Displays net change on the chart.

## Syntax

**NetChangeDisplay(PerformanceUnit, NetChangePosition location)**

**NetChangeDisplay(ISeries`<double>` input, PerformanceUnit, NetChangePosition location)**

## Return Value

double

## Parameters

{% table %}

---

* **input**
* Indicator source data ([valid input data for indicator](valid_input_data_for_indicator.md))

---

* **PerformanceUnit**
* Format of the calculation of net change

---

* **NetChangePosition**
* Location to display net change on the chart
{% /table %}

## Examples

```csharp

// Runs on realtime since there is no historical data for this indicator
if (State == State.Historical)
return;
else if (State >= State.Realtime)
{
// Prints the current tick value of the net change
var ncd = NetChangeDisplay(PerformanceUnit.Ticks, NetChangePosition.BottomRight);
Print("The current Net Change value is " + ncd.NetChange);
}
```

{% callout type="note" %}

This indicator only plots real-time. Historical values will print as 0.

{% /callout %}
