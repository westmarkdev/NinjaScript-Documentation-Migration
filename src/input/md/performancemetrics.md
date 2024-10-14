










 


PerformanceMetrics







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?performancemetrics.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
PerformanceMetrics | [Previous page](percent.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns a collection of custom [Performance Metrics](performance_metrics.htm). These need to have been enabled in [Tools &gt; Options &gt; General](general_section.htm) to be able to use them.


 


Syntax
<tradecollection>.TradesPerformance.PerformanceMetrics
-------------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the number of enabled custom Performance Metrics
     Print("Number of Performance Metrics: "
         + SystemPerformance.AllTrades.TradesPerformance.PerformanceMetrics.Length);
 
     // Find a the value of a specific custom Performance Metric named "MyPerformanceMetric"
     for (int i = 0; i &lt; SystemPerformance.AllTrades.TradesPerformance.PerformanceMetrics.Length; i++)
     {
         if (SystemPerformance.AllTrades.TradesPerformance.PerformanceMetrics[i] is 
               NinjaTrader.NinjaScript.PerformanceMetrics.MyPerformanceMetric)
         {
               Print((SystemPerformance.AllTrades.TradesPerformance.PerformanceMetrics[i] as 
                   NinjaTrader.NinjaScript.PerformanceMetrics.MyPerformanceMetric).Values[0]);
         }
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
 
 
 



</tradecollection>