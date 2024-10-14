










 


OnMergePerformanceMetric()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onmergeperformancemetric.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Performance Metrics](performance_metrics.htm) &gt;
OnMergePerformanceMetric() | [Previous page](oncopyto.htm)
[Return to chapter overview](performance_metrics.htm)










Definition
----------


This method is called when the Performance Metric would be aggregated and merged together (E.g. on the Strategy Analyzer's total row).


 


Syntax
------


protected override void OnMergePerformanceMetric(PerformanceMetricBase merge)   

{  

   

}



Examples
--------




| ns |
| --- |
| protected override void OnMergePerformanceMetric(PerformanceMetricBase target)
{
   // You need to cast, in order to access the right type
   SampleCumProfit targetMetrics = (target as SampleCumProfit);
 
   // This is just a simple weighted average sample
   if (targetMetrics != null &amp;&amp; TradesPerformance.TradesCount + targetMetrics.TradesPerformance.TradesCount &gt; 0)
     for (int i = 0; i &lt; Values.Length; i++)
         targetMetrics.Values[i] = (targetMetrics.Values[i] * targetMetrics.TradesPerformance.TradesCount + Values[i] * TradesPerformance.TradesCount) / (TradesPerformance.TradesCount + targetMetrics.TradesPerformance.TradesCount);
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
 
 
 



