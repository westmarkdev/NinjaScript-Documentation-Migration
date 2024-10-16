---
title: "Chart Style"
pathName: /docs/desktop/chart_style
---

Custom Chart Styles can be used on charts to present bars information in a different visual representation. The methods and properties covered in this section are unique to custom Chart Style development. Following is an index of properties and methods documented for Chart Styles.

## Methods and Properties

|  |  |
| --- | --- |
| [BarWidth](/docs/desktop/barwidth) | The painted width of a ChartStyle bar |
| [BarWidthUI](/docs/desktop/barwidthui) | The Bar width value which displays on the UI |
| [ChartStyleType](/docs/desktop/chartstyletype) | Defines a unique identifier value used to register a custom ChartStyle |
| [DownBrush](/docs/desktop/downbrush) | A [Brush](https://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object used to determine the color to paint the down bars for the ChartStyle |
| [DownBrushDX](/docs/desktop/downbrushdx) | A [SharpDX.Brush](/docs/desktop/sharpdx_direct2d1_brush) object used to paint the down bars for the ChartStyle |
| [GetBarPaintWidth()](/docs/desktop/getbarpaintwidth) | Returns the painted width of the chart bar |
| [IsTransparent](/docs/desktop/istransparent) | Indicates the bars in the ChartStyle are transparent |
| [OnRender()](/docs/desktop/chartstyle_onrender) | An event driven method used to render content to a ChartStyle |
| [SetPropertyName()](/docs/desktop/setpropertyname) | Sets a default property name to a custom string to be displayed on the UI |
| [TransformBrush()](/docs/desktop/transformbrush) | Scales a non-solid color brush used for rendering the chart style to properly display in NinjaTrader |
| [UpBrush](/docs/desktop/upbrush) | A [Brush](https://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object used to determine the color to paint the up bars for the ChartStyle |
| [UpBrushDX](/docs/desktop/upbrushdx) | A [SharpDX.Brush](/docs/desktop/sharpdx_direct2d1_brush) object used to paint the up bars for the ChartStyle |
