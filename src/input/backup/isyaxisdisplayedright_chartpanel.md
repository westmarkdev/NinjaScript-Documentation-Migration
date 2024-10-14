










 


IsYAxisDisplayedRight







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isyaxisdisplayedright_chartpanel.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartPanel](chartpanel.htm) &gt;
IsYAxisDisplayedRight | [Previous page](isyaxisdisplayedoverlay_chartpanel.htm)
[Return to chapter overview](chartpanel.htm)










Definition
----------


Indicates the y-axis is visible on the right side of the chart panel.



Property Value
--------------


A bool indicating the y-axis is visible to the right


 


Syntax
------


ChartPanel.IsYAxisDisplayedRight



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
 
   // Print a message if the y-axis is visible on the right
   if (ChartPanel.IsYAxisDisplayedRight)
       Print("The y-axis is visible on the right");
} |



 


 


Based on the image below, IsYAxisDisplayedRight confirms that the y-axis is not displayed on the right. The property would be set to false when applied in either chart panel in this instance.


 


![ChartPanel_IsYAxisDisplayedRight](chartpanel_isyaxisdisplayedright.png)





 
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
 
 
 



