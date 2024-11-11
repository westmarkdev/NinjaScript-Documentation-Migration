---
status: double_check
title: W (Width)
pathName: w_width_chartpanel
parent: chartpanel
section: references
lg2m: true
---

## Definition

Indicates the width (in pixels) of the paintable area of the chart panel.

{% callout type="note" %}

The paintable area does not extend all the way to the right edge of the panel itself, as seen in the image below.

{% /callout }

## Property Value

A **int** representing the width of the panel in pixels

## Syntax

ChartPanel.**W**

## Example

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)  
{  
  base.OnRender(chartControl, chartScale);  
     
  // Print the width of the panel  
  Print(ChartPanel.W);  
}
```

Based on the image below, W reveals that the chart panel is 451 pixels wide.

![chartpanel_w](https://cdn.sanity.io/images/1hlwceal/production/272505438485c2b076f0066d6626100aea434e0b-534x433.png)
