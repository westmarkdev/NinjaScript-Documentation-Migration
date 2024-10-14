










 


GetClosestAnchor()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getclosestanchor.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
GetClosestAnchor() | [Previous page](getattachedtochartbars.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Returns the closest chart anchor within a specified maximum distance from the mouse cursor.


 


Method Return Value
-------------------


This method returns an existing [ChartAnchor](chartanchor.htm)



Syntax
------


GetClosestAnchor(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, double maxDist, Point point)



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | A ChartControl representing the x-axis |
| chartPanel | A ChartPanel representing the the panel for the chart |
| chartScale | A ChartScale representing the y-axis |
| maxDist | A double value representing the cursor's sensitivity used to detect the nearest anchor |
| point | A Point in device pixels representing the current mouse cursor position  |



 


 


Examples
--------




| ns |
| --- |
| public override Cursor GetCursor(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{         
   // get the closest anchor to where the user has clicked
   ChartAnchor   closest = GetClosestAnchor(chartControl, chartPanel, chartScale, 10, point);
 
   if (closest != null)
   {
     // set cursor to indicate that it can be moved
     return Cursors.SizeNWSE;
   }   
   // otherwise set cursor back to arrow
   else return Cursors.Arrow;
} |






 
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
 
 
 



