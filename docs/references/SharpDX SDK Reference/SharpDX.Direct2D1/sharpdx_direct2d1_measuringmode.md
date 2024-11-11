---
title: SharpDX.Direct2D1.MeasuringMode
pathName: sharpdx_direct2d1_measuringmode
status: ready
section: references
parent: sharpdx_direct2d1
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Indicates the measuring method used for **text layout**.

(See also **unmanaged API documentation**)

## Syntax

enum **MeasuringMode**

## Enumerators

{% table %}

---

* **Natural**
* Specifies that text is measured using glyph ideal metrics whose values are independent to the current display resolution.

---

* **GdiClassic**
* Specifies that text is measured using glyph display-compatible metrics whose values tuned for the current display resolution.

---

* **GdiNatural**
* Specifies that text is measured using the same glyph display metrics as text measured by GDI using a font created with **CLEARTYPE_NATURAL_QUALITY**.
{% /table %}