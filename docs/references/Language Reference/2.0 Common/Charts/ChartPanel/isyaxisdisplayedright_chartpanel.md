---
title: IsYAxisDisplayedRight
pathName: isyaxisdisplayedright
parent: chartpanel
section: references
status: review
---

## Definition

Indicates the y-axis is visible on the right side of the chart panel.

## Property Value

A **bool** indicating the y-axis is visible to the right

## Syntax

**ChartPanel.IsYAxisDisplayedRight**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)

{

   base.OnRender(chartControl, chartScale);

   // Print a message if the y-axis is visible on the right

   if (ChartPanel.IsYAxisDisplayedRight)

       Print("The y-axis is visible on the right");

}
```

Based on the image below, **IsYAxisDisplayedRight** confirms that the y-axis is not displayed on the right. The property would be set to false when applied in either chart panel in this instance.

![ChartPanel_IsYAxisDisplayedRight](chartpanel_isyaxisdisplayedright.png)
