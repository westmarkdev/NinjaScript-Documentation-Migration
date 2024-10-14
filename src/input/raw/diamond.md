










 


Diamond







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?diamond.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.Diamond()](draw_diamond.htm) &gt;
Diamond | [Previous page](draw_diamond.htm)
[Return to chapter overview](draw_diamond.htm)










Definition
----------


Represents an interface that exposes information regarding a Diamond [IDrawingTool](idrawingtool.htm).


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| Anchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the point of the drawing object |
| AreaBrush | A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object representing the fill color of the draw object |
| OutlineBrush | A [Brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) object representing the color of the draw object's outline |





Example
-------




| ns |
| --- |
| // Instantiates a red diamond on the current bar 1 tick below the low
Diamond myDiamond = Draw.Diamond(this, "tag1", true, 0, Low[0] - TickSize, Brushes.Red);
 
// Set the area fill color to Red
myDiamond.AreaBrush = Brushes.Red; |






 
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
 
 
 



