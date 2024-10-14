










 


Draw.HorizontalLine()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?draw_horizontalline.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
Draw.HorizontalLine() | [Previous page](gannfan.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Draws a horizontal line.


 


Method Return Value
-------------------


A [HorizontalLine](horizontalline.htm) object that represents the draw object.


 


Syntax
------


Draw.HorizontalLine(NinjaScriptBase owner, string tag, double y, Brush brush)  

Draw.HorizontalLine(NinjaScriptBase owner, string tag, bool isAutoScale, double y, Brush brush, DashStyleHelper dashStyle, int width)  

Draw.HorizontalLine(NinjaScriptBase owner, string tag, bool isAutoscale, double y, Brush brush, bool drawOnPricePanel)  

Draw.HorizontalLine(NinjaScriptBase owner, string tag, double y, Brush brush, DashStyleHelper dashStyle, int width, bool drawOnPricePanel)  

Draw.HorizontalLine(NinjaScriptBase owner, string tag, double y, bool isGlobal, string templateName)


   

 


Parameters
----------




|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method
 
Typically will be the object which is calling the draw method (e.g., "this") |
| tag | A user defined unique id used to reference the draw object. 
 
For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| isAutoScale | Determines if the draw object will be included in the y-axis scale. Default value is false. |
| y | The y value |
| brush | The brush used to color draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx)) |
| dashStyle | DashStyleHelper.Dash 
DashStyleHelper.DashDot 
DashStyleHelper.DashDotDot 
DashStyleHelper.Dot 
DashStyleHelper.Solid 
 
Note: Fancier DashStyles like DashDotDot will require more resources than simple DashStyles like Solid. |
| width | The width of the draw object |
| isDrawOnPricePanel | Determines if the draw-object should be on the price panel or a separate panel |
| isGlobal | Determines if the draw object will be global across all charts which match the instrument |
| templateName | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead) |



 



Examples
--------




| ns |
| --- |
|  | // Draws a horizontal line
Draw.HorizontalLine(this, "tag1", 1000, Brushes.Black); |






 
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
 
 
 



