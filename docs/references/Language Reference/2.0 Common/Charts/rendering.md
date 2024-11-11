---
section: references
title: Rendering
pathName: rendering
parent: charts
status: review
---

Rendering methods and properties can be useful when carrying out custom drawing tasks for chart objects. Event handlers such as **OnCalculateMinMax()** and **OnRender()** allow you to override behavior at key points in the rendering process.

{% callout type="note" %}

1. Some rendering methods and properties make use of [SharpDX](http://sharpdx.org/) libraries, which provide a managed framework for working with DirectX technology. Please see the [SharpDX SDK Reference](sharpdx_sdk_reference) for more information.
2. For a walk through for using the SharpDX, please see the educational resource [Using SharpDX for Custom Chart Rendering](using_sharpdx_for_custom_chart_rendering).
{% /callout %}

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* [RenderTarget](rendertarget)
* Creates objects and exposes methods used for drawing in the chart area.

---

* [ForceRefresh()](forcerefresh)
* Forces **OnRender()** to be called, which will re-paint the chart.

---

* [IsInHitTest](isinhittest)
* Qualifies if object drawn in chart object should be selectable in the hit test procedure.

---

* [IsSelected](isselected)
* Indicates a chart object is currently selected.

---

* [IsVisibleOnChart()](isvisibleonchart)
* Indicates a chart object is visible on the chart canvas.

---

* [MaxValue](maxvalue)
* The maximum value used for the automatic scaling of the y axis.

---

* [MinValue](minvalue)
* The minimum value used for the automatic scaling of the y axis.

---

* [OnCalculateMinMax()](oncalculateminmax)
* An event driven method which is called while the chart scale is being updated.

---

* [OnRender()](onrender)
* Used to render custom drawing to a chart from various chart objects.

---

* [OnRenderTargetChanged()](onrendertargetchanged)
* Used for efficient handling of SharpDX resources.

---

* [PanelUI](panelui)
* The chart panel that is configured on the chart's UI.

---

* [ZOrder](chart_zorder)
* A unique identifier used to control the order in which chart objects are drawn on the chart's Z-axis.
{% /table %}
