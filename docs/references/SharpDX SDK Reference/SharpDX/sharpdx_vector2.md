---
title: SharpDX.Vector2
pathName: sharpdx_vector2
status: ready
section: references
parent: sharpdx
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Represents a two dimensional mathematical vector.

## Syntax

**struct** Vector2

## Disclaimer

{% callout type="note" %}

The [SharpDX SDK Reference](sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX / Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Tip

{% callout type="note" %}

For NinjaScript Development Purposes, you can use the **NinjaTrader.Gui.DxExtensions.ToVector2()** helper method to convert a **System.Windows.Point** structure to a **SharpDX.Vector2** used for SharpDX rendering.

{% /callout %}

## Constructors

{% table %}

* Constructor
* Description

---

* **Vector2()**
* Initializes a new instance of the Vector2 struct.

---

* **Vector2(float x, float y)**
* Initializes a new instance of the Vector2 struct using float values for x and y components.
{% /table %}

## Properties

{% table %}

* Property
* Description

---

* **X**
* A float for the X component of the vector.

---

* **Y**
* A float for the Y component of the vector.
{% /table %}