---
section: references
title: RenderTarget
pathName: rendertarget
parent: charts
status: imported
---

## Definition

A **SharpDX Direct2D1 RenderTarget** creates objects and exposes methods used for drawing in the chart area.

{% callout type="note" %}

Notes:

1. There are two RenderTarget's used in a chart. This is important to understand when creating/destroying device resources. Please see the [OnRenderTargetChanged()](onrendertargetchanged) page for more information.
2. For a walk through for using the SharpDX RenderTarget, please see the educational resource [Using SharpDX for Custom Chart Rendering](using_sharpdx_for_custom_chart_rendering).
{% /callout %}

## Property Value

A [SharpDX.Direct2D1.RenderTarget](sharpdx_direct2d1_rendertarget.md)

{% table %}

* Property
* Description

---

* **SharpDX.Direct2D1.WindowRenderTarget**
* Used to render the actual contents of the chart to the window

---

* **SharpDX.Direct2D1.WicRenderTarget**
* Used to render a bitmap for a few scenarios:
  1. A user clicks on a chart area; a bitmap is used to do any hit detection to determine where the user clicked.
  2. User clicks on the Windows task bar; a bitmap is used to render the preview of the contents of the chart display through a thumbnail on the task bar.
  3. A user re-sizes the chart; a bitmap is used to render the current contents of the chart, which is redrawn using the WindowRenderTarget after the desired changes have been set.
{% /table %}

## Syntax

**RenderTarget**

{% callout type="warning" %}

Warning: Each DirectX render target requires its own brushes. You must create brushes directly in [OnRender()](onrender) or using [OnRenderTargetChanged()](onrestorevalues). If you do not, you will receive an error at run time similar to:

"A direct X error has occurred while rendering the chart: HRESULT: [0x88990015], Module: [SharpDX.Direct2D1], ApiCode: [D2DERR_WRONG_RESOURCE_DOMAIN/WrongResourceDomain], Message: The resource was realized on the wrong render target. : Each DirectX render target requires its own brushes. You must create brushes directly in OnRender() or using OnRenderTargetChanged().

Please see [OnRenderTargetChanged()](onrendertargetchanged) for examples with brushes that need to be recalculated, or [OnRender()](onrender) for an example of recreating a static brush.

{% /callout %}

```
