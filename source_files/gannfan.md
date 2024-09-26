










 


GannFan







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?gannfan.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.GannFan()](draw_gannfan.htm) &gt;
GannFan | [Previous page](draw_gannfan.htm)
[Return to chapter overview](draw_gannfan.htm)










Definition
----------


Represents an interface that exposes information regarding a Gann Fan [IDrawingTool.](idrawingtool.htm)


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| Anchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the starting point of the drawing object |
| [PriceLevels](pricelevels.htm) | A collection of prices calculated by the drawing object |
| GannFanDirection | Possible values:
 
GannFanDirection.DownLeft
GannFanDirection.DownRight
GannFanDirection.UpLeft
GannFanDirection.UpRight |
| PointsPerBar | A double value representing the number of points per bar |
| IsTextDisplayed | A bool value representing if text will be drawn along with the draw object |





Example
-------




| ns |
| --- |
| // Instantiate a GannFan object
GannFan myFan = Draw.GannFan(this, "tag1", true, 0, Low[0]);
 
// Instantiate a new PriceLevel to be used in the step below
PriceLevel myLevel = new PriceLevel(99, Brushes.Black);
 
// Change the object's price level at index 3
myFan.PriceLevels[3] = myLevel; |






 
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
 
 
 



