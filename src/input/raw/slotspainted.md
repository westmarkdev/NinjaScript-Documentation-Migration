










 


SlotsPainted







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?slotspainted.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
SlotsPainted | [Previous page](chartcontrol_properties.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the number of index slots in which bars are painted within the chart canvas area. This covers the visible portion of the chart only, and does not include historical painted bars outside of the visible area. 



Property Value
--------------


An int representing the number of index slots in which bars are painted



Syntax
------


<chartcontrol>.SlotsPainted



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   int painted = chartControl.SlotsPainted;
 
   // Print the number of bars painted on the visible chart canvas
   Print(painted);
} |



 


 


In the image below, SlotsPainted reveals that there are 17 bars painted on the chart canvas.


 


![ChartControl_SlotsPainted](chartcontrol_slotspainted.png)





 
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