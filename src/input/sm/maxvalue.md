










 


MaxValue







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?maxvalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt;
MaxValue | [Previous page](isvisibleonchart.htm)
[Return to chapter overview](rendering.htm)










Definition
----------


The maximum value used for the automatic scaling of the y axis.  This property will only be used when the chart object is set to [IsAutoScale](isautoscale.htm)



Property Value
--------------


A double value


 


Syntax
------


MaxValue


 


Examples
--------




| ns |
| --- |
| public override void OnCalculateMinMax()
{
   if (DrawingState != DrawingState.Building)
   {
     //set the maximum value to the chart anchors price
     MaxValue = Anchor.Price;
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
 
 
 



