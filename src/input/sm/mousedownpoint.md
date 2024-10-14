










 


MouseDownPoint







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?mousedownpoint.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
MouseDownPoint | [Previous page](lasttimepainted.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the WPF x- and y-coordinates of the mouse cursor at the most recent OnMouseDown() event.



Property Value
--------------


A [Point](https://msdn.microsoft.com/en-us/library/system.drawing.point(v=vs.110).aspx) object containing x- and y-coordinates of the mouse cursor when the left mouse button is clicked or held



Syntax
------


<chartcontrol>.MouseDownPoint



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   Point cursorPoint = chartControl.MouseDownPoint;
 
   // Print the x- and y-coordinates of the mouse cursor when clicked
   Print(String.Format("Mouse clicked at coordinates {0},{1}", cursorPoint.X, cursorPoint.Y));
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
 
 
 



</chartcontrol>