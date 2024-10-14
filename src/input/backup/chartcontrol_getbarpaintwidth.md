










 


GetBarPaintWidth()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartcontrol_getbarpaintwidth.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
GetBarPaintWidth() | [Previous page](firsttimepainted.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Returns the width of the bars in the primary Bars object on the chart, in pixels.


 


Method Return Value
-------------------


A double representing the pixel width of bars on the chart


 


Syntax
<chartcontrol>.GetBarPaintWidth(ChartBars chartBars)
-----------------------------------------------------------


 



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartBars | A [ChartBars](chartbars.htm) object to measure |



 



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Use BarsArray[0] to pass in a ChartBars object representing the primary Bars object on the chart
   double barPixelWidth = chartControl.GetBarPaintWidth(chartControl.BarsArray[0]);
 
   // Print the pixel width of bars painted on the chart
   Print(String.Format("Bars on the chart are {0} pixels wide", barPixelWidth));   
} |



 


 


In the image below, GetBarPaintWidth() reveals that the bars are being drawn 27 pixels wide on the chart:


 


![ChartControl_GetBarPaintWidth](chartcontrol_getbarpaintwidth.png)





 
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