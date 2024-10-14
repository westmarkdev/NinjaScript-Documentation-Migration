










 


IsVisible







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartscale_isvisible.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
IsVisible | [Previous page](height.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


Indicates if the chart scale is viewable on the UI.  If the bar series, indicator, or strategy which uses the chart scale is not in view, the chart scale IsVisible property will return false.



Property Value
--------------


A bool value, which when true the series used to build the scale is viewable; otherwise false.  This property is read-only.



Syntax
------


<chartscale>.IsVisible



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{         
   // do not process render info chart scale is not visible
   if(!chartScale.IsVisible)
     return;
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