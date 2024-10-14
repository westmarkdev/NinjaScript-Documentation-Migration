










 


GetSlotIndexByX()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getslotindexbyx.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
GetSlotIndexByX() | [Previous page](getslotindexbytime.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Returns the slot index relative to the chart control corresponding to a specified x-coordinate


 




|  |
| --- |
| Notes: 
•A "Slot" is used in Equidistant [bar spacing](barspacingtype.htm) and represents a position on the chart canvas background which may or may not contain a bar. The concept of "Slots" does NOT exist on a TimeBased bar spacing type.  •If you are looking for information on a bar series, please see [ChartBars.GetBarIdxByX()](chartbars_getbaridxbyx.htm)•Since the slot index is based on the chart canvas, the value returned by GetSlotIndexByX() can be expected to change as new bars are painted, or as the chart is scrolled backward or forward on the x-axis.  |



 


 


Method Return Value
-------------------


A double representing a slot index; returns -1 on a time based bar spacing type



Syntax
<chartcontrol>.GetSlotIndexByX(int x)
--------------------------------------------



Method Parameters
-----------------




|  |  |
| --- | --- |
| x | An int used to determine a slot index |



 



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Find the index of the bar painted at x-coordinate 35
   double slotIndex = chartControl.GetSlotIndexByX(35);
 
   // Print the slot index of the specified time
   Print(slotIndex);
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