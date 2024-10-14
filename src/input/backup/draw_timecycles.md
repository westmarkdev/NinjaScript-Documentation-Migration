










 


Draw.TimeCycles()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?draw_timecycles.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
Draw.TimeCycles() | [Previous page](textfixed.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Draws a time cycle based on two points.


 


Method Return Value
-------------------


A [TimeCycles](timecycles.htm) object that represents the draw object.


 


Syntax
------


Draw.TimeCycles(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, double endY, Brush brush, bool drawOnPricePanel)


Draw.TimeCycles(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, bool isGlobal, string templateName)


Draw.TimeCycles(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, Brush brush, bool drawOnPricePanel)


Draw.TimeCycles(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, bool isGlobal, string templateName)


Draw.TimeCycles(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, Brush brush, Brush areaBrush, int areaOpacity)


Draw.TimeCycles(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, Brush brush, Brush areaBrush, int areaOpacity)


Draw.TimeCycles(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, Brush brush, Brush areaBrush, int areaOpacity, bool drawOnPricePanel)


Draw.TimeCycles(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, Brush brush, Brush areaBrush, int areaOpacity, bool drawOnPricePanel)


Draw.TimeCycles(NinjaScriptBase owner, string tag, DateTime startTime, DateTime endTime, Brush brush)


Draw.TimeCycles(NinjaScriptBase owner, string tag, int startBarsAgo, int endBarsAgo, Brush brush)  

 


Parameters
----------




|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method
 
Typically will be the object which is calling the draw method (e.g., "this") |
| tag | A user defined unique id used to reference the draw object. 
 
For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| startBarsAgo | The starting bar (x axis co-ordinate) where the draw object will be drawn. For example, a value of 10 would paint the draw object 10 bars back. |
| startTime | The starting time where the draw object will be drawn |
| endBarsAgo | The end bar (x axis co-ordinate) where the draw object will terminate |
| endTime | The end time where the draw object will terminate |
| brush | The brush used to color draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)) |
| drawOnPricePanel | Determines if the draw-object should be on the price panel or a separate panel |
| isGlobal | Determines if the draw object will be global across all charts which match the instrument |
| templateName | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead) |





Examples
--------




| ns |
| --- |
| // Draws a Time Cycles object based on 10 bars back to the current bar that is cornflower blue with an opacity of 40
Draw.TimeCycles(this, "tag1", 0, 10, Brushes.CornflowerBlue, Brushes.CornflowerBlue, 40); |






 
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
 
 
 



