










 


CanvasZoomState







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?canvaszoomstate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
CanvasZoomState | [Previous page](canvasright.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the current state of the Zoom tool on the chart. This property reveals the state of the tool while it is in use, and does not indicate a chart is zoomed in on or not. As soon as a zoom action is completed, the tool is considered to be no longer in use.



Property Value
--------------


An enum representing the state of the Zoom tool on the chart. Possible values are listed below:


 




|  |  |
| --- | --- |
| None | The Zoom tool is not currently being used |
| Selected | The Zoom tool is selected, but has not yet been used to zoom in |
| DrawingRectangle | The Zoom tool is currently in use (User is currently drawing the rectangle in which to zoom) |




Syntax
------


<chartcontrol>.CanvasZoomState



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   CanvasZoomState zoomState = chartControl.CanvasZoomState;
 
   // Trigger an alert while a user is zooming in on a chart
   if (zoomState == CanvasZoomState.DrawingRectangle)
       Alert("zoomAlert", Priority.Medium, "Make sure to zoom in on the entire chart pattern!", " ", 60, Brushes.White, Brushes.Black);
} |



 


 


Based on the image below, CanvasZoomState confirms that the Zoom rectangle is currently being drawn:


 


![ChartControl_CanvasZoomState](chartcontrol_canvaszoomstate.png)





 
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
 
 
 



</chartcontrol>