---
title: SharpDX.Direct2D1.GeometrySink.SetFillMode()
pathName: sharpdx_direct2d1_geometrysink_setfillmode
status: ready
section: references
parent: geometrysink
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Specifies the method used to determine which points are inside the geometry described by this geometry sink and which points are outside.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316937.aspx))

## Method Return Value

This method does not return a value.

## Syntax

**<`geometrysink>.SetFillMode(FillMode fillMode)**

## Parameters

{% table %}

---

* **fillMode**
* The [SharpDX.Direct2D1.FillMode](sharpdx_direct2d1_fillmode) used to determine whether a given point is part of the geometry.
{% /table %}
