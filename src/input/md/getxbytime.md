










 


GetXByTime()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getxbytime.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
GetXByTime() | [Previous page](getxbybarindex.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Returns the chart-canvas x-coordinate of the slot index of the primary [Bars](bars.htm) object corresponding to a specified time. 


 




|  |
| --- |
| Note: Since the time correlates with a specific bar index, and since bars move on the chart canvas as new bars are painted, the value returned by GetXByTime() can be expected to change as new bars are painted on the chart, or as the chart is scrolled backward or forward on the x-axis. |



 


 


Method Return Value
-------------------


An int representing a chart-canvas x-coordinate



Syntax
------


<chartcontrol>.GetXByTime(DateTime time)



Method Parameters
-----------------




|  |  |
| --- | --- |
| time | A [DateTime](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx) object used to determine an x-coordinate |



 



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   DateTime timeToCheck = new DateTime(2017, 8, 6, 11, 0, 0);
 
   // Find the chart-canvas x-coordinate of the bar at the specified time
    int xCoordinate = chartControl.GetXByTime(timeToCheck);
 
   // Print the x-coordinate value
   Print(xCoordinate);
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