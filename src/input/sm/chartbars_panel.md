










 


Panel







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartbars_panel.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartBars](chartbars.htm) &gt;
Panel | [Previous page](chartbars_gettimebybaridx.htm)
[Return to chapter overview](chartbars.htm)










Definition
----------


A zero-based index value that represents the [ChartPanel](chartpanel.htm) where the [ChartBars](chartbars.htm) reside.


 




|  |
| --- |
| Note:  This is NOT the same as the [PanelUI](panelui.htm) property displays on the Chart's [Data Series](working_with_price_data.htm) menu.  A ChartBars.Panel value of 0 represents the first panel on the chart. |





Property Value
--------------


An int indicating the panel of the ChartBars



Syntax
------


Bars.Panel


 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   Print("ChartBars reside on panel index: " + ChartBars.Panel);
   // Output:  ChartBars reside on panel index: 0         
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
 
 
 



