










 


Draw.Region()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?draw_region.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
Draw.Region() | [Previous page](rectangle.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Draws a region on a chart.


 


Method Return Value
-------------------


A [Region](region.htm) object that represents the draw object.


 


Syntax


Draw.Region(NinjaScriptBase owner, string tag, int startBarsAgo,  

         int endBarsAgo, ISeries<double> series, double price, Brush areaBrush, int areaOpacity, int displacement = 0)  

Draw.Region(NinjaScriptBase owner, string tag, int startBarsAgo,  

         int endBarsAgo, ISeries<double> series1, ISeries<double> series2, Brush outlineBrush,  

         Brush areaBrush, int areaOpacity, [int displacement])  

Draw.Region(NinjaScriptBase owner, string tag, DateTime startTime,  

         DateTime endTime, ISeries<double> series, double price, Brush areaBrush, int areaOpacity)  

Draw.Region(NinjaScriptBase owner, string tag, DateTime startTime,  

         DateTime endTime, ISeries<double> series1, ISeries<double> series2, Brush outlineBrush, Brush areaBrush, int areaOpacity)


 


Parameters
----------




|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method
 
Typically will be the object which is calling the draw method (e.g., "this") |
| tag | A user defined unique id used to reference the draw object. 
 
For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| startBarsAgo | The starting bar (x axis co-ordinate) where the draw object will be drawn. For example, a value of 10 would paint the draw object 10 bars back. |
| startTime | The starting time where the draw object will be drawn. |
| endBarsAgo | The end bar (x axis co-ordinate) where the draw object will terminate |
| endTime | The end time where the draw object will terminate |
| series, series1, series2 | Any Series<double> type object such as an indicator, Close, High, Low etc.. The value of the object will represent a y value. |
| price | Any double value |
| outlineBrush | The brush used to color the region outline of draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)) |
| areaBrush | The brush used to color the fill region area of the draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)) |
| areaOpacity | Sets the level of transparency for the fill color. Valid values between 0 - 100. (0 = completely transparent, 100 = no opacity) |
| displacement | An optional parameter which will offset the barsAgo value for the Series<double> value used to match the desired [Displacement](displacement.htm).  Default value is 0. |



 



Example
-------




| ns |
| --- |
| // Draw a region between upper and lower Bollinger bands
Draw.Region(this, "tag1", CurrentBar, 0, Bollinger(2, 14).Upper, Bollinger(2, 14).Lower, null, Brushes.Blue, 50); |



 


 




|  |
| --- |
| Tips:
1. Pass in null to the "outlineColor" parameter if you do not want to have an outline color. 
2. If you wanted to fill a region between a value (20 period simple moving average) and the upper edge of the chart, pass in an extreme value to the "y" parameter such as 1000000.
3. Should you be drawing regions based on Series<double> objects instead of indicator plots, be sure to create the Series<double> with the MaximumBarsLookBack.Infinite parameter if the region you are drawing would be maintained on the chart for more than 256 bars back. |






 
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
 
 
 



</double></double></double></double></double></double></double></double></double></double>