










 


DrawingState







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?drawingstate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
DrawingState | [Previous page](dispose.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Represents the current state of the drawing tool to perform various actions, such as building, editing, or moving.


 


Property Values
---------------


An enum representing the current state of the drawing tool.  Possible values are:




|  |  |
| --- | --- |
| DrawingState.Building | The initial state when a drawing tool is first being drawn, allowing for the anchors to be set for the drawing. |
| DrawingState.Editing | Allows for changing the values of any of the drawing tools anchors |
| DrawingState.Normal | The drawing tool is normal on the chart and is not in a state to allow for changes. |
| DrawingState.Moving | The entire drawing tool to be moved by a user. |



 


 


Syntax
------


DrawingState



Examples
--------




| ns |
| --- |
| public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
   switch(DrawingState)
   {                        
     case DrawingState.Normal:
         DrawingState = DrawingState.Editing; // set state to allow editing
         break;         
     case DrawingState.Editing:
         // do your edits here
         break;
     case DrawingState.Moving:
         return; // don't allow move whe editing            
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
 
 
 



