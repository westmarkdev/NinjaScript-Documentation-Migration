










 


ChartControl







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartcontrol.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt;
ChartControl | [Previous page](chartbars_toindex.htm)
[Return to chapter overview](chart.htm)










The ChartControl class provides access to a wide range of properties and methods related to the location of objects on a chart and other chart-related properties.  The ChartControl object provides information related to the entire hosting grid of the chart, which overlap with the [ChartPanel](chartpanel.htm), [ChartScale](chartscale.htm) and [ChartBars](chartbars.htm).


 


 




|  |
| --- |
| Note: The ChartControl object is ONLY guaranteed to be available when a NinjaScript type initiates from a Chart Window.  There are situations where an indicator or strategy starts from another Windows (such as the Control Center's Strategies Grid, or from a Strategy Analyzer), where the ChartContol object is NOT accessible.   Therefore, the ChartControl object should always be safely accessed (e.g., from within a try-catch, or conditionally using null reference checks) |



 


 


![ChartControl_1](chartcontrol_1.png)


 





|  |
| --- |
| Warning:  The ChartControl and its methods and properties should ONLY be access once the [State](state.htm) has reached State.Historical |



 


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [AxisXHeight](axisxheight.htm) | Measures the distance (in pixels) between the x-axis and the top of the horizontal scroll bar |
| [AxisYLeftWidth](axisyleftwidth.htm) | Measures the distance (in pixels) between the y-axis and the left margin of a chart |
| [AxisYRightWidth](axisyrightwidth.htm) | Measures the distance (in pixels) between the y-axis and the right margin of a chart |
| [BarMarginLeft](barmarginleft.htm) | Measures the margin to the left of each bar on the chart, in pixels |
| [BarsArray](chartcontrol_barsarray.htm) | Provides a collection of [ChartBars](chartbars.htm) objects currently configured on the chart |
| [BarSpacingType](barspacingtype.htm) | Provides the type of bar spacing used for the primary [Bars](bars.htm) object on the chart |
| [BarsPeriod](chartcontrol_barsperiod.htm) | Provides the period (interval) used for the primary [Bars](bars.htm) object on the chart |
| [BarWidth](chartcontrol_barwidth.htm) | Measures the value of the bar width set for the primary Bars object on the chart |
| [BarWidthArray](barwidtharray.htm) | An array containing the values of the [BarWidth](chartcontrol_barwidth.htm) properties of all Bars objects on the chart |
| [CanvasLeft](canvasleft.htm) | Indicates the x-coordinate (in pixels) of the beginning of the chart canvas area |
| [CanvasRight](canvasright.htm) | Indicates the x-coordinate (in pixels) of the end of the chart canvas area |
| [CanvasZoomState](canvaszoomstate.htm) | Indicates the current state of the Zoom tool on the chart |
| [ChartPanels](chartpanels.htm) | Holds a collection of [ChartPanel](chartpanel.htm) objects |
| [CrosshairType](crosshairtype.htm) | Indicates the [Cross Hair](cross_hair.htm) type currently enabled on the chart |
| [FirstTimePainted](firsttimepainted.htm) | Indicates a time value of the first bar painted on the chart |
| [GetBarPaintWidth()](getbarpaintwidth.htm) | Returns the width of the bars in the primary Bars object on the chart, in pixels |
| [GetSlotIndexByTime()](getslotindexbytime.htm) | Returns the slot index of the primary [Bars](bars.htm) object on the chart corresponding to a specified time value |
| [GetSlotIndexByX()](getslotindexbyx.htm) | Returns the slot index of the primary [Bars](bars.htm) object on the chart corresponding to a specified x-coordinate on the visible chart canvas |
| [GetTimeBySlotIndex()](gettimebyslotindex.htm) | Returns a time value corresponding to a specified slot index of the primary [Bars](bars.htm) object on the chart |
| [GetTimeByX()](gettimebyx.htm) | Returns a time value related to the primary [Bars](bars.htm)' slot index at a specified x-coordinate on the chart canvas |
| [GetXByBarIndex()](getxbybarindex.htm) | Returns the chart-canvas x-coordinate of the bar at a specified index of a specified [ChartBars](chartbars.htm) object on the chart |
| [GetXByTime()](getxbytime.htm) | Returns the chart-canvas x-coordinate of the slot index of the primary [Bars](bars.htm) object corresponding to a specified time |
| [Indicators](chartcontrol_indicators.htm) | Returns a collection of indicators currently configured on the chart |
| [IsScrollArrowVisible](isscrollarrowvisible.htm) | Indicates the time-axis scroll arrow is visible in the top-right corner of the chart |
| [IsStayInDrawMode](isstayindrawmode.htm) | Indicates the [Stay in Draw Mode](working_with_drawing_tools__ob.htm) is currently enabled on the chart |
| [IsYAxisDisplayedLeft](isyaxisdisplayedleft.htm) | Indicates the y-axis displays (in any chart panel) to the left side of the chart canvas |
| [IsYAxisDisplayedOverlay](isyaxisdisplayedoverlay.htm) | Indicates an object on the chart is using the Overlay scale justification |
| [IsYAxisDisplayedRight](isyaxisdisplayedright.htm) | Indicates the y-axis displays (in any chart panel) to the right side of the chart canvas |
| [LastSlotPainted](lastslotpainted.htm) | Indicates the slot index of the most recently painted bar on the primary [Bars](bars.htm) object configured on the chart |
| [LastTimePainted](lasttimepainted.htm) | Indicates the time of the most recently painted bar on the primary [Bars](bars.htm) object configured on the chart |
| [MouseDownPoint](mousedownpoint.htm) | Indicates the x- and y-coordinates of the mouse cursor at the most recent OnMouseDown() event |
| [Properties](chartcontrol_properties.htm) | A collection of properties related to the configuration of the Chart |
| [SlotsPainted](slotspainted.htm) | Indicates the number of index slots in which bars are painted within the chart canvas area |
| [Strategies](chartcontrol_strategies.htm) | A collection of strategies configured on the chart |
| [TimePainted](timepainted.htm) | Indicates the range of time in which bars are painted on the visible chart canvas |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



