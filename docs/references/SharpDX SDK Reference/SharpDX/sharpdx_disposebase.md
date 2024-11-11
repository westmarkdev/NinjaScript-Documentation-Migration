---
title: DisposeBase
pathName: sharpdx_disposebase
status: ready
section: references
parent: sharpdx
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Base class for a **System.IDisposable** class.

{% callout type="note" %}

Tip: For NinjaScript development purposes, the following documented SharpDX objects require **Dispose()** after they are used:

* [Brush](sharpdx_direct2d1_brush)
* [GeometrySink](sharpdx_direct2d1_geometrysink.md)
* [GradientStopCollection](sharpdx_direct2d1_gradientstopcollection.md)
* [LinearGradientBrush](sharpdx_direct2d1_lineargradientbrush.md)
* [PathGeometry](sharpdx_direct2d1_pathgeometry.md)
* [RadialGradientBrush](sharpdx_direct2d1_radialgradientbrush.md)
* [SolidColorBrush](sharpdx_direct2d1_solidcolorbrush)
* [StrokeStyle](sharpdx_direct2d1_strokestyle.md)
* [TextFormat](sharpdx_directwrite_textformat)
* [TextLayout](sharpdx_directwrite_textlayout)

There are other undocumented SharpDX objects which are NOT included in this reference. Please be careful to dispose of any object (SharpDX or otherwise) which implements the I**Disposable** interface - NinjaTrader is NOT guaranteed to dispose of these objects for you!

{% /callout %}

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* **IsDisposed**
* Gets a value indicating whether this instance is disposed.

---

* **Dispose()**
* Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. (Implements **IDisposable.Dispose()**)
{% /table %}
