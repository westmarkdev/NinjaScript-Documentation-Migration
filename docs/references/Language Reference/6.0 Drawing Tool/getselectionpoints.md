---
title: GetSelectionPoints()
pathName: getselectionpoints
parent: drawing_tools
status: imported
section: references
---

## Definition

Returns the chart object's data points where the user can interact. These points are used to visually indicate that the chart object is selected and allow the user to manipulate the chart object. This method is only called when **IsSelected** is set to true.

## Method Return Value

A collection of [Points](points) representing the x- and y-coordinates of the chart object.

## Syntax

You must override the method using the following syntax:

```csharp
public override Point[] GetSelectionPoints(ChartControl chartControl, ChartScale chartScale)  
{  
}
```

## Method Parameters

{% table %}

---

* **chartControl**
* A [ChartControl](chartcontrol) representing the x-axis

---

* **chartScale**
* A [ChartScale](chartscale) representing the y-axis
{% /table %}

## Examples

```csharp
public override Point[] GetSelectionPoints(ChartControl chartControl, ChartScale chartScale)
{        
    ChartPanel chartPanel = chartControl.ChartPanels[chartScale.PanelIndex];
    // get the anchor point to be displayed on the drawing tool
    Point anchorPoint = Anchor.GetPoint(chartControl, chartPanel, chartScale, false);
    return new[] { anchorPoint };
}
```
