










 


IsAttachedToNinjaScript







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isattachedtoninjascript.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
IsAttachedToNinjaScript | [Previous page](ignoresuserinput.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Indicates if the drawing tool is currently [attached to](attachedto.htm) a NinjaScript object (such an indicator or a strategy).


 


Property Value
--------------


A bool value which when true if the drawing tool is attached to a NinjaScript object; otherwise false.  This property is read-only.


 


Syntax
------


IsAttachedToNinjaScript


 


Examples
--------




| ns |
| --- |
| public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{   
   // do not interact if drawn by an indicator or strategy
   if (IsAttachedToNinjaScript)
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
 
 
 



