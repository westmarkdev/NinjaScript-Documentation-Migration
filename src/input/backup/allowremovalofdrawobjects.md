










 


AllowRemovalOfDrawObjects







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?allowremovalofdrawobjects.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
AllowRemovalOfDrawObjects | [Previous page](brushes.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Determines if programmatically drawn [DrawObjects](drawingtools_drawobjects.htm) are allowed to remove manually from the chart


 


Property Value
--------------


When set to true, the draw objects from the indicator or strategy can be deleted from the chart manually by a user. If false, draw objects from the indicator or strategy can only be removed from the chart if the script removes the drawing object, or the script is terminates.  Default set to false.


 


Syntax
------


AllowRemovalOfDrawObjects


 


Examples
--------




|  |  |
| --- | --- |
| ns |  |
| protected override void OnStateChange()
{
     Add(new Plot(Brushes.Orange, "SMA"));
     AllowRemovalOfDrawObjects = true; // Draw objects can be removed separately from the script
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
 
 
 



