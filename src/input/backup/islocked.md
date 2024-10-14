










 


IsLocked







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?islocked.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
IsLocked | [Previous page](isglobaldrawingtool.htm)
[Return to chapter overview](drawing_tools.htm)










Definition  

Determines if the drawing tool should be be locked in place.  This property can be set either manually through the UI or explicitly through code.


 


Property Value
--------------


A bool value which when true if the drawing tool is locked; otherwise false.  Default is set to false.


 




|  |
| --- |
| Note: For Drawing tools which are drawn by an indicator or strategy, this property will default to true. |



 


 


Syntax
------


IsLocked



Examples
--------




| ns |
| --- |
| public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
   if (IsLocked) //if the object is locked, do not attempt to move
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
 
 
 



