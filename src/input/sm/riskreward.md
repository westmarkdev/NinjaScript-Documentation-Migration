










 


RiskReward







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?riskreward.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Drawing](drawing.htm) &gt; [Draw.RiskReward()](draw_riskreward.htm) &gt;
RiskReward | [Previous page](draw_riskreward.htm)
[Return to chapter overview](draw_riskreward.htm)










Definition
----------


Represents an interface that exposes information regarding a Risk Reward [IDrawingTool](idrawingtool.htm).


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| EntryAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the entry point of the drawing object |
| RiskAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the stop loss point of the drawing object |
| RewardAnchor | An [IDrawingTool's ChartAnchor](idrawingtool.htm#chartanchor) representing the profit target point of the drawing object |
| Ratio | An int value determining the calculated ratio between the risk or reward based on the entry point |





Example
-------




| ns |
| --- |
| // Instantiate a RiskReward object
RiskReward myRR = Draw.RiskReward(this, "tag1", false, 0, High[0], 10, Low[0], 2, true);
 
// Change the object's risk/reward ratio to 2:1
myRR.Ratio = 2; |






 
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
 
 
 



