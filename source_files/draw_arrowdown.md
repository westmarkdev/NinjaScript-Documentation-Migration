










 


Draw.ArrowDown()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?draw_arrowdown.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
Draw.ArrowDown() | [Previous page](arc.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Draws an arrow pointing down.


 


Method Return Value
-------------------


An [ArrowDown](arrowdown.htm) object that represents the draw object.


 


Syntax
------


Draw.ArrowDown(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y, Brush brush)  

Draw.ArrowDown(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime time, double y, Brush brush)  

Draw.ArrowDown(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y, Brush brush, bool drawOnPricePanel)  

Draw.ArrowDown(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime time, double y, Brush brush, bool drawOnPricePanel)  

Draw.ArrowDown(NinjaScriptBase owner, string tag, bool isAutoScale, int barsAgo, double y, bool isGlobal, string templateName)  

Draw.ArrowDown(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime time, double y, bool isGlobal, string templateName)


 


Parameters
----------




|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method
 
Typically will be the object which is calling the draw method (e.g., "this") |
| tag | A user defined unique id used to reference the draw object. 
 
For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| isAutoScale | Determines if the draw object will be included in the y-axis scale |
| barsAgo | The bar the object will be drawn at. A value of 10 would be 10 bars ago. |
| time | The time the object will be drawn at. |
| y | The y value |
| brush | The brush used to color draw object ([reference](https://msdn.microsoft.com/en-us/library/system.windows.media.brushes%28v=vs.110%29.aspx))
  |
| drawOnPricePanel | Determines if the draw-object should be on the price panel or a separate panel |
| isGlobal | Determines if the draw object will be global across all charts which match the instrument |
| templateName | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead) |







|  |
| --- |
| Tip: The size of the arrow is tied to the chart's BarWidth and thus will scale automatically as the chart is resized                          |





Examples
--------




| ns |
| --- |
| // Paints a red down arrow on the current bar 1 tick above the high
   Draw.ArrowDown(this, "tag1", true, 0, High[0] + TickSize, Brushes.Red);
 
// Paints a blue down arrown on a three bar reversal pattern 
if (High[2] &gt; High[3] &amp;&amp; High[1] &gt; High[2] &amp;&amp; Close[0] &lt; Open[0])
     Draw.ArrowDown(this, CurrentBar.ToString(), true, 0, High[0] + TickSize, Brushes.Blue); |






 
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
 
 
 



