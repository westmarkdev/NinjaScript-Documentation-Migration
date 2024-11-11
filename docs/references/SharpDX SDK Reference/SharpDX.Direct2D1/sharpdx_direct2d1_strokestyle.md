---
title: SharpDX.Direct2D1.StrokeStyle
pathName: sharpdx_direct2d1_strokestyle
status: ready
section: references
parent: sharpdx_direct2d1
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Describes the caps, miter limit, line join, and dash information for a stroke.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd372217.aspx))

{% callout type="note" %}

1. A stroke style is a device-independent resource; you can create it once then retain it for the life of your application. Please see the [MSDN Direct2D Resources Overview](https://msdn.microsoft.com/en-us/library/dd756757(v=vs.85).aspx) for more information.
2. For convenience, Direct2D provides the [StrokeStyleProperties](sharpdx_direct2d1_strokestyleproperties.md) function for creating new a StrokeStyle. |
{% /callout %}

## Syntax

**class StrokeStyle**

## Constructors

{% table %}

---

* **new StrokeStyle(Factory factory, [StrokeStyleProperties](sharpdx_direct2d1_strokestyleproperties.md) properties)** 
* Creates an StrokeStyle that describes start cap, dash pattern, and other features of a stroke. 
---
* **new StrokeStyle(Factory factory, [StrokeStyleProperties](sharpdx_direct2d1_strokestyleproperties.md) properties, float[] dashes)** 
* Creates an StrokeStyle that describes start cap, dash pattern, and other features of a stroke. 
{% /table %}

{% callout type="note" %}

---

* Tip: For NinjaScript development purposes, when creating a StrokeStyle object you should use the [NinjaTrader.Core.Globals.D2DFactory](d2dfactory) property |
{% /callout %}

## Method and Properties

{% table %}

---

* [DashCap](sharpdx_direct2d1_strokestyle_dashcap) 
* Gets a value that specifies how the ends of each dash are drawn. 
---
* [DashesCount](sharpdx_direct2d1_strokestyle_dashescount) 
* Retrieves the number of entries in the dashes array. 
---
* [DashOffset](sharpdx_direct2d1_strokestyle_dashoffset) 
* Retrieves a value that specifies how far in the dash sequence the stroke will start. 
---
* [DashStyle](sharpdx_direct2d1_strokestyle_dashstyle) 
* Gets a value that describes the stroke's dash pattern. 
---
* [Dispose()](sharpdx_disposebase_dispose) 
* Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. (Inherited from [SharpDX.DisposeBase](sharpdx_disposebase.md).)
---
* [EndCap](sharpdx_direct2d1_strokestyle_endcap) 
* Retrieves the type of shape used at the end of a stroke. 
---
* [GetDashes()](sharpdx_direct2d1_strokestyle_getdashes)
* Copies the dash pattern to the specified array. 
---
* [IsDisposed](sharpdx_disposebase_isdisposed.md) 
* Gets a value indicating whether this instance is disposed. (Inherited from DisposeBase.)
---
* [LineJoin](sharpdx_direct2d1_strokestyle_linejoin) 
* Retrieves the type of joint used at the vertices of a shape's outline.
---
* [MiterLimit](sharpdx_direct2d1_strokestyle_miterlimit) 
* Retrieves the limit on the ratio of the miter length to half the stroke's thickness. 
---
* [StartCap](sharpdx_direct2d1_strokestyle_startcap)
* Retrieves the type of shape used at the beginning of a stroke.
{% /table %}