










 


RemoveDrawObjects()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?removedrawobjects.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
RemoveDrawObjects() | [Previous page](removedrawobject.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Removes all draw objects originating from the indicator or strategy from the chart.





|  |
| --- |
| Note:  This method will ONLY remove DrawObjects which were created by a NinjaScript object.  User drawn objects CANNOT be removed from via NinjaScript |





Method Return Value
-------------------


This method does not return a value
-----------------------------------


 


 


Syntax
------


RemoveDrawObjects()
-------------------


 


 


Examples
--------




| ns |
| --- |
| // Removes all draw objects
RemoveDrawObjects(); |






 
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
 
 
 



