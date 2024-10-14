










 


CreateOrder()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?createorder.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [Account](account_class.htm) &gt;
CreateOrder() | [Previous page](connectoptions.htm)
[Return to chapter overview](account_class.htm)










Definition
----------


Creates an [Order](order.htm) to be submitted via [Submit()](submit.htm).


 


Syntax
------


CreateOrder(Instrument instrument, OrderAction action, OrderType orderType, OrderEntry orderEntry, TimeInForce timeInForce, int quantity, double limitPrice, double stopPrice, string oco, string name, DateTime gtd, CustomOrder customOrder)


 


 


Parameters
----------




|  |  |
| --- | --- |
| instrument | Order instrument |
| orderAction | Possible values:
 
OrderAction.Buy
OrderAction.BuyToCover
OrderAction.Sell
OrderAction.SellShort |
| orderType | Possible values:
 
OrderType.Limit
OrderType.Market
OrderType.MIT
OrderType.StopMarket
OrderType.StopLimit |
| orderEntry | Possible values:
 
OrderEntry.Automated
OrderEntry.Manual
 
Allows setting the tag for orders submitted manually or via automated trading logic (CME tag 1028). |
| timeInForce | Possible values:
 
TimeInForce.Day
TimeInForce.Gtc
TimeInForce.Gtd
TimeInForce.Ioc
TimeInForce.Opg |
| quantity | Order quantity |
| limitPrice | Order limit price. Use "0" should this parameter be irrelevant for the OrderType being submitted. |
| stopPrice | Order stop price. Use "0" should this parameter be irrelevant for the OrderType being submitted. |
| oco | A string representing the OCO ID used to link OCO orders together |
| name | A string representing the name of the order. Max 50 characters.  
 
Note:  If using ATM Strategy [StartAtmStrategy()](startatmstrategy.htm), this value MUST be "Entry" |
| gtd | A DateTime value to be used with TimeInForce.Gtd - for all other cases you can pass in Core.Globals.MaxDate |
| customOrder | Custom order if it is being used |



 


 



Examples
--------




| ns |
| --- |
| Order stopOrder;
stopOrder = myAccount.CreateOrder(myInstrument, OrderAction.Sell, OrderType.StopMarket, OrderEntry.Automated, TimeInForce.Day, 1, 0, 1400, "myOCO", "stopOrder", Core.Globals.MaxDate, null);
 
myAccount.Submit(new[] { stopOrder }); |






 
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
 
 
 



