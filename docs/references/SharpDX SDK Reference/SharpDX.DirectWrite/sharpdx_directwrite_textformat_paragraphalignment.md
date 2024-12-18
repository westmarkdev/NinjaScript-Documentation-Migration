---
title: SharpDX.DirectWrite.TextFormat.ParagraphAlignment
pathName: sharpdx_directwrite_textformat_paragraphalignment
status: ready
section: references
parent: sharpdx_directwrite
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Gets or sets the alignment option of a paragraph which is relative to the top and bottom edges of a layout box.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316675.aspx))

## Property Value

A **SharpDX.DirectWrite.ParagraphAlignment** enum value that indicates the current paragraph alignment option.

## Possible values are

{% table %}

* Alignment Type
* Description

---

* Near
* The top of the text flow is aligned to the top edge of the layout box.

---

* Far
* The bottom of the text flow is aligned to the bottom edge of the layout box.

---

* Center
* The center of the flow is aligned to the center of the layout box.
{% /table %}

## Syntax

**<`textlayout`>.ParagraphAlignment**
