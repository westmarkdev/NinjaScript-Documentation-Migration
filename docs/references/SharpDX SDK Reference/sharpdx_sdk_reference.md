---
title: SharpDX SDK Reference
pathName: sharpdx_sdk_reference
status: ready
section: references
parent: sharpdx_sdk_reference
---

{% callout type="warning" %}

Disclaimer: The **SharpDX SDK Reference** section was compiled from the official **SharpDX Documentation** and was NOT authored by NinjaTrader. The contents of this section are provided as-is and only cover a fraction of what is available from the SharpDX SDK. This page was intended only as a reference guide to help you get started with some of the 2D Graphics concepts used in the NinjaTrader.Custom assembly. Please refer to the official SharpDX Documentation for additional members not covered in this reference. For more seasoned graphic developers, the original MSDN **Direct2D1** and **DirectWrite** unmanaged API documentation can also be helpful for understanding the DirectX/Direct2D run-time environment. For NinjaScript development purposes, we document only essential members in the structure of this page.

{% /callout %}

SharpDX is an [open-source](https://github.com/sharpdx/SharpDX) managed .NET wrapper of the DirectX API allowing the development of high performance game, 2D and 3D graphics rendering as well as realtime sound application.

{% callout type="note" %}

Tip: The concepts discussed in this section only apply to NinjaScript objects which use the Chart's **OnRender()** method. For code examples which demonstrate usage, please refer to the [Using SharpDX for Custom Chart Rendering](using_sharpdx_for_custom_chart_rendering) educational resource. You may also view the source code of various [ChartStyles](chartstyletype) , [DrawingTools](drawing_tools) , and [Indicators](docs/references/Language%20Reference/2.0%20Common/system_indicator_methods.md) which come pre-installed in the NinjaTrader.Custom project (Documents\NinjaTrader 8\bin\Custom).

{% /callout %}

## In this section

{% table %}

---

* [SharpDX](sharpdx) 

* The SharpDX namespace contains fundamental classes used by SharpDX. |
---

* [SharpDX.Direct2D1](sharpdx_direct2d1) 
* The SharpDX.Direct2D1 namespace provides a managed Direct2D API. Direct2D is a hardware-accelerated, immediate-mode, 2-D graphics API that provides high performance and high-quality rendering for 2-D geometry, bitmaps, and text.
---
* [SharpDX.DirectWrite](sharpdx_directwrite) 
* The SharpDX.DirectWrite namespace provides a managed DirectWrite API. DirectWrite supports high-quality text rendering, resolution-independent outline fonts, and full Unicode text and layouts.
---

{% /table %}
