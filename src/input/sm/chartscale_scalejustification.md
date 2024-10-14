










 


ScaleJustification







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartscale_scalejustification.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
ScaleJustification | [Previous page](chartscale_properties.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


Indicates the location of the chart scale relative to the chart control.



Property Value
--------------


A ScaleJustification enum.  Possible values are:


•Right

•Left

•Overlay


Syntax
------


ScaleJustification



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{         
   if (chartScale.ScaleJustification == ScaleJustification.Right)
   {
     // do something            
   }
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
 
 
 



