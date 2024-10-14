










 


IsYAxisDisplayedLeft







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isyacisdisplayedleft_chartpanel.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartPanel](chartpanel.htm) &gt;
IsYAxisDisplayedLeft | [Previous page](h_height_chartpanel.htm)
[Return to chapter overview](chartpanel.htm)










Definition
----------


Indicates the y-axis is visible on the left side of the chart panel.



Property Value
--------------


A bool indicating the y-axis is visible to the left


 


Syntax
------


ChartPanel.IsYAxisDisplayedLeft



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
 
   // Print a message if the y-axis is visible on the left
   if (ChartPanel.IsYAxisDisplayedLeft)
       Print("The y-axis is visible on the left");
} |



 


 


Based on the image below, IsYAxisDisplayedLeft confirms that the y-axis displays to the left. In this image, the property would be set to true when applied to either chart panel.


 


![ChartPanel_IsYAxisDisplayedLeft](chartpanel_isyaxisdisplayedleft.png)





 
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
 
 
 



