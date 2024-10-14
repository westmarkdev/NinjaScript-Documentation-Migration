










 


LastTimePainted







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?lasttimepainted.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
LastTimePainted | [Previous page](lastslotpainted.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the time of the most recently painted bar on the primary [Bars](bars.htm) object configured on the chart.



Property Value
--------------


A [DateTime](https://msdn.microsoft.com/en-us/library/system.datetime(v=vs.110).aspx) object corresponding to the slot index of the most recently painted bar



Syntax
------


<chartcontrol>.LastTimePainted



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   DateTime lastSlotTime = chartControl.LastTimePainted;
 
   // Print the index of the last slot painted on the chart
   Print(lastSlotTime);
} |



 


 


In the image below, LastTimePainted reveals that the last index painted on the chart corresponds to 8/12/17 at 2:10:00 PM.


 


![ChartControl_LastTimePainted](chartcontrol_lasttimepainted.png)





 
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