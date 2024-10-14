










 


GetSlotIndexByTime()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getslotindexbytime.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
GetSlotIndexByTime() | [Previous page](chartcontrol_getbarpaintwidth.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Returns the slot index relative to the chart control corresponding to a specified time value. 


 




|  |
| --- |
| Notes: 
•A "Slot" is used in Equidistant [bar spacing](barspacingtype.htm) and represents a position on the chart canvas background which may or may not contain a bar. The concept of "Slots" does NOT exist on a TimeBased bar spacing type.  •If you are looking for information on a bar series, please see [ChartBars.GetBarIdxByTime()](chartbars_getbaridxbytime.htm) |



 


 


Method Return Value
-------------------


A double representing a slot index



Syntax
<chartcontrol>.GetSlotIndexByTime(DateTime time)
-------------------------------------------------------





|  |
| --- |
| Warning:  This method CANNOT be called on BarSpacingType.TimeBased charts.  You will need to ensure an Equidistant [bar spacing type](barspacingtype.htm) is used, otherwise errors will be thrown.   |



 


 


Method Parameters
-----------------




|  |  |
| --- | --- |
| time | A [DateTime](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx) Structure used to determine a slot index |



 



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // ensure that GetSlotIndexByTime is called on TimeBased charts
   if(chartControl.BarSpacingType != BarSpacingType.TimeBased)
   {
     // get the slot index of the first time painted on the chart
     double slotIndex = chartControl.GetSlotIndexByTime(chartControl.FirstTimePainted);
      
     Print(slotIndex);
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
 
 
 



</chartcontrol>