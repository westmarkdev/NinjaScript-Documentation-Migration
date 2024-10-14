










 


CopyDataValues()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?copydatavalues.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt; [ChartAnchor](chartanchor.htm) &gt;
CopyDataValues() | [Previous page](chartanchor.htm)
[Return to chapter overview](chartanchor.htm)










Definition  

Copies the ChartAnchor time and price values from on anchor to another.  This includes the [BarsAgo](barsago.htm), [SlotIndex](barindex.htm), [Time](time.htm), [Price](price.htm), and [DrawnOnBar](drawnonbar.htm) values.  This method is useful for updating a chart anchor to a recent data point when the user interacts with the drawing chart anchor.  


 


 


Method Return Value
-------------------


This method does not return a value.


 



Syntax
------


<chartanchor>.CopyDataValues(ChartAnchor toAnchor)




Method Parameters
-----------------




|  |  |
| --- | --- |
| toAnchor | The ChartAnchor to copy |



 



Examples
--------




| ns |
| --- |
| public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint)
{   
   // if the user is moving the draw object, copy the most recent dataPoint to MyAnchor
   if (DrawingState == DrawingState.Moving)         
     dataPoint.CopyDataValues(Anchor);
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