---
title: SharpDX.Direct2D1.RadialGradientBrushProperties
pathName: sharpdx_direct2d1_radialgradientbrushproperties
status: ready
section: references
parent: radialgradientbrush
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Contains the gradient origin offset and the size and position of the gradient ellipse for a **RadialGradientBrush**.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd368149.aspx))

## Syntax

struct **RadialGradientBrushProperties**

## Constructors

{% table %}

* Constructor
* Description

---

* new **RadialGradientBrushProperties**()
* Initializes a new instance of the **RadialGradientBrushProperties** structure
{% /table %}

## Properties

{% table %}

* Property
* Description

---

* **Center**
* A **SharpDX.Vector2** representing the brush's coordinate space, the center of the gradient ellipse.

---

* **GradientOriginOffset**
* A **SharpDX.Vector2** representing brush's coordinate space, the offset of the gradient origin relative to the gradient ellipse's center.

---

* **RadiusX**
* A float in the brush's coordinate space, the x-radius of the gradient ellipse.

---

* **RadiusY**
* A float in the brush's coordinate space, the y-radius of the gradient ellipse.
{% /table %}
