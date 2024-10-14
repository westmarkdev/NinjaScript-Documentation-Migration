










 


Ruler







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ruler.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.Ruler()](draw_ruler.htm) &gt;
Ruler | [Previous page](draw_ruler.htm)
[Return to chapter overview](draw_ruler.htm)










Definition
----------


Represents an interface that exposes information regarding a Ruler [IDrawingTool](idrawingtool.htm).


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the end point of the drawing object |
| TextAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the text point of the drawing object |
| TextColor | A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) class representing the fill color of the draw object's text area |
| LineColor | A [Stroke](stroke_class.htm) object used to draw the object |






Example
-------




| ns |
| --- |
| // Instantiate a Ruler object
Ruler myRuler = Draw.Ruler(this, "tag1", true, 4, Low[4], 3, High[3], 1, Low[1]);
 
// Change the object's text color to white
myRuler.TextColor = Brushes.White; |






 
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
 
 
 



