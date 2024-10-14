










 


GetBarIdxByTime()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartbars_getbaridxbytime.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartBars](chartbars.htm) &gt;
GetBarIdxByTime() | [Previous page](chartbars_fromindex.htm)
[Return to chapter overview](chartbars.htm)










Definition
----------


Returns the [ChartBars](chartbars.htm) index value calculated from the time parameter provided.


 


Method Return Value
-------------------


An int representing the bar index value at a specific time



Syntax
ChartBars.GetBarIdxByTime(ChartControl chartControl, DateTime time)
--------------------------------------------------------------------------



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | The [ChartControl](chartcontrol.htm) object used to determine the chart's time axis |
| time | The [DateTime](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx) value used to convert to a ChartBar index value |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{   
   if (ChartBars != null)   
   {         
     Print(ChartBars.GetBarIdxByTime(ChartControl, Time[0]));  
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
 
 
 



