










 


OnRender()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartstyle_onrender.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Chart Style](chart_style.htm) &gt;
OnRender() | [Previous page](istransparent.htm)
[Return to chapter overview](chart_style.htm)










Definition
----------


An event driven method used to render content to a ChartStyle.  The OnRender() method is called every time the chart values are updated.  These updates are driven by incoming data to the chart bars or by a user manually interacting with the chart control or chart scale.


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
You must override the method in your ChartStyle with the following syntax:
---------------------------------------------------------------------------------


 


protected override void OnRender(ChartControl chartControl, ChartScale chartScale, ChartBars chartBars)  

{  

   

}



Method Parameters
-----------------




|  |  |
| --- | --- |
| chartControl | A ChartControl representing the x-axis |
| chartScale | A ChartScale representing the y-axis |
| chartBars | A ChartBars representing the Bars series for the chart |



 



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale, ChartBars chartBars)
{
     // Rendering logic for our chart style
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
 
 
 



