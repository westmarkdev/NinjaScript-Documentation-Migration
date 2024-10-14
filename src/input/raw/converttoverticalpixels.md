










 


ConvertToVerticalPixels()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?converttoverticalpixels.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
ConvertToVerticalPixels() | [Previous page](updateyfrompoint.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Used to convert the cursor position (pixels) to device pixels represented on the Y axis of the chart.  This method would only be needed if the value you are given is provided in WPF pixel point (such as the data point used in OnMouseDown), but you would need the value in the chart's rendered pixels.  This is useful when handling drawing tools and charts which would have multiple chart panels.


 


Method Return Value
-------------------


An int value representing the converted value in device pixels



Syntax
------


ConvertToVerticalPixels(ChartControl chartControl, ChartPanel chartPanel, double wpfY)


 



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | A ChartControl representing the x-axis |
| chartPanel | A ChartPanel representing the the panel for the chart |
| wpfY | A double value which needs to be converted |



 



Examples
--------




| ns |
| --- |
| public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   //get chart anchors data point when mouse is clicked
   Point myPoint = dataPoint.GetPoint(chartControl, chartPanel, chartScale);
   
   Print("before convert: " + myPoint.Y); //before convert: 630.5
 
   //convert the data point to device pixels
   double yPixel = ConvertToVerticalPixels(chartControl, chartPanel, myPoint.Y);   
 
   Print("after convert: " + yPixel); //after convert: 1108
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
 
 
 



