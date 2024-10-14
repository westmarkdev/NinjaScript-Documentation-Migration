










 


IsUserDrawn







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isuserdrawn.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
IsUserDrawn | [Previous page](islocked.htm)
[Return to chapter overview](drawing_tools.htm)










Definition  

Indicates if the drawing tool was manually drawn by a user as opposed to programmatically drawn by a NinjaScript object (such as an indicator or strategy).


 


Property Value
--------------


A bool value which when true if the draw object was manually drawn ; otherwise false. This property is read-only


 


Syntax
------


IsUserDrawn



Examples
--------




| ns |
| --- |
| if (IsUserDrawn)
{ 
 // do something only if the object was drawn manually
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
 
 
 



