










 


Time







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?time.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
Time | [Previous page](barindex.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


Determines date/time value the chart anchor is drawn.


 


Property Value
--------------


An DateTime value representing a time value


 


Syntax
------


<chartanchor>.Time


 


Examples
--------




| ns |
| --- |
| public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
Print(MyAnchor.Time); // prints the X axis datetime of the chart anchor 
// 8/26/2014 6:55:00 PM
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