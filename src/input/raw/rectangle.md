










 


Rectangle







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?rectangle.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.Rectangle()](draw_rectangle.htm) &gt;
Rectangle | [Previous page](draw_rectangle.htm)
[Return to chapter overview](draw_rectangle.htm)










Definition
----------


Represents an interface that exposes information regarding a Rectangle [IDrawingTool](idrawingtool.htm).


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the starting point of the drawing object |
| AreaBrush | A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object representing the fill color of the draw object |
| AreaOpacity | An int value representing the opacity of the area color |
| OutlineStroke | The [Stroke](stroke_class.htm) object used to draw the object's outline |





Example
-------




| ns |
| --- |
| // Instantiate a Rectangle object
Rectangle myRec = Draw.Rectangle(this, "tag1", 10, Low[10] - TickSize, 5, High[5] + TickSize, Brushes.Blue);
 
// Set the object's AreaBrush to Blue
myRec.AreaBrush = Brushes.Blue;  |






 
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
 
 
 



