










 


GetPoint()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getpoint.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
GetPoint() | [Previous page](drawnonbar.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


Returns a chart anchor's data point in device pixels


 


Method Return Value
-------------------


A [Point](https://msdn.microsoft.com/en-us/library/system.drawing.point%28v=vs.110%29.aspx) structure; a point value in device pixels for a chart's given panel &amp; scale 



Syntax
------


<chartanchor>.GetPoint(ChartControl chartControl, ChartPanel chartPanel, ChartScale, [bool pixelAlign])



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | A [ChartControl](chartcontrol.htm) representing the x-axis |
| chartPanel | A [ChartPanel](chartpanel.htm) representing the a panel of the chart |
| chartScale | A [ChartScale](chartscale.htm) representing the y-axis |
| pixelAlign | An optional bool determining if the data point should be rounded to closest .5 pixel point |



 



Examples
--------




| ns |
| --- |
| //gets the chart anchors data points
Point anchorPoint = MyAnchor.GetPoint(chartControl, chartPanel, chartScale); |






 
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
 
 
 



</chartanchor>