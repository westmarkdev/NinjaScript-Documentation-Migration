










 


RegionHighlightY







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?regionhighlighty.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.RegionHighlightY()](draw_regionhighlighty.htm) &gt;
RegionHighlightY | [Previous page](draw_regionhighlighty.htm)
[Return to chapter overview](draw_regionhighlighty.htm)










Definition
----------


Represents an interface that exposes information regarding a Region Highlight Y [IDrawingTool.](idrawingtool.htm)


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the starting point of the drawing object |
| AreaBrush | A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) class representing the fill color of the draw object |
| AreaOpacity | An int value representing the opacity of the area color |
| OutlineStroke | The [Stroke](stroke_class.htm) object used to draw the object's outline |





Example
-------




| ns |
| --- |
| // Instantiate a RegionHighlightX object
RegionHighlightY myReg = Draw.RegionHighlightY(this, "tag1", 10, 0, Brushes.Blue);
 
// Change the object's opacity
myReg.AreaOpacity = 25; |






 
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
 
 
 



