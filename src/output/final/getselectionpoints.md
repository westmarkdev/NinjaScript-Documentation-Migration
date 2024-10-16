---
title: "GetSelectionPoints()"
pathName: /docs/desktop/getselectionpoints
---

## Definition

Returns the chart object's data points where the user can interact. These points are used to visually indicate that the chart object is selected and allow the user to manipulate the chart object. This method is only called when [IsSelected](/docs/desktop/isselected) is set to true.

## Method Return Value

A collection of [Points](https://msdn.microsoft.com/en-us/library/system.drawing.point%28v=vs.110%29.aspx) representing the x- and y-coordinates of the chart object.

## Syntax

You must override the method using the following syntax:

```csharp
public override Point[] GetSelectionPoints(ChartControl chartControl, ChartScale chartScale)
{

}
```

## Method Parameters

|  |  |
| --- | --- |
| chartControl | A [ChartControl](/docs/desktop/chartcontrol) representing the x-axis |
| chartScale | A [ChartScale](/docs/desktop/chartscale) representing the y-axis |

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
