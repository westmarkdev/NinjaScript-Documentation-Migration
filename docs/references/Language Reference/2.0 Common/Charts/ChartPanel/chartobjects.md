---
title: ChartObjects
pathName: chartobjects
parent: chartpanel
section: references
status: review
---

## Definition

A collection of objects configured on the chart panel.

## Property Value

An **IList** of **Gui.NinjaScript.IChartObject** instances containing references to the objects configured on the panel.

## Syntax

**ChartPanel.ChartObjects**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    base.OnRender(chartControl, chartScale);

    IList<Gui.NinjaScript.IChartObject> myObjects = ChartPanel.ChartObjects;

    foreach (Gui.NinjaScript.IChartObject thisObject in myObjects)
    {
        Print(String.Format("{0} is of type {1}", thisObject.Name, thisObject.GetType()));
    }
}
```

The image below shows the output of the code example above, while applied in a chart panel with three objects.

![ChartPanel_ChartObjects](chartpanel_chartobjects.png)
