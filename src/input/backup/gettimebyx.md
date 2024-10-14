










 


GetTimeByX()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?gettimebyx.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
GetTimeByX() | [Previous page](gettimebyslotindex.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Returns a time value related to the primary [Bars](bars.htm)' slot index at a specified x-coordinate relative to the ChartControl.


 




|  |
| --- |
| Note:  Since the time is based upon a coordinate of the chart canvas, the value returned by GetTimeByX() can be expected to change as new bars are painted on the chart, or as the chart is scrolled backward or forward on the x-axis. |



 


 


Method Return Value
-------------------


A [DateTime](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx) object corresponding to a slot index at a specified x-coordinate



Syntax
<chartcontrol>.GetTimeByX(int x)
---------------------------------------


 



Method Parameters
-----------------




|  |  |
| --- | --- |
| x | The x-coordinate used to find a time value |



 



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Find the timestamp of the bar at x-coordinate 100
   DateTime slotTime = chartControl.GetTimeByX(100);
 
   // Print the date of slotTime
   Print(slotTime);
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
 
 
 



</chartcontrol>