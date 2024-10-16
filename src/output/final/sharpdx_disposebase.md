---
title: "DisposeBase"
pathName: /docs/desktop/sharpdx_disposebase
---

|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |

## Definition

Base class for a [System.IDisposable](https://msdn.microsoft.com/en-us/library/aax125c9) class.

{% callout type="tip" %}
For NinjaScript development purposes, the following documented SharpDX objects require [Dispose()](/docs/desktop/sharpdx_disposebase_dispose) after they are used:
[Brush](/docs/desktop/sharpdx_direct2d1_brush), [GeometrySink](/docs/desktop/sharpdx_direct2d1_geometrysink), [GradientStopCollection](/docs/desktop/sharpdx_direct2d1_gradientstopcollection), [LinearGradientBrush](/docs/desktop/sharpdx_direct2d1_lineargradientbrush), [PathGeometry](/docs/desktop/sharpdx_direct2d1_pathgeometry), [RadialGradientBrush](/docs/desktop/sharpdx_direct2d1_radialgradientbrush), [SolidColorBrush](/docs/desktop/sharpdx_direct2d1_solidcolorbrush), [StrokeStyle](/docs/desktop/sharpdx_direct2d1_strokestyle), [TextFormat](/docs/desktop/sharpdx_directwrite_textformat), [TextLayout](/docs/desktop/sharpdx_directwrite_textlayout).
There are other undocumented SharpDX objects which are NOT included in this reference. Please be careful to dispose of any object (SharpDX or otherwise) which implements the IDisposable interface - NinjaTrader is NOT guaranteed to dispose of these objects for you!
{% /callout %}

## Methods and Properties

|  |  |
| --- | --- |
| IsDisposed | Gets a value indicating whether this instance is disposed.  |
| Dispose() | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. (Implements [IDisposable.Dispose()](https://msdn.microsoft.com/en-us/library/es4s3w1d)) |
