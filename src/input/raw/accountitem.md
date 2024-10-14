










 


AccountItem







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?accountitem.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
AccountItem | [Previous page](account_class.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Represents various account variables used to reflect values the status of the account.  Each account connected in NinjaTrader will have it's own unique AccountItem values.





|  |
| --- |
| Tip:  For strategies, see also [OnAccountItemUpdate()](onaccountitemupdate.htm).  For other objects, you can also subscribe to the [AccountItemUpdate](accountitemupdate.htm) stream. |



 


 


Syntax
------


AccountItem


 


Parameters
----------




|  |
| --- |
| AccountItem.BuyingPower |
| AccountItem.CashValue |
| AccountItem.Commission |
| AccountItem.ExcessIntradayMargin |
| AccountItem.ExcessInitialMargin |
| AccountItem.ExcessMaintenanceMargin |
| AccountItem.ExcessPositionMargin |
| AccountItem.Fee |
| AccountItem.GrossRealizedProfitLoss |
| AccountItem.InitialMargin |
| AccountItem.IntradayMargin |
| AccountItem.LongOptionValue |
| AccountItem.LookAheadMaintenanceMargin |
| AccountItem.LongStockValue |
| AccountItem.MaintenanceMargin |
| AccountItem.NetLiquidation |
| AccountItem.NetLiquidationByCurrency |
| AccountItem.PositionMargin |
| AccountItem.RealizedProfitLoss |
| AccountItem.ShortOptionValue |
| AccountItem.ShortStockValue |
| AccountItem.SodCashValue |
| AccountItem.SodLiquidatingValue |
| AccountItem.UnrealizedProfitLoss |
| AccountItem.TotalCashBalance |






 
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
 
 
 



