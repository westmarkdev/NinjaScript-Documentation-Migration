










 


RemoveDrawObject()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?removedrawobject.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
RemoveDrawObject() | [Previous page](pricelevels.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Removes a draw object from the chart based on its tag value.


 




|  |
| --- |
| Note:  This method will ONLY remove DrawObjects which were created by a NinjaScript object.  User drawn objects CANNOT be removed from via NinjaScript |





Method Return Value
-------------------


This method does not return a value
-----------------------------------


 


Syntax
------


RemoveDrawObject(string tag)
----------------------------



Parameters
----------




|  |  |
| --- | --- |
| tag | A user defined unique id used to reference the draw object. For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |



 



Examples
--------




| ns |
| --- |
| // Removes a draw object with the tag "tag1"
RemoveDrawObject("tag1"); |






 
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
 
 
 



