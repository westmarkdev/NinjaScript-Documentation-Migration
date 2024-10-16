---
title: "SharpDX.RectangleF"
pathName: /docs/desktop/sharpdx_rectanglef
---

|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |

## Definition

Structure using similar layout as [System.Drawing.RectangleF](https://www.google.com/search?q=system.drawing.rectangleF&ie=utf-8&oe=utf-8).

{% callout type="note" %}
This structure is slightly different from [System.Drawing.RectangleF](https://www.google.com/search?q=system.drawing.rectangleF&ie=utf-8&oe=utf-8) as it is internally storing Left, Top, Right, Bottom instead of Left, Top, Width, Height. Although automatic casting from a to System.Drawing.Rectangle is provided.
{% /callout %}

## Syntax

```csharp
struct RectangleF
```

## Constructors

|  |  |
| --- | --- |
| new RectangleF() | Initializes a new instance of the RectangleF struct. |
| new RectangleF(float x, float y, float width, float height) | Initializes a new instance of the RectangleF with specific dimensions. |

## Properties

|  |  |
| --- | --- |
| Bottom | Gets or sets the bottom. |
| Height | Gets or sets the height. |
| Left | Gets or sets the left. |
| Right | Gets or sets the right. |
| Top | Gets or sets the top. |
| Width | Gets or sets the width. |
| X | Gets or sets the left position. |
| Y | Gets or sets the top position. |
