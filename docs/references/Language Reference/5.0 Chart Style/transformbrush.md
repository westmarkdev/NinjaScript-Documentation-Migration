---
status: double_check
title: TransformBrush()
parent: chart_style
pathName: transformbrush
section: references
lg2m: true
---

## Definition

Scales a non-solid color brush used for rendering the chart style to properly display in NinjaTrader.

{% callout type="note" %}

This method has no impact on solid color brushes.  You would only need to pass in either a linear or radial gradient brush.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax  

**TransformBrush(SharpDX.Direct2D1.Brush brush, RectangleF rect)**

## Method Parameters

{% table %}

* Parameter

* Description

---

* brush

* A [SharpDX.Direct2D1.Brush](sharpdx_direct2d1_brush) object representing the brush used to render

---

* rect

* A [RectangleF](https://msdn.microsoft.com/en-us/library/system.drawing.rectanglef%28v=vs.110%29.aspx) structure representing the rectangle to be rendered

---

{% /table %}

## Examples

```csharp
protected override void OnRender(ChartControl chartControl, ChartScale chartScale, ChartBars chartBars)

{

  TransformBrush(brush, rect);

}
```
