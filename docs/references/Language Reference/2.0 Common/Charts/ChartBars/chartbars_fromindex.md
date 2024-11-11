---
title: FromIndex
pathName: fromindex
parent: chartbars
section: references
status: review
---

## Definition

An index value representing the first bar rendered on the chart. See also **ToIndex**.

{% callout type="note" %}

This value is NOT the first value that exists on the **ChartBars**, but rather the first bar index that is within the viewable range of the chart canvas area. This value changes as the user interacts with the **ChartControl** time-scale (x-axis).

{% /callout %}

## Property Value

An int representing the first bar index painted on the chart.

## Syntax

**ChartBars.FromIndex**

## Examples

```csharp

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if (ChartBars != null)
   {
     // loop through all of the viewable range of the chart
     for (int barIndex = ChartBars.FromIndex; barIndex <= ChartBars.ToIndex; barIndex++)
     {
         // print the High value for each index within the viewable range
         Print(High.GetValueAt(barIndex));
     }
   }
}
```
