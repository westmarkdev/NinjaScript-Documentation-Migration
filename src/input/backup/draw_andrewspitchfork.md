










 


Draw.AndrewsPitchfork()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?draw_andrewspitchfork.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
Draw.AndrewsPitchfork() | [Previous page](drawing.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Draws an Andrew's Pitchfork.


 


Method Return Value
-------------------


An [AndrewsPitchfork](andrewspitchfork.htm) object that represents the draw object.


 


Syntax
------


Draw.AndrewsPitchfork(NinjaScriptBase owner, string tag, bool isAutoScale, int anchor1BarsAgo, double anchor1Y, int anchor2BarsAgo, double anchor2Y, int anchor3BarsAgo, double anchor3Y, Brush brush, DashStyleHelper dashStyle, int width)  

Draw.AndrewsPitchfork(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime anchor1Time, double anchor1Y, DateTime anchor2Time, double anchor2Y, DateTime anchor3Time, double anchor3Y, Brush brush, DashStyleHelper dashStyle, int width)  

Draw.AndrewsPitchfork(NinjaScriptBase owner, string tag, bool isAutoScale, int anchor1BarsAgo, double anchor1Y, int anchor2BarsAgo, double anchor2Y, int anchor3BarsAgo, double anchor3Y, bool isGlobal, string templateName)  

Draw.AndrewsPitchfork(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime anchor1Time, double anchor1Y, DateTime anchor2Time, double anchor2Y, DateTime anchor3Time, double anchor3Y, bool isGlobal, string templateName)


 


   

 


Parameters
----------




|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method
 
Typically will be the object which is calling the draw method (e.g., "this") |
| tag | A user defined unique id used to reference the draw object. 
 
For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| isAutoScale | Determines if the draw object will be included in the y-axis scale |
| anchor1BarsAgo | The number of bars ago (x value) of the 1st anchor point |
| anchor1Time | The time of the 1st anchor point |
| anchor1Y | The y value of the 1st anchor point |
| anchor2BarsAgo | The number of bars ago (x value) of the 2nd anchor point |
| anchor2Time | The time of the 2nd anchor point |
| anchor2Y | The y value of the 2nd anchor point |
| anchor3BarsAgo | The number of bars ago (x value) of the 3rd anchor point |
| anchor3Time | The time of the 3rd anchor point |
| anchor3Y | The y value of the 3rd anchor point |
| brush | The brush used to color draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)) |
| dashStyle | DashStyleHelper.Dash 
DashStyleHelper.DashDot 
DashStyleHelper.DashDotDot 
DashStyleHelper.Dot 
DashStyleHelper.Solid
 
Note: Drawing objects with y values very far off the visible canvas can lead to performance hits. Fancier DashStyles like DashDotDot will also require more resources than simple DashStyles like Solid. |
| width | The width of the draw object |
| isGlobal | Determines if the draw object will be global across all charts which match the instrument |
| templateName | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead) |



 



Examples
--------




| ns |
| --- |
| // Draws an Andrew's Pitchfork 
Draw.AndrewsPitchfork(this, "tag1", true, 4, Low[4], 3, High[3], 1, Low[1], Brushes.Blue, DashStyleHelper.Solid, 3); |






 
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
 
 
 



