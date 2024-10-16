---
title: "ColorInterpolationGamma"
pathName: sharpdx_direct2d1_gradientstopcollection_colorinterpolationgamma
---

## Definition

Indicates the gamma space in which the gradient stops are interpolated.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316786.aspx))

{% callout type="note" %}
Interpolating in a linear gamma space (Gamma.Linear) can avoid changes in perceived brightness caused by the effect of gamma correction in spaces where the gamma is not 1.0, such as the default sRGB color space, where the gamma is 2.2.
{% /callout %}

## Property Value

A `SharpDX.Direct2D1.Gamma` enum value specifies which gamma is used for interpolation.

Possible values include:

|  |  |
| --- | --- |
| StandardRgb | Interpolation is performed in the standard RGB (sRGB) gamma. |
| Linear | Interpolation is performed in the linear-gamma color space. |

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd368113.aspx))

## Syntax

`<gradientstopcollection>.ColorInterpolationGamma`

{% callout type="note" %}
Disclaimer: The [SharpDX SDK Reference](sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.
{% /callout %}
