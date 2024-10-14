










 


CanvasRight







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?canvasright.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
CanvasRight | [Previous page](canvasleft.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the x-coordinate (in pixels) of the end of the chart canvas area.



Property Value
--------------


A double representing the end of the chart canvas area.



Syntax
------


<chartcontrol>.CanvasRight



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Store the beginning and ending x-coordinates of the canvas area
   double canvasBeginCoordinate = chartControl.CanvasLeft;
   double canvasEndCoordinate = chartControl.CanvasRight;
 
   // Print the stored values
   Print(String.Format("Chart canvas begins at x-coordinate {0} and ends at x-coordinate {1}", canvasBeginCoordinate, canvasEndCoordinate)); 
} |



 


 


Based on the image below, CanvasRight reveals that the chart canvas ends at x-coordinate 526.


 


![ChartControl_CanvasRight](chartcontrol_canvasright.png)Yes,





 
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