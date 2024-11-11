---
title: MaxValue
pathName: maxvalue
parent: common
section: references
status: imported
---

## Definition

The maximum value used for the automatic scaling of the y axis. This property will only be used when the chart object is set to **IsAutoScale**.

## Property Value

A **double** value.

## Syntax

**MaxValue**

## Examples

```csharp

public override void OnCalculateMinMax()
{
    if (DrawingState != DrawingState.Building)
    {
        //set the maximum value to the chart anchors price
        MaxValue = Anchor.Price;
    }
}
```
