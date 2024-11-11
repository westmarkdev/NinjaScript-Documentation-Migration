---
title: sharpdx_size2f
pathName: sharpdx_size2f
status: ready
section: references
parent: sharpdx
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Structure using the same layout as [System.Drawing.SizeF](https://msdn.microsoft.com/en-us/library/system.drawing.sizef(v=vs.110).aspx)

## Syntax

struct **Size2F**

## Constructors

{% table %}

* Constructor
* Description

---

* new **Size2F**()
* Initializes a new instance of the **SizeF** struct

---

* new **Size2F**(float width, float height)
* Initializes a new instance of the **SizeF** struct from the specified dimensions.
{% /table %}

## Properties

{% table %}

* Property
* Description

---

* **Height**
* Gets or sets the vertical component of this **SizeF** structure.

---

* **Width**
* Gets or sets the horizontal component of this **SizeF** structure.
{% /table %}

```