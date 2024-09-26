










 


PanelIndex







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?minvalue_chartpanel.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartPanel](chartpanel.htm) &gt;
PanelIndex | [Previous page](maxvalue_chartpanel.htm)
[Return to chapter overview](chartpanel.htm)










Definition
----------


Indicates the minimum Y value of objects within the chart panel, based on the current y-axis scale. The scale of the y-axis is dependent upon the values of objects in the panel which have Auto Scale enabled.



Property Value
--------------


A double representing the minimum Y value in the panel's vertical scale


 


Syntax
------


ChartPanel.MinValue



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
 
   // Print the minimum and maximum Y values for objects in the panel
   Print(String.Format("Min value: {0}, Max value: {1}",ChartPanel.MinValue, ChartPanel.MaxValue));
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
 
 
 



