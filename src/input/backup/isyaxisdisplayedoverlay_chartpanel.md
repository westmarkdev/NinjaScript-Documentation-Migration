










 


IsYAxisDisplayedOverlay







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isyaxisdisplayedoverlay_chartpanel.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartPanel](chartpanel.htm) &gt;
IsYAxisDisplayedOverlay | [Previous page](isyacisdisplayedleft_chartpanel.htm)
[Return to chapter overview](chartpanel.htm)










Definition
----------


Indicates any objects configured in the panel are using the Overlay scale justification.



Property Value
--------------


A bool indicating any objects use the Overlay scale justification


 


Syntax
------


ChartPanel.IsYAxisDisplayedOverlay



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
 
   // Trigger an alert when the Overlay scale justification is used
   if (ChartPanel.IsYAxisDisplayedOverlay)
       Alert("overlayAlert", Priority.Low, "It is not recommended to use 'Overlay' with this indicator", "", 300, Brushes.Yellow, Brushes.Black);
} |



 


 


Based on the image below, IsYAxisDisplayedOverlay is set to True, since the SMA indicator is using the Overlay scale justification.


 


![ChartPanel_IsYAxisDisplayedOverlay](chartpanel_isyaxisdisplayedoverlay.png)





 
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
 
 
 



