---
title: IsYAxisDisplayedLeft
pathName: isyaxisdisplayedleft
parent: chartcontrol
section: references
status: review
---

## Definition

Indicates the y-axis displays (in any chart panel) to the left side of the chart.

## Property Value

A boolean value. When **True**, indicates that the y-axis displays to the left of the chart canvas; otherwise **False**.

## Syntax

**<`chartcontrol`>.IsYAxisDisplayedLeft**

## Examples

{% callout type="note" %}

Based on the image below, IsYAxisDisplayedLeft confirms that the y-axis displays to the left of the chart canvas.

{% /callout %}

![ChartControl_isYAxisDisplayedLeft](chartcontrol_isyaxisdisplayedleft.png)

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print the value of IsYAxisDisplayedLeft
   Print("Y-Axis visible to the left of the chart canvas? " + chartControl.IsYAxisDisplayedLeft);
}
```
