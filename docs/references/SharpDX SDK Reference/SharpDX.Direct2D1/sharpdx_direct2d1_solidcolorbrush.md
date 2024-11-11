---
title: SharpDX.Direct2D1.SolidColorBrush
pathName: sharpdx_direct2d1_solidcolorbrush
status: ready
section: references
parent: sharpdx_direct2d1
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Paints an area with a solid color.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd372207.aspx))

{% callout type="note" %}

* The **SolidColorBrush** can only be used with the render target that created it or with the compatible targets for that render target.
* A **SolidColorBrush** is a device-dependent resource. Please see the [MSDN Direct2D Resources Overview](https://msdn.microsoft.com/en-us/library/dd756757(v=vs.85).aspx) for more information.
* For convenience, Direct2D provides the [BrushProperties](sharpdx_direct2d1_brushproperties) function for creating a new **SolidColorBrush**.
{% /callout %}

## Syntax

class **SolidColorBrush**

{% table %}

* Tips

---

* 1. For NinjaScript Development purposes, you can use the [NinjaTrader.Gui.DxExtensions.ToDxBrush()](dxextensions_todxbrush) helper method to convert a **System.Windows.Media.SolidColorBrush** to a **SharpDX.Direct2D1.SolidColorBrush**.
* 2. General information on Direct2D brushes can be found on the [MSDN Direct2D Brushes Overview](https://msdn.microsoft.com/en-us/library/dd756651(v=vs.85).aspx).
{% /table %}

## Constructors

{% table %}

* Constructor
* Description

---

* new **SolidColorBrush**(RenderTarget renderTarget, Color4 color) | Creates a new **SolidColorBrush** that has the specified color and opacity.
* new **SolidColorBrush**(RenderTarget renderTarget, Color4 color, Nullable<`brushproperties`> brushProperties) | Creates a new **SolidColorBrush** that has the specified color and opacity.
{% /table %}

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* [Color](sharpdx_direct2d1_solidcolorbrush_color) 
* Retrieves or sets the color of the solid color brush.
---
* [Dispose()](sharpdx_disposebase_dispose) 
* Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. (Inherited from [SharpDX.DisposeBase](sharpdx_disposebase.md).)
---
* [IsDisposed](sharpdx_disposebase_isdisposed.md) 
* Gets a value indicating whether this instance is disposed. (Inherited from [SharpDX.DisposeBase](sharpdx_disposebase.md).)
---
* [Opacity](sharpdx_direct2d1_brush_opacity) 
* Gets or sets the degree of opacity of this brush. (Inherited from [Brush](sharpdx_direct2d1_brush).)
---
* [Transform](sharpdx_direct2d1_brush_transform) 
* Gets or sets the transform applied to this brush. (Inherited from [Brush](sharpdx_direct2d1_brush).)
---

{% /table %}