










 


AtmStrategyClose()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?atmstrategyclose.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
AtmStrategyClose() | [Previous page](atmstrategychangestoptarget.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Cancels any working orders and closes any open position of a strategy using the default [ATM strategy close behavior](closing_a_position_or_atm_stra.htm).


 


Method Return Value
-------------------


Returns true if the specified ATM strategy was found; otherwise false. 


 




|  |
| --- |
| Note:  A method return value of true in NO WAY indicates that the strategy in fact is closed. It indicates that the the specified ATM strategy was found and the internal close routine was triggered. |



 


 


Syntax
------


AtmStrategyClose(string atmStrategyId)



Parameters
----------




|  |  |
| --- | --- |
| atmStrategyId | The unique identifier for the ATM strategy |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Check for valid condition and create an ATM Strategy
     if (GetAtmStrategyUnrealizedProfitLoss("idValue") &gt; 500)
         AtmStrategyClose("idValue");
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
 
 
 



