










 


AtmStrategyChangeStopTarget()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?atmstrategychangestoptarget.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
AtmStrategyChangeStopTarget() | [Previous page](atmstrategychangeentryorder.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Changes the price of the specified order of the specified ATM strategy.


 


Method Return Value
-------------------


Returns true if the specified order was found; otherwise false.



Syntax
------


AtmStrategyChangeStopTarget(double limitPrice, double stopPrice, string orderName, string atmStrategyId)



Parameters
----------




|  |  |
| --- | --- |
| limitPrice | Order limit price |
| stopPrice | Order stop price |
| orderName | The order name such as "Stop1" or "Target2" |
| atmStrategyId | The unique identifier for the ATM strategy |



 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     AtmStrategyChangeStopTarget(0, SMA(10)[0], "Stop1", "AtmIdValue");
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
 
 
 



