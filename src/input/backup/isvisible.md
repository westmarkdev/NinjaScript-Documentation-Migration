










 


IsVisible







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isvisible.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
IsVisible | [Previous page](indicator_displayname.htm)
[Return to chapter overview](common.htm)










Definition
----------


Determines if the current NinjaScript object should be visible on the chart. When an object's IsVisible property is set to false, the object will NOT be displayed on the chart and will not be calculated to save resources.


 




|  |
| --- |
| Note: Strategies intentionally contain no IsVisible property. |






|  |
| --- |
| Warning: This property should NOT be set on indicators which add a panel or own their own panel. Panel addition/removal is determined when an indicator is added/removed to a chart and is not modified through the IsVisible property. |




Property Value
--------------


A bool value when true will be displayed on the chart; otherwise false; default value is true.


 


Syntax
------


IsVisible


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // Loops through the DrawObjects collection via a threadsafe list copy
   foreach (DrawingTool draw in DrawObjects.ToList())
   {
     // Detect all manual drawn line objects and change their visibility
     if (draw is DrawingTools.Line &amp;&amp; draw.IsUserDrawn)
     {
         draw.IsVisible = false;
     }
   }             
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
 
 
 



