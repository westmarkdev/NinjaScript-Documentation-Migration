---
title: ChartControl
pathName: chartcontrol
parent: charts
section: references
status: review
---

The **ChartControl** class provides access to a wide range of properties and methods related to the location of objects on a chart and other chart-related properties. The **ChartControl** object provides information related to the entire hosting grid of the chart, which overlap with the [ChartPanel](chartpanel), [ChartScale](chartscale) and [ChartBars](chartbars).

{% callout type="note" %}

The **ChartControl** object is ONLY guaranteed to be available when a **NinjaScript** type initiates from a Chart Window. There are situations where an indicator or strategy starts from another Windows (such as the Control Center's Strategies Grid, or from a Strategy Analyzer), where the **ChartControl** object is NOT accessible. Therefore, the **ChartControl** object should always be safely accessed (e.g., from within a try-catch, or conditionally using null reference checks).

{% /callout %}

![ChartControl_1](chartcontrol_1.png)

{% callout type="warning" %}

Warning: The **ChartControl** and its methods and properties should ONLY be accessed once the **State** has reached **State.Historical**.

{% /callout %}

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* [AxisXHeight](axisxheight)
* Measures the distance (in pixels) between the x-axis and the top of the horizontal scroll bar

---

* [AxisYLeftWidth](axisyleftwidth)
* Measures the distance (in pixels) between the y-axis and the left margin of a chart

---

* [AxisYRightWidth](axisyrightwidth)
* Measures the distance (in pixels) between the y-axis and the right margin of a chart

---

* [BarMarginLeft](barmarginleft)
* Measures the margin to the left of each bar on the chart, in pixels

---

* [BarsArray](chartcontrol_barsarray)
* Provides a collection of [ChartBars](chartbars) objects currently configured on the chart

---

* [BarSpacingType](barspacingtype)
* Provides the type of bar spacing used for the primary [Bars](bars) object on the chart

---

* [BarsPeriod](chartcontrol_barsperiod)
* Provides the period (interval) used for the primary [Bars](bars) object on the chart

---

* [BarWidth](chartcontrol_barwidth)
* Measures the value of the bar width set for the primary [Bars](bars) object on the chart

---

* [BarWidthArray](barwidtharray)
* An array containing the values of the [BarWidth](chartcontrol_barwidth) properties of all [Bars](bars) objects on the chart

---

* [CanvasLeft](canvasleft)
* Indicates the x-coordinate (in pixels) of the beginning of the chart canvas area

---

* [CanvasRight](canvasright)
* Indicates the x-coordinate (in pixels) of the end of the chart canvas area

---

* [CanvasZoomState](canvaszoomstate)
* Indicates the current state of the Zoom tool on the chart

---

* [ChartPanels](chartpanels)
* Holds a collection of [ChartPanel](chartpanel) objects

---

* [CrosshairType](crosshairtype)
* Indicates the [Cross Hair](cross_hair) type currently enabled on the chart

---

* [FirstTimePainted](firsttimepainted)
* Indicates a time value of the first bar painted on the chart

---

* [GetBarPaintWidth()](getbarpaintwidth)
* Returns the width of the bars in the primary [Bars](bars) object on the chart, in pixels

---

* [GetSlotIndexByTime()](getslotindexbytime)
* Returns the slot index of the primary [Bars](bars) object on the chart corresponding to a specified time value

---

* [GetSlotIndexByX()](getslotindexbyx)
* Returns the slot index of the primary [Bars](bars) object on the chart corresponding to a specified x-coordinate on the visible chart canvas

---

* [GetTimeBySlotIndex()](gettimebyslotindex)
* Returns a time value corresponding to a specified slot index of the primary [Bars](bars) object on the chart

---

* [GetTimeByX()](gettimebyx)
* Returns a time value related to the primary [Bars](bars)' slot index at a specified x-coordinate on the chart canvas

---

* [GetXByBarIndex()](getxbybarindex)
* Returns the chart-canvas x-coordinate of the bar at a specified index of a specified [ChartBars](chartbars) object on the chart

---

* [GetXByTime()](getxbytime)
* Returns the chart-canvas x-coordinate of the slot index of the primary [Bars](bars) object corresponding to a specified time

---

* [Indicators](chartcontrol_indicators)
* Returns a collection of indicators currently configured on the chart

---

* [IsScrollArrowVisible](isscrollarrowvisible)
* Indicates the time-axis scroll arrow is visible in the top-right corner of the chart

---

* [IsStayInDrawMode](isstayindrawmode)
* Indicates the [Stay in Draw Mode](working_with_drawing_tools__ob) is currently enabled on the chart

---

* [IsYAxisDisplayedLeft](isyaxisdisplayedleft)
* Indicates the y-axis displays (in any chart panel) to the left side of the chart canvas

---

* [IsYAxisDisplayedOverlay](isyaxisdisplayedoverlay)
* Indicates an object on the chart is using the Overlay scale justification

---

* [IsYAxisDisplayedRight](chartcontrol_isyaxisdisplayedright.md)
* Indicates the y-axis displays (in any chart panel) to the right side of the chart canvas

---

* [LastSlotPainted](lastslotpainted)
* Indicates the slot index of the most recently painted bar on the primary [Bars](bars) object configured on the chart

---

* [LastTimePainted](lasttimepainted)
* Indicates the time of the most recently painted bar on the primary [Bars](bars) object configured on the chart

---

* [MouseDownPoint](mousedownpoint)
* Indicates the x- and y-coordinates of the mouse cursor at the most recent **OnMouseDown()** event

---

* [Properties](chartcontrol_properties)
* A collection of properties related to the configuration of the Chart

---

* [SlotsPainted](slotspainted)
* Indicates the number of index slots in which bars are painted within the chart canvas area

---

* [Strategies](chartcontrol_strategies)
* A collection of strategies configured on the chart

---

* [TimePainted](timepainted)
* Indicates the range of time in which bars are painted on the visible chart canvas
{% /table %}
