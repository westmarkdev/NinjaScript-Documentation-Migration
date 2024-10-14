










 


H (Height)







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?h_height_chartpanel.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartPanel](chartpanel.htm) &gt;
H (Height) | [Previous page](chartobjects.htm)
[Return to chapter overview](chartpanel.htm)










Definition
----------


Indicates the height (in pixels) of the rendered area of the chart panel. 


 




|  |
| --- |
| Note:  The paintable area does not extend all the way to the top edge of the panel itself, as seen in the image below. |



 


 


Property Value
--------------


A int representing the height of the panel in pixels


 


Syntax
------


ChartPanel.H



Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   base.OnRender(chartControl, chartScale);
    
   // Print the height of the panel
   Print(ChartPanel.H);
} |



 


 


Based on the image below, H reveals that the paintable area of the chart panel is 69 pixels high.


 


![ChartPanel_H](chartpanel_h.png)





 
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
 
 
 



