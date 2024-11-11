---
title: SlotsPainted
pathName: slotspainted
parent: chartcontrol
section: references
status: review
---

## Definition

Indicates the number of index slots in which bars are painted within the chart canvas area. This covers the visible portion of the chart only, and does not include historical painted bars outside of the visible area.

## Property Value

An int representing the number of index slots in which bars are painted.

## Syntax

**<`chartcontrol`>.SlotsPainted**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   int painted = chartControl.SlotsPainted;
 
   // Print the number of bars painted on the visible chart canvas
   Print(painted);
}
```

In the image below, **SlotsPainted** reveals that there are 17 bars painted on the chart canvas.

![ChartControl_SlotsPainted](chartcontrol_slotspainted.png)
