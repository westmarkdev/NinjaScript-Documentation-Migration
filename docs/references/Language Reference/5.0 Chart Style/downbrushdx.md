---
title: DownBrushDX
pathName: downbrushdx
parent: chart_style
status: imported
section: references
---

## Definition

A **SharpDX** [Brush](sharpdx_direct2d1_brush) object used to paint the down bars for the ChartStyle.

## Property  Value

A **SharpDX** [Brush](sharpdx_direct2d1) object used to paint the down bars.

## Syntax

**DownBrushDX**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale, ChartBars chartBars)
{
   for (int idx = chartBars.FromIndex; idx <= chartBars.ToIndex; idx++)
       {
           double     closeValue             = bars.GetClose(idx); 
           double     openValue               = bars.GetOpen(idx);
 
           // Set the brush of the current candle to UpBrushDX or DownBrushDX, depending on the 
           // bar direction
           Brush brush = closeValue >= openValue ? UpBrushDX : DownBrushDX;
       }
}
```
