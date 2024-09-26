










 


GetYByValue()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getybyvalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
GetYByValue() | [Previous page](getvaluebyywpf.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


Returns the chart's y-pixel coordinate on the chart determined by a series value represented on the chart scale.


 


Method Return Value
-------------------


An int value representing a y pixel coordinate on the chart scale.



Syntax
<chartscale>.GetYByValue(double val)
-------------------------------------------



Method Parameters
-----------------




|  |  |
| --- | --- |
| val | A double value which usually represents a price or indicator value |



 



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // gets the pixel coordinate of the price value passed to the method
   int     yByValue = chartScale.GetYByValue(Bars.GetClose(Bars.Count - 1));
 
   Print("yByValue: " + yByValue); // 207
} |



 


 


 In the image below, we pass the last bar close as the value (example logic avoids using a bars ago index, see also [OnRender()](onrender.htm) note #5), which in return tells us the last price displayed on the chart is at a y location of 207 pixels.


 


![getybyvalue](getybyvalue.png)





 
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