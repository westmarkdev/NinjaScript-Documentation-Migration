---
title: "SharpDX.DirectWrite.TextFormat.FontWeight"
pathName: sharpdx_directwrite_textformat_fontweight
---

{% callout type="warning" %}
The [SharpDX SDK Reference](sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.
{% /callout %}

## Definition

Gets the font weight of the text.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd316652.aspx))

{% callout type="note" %}

1. Weight differences are generally differentiated by an increased stroke or thickness that is associated with a given character in a typeface, as compared to a "normal" character from that same typeface.
2. Not all weights are available for all typefaces. When a weight is not available for a typeface, the closest matching weight is returned.
3. Font weight values less than 1 or greater than 999 are considered invalid, and they are rejected by font API functions.

{% /callout %}

## Property Value

A SharpDX.DirectWrite.FontWeight enum value that indicates the type of weight (such as normal, bold, or black). See table below.

## Syntax

```csharp
<textlayout>.FontWeight
```

Possible values are:

|  |  |
| --- | --- |
| Thin | Predefined font weight: Thin (100). |
| ExtraLight | Predefined font weight: Extra-light (200). |
| UltraLight | Predefined font weight: Ultra-light (200). |
| Light | Predefined font weight: Light (300). |
| Normal | Predefined font weight: Normal (400). |
| Regular | Predefined font weight: Regular (400). |
| Medium | Predefined font weight: Medium (500). |
| DemiBold | Predefined font weight: Demi-bold (600). |
| SemiBold | Predefined font weight: Semi-bold (600). |
| Bold | Predefined font weight: Bold (700). |
| ExtraBold | Predefined font weight: Extra-bold (800). |
| UltraBold | Predefined font weight: Extra-bold (800). |
| Black | Predefined font weight: Black (900). |
| Heavy | Predefined font weight: Heavy (900). |
| ExtraBlack | Predefined font weight: Extra-black (950). |
| UltraBlack | Predefined font weight: Ultra-black (950). |
| SemiLight | Predefined font weight: Normal (400). |