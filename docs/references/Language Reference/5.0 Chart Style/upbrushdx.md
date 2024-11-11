---
status: double_check
title: UpBrushDX
parent: chart_style
pathName: upbrushdx
section: references
lg2m: true
---

## Definition

A SharpDX [Brush](sharpdx_direct2d1_brush) object used to paint the up bars for the ChartStyle.

## Property  Value

A [SharpDX](sharpdx_direct2d1) Brush object used to paint the up bars

## Syntax

**UpBrushDX**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale, ChartBars chartBars)  
{  
  for (int idx = chartBars.FromIndex; idx <= chartBars.ToIndex; idx++)  
      {  
          double     closeValue             = bars.GetClose(idx);  
          double     openValue               = bars.GetOpen(idx);  
   
          // Set the brush of the current candle to UpBrushDX or DownBrushDX, depending on the  
          // bar direction  
          Brush brush = closeValue >= openValue ? UpBrushDX : DownBrushDX;  
      }  
}
```
