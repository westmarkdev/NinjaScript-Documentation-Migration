---
title: ChartPanels
pathName: chartpanels
parent: chartpanel
section: references
status: review
---

## Definition

Holds a collection of **ChartPanel** objects containing information about the panels active on the chart.

## Property Value

An **ObservableCollection** of **ChartPanel** objects

## Syntax

**<`chartcontrol`>.ChartPanels**

## Examples

{% callout type="note" %}

Based on the image below, there are three ChartPanel objects in the ChartPanels collection, as seen by **ChartPanels.Count** in the code above.

{% /callout %}

![ChartControl_ChartPanels](chartcontrol_chartpanels.png)

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print the number of panels currently displayed on the chart
   Print(String.Format("There are {0} panels on the chart", chartControl.ChartPanels.Count));  
}
```
