---
title: SharpDX.Direct2D1.CapStyle
pathName: sharpdx_direct2d1_capstyle
status: ready
section: references
parent: sharpdx_direct2d1
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Describes the shape at the end of a line or segment.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd368079.aspx))

## Syntax

enum **CapStyle**

## Enumerators

{% table %}

* Enumerator
* Description

---

* **Flat**
* A cap that does not extend past the last point of the line. Comparable to cap used for objects other than lines.

---

* **Square**
* Half of a square that has a length equal to the line thickness.

---

* **Round**
* A semicircle that has a diameter equal to the line thickness.

---

* **Triangle**
* An isosceles right triangle whose hypotenuse is equal in length to the thickness of the line.
{% /table %}
