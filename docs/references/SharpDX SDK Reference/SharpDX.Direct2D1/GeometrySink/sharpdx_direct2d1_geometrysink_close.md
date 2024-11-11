---
title: SharpDX.Direct2D1.GeometrySink.Close()
pathName: sharpdx_direct2d1_geometrysink_close
status: ready
section: references
parent: geometrysink
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Closes the geometry sink, indicates whether it is in an error state, and resets the sink's error state.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316932.aspx))

{% callout type="note" %}

Do not close the geometry sink while a figure is still in progress; doing so puts the geometry sink in an error state. For the close operation to be successful, there must be one **EndFigure()** call for each call to **BeginFigure()**. After calling this method, the geometry sink might not be usable. Direct2D implementations of this interface do not allow the geometry sink to be modified after it is closed, but other implementations might not impose this restriction.

{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

**<`geometrysink>**.Close()

## Parameters

This method does not accept any parameters.