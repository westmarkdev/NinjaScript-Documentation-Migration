---
status: double_check
title: Y (Coordinate)
pathName: y_coordinate_chartpanel
parent: chartpanel
section: references
lg2m: true
---

## Definition

Indicates the **y-coordinate** on the chart canvas at which the chart panel begins.

## Property Value

A **int** representing the **y-coordinate** at which the panel begins.

## Syntax

ChartPanel.**Y**

## Example

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)  
{  
  base.OnRender(chartControl, chartScale);  
     
  // Print the coordinates of the top-left corner of the panel  
  Print(String.Format("The panel begins at coordinates {0},{1}",ChartPanel.X ,ChartPanel.Y));  
}
```

Based on the image below, Y reveals that the chart panel begins at y-coordinate 232.

![chartpanel_y](https://cdn.sanity.io/images/1hlwceal/production/a4f39c5505ac60533a86ccc155406dd304d0bfb9-534x433.png)
