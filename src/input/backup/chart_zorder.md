










 


ZOrder







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chart_zorder.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [Rendering](rendering.htm) &gt;
ZOrder | [Previous page](setzorder.htm)
[Return to chapter overview](rendering.htm)










Definition
----------


A unique identifier representing the index in which chart objects are drawn on the chart's Z-axis (front to back ordering). Objects with a higher ZOrder are drawn first.  


 




|  |
| --- |
| Note:  The ZOrder index should NOT be set using this property. Please use the dedicated [SetZOrder()](setzorder.htm) for this purpose. |



 


Property Value
--------------


A int value representing the order that the object is drawn.  Default value is categorized by the type of object drawn, which will then increment for each instance of the chart object that is drawn.  Each type of object will have a different default starting value to keep these objects separate:


 




|  |  |
| --- | --- |
| Chart Bars | 1 |
| NinjaScript Objects | 10001 |
| Global Draw Objects | 20001 |
| Draw Objects | 30001 |



 


Syntax
------


ZOrder


 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // call the base.OnRender() to ensure standard Plots work as designed
   base.OnRender(chartControl, chartScale);
 
   // Print the currently assigned ZOrder index for this NinjaScript object
   Print("Current ZOrder level is: " + ZOrder);
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
 
 
 



