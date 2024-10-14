










 


Draw.RiskReward()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?draw_riskreward.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt;
Draw.RiskReward() | [Previous page](regressionchannel.htm)
[Return to chapter overview](drawing.htm)










Definition
----------


Draws a risk/reward on a chart.


 


Method Return Value
-------------------


A [RiskReward](riskreward.htm) object that represents the draw object.


 


Syntax
------


Draw.RiskReward(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime entryTime, double entryY, DateTime endTime, double endY, double ratio, bool isStop)  

Draw.RiskReward(NinjaScriptBase owner, string tag, bool isAutoScale, int entryBarsAgo , double entryY, int endBarsAgo, double endY, double ratio, bool isStop)  

Draw.RiskReward(NinjaScriptBase owner, string tag, bool isAutoScale, DateTime entryTime, double entryY, DateTime endTime, double endY, double ratio, bool isStop, bool isGlobal, string templateName)  

Draw.RiskReward(NinjaScriptBase owner, string tag, bool isAutoScale, int entryBarsAgo , double entryY, int endBarsAgo, double endY, double ratio, bool isStop, bool isGlobal, string templateName)


 


 


Parameters
----------




|  |  |
| --- | --- |
| owner | The hosting NinjaScript object which is calling the draw method
 
Typically will be the object which is calling the draw method (e.g., "this") |
| tag | A user defined unique id used to reference the draw object. 
 
For example, if you pass in a value of "myTag", each time this tag is used, the same draw object is modified. If unique tags are used each time, a new draw object will be created each time. |
| isAutoScale | Determines if the draw object will be included in the y-axis scale. Default value is false. |
| entryTime | The time where the draw object's entry will be drawn. |
| entryBarsAgo | The starting bar (x axis co-ordinate) where the draw object's entry will be drawn. For example, a value of 10 would paint the draw object 10 bars back. |
| entryY | The y value co-ordinate where the draw object's entry price will be drawn |
| endBarsAgo | The end bar (x axis co-ordinate) where the draw object will terminate |
| endTime | The end time where the draw object will terminate |
| endY | The starting y value co-ordinate where the draw object will be drawn |
| ratio | An double value determining the calculated ratio between the risk and reward based on the entry point. Example: reward : risk is ratio of 1.0 |
| isStop | A bool value, when true will use the endTime / endBarsAgo and endY to set the stop and will automatically calculate the target based off the ratio value. When false, will set the target and will automatically calculate the stop based off the ratio value. |
| isGlobal | Determines if the draw object will be global across all charts which match the instrument |
| templateName | The name of the drawing tool template the object will use to determine various visual properties (empty string could be used to just use the UI default visuals instead) |



 



Examples
--------




| ns |
| --- |
| // draw a risk/reward tool starting from the current bar to 10 bars ago
// with calcuate a ratio of 2 based on stop level
Draw.RiskReward(this, "tag1", false, 0, High[0], 10, Low[0], 2, true); |






 
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
 
 
 



