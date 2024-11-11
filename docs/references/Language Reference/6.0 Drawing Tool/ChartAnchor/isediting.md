---
title: IsEditing
pathName: isediting
parent: chartanchor
status: imported
section: references
---

## Definition  

Determines if the anchor can be edited.

## Property Value

A bool value which when true determines if the chart anchor is currently in a state it can be edited. Default is false.

## Syntax

**`<chartanchor>`.IsEditing**

## Examples

```csharp
public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
    if (DrawingState == DrawingState.Building)
    {
        // if drawing tool is currently editing, update to current mouse point
        if (MyAnchor.IsEditing)
        {
            MyAnchor.UpdateFromPoint(point, chartControl, chartScale);

            //set the anchor to disable editing when done updating
            MyAnchor.IsEditing = false;
        }
    }
}
```
