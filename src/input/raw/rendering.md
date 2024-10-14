










 


Rendering







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?rendering.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt;
Rendering | [Previous page](width.htm)
[Return to chapter overview](chart.htm)










Rendering methods and properties can be useful when carrying out custom drawing tasks for chart objects. Event handlers such as [OnCalculateMinMax()](oncalculateminmax.htm) and [OnRender()](onrender.htm) allow you to override behavior at key points in the rendering process.


 




|  |
| --- |
| Notse: 
1.Some rendering methods and properties make use of [SharpDX](http://sharpdx.org/) libraries, which provide a managed framework for working with DirectX technology.  Please see the [SharpDX SDK Reference](sharpdx_sdk_reference.htm) for more information.2.For a walk through for using the SharpDX, please see the educational resource [Using SharpDX for Custom Chart Rendering](using_sharpdx_for_custom_chart_rendering.htm) |





Methods and Properties
----------------------




|  |  |
| --- | --- |
| [RenderTarget](rendertarget.htm) | Creates objects and exposes methods used for drawing in the chart area.  |
| [ForceRefresh()](forcerefresh.htm) | Forces OnRender() to be called, which will re-paint the chart |
| [IsInHitTest](isinhittest.htm) | Qualifies if object drawn in chart object should be selectable in the hit test procedure |
| [IsSelected](isselected.htm) | Indicates a chart object is currently selected |
| [IsVisibleOnChart()](isvisibleonchart.htm) | Indicates a chart object is visible on the chart canvas |
| [MaxValue](maxvalue.htm) | The maximum value used for the automatic scaling of the y axis |
| [MinValue](minvalue.htm) | The minimum value used for the automatic scaling of the y axis |
| [OnCalculateMinMax()](oncalculateminmax.htm) | An event driven method which is called while the chart scale is being updated |
| [OnRender()](onrender.htm) | Used to render custom drawing to a chart from various chart objects |
| [OnRenderTargetChanged()](onrendertargetchanged.htm) | Used for efficient handling of SharpDX resources |
| [PanelUI](panelui.htm) | The chart panel that is configured on the chart's UI |
| [ZOrder](chart_zorder.htm) | A unique identifier used to control the order in which chart objects are drawn on the chart's Z-axis |






 
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
 
 
 



