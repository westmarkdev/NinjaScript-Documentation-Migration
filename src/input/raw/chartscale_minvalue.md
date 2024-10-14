










 


MinValue







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartscale_minvalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
MinValue | [Previous page](chartscale_maxvalue.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


The lowest rendered value on the chart scale.



Property Value
--------------


A double value representing lowest value on the chart scale as a y value.


 


Syntax


<chartscale>.MinValue



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{         
   // the minimum value of the chart scale
   double minValue   = chartScale.MinValue;
 
   Print("minValue: " + minValue);
} |



 


 


In the image below, the lowest value displayed as text on the y-axis reads 2102.50, however as you can see, there are a few pixels on the chart scale below this tick.  The absolute rendered MinValue on the chart scale is calculated as 2102.29.  


 


![MinValue](minvalue.png)





 
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