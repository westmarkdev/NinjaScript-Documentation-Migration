










 


Price







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?price.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
Price | [Previous page](moveanchory.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


Determines price value the chart anchor is drawn.


 


Property Value
--------------


An double value representing a price value


 


Syntax
------


<chartanchor>.Price


 


Examples
--------




| ns |
| --- |
| public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, Point point)
{
   Print(MyAnchor.Price); // prints the Y axis data point of the chart anchor 
   // 1999.25
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