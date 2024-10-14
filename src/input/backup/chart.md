










 


Charts







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chart.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
Charts | [Previous page](tochartstring.htm)
[Return to chapter overview](common.htm)










The following section covers information related to accessing chart related data, such as [ChartControl](chartcontrol.htm), [ChartBars](chartbars.htm), [ChartScales](chartscale.htm), and [ChartPanels](chartpanels.htm), and advanced Indicator [Rendering](rendering.htm).


 


In this section
---------------




|  |  |
| --- | --- |
| 1. [ChartBars](chartbars.htm) | The Chart's Primary Data Series which the NinjaScript object is running |
| 2. [ChartControl](chartcontrol.htm) | The entire grid hosting the chart including the X-axis, additional panels, and chart related properties |
| 3. [ChartPanel](chartpanel.htm) | The Panel that the indicator object is running |
| 4. [ChartScale](chartscale.htm) | The Y-axis of the indicator object's panel |



 



A chart's objects can be broken down into the four following areas:


 


GuiChart
--------





 
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
 
 
 



