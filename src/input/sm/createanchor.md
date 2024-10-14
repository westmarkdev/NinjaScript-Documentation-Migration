










 


CreateAnchor()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?createanchor.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
CreateAnchor() | [Previous page](converttoverticalpixels.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Used to create a new chart anchor at a specified mouse point.


 


Method Return Value
-------------------


A new [ChartAnchor](chartanchor.htm) at a specified point in device pixels.



Syntax
------


CreateAnchor(Point point, ChartControl chartControl, ChartScale chartScale)   



Method Parameters
-----------------




|  |  |
| --- | --- |
| point | A Point in device pixels representing the current mouse cursor position  |
| chartControl | A ChartControl representing the x-axis |
| chartScale | A ChartScale representing the y-axis |



 



Examples
--------




| ns |
| --- |
| public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   // get the point where the mouse was clicked
   Point myPoint = dataPoint.GetPoint(chartControl, chartPanel, chartScale);
   
   // create an anchor at that point
   ChartAnchor MyAnchor = CreateAnchor(myPoint, chartControl, chartScale);
   
   Print(MyAnchor.Time); // 3/16/2015 8:18:48 AM
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
 
 
 



