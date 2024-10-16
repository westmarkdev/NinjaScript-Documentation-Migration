---
title: "Line Class"
pathName: /docs/desktop/line_class
---

## Definition

Objects derived from the Line class are used to characterize how an oscillator line is visually displayed (plotted) on a chart.

## Properties

|  |  |
| --- | --- |
| Brush | The System.Windows.Media.Brush used to construct the line ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)) |
| BrushDX | A [SharpDX.Direct2D1.Brush](/docs/desktop/sharpdx_direct2d1_brush) used to actually render the line.<br>Note: To avoid and resolve access violation exceptions, please see Warning and examples remarked below. |
| DashStyleDX | A [SharpDX.Direct2D1.DashStyle](/docs/desktop/sharpdx_direct2d1_strokestyle_dashstyle) used to render the stroke style.<br>Note: To avoid and resolve access violation exceptions, please see Warning and examples remarked below. |
| DashStyleHelper | A dashstyle used to construct the stroke. Possible values are:<br>&bull; DashStyleHelper.Dash<br>&bull; DashStyleHelper.DashDot<br>&bull; DashStyleHelper.DashDotDot<br>&bull; DashStyleHelper.Dot<br>&bull; DashStyleHelper.Solid |
| Name | A string representing the name of the line. |
| RenderTarget | The [RenderTarget](/docs/desktop/rendertarget) drawing context used for the line.<br>Note: This property must be set before accessing a stroke's BrushDX property. Please see Warning and examples remarked below. |
| StrokeStyle | A [SharpDX.Direct2D1.StrokeStyle](/docs/desktop/sharpdx_direct2d1_strokestyle) |
| Value | A double representing the value of the line. |
| Width | A float representing the width in pixels. |

## Examples

See the [AddLine()](/docs/desktop/addline) method for examples.

