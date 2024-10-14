










 


BarMarginLeft







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barmarginleft.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
BarMarginLeft | [Previous page](axisyrightwidth.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


A hard-coded minimum bar margin value, set to 8 pixels, which can be used as a base value when creating custom Chart Styles.



Property Value
--------------


A value representing the minimum margin applied to the left edge of bars. This value is hard-coded to 8 pixels, and it can be used as a base value when setting the bar margin in custom [Chart Styles](chart_style.htm).



Syntax
------


<chartcontrol>.BarMarginLeft



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
     // Print the number of pixels maintained as a margin to the left of bars
     double barMargin = chartControl.BarMarginLeft;
     Print(barMargin);
} |



 


 


Based on the image below, BarMarginLeft reveals that the minimum margin maintained to the left of each bar is 8 pixels on this chart.


 


![ChartControl_BarMarginLeft](chartcontrol_barmarginleft.png)





 
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