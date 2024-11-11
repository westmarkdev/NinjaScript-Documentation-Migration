---
title: SharpDX.Direct2D1
pathName: sharpdx_direct2d1
status: ready
section: references
parent: sharpdx_sdk_reference
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

The SharpDX.Direct2D1 namespace provides a managed Direct2D API. Direct2D is a hardware-accelerated, immediate-mode, 2-D graphics API that provides high performance and high-quality rendering for 2-D geometry, bitmaps, and text.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd370990.aspx))

## In this section

{% table %}

* Member
* Description

---

* [AntialiasMode](sharpdx_direct2d1_antialiasmode)
* Specifies how the edges of nontext primitives are rendered.

---

* [ArcSegment](sharpdx_direct2d1_arcsegment)
* Describes an elliptical arc between two points.

---

* [ArcSize](sharpdx_direct2d1_arcsize)
* Specifies whether an arc should be greater than 180 degrees.

---

* [Brush](sharpdx_direct2d1_brush)
* Defines an object that paints an area. Interfaces that derive from Brush describe how the area is painted.

---

* [BrushProperties](sharpdx_direct2d1_brushproperties)
* Describes the opacity and transformation of a brush.

---

* [DrawTextOptions](sharpdx_direct2d1_drawtextoptions)
* Specifies whether text snapping is suppressed or clipping to the layout rectangle is enabled. This enumeration allows a bitwise combination of its member values.

---

* [Ellipse](sharpdx_direct2d1_ellipse)
* Contains the center point, x-radius, and y-radius of an ellipse.

---

* [FigureBegin](sharpdx_direct2d1_figurebegin)
* Indicates whether a specific GeometrySink figure is filled or hollow.

---

* [FigureEnd](sharpdx_direct2d1_figureend)
* Indicates whether a specific GeometrySink figure is open or closed.

---

* [FillMode](sharpdx_direct2d1_fillmode)
* Specifies how the intersecting areas of geometries or figures are combined to form the area of the composite geometry.

---

* [GeometrySink](sharpdx_direct2d1_geometrysink.md)
* Describes a geometric path that can contain lines, arcs, cubic Bezier curves, and quadratic Bezier curves.

---

* [MeasuringMode](sharpdx_direct2d1_measuringmode)
* Indicates the measuring method used for **text layout**.

---

* [PathGeometry](sharpdx_direct2d1_pathgeometry.md)
* Represents a complex shape that may be composed of arcs, curves, and lines.

---

* [RenderTarget](sharpdx_direct2d1_rendertarget.md)
* Represents an object that can receive drawing commands.

---

* [SolidColorBrush](sharpdx_direct2d1_solidcolorbrush)
* Paints an area with a solid color.

---

* [StrokeStyle](sharpdx_direct2d1_strokestyle.md)
* Describes the caps, miter limit, line join, and dash information for a stroke.

---

* [SweepDirection](sharpdx_direct2d1_sweepdirection)
* Defines the direction that an elliptical arc is drawn.
{% /table %}
