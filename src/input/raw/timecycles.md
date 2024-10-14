










 


TimeCycles







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?timecycles.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.TimeCycles()](draw_timecycles.htm) &gt;
TimeCycles | [Previous page](draw_timecycles.htm)
[Return to chapter overview](draw_timecycles.htm)










Definition
----------


Represents an interface that exposes information regarding a TimeCyles [IDrawingTool](idrawingtool.htm).


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| Anchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the point of the drawing object |
| OutlineStroke | A Stroke used for the outline of the region |
| AreaBrush | A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object representing the fill color of the draw object |






Example
-------




| ns |
| --- |
| // Instantiate a Time Cycles object
TimeCycles myTimeCycles = (this, "tag1", 0, 10, Brushes.CornflowerBlue, Brushes.CornflowerBlue, 40);
 
// Change the object's OutlineBrush
myTimeCycles.OutlineStroke = newÂ Stroke(Brushes.Red); |






 
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
 
 
 



