---
title: SharpDX.Direct2D1.LinearGradientBrush.StartPoint
pathName: sharpdx_direct2d1_lineargradientbrush_startpoint
status: ready
section: references
parent: lineargradientbrush
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Retrieves the starting coordinates of the linear gradient.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd371497.aspx))

{% callout type="note" %}

The start point and end point are described in the brush's space and are mapped to the render target when the brush is used. If there is a non-identity brush transform or render target transform, the brush's start point and end point are also transformed.

{% /callout %}

## Property Value

A **SharpDX.Vector2** representing the starting two-dimensional coordinates of the linear gradient, in the brush's coordinate space.

## Syntax

**<`lineargradientbrush`>.StartPoint**
