










 


MaxMinusMin







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?maxminusmin.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartScale](chartscale.htm) &gt;
MaxMinusMin | [Previous page](chartscale_isvisible.htm)
[Return to chapter overview](chartscale.htm)










Definition
----------


The difference between the chart scale's [MaxValue](chartscale_maxvalue.htm) and [MinValue](chartscale_minvalue.htm) represented as a y value.



Property Value
--------------


A double value representing the difference in scale as a y value.



Syntax
------


<chartscale>.MaxMinusMin



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{         
   // the difference between the scales maximum and minimum value
   double   maxMinusMin = chartScale.MaxMinusMin;
   
   Print("maxMinusMin: " + maxMinusMin); // maxMinusMin: 3.92
} |



 


 


In the image below, the highest calculated value on the chart scale is 2106.21, with the lowest value being 2102.29;  the MaxMinusMin property therefore provides us calculated value of 3.92.


 


![MaxMinusMin](maxminusmin.png)





 
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