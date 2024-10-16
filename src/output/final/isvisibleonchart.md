---
title: "IsVisibleOnChart()"
pathName: /docs/desktop/isvisibleonchart
---

## Definition

Indicates a chart object is visible on the chart. When the IsVisibleOnChart() method determines a chart object is not visible and returns false, the object will not be used in a render pass, will not be considered in a hit test, and will not be used for alerting. The base implementation is to always return true on all chart objects, however this behavior can be overridden for your custom object if desired.

## Method Return Value

A virtual `bool` value which when true, the object will be rendered and can be interacted with by a user; otherwise false. Default value is true.

## Syntax

You must override this method using the following syntax:

```csharp
public override bool IsVisibleOnChart(ChartControl chartControl, ChartScale chartScale, DateTime firstTimeOnChart, DateTime lastTimeOnChart)
{
    return true;
}
```

## Method Parameters

|  |  |
| --- | --- |
| chartControl | A [ChartControl](/docs/desktop/chartcontrol) representing the x-axis |
| chartScale | A [ChartScale](/docs/desktop/chartscale) representing the y-axis |
| firstTimeOnChart | A `DateTime` representing the first painted bar displayed on the chart |
| lastTimeOnChart | A `DateTime` representing the last painted bar displayed on the chart |

## Examples

```csharp
public override bool IsVisibleOnChart(ChartControl chartControl, ChartScale chartScale, DateTime firstTimeOnChart, DateTime lastTimeOnChart)
{
    // check if any chart anchors are visible
    foreach (ChartAnchor anchor in Anchors)
    {
        if (anchor.Time >= firstTimeOnChart && anchor.Time <= lastTimeOnChart)
            return true;
    }
    return false; // otherwise the object should not be displayed
}
```
