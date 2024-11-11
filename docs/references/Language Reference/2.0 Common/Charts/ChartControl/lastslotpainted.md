---
title: LastSlotPainted
pathName: lastslotpainted
parent: chartcontrol
section: references
status: review
---

## Definition

Indicates the most recent (last) slot index of the Data Series on the chart, regardless if a bar is actually painted in that slot.

{% callout type="note" %}

LastSlotPainted differs from **ChartBars.ToIndex**, which returns the last index containing a bar painted in the visible area of the chart.

{% /callout %}

## Property Value

A int representing the most recent (last) slot index on the chart.

## Syntax

**<`chartcontrol`>.LastSlotPainted**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   int lastSlot = chartControl.LastSlotPainted;
 
   // Print the index of the last slot on the chart
   Print(lastSlot);
}
```
