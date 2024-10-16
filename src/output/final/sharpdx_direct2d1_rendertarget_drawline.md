---
title: "SharpDX.Direct2D1.RenderTarget.DrawLine()"
pathName: /docs/desktop/sharpdx_direct2d1_rendertarget_drawline
---

|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |


## Definition

Draws a line between the specified points.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd371895.aspx))

{% callout type="note" %}
This method doesn't return an error code if it fails.
{% /callout %}


## Method Return Value

This method does not return a value.


## Syntax

```csharp
RenderTarget.DrawLine(Vector2 point0, Vector2 point1, Brush brush)
```

```csharp
RenderTarget.DrawLine(Vector2 point0, Vector2 point1, Brush brush, float strokeWidth)
```

```csharp
RenderTarget.DrawLine(Vector2 point0, Vector2 point1, Brush brush, float strokeWidth, StrokeStyle strokeStyle)
```

## Parameters

|  |  |
| --- | --- |
| brush | The [SharpDX.Direct2D1.Brush](/docs/desktop/sharpdx_direct2d1_brush) brush used to paint the line's stroke. |
| point0 | A [SharpDX.Vector2](/docs/desktop/sharpdx_vector2) which determines the start point of the line, in device-independent pixels. |
| point1 | A [SharpDX.Vector2](/docs/desktop/sharpdx_vector2) which determines the end point of the line, in device-independent pixels. |
| strokeStyle | The [SharpDX.Direct2D1.StrokeStyle](/docs/desktop/sharpdx_direct2d1_strokestyle) to paint, or null to paint a solid line. |
| strokeWidth | A value greater than or equal to 0.0f that specifies the width of the stroke. If this parameter isn't specified, it defaults to 1.0f. The stroke is centered on the line. |

