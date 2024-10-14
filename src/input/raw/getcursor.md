










 


GetCursor()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getcursor.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
GetCursor() | [Previous page](getclosestanchor.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


An event driven method which is called when a chart object is selected.  This method can be used to change the cursor image used in various states.


 


Method Return Value
-------------------


This method returns a [Cursor](https://msdn.microsoft.com/en-us/library/system.windows.forms.cursor(v=vs.110).aspx) used to paint the mouse pointer.



Syntax
You must override the method in your Drawing Tool with the following syntax:
-----------------------------------------------------------------------------------


 


public override Cursor GetCursor(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)


{


 


}



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | A [ChartControl](chartcontrol.htm) representing the x-axis |
| chartPanel | A [ChartPanel](chartpanel.htm) representing the the panel for the chart |
| chartScale | A [ChartScale](chartscale.htm) representing the y-axis |
| point | A Point in device pixels representing the current mouse cursor position  |





Examples
--------




| ns |
| --- |
| public override Cursor GetCursor(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
   switch (DrawingState)
   {
     //when drawing, display the cursor as a pen
     case DrawingState.Building:   return Cursors.Pen;
 
     // when moving, display a four-headed sizing cursor
     case DrawingState.Moving:   return Cursors.SizeAll;
 
     default: return Cursors.Pen;
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
 
 
 



