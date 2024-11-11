---
title: SharpDX.Direct2D1.Ellipse
pathName: sharpdx_direct2d1_ellipse
status: ready
section: references
parent: sharpdx_direct2d1
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Contains the center point, x-radius, and y-radius of an ellipse.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd368097.aspx))

## Syntax

struct **Ellipse**

## Constructors

{% table %}

* Constructor
* Description

---

* new **Ellipse**()
* Initializes a new instance of the **Ellipse** struct

---

* new **Ellipse**(**Vector2** center, float radiusX, float radiusY)
* Initializes a new instance of the **Ellipse** struct with specific dimensions
{% /table %}

## Properties

{% table %}

* Property
* Description

---

* **Point**
* A **SharpDX.Vector** for the center point of the ellipse

---

* **RadiusX**
* A float for the X-radius of the ellipse

---

* **RadiusY**
* A float for the Y-radius of the ellipse
{% /table %}