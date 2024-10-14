










 


IsGlobalDrawingTool







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isglobaldrawingtool.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
IsGlobalDrawingTool | [Previous page](isattachedtoninjascript.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Indicates if the drawing tool is currently set as a Global Drawing object. Global draw objects display on any chart which matches the parent chart's underlying instrument.


 


Property Value
--------------


A bool value which returns true if the drawing tool is currently attached as a global drawing object; otherwise false. 


 


Syntax
------


IsGlobalDrawingTool


 


Examples
--------




| ns |
| --- |
| public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{   
   // do not interact if attached to global chart
   if (IsGlobalDrawingTool)
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
 
 
 



