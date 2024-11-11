---
title: PanelIndex
pathName: panelindex
parent: chartcontrol
section: references
status: review
---

## Definition

Indicates the minimum Y value of objects within the chart panel, based on the current y-axis scale. The scale of the y-axis is dependent upon the values of objects in the panel which have Auto Scale enabled.

## Property Value

A double representing the minimum Y value in the panel's vertical scale

## Syntax

**ChartPanel.MinValue**

## Examples

```csharp

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)**
{
   base.OnRender(chartControl, chartScale);

   // Print the minimum and maximum Y values for objects in the panel
   Print(String.Format("Min value: {0}, Max value: {1}", **ChartPanel.MinValue**, **ChartPanel.MaxValue**));
}

```
