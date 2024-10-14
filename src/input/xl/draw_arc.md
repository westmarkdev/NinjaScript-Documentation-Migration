﻿










 


Draw.Arc()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?draw_arc.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
Draw.Arc() | [Previous page](andrewspitchfork.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Draws an arc.


 


Method Return Value
-------------------


An [Arc](arc.htm) object that represents the draw object.


 


Syntax
------


Draw.Arc(NinjaScriptBase owner, string tag, int startBarsAgo, double startY, int endBarsAgo, double endY, Brush brush)  

Draw.Arc(NinjaScriptBase owner, string tag, DateTime startTime, double startY, DateTime endTime, double endY, Brush brush)  

Draw.Arc(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int endBarsAgo, double endY, Brush brush, DashStyleHelper dashStyle, int width)  

Draw.Arc(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime endTime, double endY, Brush brush, DashStyleHelper dashStyle, int width)  

Draw.Arc(NinjaScriptBase owner, string tag, bool isAutoScale, int startBarsAgo, double startY, int endBarsAgo, double endY, Brush brush, DashStyleHelper dashStyle, int width, bool drawOnPricePanel)  

Draw.Arc(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime startTime, double startY, DateTime endTime, double endY, Brush brush, DashStyleHelper dashStyle, int width, bool drawOnPricePanel)  

Draw.Arc(NinjaScriptBase owner, string tag, int startBarsAgo, double startY, int endBarsAgo, double endY, bool isGlobal, string templateName)  

Draw.Arc(NinjaScriptBase owner, string tag, DateTime startTime, double startY, DateTime endTime, double endY, bool isGlobal, string templateName)


 


 


Parameters
----------





|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method
 
Typically will be the object which is calling the draw method (e.g., "this") |
| tag | A user defined unique id used to reference the draw object. 
 
For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| isAutoScale | Determines if the draw object will be included in the y-axis scale. Default value is false. |
| startBarsAgo | The starting bar (x axis co-ordinate) where the draw object will be drawn. For example, a value of 10 would paint the draw object 10 bars back. |
| startTime | The starting time where the draw object will be drawn. |
| startY | The starting y value co-ordinate where the draw object will be drawn |
| endBarsAgo | The end bar (x axis co-ordinate) where the draw object will terminate |
| endTime | The end time where the draw object will terminate |
| endY | The end y value co-ordinate where the draw object will terminate |
| brush | The brush used to color draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)) |
| dashStyle | DashStyleHelper.Dash 
DashStyleHelper.DashDot 
DashStyleHelper.DashDotDot 
DashStyleHelper.Dot 
DashStyleHelper.Solid 
 
Note: Drawing objects with y values very far off the visible canvas can lead to performance hits. Fancier DashStyles like DashDotDot will also require more resources than simple DashStyles like Solid. |
| width | The width of the draw object |
| drawOnPricePanel | Determines if the draw-object should be on the price panel or a separate panel
  |
| isGlobal | Determines if the draw object will be global across all charts which match the instrument |
| templateName | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead) |



 



Examples
--------




| ns |
| --- |
| // Draws a dotted lime green arc
Draw.Arc(this, "tag1", false, 10, 1000, 0, 1001, Brushes.LimeGreen, DashStyleHelper.Dot, 2); |






 
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
 
 
 


