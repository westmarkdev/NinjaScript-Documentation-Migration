---
title: PanelIndex
pathName: panelindex_chartpanel
parent: chartpanel
section: references
status: double_check
lg2m: true
---

## Definition

Indicates the index of the chart panel in the collection of configured panels.

{% callout type="note" %}

This property comes from a zero-based index, which is not the same as the panel number displayed in the Indicators window opened from within the chart. The panel number displayed in the Indicators window will equate to **ChartPanel.PanelIndex** + 1.

{% /callout %}

## Property Value

A **int** representing the zero-based index of the panel.

## Syntax

**ChartPanel.PanelIndex**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    base.OnRender(chartControl, chartScale);

    // Print the panel's zero-based index
    Print(String.Format("This panel sits at index {0}", ChartPanel.PanelIndex));
}
```

Notice three things in the image below:

* An indicator containing the example code above is configured on the second chart panel.
* In the Indicators window, the "Panel" property is set to 2.
* The output of the example code displays the zero-based index of Panel #2, which is at index 1.

![ChartPanel_PanelIndex](chartpanel_panelindex.png)
