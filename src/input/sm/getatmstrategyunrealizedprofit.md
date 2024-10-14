










 


GetAtmStrategyUnrealizedProfitLoss()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getatmstrategyunrealizedprofit.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
GetAtmStrategyUnrealizedProfitLoss() | [Previous page](getatmstrategystoptargetorders.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Gets the unrealized profit and loss value of the specified ATM Strategy.



Method Return Value
-------------------


A double value representing the unrealized profit and loss.


 


Syntax
------


GetAtmStrategyUnrealizedProfitLoss(string atmStrategyId)


 



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
     Print("Unrealized PnL is " + GetAtmStrategyUnrealizedProfitLoss("id").ToString());
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
 
 
 



