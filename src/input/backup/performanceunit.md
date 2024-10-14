










 


PerformanceUnit







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?performanceunit.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Performance Metrics](performance_metrics.htm) &gt;
PerformanceUnit | [Previous page](onmergeperformancemetric.htm)
[Return to chapter overview](performance_metrics.htm)










Definition
----------


Enumeration defining each type of PerformanceUnit calculated by NinjaTrader. Used to store a value for this performance type in PerformanceMetrics.


 


Syntax
------


PerformanceUnit.Currency


PerformanceUnit.Percent


PerformanceUnit.Pips


PerformanceUnit.Points


PerformanceUnit.Ticks


 


Examples
--------




| ns |
| --- |
| //Prints unrealized PnL in ticks at the close of each bar
Print(Position.GetUnrealizedProfitLoss(PerformanceUnit.Ticks, Close[0])); |






 
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
 
 
 



