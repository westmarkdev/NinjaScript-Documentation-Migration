---
title: SharpDX.Direct2D1.RenderTarget.FillEllipse()
pathName: sharpdx_direct2d1_rendertarget_fillellipse
status: ready
section: references
parent: rendertarget
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Paints the interior of the specified ellipse.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd371928.aspx))

{% callout type="note" %}

This method doesn't return an error code if it fails.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

**RenderTarget.FillEllipse**(**Ellipse ellipse**, **Brush brush**)

## Parameters

{% table %}

* Parameter
* Description

---

* **brush**
* A **SharpDX.Direct2D1.Brush** used to paint the interior of the ellipse.

---

* **ellipse**
* A **SharpDX.Direct2D1.Ellipse** which describes the position and radius, in device-independent pixels, of the ellipse to paint.
{% /table %}
