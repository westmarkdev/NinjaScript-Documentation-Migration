










 


Arc







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?arc.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.Arc()](draw_arc.htm) &gt;
Arc | [Previous page](draw_arc.htm)
[Return to chapter overview](draw_arc.htm)










Definition
----------


Represents an interface that exposes information regarding an Arc [IDrawingTool](idrawingtool.htm).


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the end point of the drawing object |
| AreaBrush | A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object representing the fill color of the draw object |
| AreaOpacity | An int value representing the opacity of the area color |
| ArcStroke | The [Stroke](stroke_class.htm) object used to draw the arc line of the object's outline |
| Stroke | The [Stroke](https://ninjatrader.com/support/helpGuides/nt8/stroke_class.htm) object used to draw the straight line of the object's outline |





Example
-------




| ns |
| --- |
| // Draw an Arc object
Arc myArc = Draw.Arc(this, "myArc", Time[10], Close[10], Time[0], Close[0], Brushes.Blue);
 
// Set the opacity of the shading between the arc and the chord
myArc.AreaOpacity = 100; |






 
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
 
 
 



