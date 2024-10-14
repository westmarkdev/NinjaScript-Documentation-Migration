










 


AtmStrategyChangeEntryOrder()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?atmstrategychangeentryorder.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
AtmStrategyChangeEntryOrder() | [Previous page](atmstrategycancelentryorder.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Changes the price of the specified entry order.


 


Method Return Value
-------------------


Returns true if the specified order was found; otherwise false.


 


Syntax
------


AtmStrategyChangeEntryOrder(double limitPrice, double stopPrice, string orderId)


 



Parameters
----------




|  |  |
| --- | --- |
| limitPrice | Order limit price |
| stopPrice | Order stop price |
| orderId | The unique identifier for the entry order |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     AtmStrategyChangeEntryOrder(GetCurrentBid(), 0, "orderIdValue");
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
 
 
 



