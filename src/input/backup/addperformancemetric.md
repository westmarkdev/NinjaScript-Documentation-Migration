










 


AddPerformanceMetric()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?addperformancemetric.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
AddPerformanceMetric() | [Previous page](addchartindicator.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Adds an instance of custom [Performance Metric](performancemetrics.htm) to a strategy used in strategy calculations.


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
AddPerformanceMetric(PerformanceMetricBase performanceMetric)
--------------------------------------------------------------------


 




|  |
| --- |
| Warning:  This method should ONLY be called from the [OnStateChange()](onstatechange.htm) method during State.Configure  |



 


 


Parameters
----------




|  |  |
| --- | --- |
| performanceMetric | The performance metric object to be added |






Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         AddPerformanceMetric(new NinjaTrader.NinjaScript.PerformanceMetrics.SampleCumProfit());
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
 
 
 



