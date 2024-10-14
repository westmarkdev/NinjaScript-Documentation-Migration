










 


GetTimeByBarIdx()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartbars_gettimebybaridx.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartBars](chartbars.htm) &gt;
GetTimeByBarIdx() | [Previous page](chartbars_getbaridxbyx.htm)
[Return to chapter overview](chartbars.htm)










Definition
----------


Returns the [ChartBars](chartbars.htm) time value calculated from a bar index parameter provided.


 


Method Return Value
-------------------


A [DateTime](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx) struct representing a bar time value at a specific bar index value



Syntax
ChartBars.GetTimeByBarIdx(ChartControl chartControl, int barIndex)
-------------------------------------------------------------------------



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | The [ChartControl](chartcontrol.htm) object used to determine the chart's time axis |
| barIndex | An int value representing a bar index used to convert to a ChartBar index value |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   if (ChartBars != null)
   {
     Print(ChartBars.GetTimeByBarIdx(ChartControl, 50)); //8/11/2015 4:30:00 AM    
   }
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
 
 
 



