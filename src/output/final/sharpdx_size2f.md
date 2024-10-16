---
title: "SharpDX.Size2F"
pathName: /docs/desktop/sharpdx_size2f
---

|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |

## Definition

Structure using the same layout as [System.Drawing.SizeF](https://msdn.microsoft.com/en-us/library/system.drawing.sizef(v=vs.110).aspx)

## Syntax

```csharp
struct Size2F
```

## Constructors

|  |  |
| --- | --- |
| new Size2F() | Initializes a new instance of the SizeF struct  |
| new Size2F(float width, float height) | Initializes a new instance of the SizeF struct from the specified dimensions. |

## Properties

|  |  |
| --- | --- |
| Height | Gets or sets the vertical component of this SizeF structure. |
| Width | Gets or sets the horizontal component of this SizeF structure. |


