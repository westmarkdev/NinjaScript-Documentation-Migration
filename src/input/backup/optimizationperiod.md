










 


OptimizationPeriod







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?optimizationperiod.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
OptimizationPeriod | [Previous page](onpositionupdate.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Reserved for [Walk-Forward Optimization](walk_forward_optimize_a_strate.htm), this property determines the number of days used for the "in sample" backtest period for a given strategy.  See also [TestPeriod](testperiod.htm).


 




|  |
| --- |
| Note:  This property should ONLY be called from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults |



 


Property Value
--------------


An int value representing the number of "in sample" days used for walk-forward optimization; Default value is set to 10.


 


Syntax
------


OptimizationPeriod


 



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {         
         //set the default optimization period to 20 days for WFOs
         OptimizationPeriod = 20;
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
 
 
 



