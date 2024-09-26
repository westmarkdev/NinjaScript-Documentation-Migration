










 


BarsPeriod







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartcontrol_barsperiod.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
BarsPeriod | [Previous page](barspacingtype.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Provides the period (interval) used for the primary [Bars](bars.htm) object on the chart.



Property Value
--------------


A NinjaTrader.Data.BarsPeriod object containing information on the period used by the Bars object on the chart.



Syntax
------


<chartcontrol>.BarsPeriod



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   BarsPeriod period = chartControl.BarsPeriod;
 
   // Print the period (interval) of the Bars object on the chart
   Print(period);
} |



 


 


Based on the image below, BarsPeriod confirms that the primary Bars object on the chart is configured to a 5-minute interval.


 


![ChartControl_BarsPeriod](chartcontrol_barsperiod.png)





 
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