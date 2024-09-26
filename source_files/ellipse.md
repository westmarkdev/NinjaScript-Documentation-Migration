










 


Ellipse







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ellipse.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.Ellipse()](draw_ellipse.htm) &gt;
Ellipse | [Previous page](draw_ellipse.htm)
[Return to chapter overview](draw_ellipse.htm)










Definition
----------


Represents an interface that exposes information regarding an Ellipse [IDrawingTool](idrawingtool.htm).


 


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
| // Paint a red ellipse on the current bar
Ellipse myEllipse = Draw.Ellipse(this, "tag1", true, 5, Close[5], 0, Close[0], Brushes.Red, Brushes.Red, 5);
 
// Change the AreaOpacity of the Ellipse
myEllipse.AreaOpacity = 0; |






 
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
 
 
 



