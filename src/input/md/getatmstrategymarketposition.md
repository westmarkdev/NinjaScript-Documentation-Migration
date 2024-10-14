










 


GetAtmStrategyMarketPosition()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getatmstrategymarketposition.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
GetAtmStrategyMarketPosition() | [Previous page](getatmstrategyentryorderstatus.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Gets the current market position of the specified ATM Strategy.


 




|  |
| --- |
| Notes:
 
1. Changes to positions will not be reflected till at least the next [OnBarUpdate()](onbarupdate.htm) event after an order fill.
2. If the ATM Strategy does not exist then MarketPosition.Flat returns 
3. Please note this provides access to the current ATM strategy position, which should not be confused with the NinjaScript strategy position or account position. For more information please see the [Using ATM Strategies](using_atm_strategies.htm) section. |



 


 


Method Return Value
-------------------


MarketPosition.Flat


MarketPosition.Long


MarketPosition.Short



Syntax
------


GetAtmStrategyMarketPosition(string atmStrategyId)



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
     // Check if flat
     if (GetAtmStrategyMarketPosition("id") == MarketPosition.Flat)
         Print("ATM Strategy position is currently flat");
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
 
 
 



