---
title: SharpDX.Direct2D1.PathGeometry.FillContainsPoint()
pathName: sharpdx_direct2d1_pathgeometry_fillcontainspoint
status: ready
section: references
parent: pathgeometry
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Indicates whether the area filled by the geometry would contain the specified point given the specified flattening tolerance.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd316687.aspx))

## Method Return Value

A bool value which is true if the area filled by the geometry contains point; otherwise, false.

## Syntax

**<`pathgeometry>**.FillContainsPoint(**Vector2** point)

## Parameters

{% table %}

* Parameter
* Description

---

* **point**
* The [SharpDX.Vector2](sharpdx_vector2) point to test.
{% /table %}
