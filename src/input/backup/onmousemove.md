










 


OnMouseMove()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onmousemove.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
OnMouseMove() | [Previous page](onmousedown.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


An event driven method which is called any time the mouse pointer is over the chart control and a mouse is moving.


 


Method Return Value
-------------------


This method does not return a value.


 




|  |
| --- |
| Note:  For a combined single click operation, i.e. mouse down click, move and release the dataPoint reported will always be the initial starting one. |



 


Syntax
You must override the method in your Drawing Tool with the following syntax.
-----------------------------------------------------------------------------------


   

public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)  

{  

   

}



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | A [ChartControl](chartcontrol.htm) representing the x-axis |
| chartPanel | A [ChartPanel](chartpanel.htm) representing the the panel for the chart |
| chartScale | A [ChartScale](chartscale.htm) representing the y-axis |
| dataPoint | A [ChartAnchor](chartanchor.htm) representing a point where the user is moving the mouse |





Examples
--------




| ns |
| --- |
| private   ChartAnchor                     lastMouseMoveAnchor     = new ChartAnchor();
private ChartAnchor MyAnchor;
public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   // add any logic for when the mouse is moved here
   if (DrawingState == DrawingState.Moving)
   {
     //move the chart anchor when the drawing tool is in a moving state
 
     MyAnchor.MoveAnchor(lastMouseMoveAnchor, dataPoint, chartControl, chartPanel, chartScale, this);
     // dont forget to update delta point to last used!
     dataPoint.CopyDataValues(lastMouseMoveAnchor);
   }         
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
 
 
 



