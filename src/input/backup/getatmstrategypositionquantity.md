










 


GetAtmStrategyPositionQuantity()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getatmstrategypositionquantity.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
GetAtmStrategyPositionQuantity() | [Previous page](getatmstrategypositionaveragep.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Gets the current position quantity of the specified ATM Strategy.


 




|  |
| --- |
| Note:  Changes to positions will not be reflected till at least the next [OnBarUpdate()](onbarupdate.htm) event after an order fill. |



 


Method Return Value
-------------------


An int value representing the quantity.


 


Syntax
------


GetAtmStrategyPositionQuantity(string atmStrategyId)


 



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
     if (GetAtmStrategyMarketPosition("idValue") != MarketPosition.Flat)
         Print("Position size is " + GetAtmStrategyPositionQuantity("id").ToString());
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
 
 
 



