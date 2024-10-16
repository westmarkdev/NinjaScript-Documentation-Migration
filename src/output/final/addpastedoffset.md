---
title: "AddPastedOffset()"
pathName: /docs/desktop/addpastedoffset
---

## Definition

A [virtual method](https://msdn.microsoft.com/en-us/library/9fkccyh4.aspx) which is called every time a DrawingTool is copied and pasted to a chart. The default behavior will offset the chart anchor's price value down by 1 percent. However, this behavior can be overridden for your custom drawing tool if desired.

## Method Return Value

This method does not return a value.

## Syntax

You must override this method using the following syntax:

```csharp
public override void AddPastedOffset(ChartPanel panel, ChartScale chartScale)
{

}
```

## Method Parameters

|  |  |
| --- | --- |
| panel | A `ChartPanel` representing the panel for the chart. |
| chartScale | A `ChartScale` representing the Y-axis. |

## Examples

```csharp
public override void AddPastedOffset(ChartPanel chartPanel, ChartScale chartScale)
{
    foreach (ChartAnchor anchor in Anchors)
    {
        // bump each anchor 1 minute to the right
        DateTime tmpTime = anchor.Time;
        anchor.Time = tmpTime.AddMinutes(1);
    }
}
```
