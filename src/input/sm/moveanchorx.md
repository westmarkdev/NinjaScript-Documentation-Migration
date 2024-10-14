










 


MoveAnchorX()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moveanchorx.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
MoveAnchorX() | [Previous page](moveanchor.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


Moves an anchor's x value from start point by a delta point amount.


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


<chartanchor>.MoveAnchorX(Point startPoint, Point deltaPoint, ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale)
======================================================================================================================================



Method Parameters
-----------------




|  |  |
| --- | --- |
| startPoint | The chart anchor's original starting point value |
| deltaPoint | The chart anchor's new point value to be updated |
| chartControl | A ChartControl representing the x-axis |
| chartScale | A ChartScale representing the y-axis |





Examples
--------




| ns |
| --- |
| //move only the chart anchors x (bar/time) value
MyAnchor.MoveAnchorX(lastPoint, newPoint, chartControl, chartScale); |






 
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