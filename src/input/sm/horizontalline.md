










 


HorizontalLine







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?horizontalline.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.HorizontalLine()](draw_horizontalline.htm) &gt;
HorizontalLine | [Previous page](draw_horizontalline.htm)
[Return to chapter overview](draw_horizontalline.htm)










Definition
----------


Represents an interface that exposes information regarding a Horizontal Line [IDrawingTool.](idrawingtool.htm)


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the starting point of the drawing object |
| Stroke | A [Stroke](stroke_class.htm) object used to draw the object |





Example
-------




| ns |
| --- |
| // Instantiate a HorizontalLine object
HorizontalLine myLine = Draw.HorizontalLine(this, "tag1", 1000, Brushes.Black);
 
// Set a new Stroke for the object
myLine.Stroke = new Stroke(Brushes.Green, DashStyleHelper.Dash, 5); |






 
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
 
 
 



