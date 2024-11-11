---
title: BarSpacingType
pathName: barspacingtype
parent: chartcontrol
section: references
status: review
---

## Definition

Indicates the type of bar spacing used for the primary [Bars](bars) object on the chart.

## Property Value

An enum representing one of the values below:

{% table %}
*
*
---

* EquidistantSingle
* Indicates Equidistant Bar Spacing is used, and only one Bars object exists on the chart

---

* EquidistantMulti
* Indicates Equidistant Bar Spacing is used, and more than one Bars objects exist on the chart

---

* TimeBased
* Indicates Time-Based bar spacing is used
{% /table %}

## Syntax

**chartcontrol.BarSpacingType**

## Example

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print the type of bar spacing used on the chart
   Print(chartControl.BarSpacingType);
}
```

Based on the image below, BarSpacingType confirms that there are multiple Bars objects configured on the chart, and that the chart is set to Equidistant Bar Spacing:

![ChartControl_BarSpacingType](chartcontrol_barspacingtype.png)
