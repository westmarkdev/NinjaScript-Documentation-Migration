---
title: "RenderTarget"
pathName: rendertarget
---

## Definition

A SharpDX Direct2D1 RenderTarget creates objects and exposes methods used for drawing in the chart area.

{% callout type="note" %}
Notes:

1. There are two RenderTarget's used in a chart. This is important to understand when creating/destroying device resources. Please see the [OnRenderTargetChanged()](onrendertargetchanged) page for more information.
2. For a walkthrough for using the SharpDX RenderTarget, please see the educational resource [Using SharpDX for Custom Chart Rendering](using_sharpdx_for_custom_chart_rendering).
{% /callout %}

## Property Value

A [SharpDX.Direct2D1.RenderTarget](sharpdx_direct2d1_rendertarget).

|  |  |
| --- | --- |
| SharpDX.Direct2D1.WindowRenderTarget  | Used to render the actual contents of the chart to the window. |
| SharpDX.Direct2D1.WicRenderTarget | Used to render a bitmap for a few scenarios: <ol><li>A user clicks on a chart area; a bitmap is used to do any hit detection to determine where the user clicked.</li><li>User clicks on the Windows task bar; a bitmap is used to render the preview of the contents of the chart display through a thumbnail on the task bar.</li><li>A user resizes the chart; a bitmap is used to render the current contents of the chart, which is redrawn using the WindowRenderTarget after the desired changes have been set.</li></ol> |

## Syntax

RenderTarget

{% callout type="warning" %}
Each DirectX render target requires its own brushes. You must create brushes directly in [OnRender()](onrender) or using [OnRenderTargetChanged()](onrestorevalues). If you do not, you will receive an error at runtime similar to:
"A DirectX error has occurred while rendering the chart: HRESULT: [0x88990015], Module: [SharpDX.Direct2D1], ApiCode: [D2DERR_WRONG_RESOURCE_DOMAIN/WrongResourceDomain], Message: The resource was realized on the wrong render target. Each DirectX render target requires its own brushes. You must create brushes directly in OnRender() or using OnRenderTargetChanged()."
Please see [OnRenderTargetChanged()](onrendertargetchanged) for examples with brushes that need to be recalculated, or [OnRender()](onrender) for an example of recreating a static brush.
{% /callout %}
