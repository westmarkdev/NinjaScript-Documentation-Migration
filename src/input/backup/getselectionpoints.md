










 


GetSelectionPoints()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getselectionpoints.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
GetSelectionPoints() | [Previous page](getcursor.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Returns the chart object's data points where the user can interact.   These points are used to visually indicate that the chart object is selected and allow the user to manipulate the chart object.  This method is only called when [IsSelected](isselected.htm) is set to true.


 


Method Return Value
-------------------


A collection of [Points](https://msdn.microsoft.com/en-us/library/system.drawing.point%28v=vs.110%29.aspx) representing the x- and y-coordinates of the chart object. 



Syntax
You must override the method using the following syntax:
---------------------------------------------------------------


public override Point[] GetSelectionPoints(ChartControl chartControl, ChartScale chartScale)  

{  

   

}



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | A [ChartControl](chartcontrol.htm) representing the x-axis |
| chartScale | A [ChartScale](chartscale.htm) representing the y-axis |





Examples
--------




| ns |
| --- |
| public override Point[] GetSelectionPoints(ChartControl chartControl, ChartScale chartScale)
{        
 
 ChartPanel chartPanel = chartControl.ChartPanels[chartScale.PanelIndex];
                 
// get the anchor point to be displayed on the drawing tool
 Point anchorPoint = Anchor.GetPoint(chartControl, chartPanel, chartScale, false);
         return new[] { anchorPoint } ;
} |






 
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
 
 
 



