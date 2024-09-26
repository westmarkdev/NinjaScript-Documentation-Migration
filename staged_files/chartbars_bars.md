










 


Bars







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?chartbars_bars.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Charts](chart.htm) &gt; [ChartBars](chartbars.htm) &gt;
Bars | [Previous page](chartbars.htm)
[Return to chapter overview](chartbars.htm)










Definition
----------


Represents the data returned from the historical data repository in relation to the primary [ChartBars](chartbars.htm) object configured on the chart.  See also [Bars](bars.htm)



Property Value
--------------


A [Bars](bars.htm) object


 


Syntax
------


ChartBars.Bars



Examples
--------




| ns |
| --- |
| protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
   if(ChartBars != null &amp;&amp; ChartBars.Bars != null)
   {
     Print("The configured bars period type represented on the chart is" + ChartBars.Bars.BarsPeriod.BarsPeriodType);
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
 
 
 



