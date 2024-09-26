










 


TimePainted







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?timepainted.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
TimePainted | [Previous page](chartcontrol_strategies.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the range of time in which bars are painted on the visible chart canvas.



Property Value
--------------


A TimeSpan measuring the difference between the earliest and latest times at which bars are painted on the chart



Syntax
------


<chartcontrol>.TimePainted



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print a message if less than three hours' worth of data is painted on the chart canvas
   if(chartControl.TimePainted.Hours &lt; 3)
       Print(String.Format("It is recommended to view at least three hours worth of data on your chart with this indicator. You are currently viewing {0}", chartControl.TimePainted));
} |



 


 




|  |
| --- |
| Note: TimePainted is intended to be used when Non-Equidistant (time-based) bar spacing is enabled on the chart. Otherwise, it will have a value of 0. |






 
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