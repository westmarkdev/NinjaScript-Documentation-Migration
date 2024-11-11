---
title: SharpDX.DirectWrite.TextLayout.GetLineMetrics()
pathName: sharpdx_directwrite_textlayout_getlinemetrics
status: ready
section: references
parent: sharpdx_directwrite
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

## Definition

Retrieves the information about each individual text line of the text string.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316763(v=vs.85).aspx))

## Method Return Value

A [LineMetrics](sharpdx_directwrite_linemetrics)[] contains a pointer to an array of structures containing various calculated length values of individual text lines.

## Syntax

**<`textlayout`>.GetLineMetrics()**

## Parameters

This method does not accept any parameters.
