---
title: "SharpDX.Direct2D1.Color4"
pathName: /docs/desktop/sharpdx_color4
---

|  |
| --- |
| Disclaimer: The [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page. |

## Definition

Represents a color in the form of rgba.

## Syntax

```csharp
struct Color4
```

### Constructor

|  |  |
| --- | --- |
| Color4() | Initializes a new instance of the Color4 struct |
| Color4([Color3](/docs/desktop/sharpdx_color3) color) | Initializes a new instance of the Color4 struct using a [SharpDX.Color3](/docs/desktop/sharpdx_color3) struct |
| Color4([Color3](/docs/desktop/sharpdx_color3) color, float alpha) | Initializes a new instance of the Color4 struct using a [SharpDX.Color3](/docs/desktop/sharpdx_color3) struct with a float for alpha values |
| Color4(float red, float green, float blue, float alpha) | Initializes a new instance of the Color4 struct using float values for red, green, blue |

## Properties

|  |  |
| --- | --- |
| Black | The Black color (0, 0, 0, 1) |
| White | The White color (1, 1, 1, 1) |
| Red | The red component of the color |
| Green | The green component of the color |
| Blue | The blue component of the color |
| Alpha | The alpha component of the color |