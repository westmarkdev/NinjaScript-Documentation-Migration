---
section: references
title: ToDirectWriteTextFormat()
pathName: todirectwritetextformat
parent: simplefont
status: imported
---

## Definition

Converts a **SimpleFont** object to a **SharpDX** compatible font which can be used for chart rendering.

{% callout type="note" %}

Note: For more information please see the educational resource on [Using SharpDX for Custom Chart Rendering](using_sharpdx_for_custom_chart_rendering).

{% /callout %}

## Method Return Value

A **DirectWrite.TextFormat** object

{% callout type="warning" %}

Warning: The returned DirectWrite.TextFormat object should be disposed of immediately when finished drawing text.

{% /callout %}

## Syntax

**<simplefont`>.ToDirectWriteTextFormat()**

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Set text to chart label simple font object
   SharpDX.DirectWrite.TextFormat textFormat = chartControl.Properties.LabelFont.ToDirectWriteTextFormat();
 
   // use the textFormat in a RenderTarget.DrawText() or DrawTextLayout() method
 
   // do not forget to dispose text format when finished
   textFormat.Dispose();
}
```
