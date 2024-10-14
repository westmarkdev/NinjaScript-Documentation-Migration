










 


Performance Metrics







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?performance_metrics.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt;
Performance Metrics | [Previous page](supportsmultiobjectiveoptimiza.htm)
[Return to chapter overview](language_reference_wip.htm)










Custom Performance Metrics can be used when generating Trade Performance statistics. 


 


Once custom performance metrics are created be sure to enable their usage in [Tools &gt; Options &gt; General](general_section.htm) or else they will not be available in the [Strategy Analyzer](strategy_analyzer.htm) or [Trade Performance](trade_performance.htm) windows.


 


In this section
---------------




|  |  |
| --- | --- |
| [Format()](format.htm) | This method allows you to customize the rendering of the performance value on the Summary grid. |
| [OnAddTrade()](onaddtrade.htm) | This method is called as each trade is added. |
| [OnCopyTo()](oncopyto.htm) | Called as the values of a trade metric are saved. |
| [OnMergePerformanceMetric()](onmergeperformancemetric.htm) | This method is called when the Performance Metric would be aggregated and merged together. |
| [PerformanceUnit](performanceunit.htm) | Enumeration defining each type of PerformanceUnit calculated by NinjaTrader. Used to store a value for this performance type in PerformanceMetrics. |
| [Values](performancemetric_values.htm) | The Values array holds an 5 values corresponding to each Cbi.PerformanceUnit. |






 
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
 
 
 



