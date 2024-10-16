---
title: "SharpDX.Direct2D1.GradientStop"
pathName: sharpdx_direct2d1_gradientstop
---

{% callout type="warning" %}
The [SharpDX SDK Reference](sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.
{% /callout %}

## Definition

Contains the position and color of a gradient stop.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd368119.aspx))

{% callout type="note" %}

1. Gradient stops can be specified in any order if they are at different positions. Two stops may share a position. In this case, the first stop specified is treated as the "low" stop (nearer 0.0f) and subsequent stops are treated as "higher" (nearer 1.0f). This behavior is useful if a caller wants an instant transition in the middle of a stop.
2. Typically, there are at least two points in a collection, although creation with only one stop is permitted. For example, one point is at position 0.0f, another point is at position 1.0f, and additional points are distributed in the [0, 1] range. Where the gradient progression is beyond the range of [0, 1], the stops are stored, but may affect the gradient.
3. When drawn, the [0, 1] range of positions is mapped to the brush, in a brush-dependent way. For details, see LinearGradientBrush and RadialGradientBrush.
4. Gradient stops with a position outside the [0, 1] range cannot be seen explicitly, but they can still affect the colors produced in the [0, 1] range. For example, a two-stop gradient {0.0f, Black}, {2.0f, White} is indistinguishable visually from {0.0f, Black}, {1.0f, Mid-level gray}. Also, the colors are clamped before interpolation.
{% /callout %}

## Syntax

struct GradientStop

## Properties

|  |  |
| --- | --- |
| Position | A float value that indicates the relative position of the gradient stop in the brush. This value must be in the [0.0f, 1.0f] range if the gradient stop is to be seen explicitly. |
| Color | The [SharpDX.Color](sharpdx_color) of the gradient stop. |
