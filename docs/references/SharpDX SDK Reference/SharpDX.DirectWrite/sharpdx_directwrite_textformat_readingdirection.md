---
title: SharpDX.DirectWrite.TextFormat.ReadingDirection
pathName: sharpdx_directwrite_textformat_readingdirection
status: ready
section: references
parent: sharpdx_directwrite
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Gets or sets the current reading direction for text in a paragraph.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd316678.aspx))

## Property Value

A **SharpDX.DirectWrite.ReadingDirection** enum value that indicates the current reading direction for text in a paragraph.

## Possible values are

{% table %}

---

* LeftToRight
* Indicates that reading progresses from left to right.

---

* RightToLeft
* Indicates that reading progresses from right to left.
{% /table %}

## Syntax

**<`textlayout>**.ReadingDirection
