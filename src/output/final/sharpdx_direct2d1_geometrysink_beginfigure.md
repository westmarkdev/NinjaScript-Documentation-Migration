---
title: "SharpDX.Direct2D1.GeometrySink.BeginFigure()"
pathName: /docs/desktop/sharpdx_direct2d1_geometrysink_beginfigure
---

|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |

## Definition

Starts a new figure at the specified point.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316929.aspx))

## Method Return Value

This method does not return a value.

## Syntax

```csharp
<geometrysink>.BeginFigure(Vector2 vector2, FigureBegin figureBegin)
```

## Parameters

|  |  |
| --- | --- |
| vector2 | The [SharpDX.Vector2](/docs/desktop/sharpdx_vector2) at which to begin the new figure. |
| figureBegin | The [SharpDX.Direct2D1.FigureBegin](/docs/desktop/sharpdx_direct2d1_figurebegin) which determines whether the new figure should be hollow or filled. |
