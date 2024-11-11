---
title: Time
pathName: time
parent: chartanchor
status: imported
section: references
---

## Definition

Determines date/time value the chart anchor is drawn.

## Property Value

An **DateTime** value representing a time value

## Syntax

**`<chartanchor>`.Time**

## Examples

```csharp
public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
    Print(MyAnchor.Time); // prints the X axis datetime of the chart anchor 
    // 8/26/2014 6:55:00 PM
}
```
