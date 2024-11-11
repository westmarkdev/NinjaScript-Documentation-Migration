---
title: SharpDX.Direct2D1.GeometrySink.EndFigure()
pathName: sharpdx_direct2d1_geometrysink_endfigure
status: ready
section: references
parent: geometrysink
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Ends the current figure; optionally, closes it.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316934.aspx))

## Method Return Value

This method does not return a value.

## Syntax

**<`geometrysink>.EndFigure(FigureEnd figureEnd)**

## Parameters

{% table %}

---

* figureEnd
* A **SharpDX.Direct2D1.FigureEnd** value that indicates whether the current figure is closed. If the figure is closed, a line is drawn between the current point and the start point specified by **BeginFigure()**.
{% /table %}