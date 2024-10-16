---
title: "SharpDX.Direct2D1.PathGeometry.GetBounds()"
pathName: /docs/desktop/sharpdx_direct2d1_pathgeometry_getbounds
---

|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |

## Definition

Retrieves the bounds of the geometry.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd742751.aspx))

## Method Return Value

A [SharpDX.RectangleF](/docs/desktop/sharpdx_rectanglef) which contains the bounds of this geometry. If the bounds are empty, this will be a rect where bounds.left > bounds.right.

## Syntax

```csharp
<pathgeometry>.GetBounds()
```

## Parameters

This method does not accept any parameters.

