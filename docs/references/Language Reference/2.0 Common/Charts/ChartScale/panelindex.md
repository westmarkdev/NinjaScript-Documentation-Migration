---
title: PanelIndex
pathName: panelindex
parent: chartscale
section: references
status: review
---

## Definition

The panel on which the chart scale resides.

{% callout type="note" %}

This value is NOT the same value as the indicator's **PanelUI**. **PanelIndex** will provide the actual indexed value of the chart panel used for this chart scale.

{% /callout %}

## Property Value

An **int** value representing the panel as an index value which starts at 0 and will increment for each panel configured on the chart. This property is read-only.

## Syntax

**<`chartscale>.PanelIndex**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{         
   // the index value of the panel (not the same as the panelUI)
   int     panel     = chartScale.PanelIndex;
   Print("panel: " + panel);
}
```
