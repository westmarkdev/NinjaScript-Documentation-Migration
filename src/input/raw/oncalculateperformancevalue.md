










 


OnCalculatePerformanceValue()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?oncalculateperformancevalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Optimization Fitness](optimization_fitness.htm) &gt;
OnCalculatePerformanceValue() | [Previous page](optimization_fitness.htm)
[Return to chapter overview](optimization_fitness.htm)










Definition
----------


This method calculates the value for the Optimization Fitness.


 


Syntax
------


protected override void OnCalculatePerformanceValue(StrategyBase strategy)   

{


   

}


 


 


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
 
 
 



