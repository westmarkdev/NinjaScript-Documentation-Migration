










 


Height







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?height.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
Height | [Previous page](getybyvaluewpf.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


Indicates the overall distance (from top to bottom) of the chart scale.


 




|  |
| --- |
| Note: Height does not return its value in terms of device pixels. However, using Height.ConvertToVerticalPixels or Height.ConvertToHorizontalPixels will convert the Height value to device pixels. Alternatively, RenderTarget.PixelSize.Height or ChartPanel.H will also provide the height in terms of device pixels. |





Property Value
--------------


A double value representing the height of the chart scale.


 


Syntax
------


<chartscale>.Height


 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // the height of the entire chart scale
   double   height       = chartScale.Height;
   Print("the height of the chart scale is: " + height);  
} |





In the image below, the entire of height of the chart scale is represented by the blue line which is calculated at 300 pixels.
------------------------------------------------------------------------------------------------------------------------------


 


![Height](height.png)





 
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