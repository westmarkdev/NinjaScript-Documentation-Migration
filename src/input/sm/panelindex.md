










 


PanelIndex







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?panelindex.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
PanelIndex | [Previous page](chartscale_minvalue.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


The panel on which the chart scale resides.  





|  |
| --- |
| Note:  This value is NOT the same value as the indicator's [PanelUI](panelui.htm). PanelIndex will provide the actual indexed value of the chart panel used for this chart scale. |





Property Value
--------------


An int value representing the panel as an index value which starts at 0 and will increment for each panel configured on the chart.  This property is read-only.



Syntax
------


<chartscale>.PanelIndex



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{         
   // the index value of the panel (not the same as the panelUI)
   int     panel     = chartScale.PanelIndex;
   Print("panel: " + panel);
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
 
 
 



</chartscale>