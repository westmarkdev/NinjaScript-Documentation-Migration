










 


GetValueByY()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getvaluebyy.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
GetValueByY() | [Previous page](getpixelsfordistance.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


Returns the series value on the chart scale determined by a y pixel coordinate on the chart.


 


Method Return Value
-------------------


A double value representing a series value on the chart scale.  This is normally a price value, but can represent indicator plot values as well.



Syntax
<chartscale>.GetValueByY(float y)
----------------------------------------



Method Parameters
-----------------




|  |  |
| --- | --- |
| y | A float value representing a pixel coordinate on the chart scale |



 



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // the price value of the pixel coordinate passed in the method
   double valueByY =   chartScale.GetValueByY(1);
 
   Print("valueByY: " + valueByY); //2106.19693333   
} |



 


 


In the image below, we pass a value of 1 for the y value, which tells us the pixel coordinate of 1 is located at a price of 2106.19 on the chart scale


 


![getvaluebyY](getvaluebyy.png)





 
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
 
 
 



</chartscale>