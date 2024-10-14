










 


Count







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartbars_count.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartBars](chartbars.htm) &gt;
Count | [Previous page](chartbars_bars.htm)
[Return to chapter overview](chartbars.htm)










Definition
----------


The total number of [ChartBars](chartbars.htm) in the charts primary data series



Property Value
--------------


An int value representing the the total number of bars.


 


Syntax
------


ChartBars.Count


 


Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if(ChartBars != null)
   {
     Print("ChartBars contain " + ChartBars.Count + " bars");
     //Output:  ChartBars contain 73 bars 
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
 
 
 



