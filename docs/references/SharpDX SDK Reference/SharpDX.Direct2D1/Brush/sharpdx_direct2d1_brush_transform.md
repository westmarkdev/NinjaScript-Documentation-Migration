---
title: SharpDX.Direct2D1.Brush.Transform
pathName: sharpdx_direct2d1_brush_transform
status: ready
section: references
parent: brush
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Gets or sets the transform applied to this brush.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd371179(v=vs.85).aspx))

## Note

{% callout type="note" %}

When the brush transform is the identity matrix, the brush appears in the same coordinate space as the render target in which it is drawn.

{% /callout %}

## Property Value

A **Matrix3x2** transform applied to this brush.

## Syntax

**<`brush`>.Transform**
