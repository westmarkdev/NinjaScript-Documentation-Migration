










 


LastSlotPainted







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?lastslotpainted.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
LastSlotPainted | [Previous page](isyaxisdisplayedright.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the most recent (last) slot index of the Data Series on the chart, regardless if a bar is actually painted in that slot.


 




|  |
| --- |
| Note: LastSlotPainted differs from [ChartBars.ToIndex](chartbars_toindex.htm), which returns the last index containing a bar painted in the visible area of the chart. |




Property Value
--------------


A int representing the most recent (last) slot index on the chart



Syntax
------


<chartcontrol>.LastSlotPainted



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   int lastSlot = chartControl.LastSlotPainted;
 
   // Print the index of the last slot on the chart
   Print(lastSlot);
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