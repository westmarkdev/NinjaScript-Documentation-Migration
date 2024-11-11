---
title: sharpdx_direct2d1_lineargradientbrushproperties
pathName: sharpdx_direct2d1_lineargradientbrushproperties
status: ready
section: references
parent: lineargradientbrush
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Contains the starting point and endpoint of the gradient axis for an **LinearGradientBrush**.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd368128.aspx))

## Syntax

struct **LinearGradientBrushProperties**

## Constructors

{% table %}

* Constructor
* Description

---

* new **LinearGradientBrushProperties**()
* Initializes a new instance of the **LinearGradientBrushProperties** structure
{% /table %}

## Properties

{% table %}

* Property
* Description

---

* **StartPoint**
* A **SharpDX.Vector2** representing brush's coordinate space, the starting point of the gradient axis.

---

* **EndPoint**
* A **SharpDX.Vector2** representing the brush's coordinate space, the endpoint of the gradient axis.
{% /table %}
