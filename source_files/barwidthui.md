










 


BarWidthUI







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barwidthui.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Chart Style](chart_style.htm) &gt;
BarWidthUI | [Previous page](barwidth.htm)
[Return to chapter overview](chart_style.htm)










Definition
----------


The Bar width value which displays on the UI.  This value will be rounded from the internal [BarWidth](barwidth.htm) property which is updated as the ChartControl is resized


 


Property Value
--------------


A int value representing the width of the chart bars which can be set by a user.


 


Syntax
------


BarWidthUI


 


 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale, ChartBars chartBars)
{
   
   int barWidth = GetBarPaintWidth(BarWidthUI);
 
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
 
 
 



