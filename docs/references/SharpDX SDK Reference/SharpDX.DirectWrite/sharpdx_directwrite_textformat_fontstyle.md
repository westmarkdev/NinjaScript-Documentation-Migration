---
title: SharpDX.DirectWrite.TextFormat.FontStyle
pathName: sharpdx_directwrite_textformat_fontstyle
status: ready
section: references
parent: sharpdx_directwrite
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Gets the font style of the text.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316649.aspx))

## Property Value

A **SharpDX.DirectWrite.FontStyle** enum value which indicates the type of font style (such as slope or incline).

## Possible values are

{% table %}

* Font Style
* Description

---

* Normal
* The characters in a normal, or roman, font are upright.

---

* Oblique
* The characters in an oblique font are artificially slanted.

---

* Italic
* The characters in an italic font are truly slanted and appear as they were designed.
{% /table %}

## Syntax

**<`textlayout`>.FontStyle**
