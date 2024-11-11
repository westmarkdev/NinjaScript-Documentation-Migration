---
title: Properties
pathName: chartscale_properties
parent: chartscale
section: references
status: double_check
lg2m: true
---

## Definition

Represents a number of properties available to the Chart Scale which can be configured to change the appearance of the scale.

![ChartPanel_Properites](chartpanel_properites.png)

{% callout type="warning" %}

These are UI properties which are designed to be set by a user. Attempting to modify these values through a custom script is NOT guaranteed to take effect.

{% /callout %}

## Property Values

{% table %}

* Property
* Description

---

* **YAxisRangeType**
* An **YAxisRangeType** enum, possible values are:
  * Automatic
  * Fixed

---

* **AutoScaleDateRangeType**
* An **AutoScaleDateRangeType** enum, possible values are:
  * ScreenDateRange
  * EntireDateRangeSeriesOnly

---

* **HorizontalGridlinesCalculation**
* An **YAxisRangeType** enum, possible values are:
  * Automatic
  * Fixed

---

* **HorizontalGridlinesIntervalType**
* A **HorizontalGridlinesIntervalType** enum, possible values are:
  * Ticks
  * Points
  * Pips

---

* **HorizontalGridlinesInterval**
* A **double** value representing the vertical interval of the horizontal axis

---

* **AutoScaleMarginType**
* An **AutoScaleMarginType** enum, possible values are:
  * Percent
  * Price

---

* **AutoScaleMarginLower**
* A **double** value representing the lowest margin used for the chart scale

---

* **AutoScaleMarginUpper**
* A **double** value representing the highest margin used for the chart scale

---

* **YAxisScalingType**
* An **YAxisScalingType** enum, possible values are:
  * Linear
  * Logarithmic

---

* **FixedScaleMax**
* A double representing the highest series value used for the chart scale when the scale is fixed

---

* **FixedScaleMin**
* A double representing the lowest series value used for the chart scale when the scale is fixed
{% /table %}

## Syntax

**<`chartscale`>.Properties**

## Examples

```csharp

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    if (chartScale.Properties.YAxisScalingType == AxisScalingTypeLinear)
    {
        // do something
    }
}
```
