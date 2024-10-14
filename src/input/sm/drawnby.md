










 


DrawnBy







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?drawnby.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
DrawnBy | [Previous page](drawingstate.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Represents the NinjaScript object which created the drawing object


 


Property Value
--------------


The NinjaScript object which created the drawing tool; this value will be null if drawn by a user.


 


Syntax
------


DrawnBy


 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{      
   // if the drawing tool was not created by a user, 
   // print the name of the object that it was created      
   if(!IsUserDrawn)
   Print(DrawnBy.Name);
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
 
 
 



