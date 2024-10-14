---
title: "SharpDX.Direct2D1.StrokeStyle.LineJoin"
pathName: sharpdx_direct2d1_strokestyle_linejoin
---

{% callout type="warning" %}
The [SharpDX SDK Reference](sharpdx_sdk_reference) section was compiled from the official [SharpDX Documentation](http://sharpdx.org/) and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN [Direct2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370990.aspx) and [DirectWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038.aspx) unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.
{% /callout %}

## Definition

Retrieves the type of joint used at the vertices of a shape's outline.

(See also [unmanaged API documentation](https://msdn.microsoft.com/en-us/library/dd372240.aspx))

{% callout type="note" %}
A miter limit affects how sharp miter joins are allowed to be. If the line join style is MiterOrBevel, then the join will be mitered with regular angular vertices if it doesn't extend beyond the miter limit; otherwise, the line join will be beveled.
{% /callout %}

## Property Value

A SharpDX.Direct2D1.LineJoin enum value that specifies the type of joint used at the vertices of a shape's outline.

Possible values are:

|  |  |
| --- | --- |
| Miter | Regular angular vertices.  |
| Bevel | Beveled vertices.  |
| Round | Rounded vertices.  |
| MiterOrBevel | Regular angular vertices unless the join would extend beyond the miter limit; otherwise, beveled vertices.  |

(See also [unmanaged API documentation](http://msdn.microsoft.com/en-us/library/dd368130.aspx))

## Syntax

```csharp
<strokestyle>.LineJoin
```