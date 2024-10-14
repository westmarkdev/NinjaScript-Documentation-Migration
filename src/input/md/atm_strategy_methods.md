










 


ATM Strategy Methods







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?atm_strategy_methods.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
ATM Strategy Methods | [Previous page](addperformancemetric.htm)
[Return to chapter overview](strategy.htm)










 


 




|  |
| --- |
| ATM Strategy Methods
From a NinjaScript strategy it is possible to use ATM strategies to manage your positions. Benefit of such an approach is that you can use the NinjaScript strategy to generate automated entry signals and once entered, you can delegate exit management to an ATM strategy which allows you degrees of manual control over how to close out of a trade.
 
For more information please see the [Using ATM Strategies](using_atm_strategies.htm) section. |
| ATM Strategy Management
›[AtmStrategyCancelEntryOrder()](atmstrategycancelentryorder.htm)›[AtmStrategyChangeEntryOrder()](atmstrategychangeentryorder.htm)›[AtmStrategyChangeStopTarget()](atmstrategychangestoptarget.htm)›[AtmStrategyClose()](atmstrategyclose.htm)›[AtmStrategyCreate()](atmstrategycreate.htm) | ATM Strategy Monitoring
›[GetAtmStrategyEntryOrderStatus()](getatmstrategyentryorderstatus.htm)›[GetAtmStrategyMarketPosition()](getatmstrategymarketposition.htm)›[GetAtmStrategyPositionAveragePrice()](getatmstrategypositionaveragep.htm)›[GetAtmStrategyPositionQuantity()](getatmstrategypositionquantity.htm)›[GetAtmStrategyRealizedProfitLoss()](getatmstrategyrealizedprofitlo.htm)›[GetAtmStrategyStopTargetOrderStatus()](getatmstrategystoptargetorders.htm)›[GetAtmStrategyUniqueId()](getatmstrategyuniqueid.htm)›[GetAtmStrategyUnrealizedProfitLoss()](getatmstrategyunrealizedprofit.htm) |






 
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
 
 
 



