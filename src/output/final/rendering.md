---
title: "Rendering"
pathName: /docs/desktop/rendering
---

Rendering methods and properties can be useful when carrying out custom drawing tasks for chart objects. Event handlers such as [OnCalculateMinMax()](/docs/desktop/oncalculateminmax) and [OnRender()](/docs/desktop/onrender) allow you to override behavior at key points in the rendering process.

{% callout type="note" %}

1. Some rendering methods and properties make use of [SharpDX](http://sharpdx.org/) libraries, which provide a managed framework for working with DirectX technology. Please see the [SharpDX SDK Reference](/docs/desktop/sharpdx_sdk_reference) for more information.
2. For a walk through for using the SharpDX, please see the educational resource [Using SharpDX for Custom Chart Rendering](/docs/desktop/using_sharpdx_for_custom_chart_rendering).
{% /callout %}

## Methods and Properties

|  |  |
| --- | --- |
| [RenderTarget](/docs/desktop/rendertarget) | Creates objects and exposes methods used for drawing in the chart area. |
| [ForceRefresh()](/docs/desktop/forcerefresh) | Forces OnRender() to be called, which will re-paint the chart. |
| [IsInHitTest](/docs/desktop/isinhittest) | Qualifies if object drawn in chart object should be selectable in the hit test procedure. |
| [IsSelected](/docs/desktop/isselected) | Indicates a chart object is currently selected. |
| [IsVisibleOnChart()](/docs/desktop/isvisibleonchart) | Indicates a chart object is visible on the chart canvas. |
| [MaxValue](/docs/desktop/maxvalue) | The maximum value used for the automatic scaling of the y axis. |
| [MinValue](/docs/desktop/minvalue) | The minimum value used for the automatic scaling of the y axis. |
| [OnCalculateMinMax()](/docs/desktop/oncalculateminmax) | An event driven method which is called while the chart scale is being updated. |
| [OnRender()](/docs/desktop/onrender) | Used to render custom drawing to a chart from various chart objects. |
| [OnRenderTargetChanged()](/docs/desktop/onrendertargetchanged) | Used for efficient handling of SharpDX resources. |
| [PanelUI](/docs/desktop/panelui) | The chart panel that is configured on the chart's UI. |
| [ZOrder](/docs/desktop/chart_zorder) | A unique identifier used to control the order in which chart objects are drawn on the chart's Z-axis. |
