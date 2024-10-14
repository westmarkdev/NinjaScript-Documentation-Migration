










 


BarWidth







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartcontrol_barwidth.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
BarWidth | [Previous page](chartcontrol_barsperiod.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Measures the value of the [bar width](barwidth.htm) set for the primary Bars object on the chart. 


 




|  |
| --- |
| Note: This property value is not stated in pixels. To obtain the pixel-width of bars on the chart, use [GetBarPaintWidth(](chartcontrol_getbarpaintwidth.htm)) instead. |



 


 


Property Value
--------------


A double representing the value of the bar width.



Syntax
------


<chartcontrol>.BarWidth



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   double barWidth = chartControl.BarWidth;
 
   // Prints the width of bars on the chart
   Print(barWidth);
} |



 


 


Based on the image below, BarWidth reveals that the bars on the chart are 4.02 pixels wide.


 


![ChartControl_BarWidth](chartcontrol_barwidth.png)





 
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