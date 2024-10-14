










 


GetXByBarIndex()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getxbybarindex.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
GetXByBarIndex() | [Previous page](gettimebyx.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Returns the chart-canvas x-coordinate of the bar at a specified index of a specified [ChartBars](chartbars.htm) object on the chart. 


 




|  |
| --- |
| Note:  Since the index is based upon bars that move across the chart canvas as new bars are painted, the value returned by GetXByBarIndex() can be expected to change as new bars are painted on the chart, or as the chart is scrolled backward or forward on the x-axis. |



 


 


Method Return Value
-------------------


An int representing a chart-canvas x-coordinate



Syntax
------


<chartcontrol>.GetXByBarIndex(ChartBars chartBars, int barIndex)



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartBars | The [ChartBars](chartbars.htm) object to check |
| barIndex | The slot index used to determine an x-coordinate |



 



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   double xCoordinate = chartControl.GetXByBarIndex(ChartBars, 100);
 
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