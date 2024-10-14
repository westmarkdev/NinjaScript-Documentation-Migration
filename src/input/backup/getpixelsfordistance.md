










 


GetPixelsForDistance()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getpixelsfordistance.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
GetPixelsForDistance() | [Previous page](chartscale.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


Returns the number of device pixels between the value passed to the method representing a series point value on the chart scale. 


 


Method Return Value
-------------------


A float representing the number of pixels between a value.



Syntax
<chartscale>.GetPixelsForDistance(double distance)
---------------------------------------------------------



Method Parameters
-----------------




|  |  |
| --- | --- |
| distance | A double value representing the distance in points to be measured  |




Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{      
   // the number of pixels between the point value passed as a distance to the method
   float   pixelForDistance = chartScale.GetPixelsForDistance(0.25);
 
   Print("pixelForDistance: " + pixelForDistance); //20 pixels per every 1 tick on the chart scale
} |



 


 


In the image below, we pass a value of 1 for the distance, which tells us there are 76 pixels for every 1 point on the ES 06-15 chart scale.


 


![GetPixelsForDistance](getpixelsfordistance.png)





 
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
 
 
 



</chartscale>