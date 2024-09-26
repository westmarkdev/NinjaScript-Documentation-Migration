










 


Order Methods







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?order_methods.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
Order Methods | [Previous page](isterminalstate.htm)
[Return to chapter overview](strategy.htm)










 




|  |
| --- |
| Note: You will not be able to mix and match the two approaches. If you decide to go with the Managed approach you will only be able to use the Managed order methods. If you decide to go with the Unmanaged approach you will only be able to use the Unmanaged order methods. |



 




|  |
| --- |
| Order Methods Overview
NinjaScript provides several approaches you can use for order placement within your NinjaScript strategy. The main approaches can be categorized as a Managed approach and an Unmanaged approach. |
| Managed
The Managed approach offers you order methods that are wrapped with an invisible convenience layer that allows you to focus on your system's trading rules leaving the underlying mechanics of order management and the relationships between entry and exit orders and positions to NinjaTrader. The cost for having the convenience layer is that there are [order handling rules](managed_approach.htm) that must be followed to prevent order errors.
 
›[Understanding the Managed approach](managed_approach.htm)›[Advanced Order Handling](advanced_order_handling.htm)›[CancelOrder()](managed_cancelorder.htm)›[EnterLong()](enterlong.htm)›[EnterLongLimit()](enterlonglimit.htm)›[EnterLongMIT()](enterlongmit.htm)›[EnterLongStopMarket()](enterlongstopmarket.htm)›[EnterLongStopLimit()](enterlongstoplimit.htm)›[EnterShort()](entershort.htm)›[EnterShortLimit()](entershortlimit.htm)›[EnterShortMIT()](entershortmit.htm)›[EnterShortStopMarket()](entershortstopmarket.htm)›[EnterShortStopLimit()](entershortstoplimit.htm)›[ExitLong()](exitlong.htm)›[ExitLongLimit()](exitlonglimit.htm)›[ExitLongMIT()](exitlongmit.htm)›[ExitLongStopMarket()](exitlongstopmarket.htm)›[ExitLongStopLimit()](exitlongstoplimit.htm)›[ExitShort()](exitshort.htm)›[ExitShortLimit()](exitshortlimit.htm)›[ExitShortMIT()](exitshortmit.htm)›[ExitShortStopMarket()](exitshortstopmarket.htm)›[ExitShortStopLimit()](exitshortstoplimit.htm)›[GetRealtimeOrder()](getrealtimeorder.htm)›[SetProfitTarget()](setprofittarget.htm)›[SetStopLoss()](setstoploss.htm)›[SetTrailStop()](settrailstop.htm)›[SetParabolicStop()](setparabolicstop.htm) | Unmanaged
The Unmanaged approach offers you more flexible order methods without the convenience layer. This means you are not restricted to any order handling rules besides those imposed by the brokerage/exchange. With such flexibility though, you will have to ensure to program your strategy to handle any and all issues that may arise with placing orders.
 
›[Understanding the Unmanaged approach](unmanaged_approach.htm)›[CancelOrder()](unmanaged_cancelorder.htm)›[ChangeOrder()](managed_changeorder.htm)›[GetRealtimeOrder()](getrealtimeorder.htm)›[IgnoreOverfill](ignoreoverfill.htm)›[IsUnmanaged](isunmanaged.htm)›[SubmitOrderUnmanaged()](submitorderunmanaged.htm) |



 


 





 
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
 
 
 



