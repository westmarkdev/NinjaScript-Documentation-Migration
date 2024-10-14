










 


MoveAnchor()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?moveanchor.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
MoveAnchor() | [Previous page](isypropertyvisibile.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


Moves a Chart Anchor's x and y values from start point by a delta point amount.


 


Method Return Value
-------------------


This method does not return a value.



Syntax
------


<chartanchor>.MoveAnchor(ChartAnchor startDataPoint, ChartAnchor deltaDataPoint, ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, DrawingTool drawingTool)



Method Parameters
-----------------




|  |  |
| --- | --- |
| startPoint | The chart anchor's original starting location value represented by a point structure |
| startDataPoint | A chart anchor's original starting location value represented by a chart anchor |
| deltaPoint | The chart anchor's new location value to be updated represented by a point structure |
| deltaDataPoint | The chart anchor's new location value to be udpated represened by a chart anchor |
| chartControl | A ChartControl representing the x-axis |
| chartScale | A ChartScale representing the y-axis |
| chartPanel | A ChartPanel representing the the panel for the chart |
| drawingTool | The drawing tool which owns the chart anchor to be moved (usually this). |



 



Examples
--------




| ns |
| --- |
| //move the chart anchors x and y values
MyAnchor.MoveAnchor(lastPoint, newPoint, chartControl, chartPanel, chartScale, this); |






 
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