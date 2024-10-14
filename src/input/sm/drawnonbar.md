










 


DrawnOnBar







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?drawnonbar.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
DrawnOnBar | [Previous page](drawingtool.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


Gets the current bar value that the chart anchor is drawn by a NinjaScript object.  Please see the [Drawing](drawing.htm) section for more information.





|  |
| --- |
| Note:  This value will NOT work on manually drawn objects.  This property is reserved for chart anchors which were drawn by another NinjaScript object (e.g, using a Draw method in an indicator).  For manually drawn objects, please see the [SlotIndex](barindex.htm) property |



 


 


Property Value
--------------


A int value that value which the current bar the chart anchor is drawn.  This property is read-only.


 


Syntax
------


<chartanchor>.DrawnOnBar
========================


 


Examples
--------




| ns |
| --- |
| //Places text if high is 2419 and prints what bar the text was drawn on
if (High[0] == 2419)
{
 Text myText = Draw.Text(this, @"Text " + CurrentBar, @"High is 2419" , 0, High[0]);
 Print("Text is on bar " + myText.Anchor.DrawnOnBar);
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