










 


MaxValue







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartscale_maxvalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
MaxValue | [Previous page](maxminusmin.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


The highest displayed value on the chart scale. 



Property Value
--------------


A double value representing highest value on the chart scale as a y value.


 


Syntax
------


<chartscale>.MaxValue


 


Example
-------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{         
   // the maximum value of the chart scale
   double maxValue   = chartScale.MaxValue;
 
   Print("maxValue: " + maxValue);
} |



 


 


In the image below, the highest value displayed as text on the y-axis reads 2106.00, however as you can see, there are a few pixels on the chart scale above this tick.  The absolute rendered MaxValue on the chart scale is calculated as 2106.21  


 


![MaxValue](maxvalue.png)





 
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