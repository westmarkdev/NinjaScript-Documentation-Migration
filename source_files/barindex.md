










 


SlotIndex







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barindex.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
SlotIndex | [Previous page](price.htm)
[Return to chapter overview](chartanchor.htm)










Definition
----------


Indicates the nearest bar slot value where anchor is drawn on a chart.  In a single series chart there will always be equal number of slots and bars, however for multi-series charts there may be additonal slots compared to the bar series your drawing tool resides.


 


Property Value
--------------


An double value representing the current bar.  


 




|  |
| --- |
| Note:  The bar index value is represented as a double as it is possible (and likely) that a given chart anchor is drawn between bars (i.e., if a user draws the tool with snap mode disabled) |



 


 


Syntax
------


ChartAnchor.SlotIndex


 


Examples
--------




| ns |
| --- |
| public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{
   Print(MyAnchor.SlotIndex); // prints the nearest current bar value
   //4502.02734375
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
 
 
 



