










 


IsYAxisDisplayedRight







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isyaxisdisplayedright.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
IsYAxisDisplayedRight | [Previous page](isyaxisdisplayedoverlay.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the y-axis displays (in any chart panel) to the right side of the chart.



Property Value
--------------


A boolean value. When True, indicates that the y-axis displays to the right of the chart canvas; otherwise False.



Syntax
------


<chartcontrol>.IsYAxisDisplayedRight



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print the value of IsYAxisDisplayedRight
   Print("Y-Axis visible to the right of the chart canvas? " + chartControl.IsYAxisDisplayedRight);
} |



 


 


Based on the image below, IsYAxisDisplayedRight confirms that the y-axis is not displayed to the right of the chart canvas.


 


![ChartControl_IsYAxisDisplayedRight](chartcontrol_isyaxisdisplayedright.png)





 
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