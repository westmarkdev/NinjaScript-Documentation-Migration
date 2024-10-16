---
title: "SharpDX.DisposeBase.Dispose()"
path: sharpdx_disposebase_dispose
---

{% callout type="warning" %}
The [SharpDX SDK Reference](sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.
{% /callout %}

## Definition

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. (Implements I[Disposable.Dispose()](https://msdn.microsoft.com/en-us/library/es4s3w1d))

{% callout tip %}
For NinjaScript development purposes, the following documented SharpDX objects require Dispose() after they are used:
[Brush](sharpdx_direct2d1_brush), [GeometrySink](sharpdx_direct2d1_geometrysink), [GradientStopCollection](sharpdx_direct2d1_gradientstopcollection), [LinearGradientBrush](sharpdx_direct2d1_lineargradientbrush), [PathGeometry](sharpdx_direct2d1_pathgeometry), [RadialGradientBrush](sharpdx_direct2d1_radialgradientbrush), [SolidColorBrush](sharpdx_direct2d1_solidcolorbrush), [StrokeStyle](sharpdx_direct2d1_strokestyle), [TextFormat](sharpdx_directwrite_textformat), [TextLayout](sharpdx_directwrite_textlayout).
There are other undocumented SharpDX objects which are NOT included in this reference. Please be careful to dispose of any object (SharpDX or otherwise) which implements the IDisposeable interface - NinjaTrader is NOT guaranteed to dispose of these objects for you!
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

```csharp
<disposebaseobject>.Dispose()
```
