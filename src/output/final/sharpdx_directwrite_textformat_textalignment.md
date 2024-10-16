---
title: "SharpDX.DirectWrite.TextFormat.TextAlignment"
pathName: /docs/desktop/sharpdx_directwrite_textformat_textalignment
---

|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader.  The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK.  This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly.  Please refer to the official SharpDX Documentation for additional members not covered in this reference.  For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |

## Definition

Gets or sets the alignment option of text relative to the layout box's leading and trailing edge.

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd316681.aspx))

## Property Value

A SharpDX.DirectWrite.TextAlignment enum value of the current paragraph.

Possible values are:

|  |  |
| --- | --- |
| Leading | The leading edge of the paragraph text is aligned to the leading edge of the layout box. |
| Trailing | The trailing edge of the paragraph text is aligned to the trailing edge of the layout box. |
| Center | The center of the paragraph text is aligned to the center of the layout box. |
| Justified | Align text to the leading side, and also justify text to fill the lines. |

## Syntax

<textlayout>.TextAlignment  
--------------------------  