










 


Value







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?optimization_fitness_value.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Optimization Fitness](optimization_fitness.htm) &gt;
Value | [Previous page](oncalculateperformancevalue.htm)
[Return to chapter overview](optimization_fitness.htm)










Definition
----------


The value an optimization would be calculating against when using this Optimization Fitness.


 


Property Value
--------------


A double value.


 


Syntax
------


Value


 


 


Examples
--------




| ns |
| --- |
| protected override void OnCalculatePerformanceValue(StrategyBase strategy)
{
     Value = strategy.SystemPerformance.AllTrades.TradesPerformance.Percent.Drawdown;
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
 
 
 



