










 


IsYAxisDisplayedLeft







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isyaxisdisplayedleft.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
IsYAxisDisplayedLeft | [Previous page](isstayindrawmode.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the y-axis displays (in any chart panel) to the left side of the chart.



Property Value
--------------


A boolean value. When True, indicates that the y-axis displays to the left of the chart canvas; otherwise False.



Syntax
------


<chartcontrol>.IsYAxisDisplayedLeft



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print the value of IsYAxisDisplayedLeft
   Print("Y-Axis visible to the left of the chart canvas? " + chartControl.IsYAxisDisplayedLeft);
} |



 


 


Based on the image below, IsYAxisDisplayedLeft confirms that the y-axis displays to the left of the chart canvas.


 


![ChartControl_isYAxisDisplayedLeft](chartcontrol_isyaxisdisplayedleft.png)





 
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