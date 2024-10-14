










 


AxisXHeight







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?axisxheight.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
AxisXHeight | [Previous page](chartcontrol.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Measures the distance (in pixels) between the x-axis and the top of the horizontal scroll bar near the bottom of the chart.



Property Value
--------------


A double representing the number of pixels separating the x-axis and the top of the horizontal scroll bar on the chart.



Syntax
------


<chartcontrol>.AxisXHeight



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
     // Print the number of pixels between the x-axis and the top of the horizontal scrollbar
     double height = chartControl.AxisXHeight;
     Print(height);
} |



 


 


Based on the image below, AxisXHeight reveals that the space between the x-axis and the top of the horizontal scrollbar is 31 pixels on this chart.


 


![ChartControl_AxisXHeight](chartcontrol_axisxheight.png)





 
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