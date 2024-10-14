










 


IsEditing







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isediting.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
IsEditing | [Previous page](isbrowsable.htm)
[Return to chapter overview](chartanchor.htm)










Definition  

Determines if the anchor can be edited.


 


Property Value
--------------


A bool value which when true determines if the chart anchor is currently in a state it can be edited.  Default is false.


 


Syntax
------


<chartanchor>.IsEditing
=======================



Examples
--------




| ns |
| --- |
| public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
if(DrawingState == DrawingState.Building)
{
   // if drawing tool is currently editing, update to current mouse point
if(MyAnchor.IsEditing)
{
 MyAnchor.UpdateFromPoint(point, chartControl, chartScale);
 
 //set the anchor to disable editing when done updating
 MyAnchor.IsEditing = false;                                        
}
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
 
 
 



</chartanchor>