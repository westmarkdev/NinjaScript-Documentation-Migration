










 


OnMouseUp()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onmouseup.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
OnMouseUp() | [Previous page](onmousemove.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


An event driven method is called any time the mouse pointer is over the chart control and a mouse button is being released.


 


Method Return Value
-------------------


This method does not return a value


 




|  |
| --- |
| Note:  For a combined single click operation, i.e. mouse down click, move and release the dataPoint reported will always be the initial starting one. |



 


Syntax
You must override the method with the following syntax.
--------------------------------------------------------------


   

public override void OnMouseUp(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)  

{  

   

}



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | A [ChartControl](chartcontrol.htm) representing the x-axis |
| chartPanel | A [ChartPanel](chartpanel.htm) representing the the panel for the chart |
| chartScale | A [ChartScale](chartscale.htm) representing the y-axis |
| dataPoint | A [ChartAnchor](chartanchor.htm) representing a point where the user is releasing the mouse |





Examples
--------




| ns |
| --- |
| public override void OnMouseUp(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   //when the user releases the mouse, ensure the drawing state is set to normal
   if (DrawingState == DrawingState.Editing || DrawingState == DrawingState.Moving)
     DrawingState = DrawingState.Normal;
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
 
 
 



