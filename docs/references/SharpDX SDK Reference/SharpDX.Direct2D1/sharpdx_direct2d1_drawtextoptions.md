---
title: SharpDX.Direct2D1.DrawTextOptions
pathName: sharpdx_direct2d1_drawtextoptions
status: ready
section: references
parent: sharpdx_direct2d1
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Specifies whether text snapping is suppressed or clipping to the layout rectangle is enabled. This enumeration allows a bitwise combination of its member values.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd368095.aspx))

## Syntax

enum **DrawTextOptions**

## Enumerators

{% table %}

* Enumerator
* Description

---

* **NoSnap**
* Text is not vertically snapped to pixel boundaries. This setting is recommended for text that is being animated.

---

* **Clip**
* Text is clipped to the layout rectangle.

---

* **None**
* Text is vertically snapped to pixel boundaries and is not clipped to the layout rectangle.
{% /table %}
