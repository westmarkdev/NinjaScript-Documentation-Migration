---
title: SharpDX.Direct2D1.BrushProperties
pathName: sharpdx_direct2d1_brushproperties
status: ready
section: references
parent: sharpdx_direct2d1
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Describes the opacity and transformation of a brush.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd368077.aspx))

## Syntax

struct **BrushProperties**

## Constructors

{% table %}

* Constructor
* Description

---

* new **BrushProperties**()
* Initializes a new instance of the **BrushProperties** structure
{% /table %}

## Properties

{% table %}

* Property
* Description

---

* **Opacity**
* A value between 0.0f and 1.0f, inclusive, that specifies the degree of opacity of the brush.

---

* **Transform**
* The transformation that is applied to the brush.
{% /table %}