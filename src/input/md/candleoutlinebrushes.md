










 


CandleOutlineBrushes







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?candleoutlinebrushes.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
CandleOutlineBrushes | [Previous page](candleoutlinebrush.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


A collection of historical outline brushes for candlesticks.


 


Property Value
--------------


A brush series type object. Accessing this property via an index value [int barsAgo] returns a [brush](http://msdn.microsoft.com/en-us/library/system.windows.media.brush(v=vs.110).aspx) structure representing the referenced bar's outline color.


 




|  |
| --- |
| Note: This will only return the color of a candlestick outline in which an explicit color overwrite was used. Otherwise it will return null. |



 


 


Syntax
------


CandleOutlineBrushes  

CandleOutlineBrushes[int barsAgo]


 




|  |
| --- |
| Warning:  You may have up to 65,535 unique CandleOutlineBrushes instances, therefore, using [static predefined brushes](working_with_brushes.htm) should be favored.  Alternatively,  in order to use fewer brushes, please try to cache your custom brushes until a new brush would actually need to be created. |



 


 


Examples
--------




| ns |
| --- |
| // Sets the outline color of the current bar to black.
CandleOutlineBrushes[0] = Brushes.Black;
 
// Sets the outline color of the previous bar to blue.
CandleOutlineBrushes[1] = Brushes.Blue; |






 
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
 
 
 



