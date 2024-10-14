










 


GetAttachedToChartBars()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getattachedtochartbars.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
GetAttachedToChartBars() | [Previous page](drawnby.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


Returns information which relate to the underlying bars series in which the drawing tool is attached.  If the drawing tool is attached to an indicator rather than a bar series, the indicator's bars series used for input will be returned.


 




|  |
| --- |
| Note: For drawing tools made global, this method will not be returning meaningful values - since those are not attached to a specific bars series |




Method Return Value
-------------------


A [ChartBars](chartbars.htm) object



Syntax
------


GetAttachedToChartBars()



Method Parameters
-----------------


This method does not accept any parameters



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{   
   // get the attached chart bars
   ChartBars myBars = GetAttachedToChartBars();
   
   Print(myBars.Bars.ToChartString()); // NQ 03-15 (1 Minute)
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
 
 
 



