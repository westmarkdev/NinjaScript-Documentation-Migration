










 


IsScrollArrowVisible







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isscrollarrowvisible.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartControl](chartcontrol.htm) &gt;
IsScrollArrowVisible | [Previous page](chartcontrol_indicators.htm)
[Return to chapter overview](chartcontrol.htm)










Definition
----------


Indicates the time-axis scroll arrow is visible in the top-right corner of the chart.



Property Value
--------------


A bool value. When True, indicates that the scroll arrow is visible on the chart; otherwise False.



Syntax
------


<chartcontrol>.IsScrollArrowVisible



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   // Print a message if the scroll arrow is visible on the chart
   if(chartControl.IsScrollArrowVisible);
       Print("The chart is currently not set to auto-scroll. Click the scroll arrow to return to auto-scrolling");
} |



 


 


Based on the image below, IsScrollArrowVisible confirms that the scroll arrow is currently visible on the chart.


 


![ChartControl_IsScrollArrowVisible](chartcontrol_isscrollarrowvisible.png)





 
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
 
 
 



</chartcontrol>