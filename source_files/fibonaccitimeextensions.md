










 


FibonacciTimeExtensions







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?fibonaccitimeextensions.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.FibonacciTimeExtensions()](draw_fibonaccitimeextensions.htm) &gt;
FibonacciTimeExtensions | [Previous page](draw_fibonaccitimeextensions.htm)
[Return to chapter overview](draw_fibonaccitimeextensions.htm)










Definition
----------


Represents an interface that exposes information regarding a Fibonacci Time Extensions [IDrawingTool](idrawingtool.htm).


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| StartAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the starting point of the drawing object |
| EndAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the end point of the drawing object |
| [PriceLevels](pricelevels.htm) | A collection of prices calculated by the drawing object |
| IsTextDisplayed | A bool value determining if the draw object should display text on the chart. |
| IsExtendedLinesLeft | A bool value determining if the draw object should draw lines to the far left side of the screen |
| IsExtendedLinesRight | A bool value determining if the draw object should draw lines to the far right side of the screen |





Example
-------




| ns |
| --- |
| // Instantiate a FibonacciTimeExtensions object
FibonacciTimeExtensions myFibTime = Draw.FibonacciTimeExtensions(this, "tag1", false, 10, Low[10], 0, High[0]);
 
// Instantiate a new PriceLevel to be used in the step below
PriceLevel myLevel = new PriceLevel(99, Brushes.Black);
 
// Change the object's price level at index 3
myFibTime.PriceLevels[3] = myLevel; |






 
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
 
 
 



