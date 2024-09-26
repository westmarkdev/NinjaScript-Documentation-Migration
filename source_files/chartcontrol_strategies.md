










 


Strategies







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartcontrol_strategies.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
Strategies | [Previous page](slotspainted.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


A collection of strategies configured on the chart.



Property Value
--------------


A ChartObjectCollection of StrategyRenderBase objects containing information on all configured strategies on the chart.



Syntax
------


<chartcontrol>.Strategies



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print the number of strategies configured on the chart
   if (chartControl.Strategies.Count &gt; 0) 
           Print(chartControl.Strategies[0].Name);
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