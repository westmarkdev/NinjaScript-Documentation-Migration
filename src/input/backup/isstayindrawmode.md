










 


IsStayInDrawMode







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isstayindrawmode.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
IsStayInDrawMode | [Previous page](isscrollarrowvisible.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates [Stay in Draw Mode](working_with_drawing_tools__ob.htm) is currently enabled on the chart.



Property Value
--------------


A bool value. When True, indicates that Stay in Draw Mode is enabled on the chart; otherwise False.



Syntax
------


<chartcontrol>.IsStayInDrawMode 



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print a message if Stay in Draw Mode is enabled
   if(chartControl.IsStayInDrawMode);
       Print("Stay in Draw Mode is currently enabled");
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
 
 
 



</chartcontrol>