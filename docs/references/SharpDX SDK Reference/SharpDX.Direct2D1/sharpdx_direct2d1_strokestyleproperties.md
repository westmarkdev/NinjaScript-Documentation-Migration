---
title: SharpDX.Direct2D1.StrokeStyleProperties
pathName: sharpdx_direct2d1_strokestyleproperties
status: ready
section: references
parent: sharpdx_direct2d1
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Describes the stroke that outlines a shape.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd368164.aspx))

## Syntax

struct **StrokeStyleProperties**

## Properties

{% table %}

* Property
* Description

---

* **StartCap**
* The [StartCap](sharpdx_direct2d1_strokestyle_startcap) value applied to the start of all the open figures in a stroked geometry.

---

* **EndCap**
* The [EndCap](sharpdx_direct2d1_strokestyle_endcap) value applied to the end of all the open figures in a stroked geometry.

---

* **DashCap**
* The [DashCap](sharpdx_direct2d1_strokestyle_dashcap) value for the shape at either end of each dash segment.

---

* **LineJoin**
* A [LineJoin](sharpdx_direct2d1_strokestyle_linejoin) value that describes how segments are joined. This value is ignored for a vertex if the segment flags specify that the segment should have a smooth join.

---

* **MiterLimit**
* The [MeterLImit](sharpdx_direct2d1_strokestyle_miterlimit) value of the thickness of the join on a mitered corner. This value is always treated as though it is greater than or equal to 1.0f.

---

* **DashStyle**
* A [DashStyle](sharpdx_direct2d1_strokestyle_dashstyle) value that specifies whether the stroke has a dash pattern and, if so, the dash style.

---

* **DashOffset**
* A [DashOffset](sharpdx_direct2d1_strokestyle_dashoffset) value that specifies an offset in the dash sequence. A positive dash offset value shifts the dash pattern, in units of stroke width, toward the start of the stroked geometry. A negative dash offset value shifts the dash pattern, in units of stroke width, toward the end of the stroked geometry.
{% /table %}
