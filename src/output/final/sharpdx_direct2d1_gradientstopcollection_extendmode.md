---
title: "SharpDX.Direct2D1.GradientStopCollection.ExtendMode"
pathName: /docs/sharpdx_direct2d1_gradientstopcollection_extendmode
---

|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |

## Definition

Indicates the behavior of the gradient outside the normalized gradient range.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316789.aspx))

{% callout type="note" %}
For an [LinearGradientBrush](/docs/desktop/sharpdx_direct2d1_lineargradientbrush), the brush's content area is the gradient axis. For an [RadialGradientBrush](/docs/desktop/sharpdx_direct2d1_radialgradientbrush), the brush's content is the area within the gradient ellipse.
{% /callout %}

## Property Value

A SharpDX.ExtendMode enum value which determines how a brush paints areas outside of its normal content area.

Possible values include:

|  |  |
| --- | --- |
| Clamp | Repeat the edge pixels of the brush's content for all regions outside the normal content area. |
| Wrap | Repeat the brush's content. |
| Mirror | The same as Wrap, except that alternate tiles of the brush's content are flipped. (The brush's normal content is drawn untransformed.) |

(see also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd368100.aspx))

## Syntax

<gradientstopcollection>.ExtendMode
