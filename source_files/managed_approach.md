










 


Managed Approach







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?managed_approach.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order Methods](order_methods.htm) &gt;
Managed Approach | [Previous page](order_methods.htm)
[Return to chapter overview](order_methods.htm)



[Show/Hide Hidden Text](javascript:HMToggleExpandAll(!HMAnyToggleOpen()) "Click to open/close expanding sections")









The Managed approach in NinjaScript is designed to offer the greatest ease of use for beginner to intermediate programmers. The order methods are wrapped in a convenience layer that allows you to focus on your system's trading rules, leaving the underlying mechanics of order management and the relationships between entry orders, exit orders, and positions to NinjaTrader. This approach is best suited for simple to moderate order complexity, and can be further broken down into a Basic/Common Managed approach and a more [Advanced](advanced_order_handling.htm) Managed approach. The following section will discuss the use of the Basic/Common approach.


 


A few key points to keep in mind:


 


•Orders are submitted as live and working when a strategy is running in real-time 

•Profit target, stop loss and trail stop orders are submitted immediately when an entry order is filled, and are tied together via OCO (One Cancels Other)

•Order changes and cancellations are queued in the event that the order is in a state where it can't be cancelled or modified 

•By default, orders submitted via Entry() and Exit() methods automatically cancel at the end of a bar if not re-submitted

•Entry() methods will reverse the position automatically. For example if you are in a 1 contract long position and now call EnterShort() -&gt; you will see 2 executions, one to close the prior long position and the other to get you into the desired 1 contract short position.

 


* Via the [SetProfitTarget()](setprofittarget.htm), [SetStopLoss()](setstoploss.htm), [SetTrailStop()](settrailstop.htm) and [SetParabolicStop](setparabolicstop.htm) methods


 


![tog_minus](tog_minus.gif)        [Order submission for entry and exit methods - basic operation](javascript:HMToggle('toggle','OrderSubmissionForEntryAndExitMethodsBasicOperation','OrderSubmissionForEntryAndExitMethodsBasicOperation_ICON'))




|  |  |  |
| --- | --- | --- |
| Orders are primarily submitted from within the [OnBarUpdate()](onbarupdate.htm) method when a specific order method is called. By default, orders are kept alive, provided they are re-submitted on each call of the OnBarUpdate() method. If an order is not re-submitted, it is then canceled. Orders can be modified by re-submitting them with changed parameters (a new limit price, for example).
 
In the example below, a Buy Limit order is working at the bid price, provided that the Close price of the current bar is greater than the current value of the 20 period Simple Moving Average. If the entry condition is no longer true and the order is still active, it will be immediately canceled.
 


| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Entry condition
     if (Close[0] &gt; SMA(20)[0])
         EnterLongLimit(GetCurrentBid());
} |



 
This technique allows you the quickest and easiest order submission method suitable for programmers of all levels. Should you want to submit an order and not have to keep re-submitting it to keep it alive you can use an [advanced approach](advanced_order_handling.htm) reserved for experienced programmers, which includes an option to keep orders alive until specifically canceled in code. |



![tog_minus](tog_minus.gif)        [Order Entry Methods](javascript:HMToggle('toggle','EntryMethods','EntryMethods_ICON'))




|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Order Entry Methods
Order entry methods are used to submit orders of different types. Methods exist to submit Market, Market-if-Touched, Limit, Stop Market, and Stop Limit orders. See the order-entry method pages listed in the help guide table of contents under this page for more information on a specific method.
 
Signal Names on Entry Methods
You can optionally tag an entry order with a signal name. Signal names are used to identify executions resulting from the order on a chart and in performance reports. Market positions created from a tagged entry method are marked with the signal name which serves two purposes:
 
•Used to tie an exit method to a specific position •Used to identify unique entries in a strategy  
Below is an example of placing an Market entry order and an associated Limit exit order, tied together by the signal name of the entry order.
 


| ns |
| --- |
| protected override void OnBarUpdate()
{
   if (CurrentBar &lt; 1) return;
 
   if (Close[0] &gt; Close[1])
   {
       // Place a Market order to enter long
       EnterLong("longEntry");
 
       // Manually place a Profit Target 10 ticks above the current price, tied to the entry order's SignalName
       ExitLongLimit(Close[0] + (10 * TickSize), "longEntry");
   }
} |



 
 
Defining how Entry Methods are Processed in a Strategy
You can limit how many entry methods are processed by determining the maximum number of entries in a single direction across all entry methods, or across unique signal names. The following properties can be set in the Strategies window when adding a strategy to a chart or to the Strategies tab of the Control Center window.
 
•[EntriesPerDirection](entriesperdirection.htm) property - Sets the maximum number of entries in a single direction •[EntryHandling](entryhandling.htm) property - Determines if EntriesPerDirection applies across all entries or for entries with specified signal names 
The example code below illustrates how the above properties control the processing of entry methods. The code contains two entry conditions and two EnterLong methods, each tagged with unique signal names.
 


| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
       EntriesPerDirection = 1;
       EntryHandling = EntryHandling.AllEntries;
   }
}
 
protected override void OnBarUpdate()
{
   // Entry condition 1
   if (CrossAbove(SMA(10), SMA(20), 1))
       EnterLong("Condition 1 Entry");
 
   // Entry condition 2
   if (CrossAbove(RSI(14, 3), 30, 1))
       EnterLong("Condition 2 Entry");
} |



 
 
Entry Methods on Multi-Instrument Strategies
When running strategies that submit orders to multiple instruments, entry methods will submit orders to the instrument referenced by the [BarsInProgress](barsinprogress.htm). The following example assumes that the strategy is running on a 1 minute E-Mini S&amp;P 500 chart. It adds an NQ data series, then enters a position on both instruments.
 


| ns |
| --- |
| protected override void OnStateChange()
{
     AddDataSeries("NQ 09-14", BarsPeriodType.Minute, 1);
}
 
protected override void OnBarUpdate()
{
     if (BarsInProgress == 0)
         EnterLong("ES Trade");
     else if (BarsInProgress == 1)
         EnterLong("NQ Trade");
} |



 
More information on using BarsInProgress to filter instruments can be found in the [Advanced Order Handling](advanced_order_handling.htm) page. |



![tog_minus](tog_minus.gif)        [Quantity Type and TIF](javascript:HMToggle('toggle','QuantityTypeAndTif','QuantityTypeAndTif_ICON'))




|  |
| --- |
| You can set the entry order quantity and order type directly in code via the following properties:
•QuantityType - Sets the order quantity is taken from the entry method quantity property or the default strategy quantity size•[TimeInForce](timeinforce.htm) propery - Sets the time in force of the order |



![tog_minus](tog_minus.gif)        [How to close a position](javascript:HMToggle('toggle','HowToCloseAPosition','HowToCloseAPosition_ICON'))




|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Closing a Position using a Stop Loss, Trailing Stop and/or Profit Target
You can predefine a stop loss, trailing stop and/or profit target in a strategy by calling the [SetStopLoss()](setstoploss.htm), [SetTrailStop()](settrailstop.htm), [SetParabolicStop()](setparabolicstop.htm) or [SetProfitTarget()](setprofittarget.htm) methods from inside the [OnStateChange()](onstatechange.htm) event handler. When these methods are called, they submit live working orders in real-time as executions are reported as a result of calling an entry method. These orders are also tied via OCO (One Cancels Other).
 
Stop losses and profit target can be generated for each fill or each position. This is determined by the "Stop &amp; target submission" property which is set in the Strategies window. Possible values are listed below:
 
ByStrategyPosition - When this is selected, only one stop loss, trail stop and/or profit target order is submitted. As entry executions come in, the order size is amended. The downside of this approach is that if you receive partial fills, the orders are re-inserted into the exchange order queue. The upside is that if you broker charges you commission per order (not per quantity), you will not incur additional commission expenses.
 
PerEntryExecution - When this is selected, a stop loss, trail stop and/or profit target order is submitted for each partial fill received. The downside is that if your broker charges commission per order, you can incur very expensive commission costs if you receive partial fills. The upside is that orders are submitted as soon as possible, giving you the advantage of getting into the order queue immediately.
 
 
Closing a Position using an Exit Method
Exit methods submit orders to close out a position in whole or in part. When closing a position with Exit orders, the order quantity will be reduced as the strategy position reduces - for example, if we use [ExitLongStopMarket()](exitlongstopmarket.htm) and [ExitLongStopLimit()](exitlongstoplimit.htm) to protect a position and one of those orders gets filled, the other order associated with exiting that position will reduce their quantity. 
 
As with entry methods, more information about specific exit methods can be found in this Help Guide's table of contents, beneath this page.
 
 
Closing a Partial Position using an Exit Method
You can close out a partial position by specifying the exit quantity. The following example first enters long for three contracts. Then, each subsequent bar update submits a market order to exit one contract until the position is completely closed. "ExitLong(1)" will be ignored if a long market position does not exist.
 


| ns |
| --- |
| protected override void OnBarUpdate()
{
     if (CrossAbove(SMA(10), SMA(20), 1))
         EnterLong(3);
 
     ExitLong(1);
} |



 
 
FromEntrySignal -- Using Signal Names in Exit Methods
Identifying entries with a signal name allows you to place multiple unique entries within a single strategy and call exit methods with specified signal names, so that only a position created with the specified signal name is closed. In the example below, there are two entry conditions which create positions, and two exit conditions specifying which position to close based on the signal name.
 


| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Entry condition 1
     if (CrossAbove(SMA(10), SMA(20), 1))
         EnterLong("Condition 1 Entry");
 
     // Entry condition 2
     if (CrossAbove(RSI(14, 3), 30, 1))
         EnterLong("Condition 2 Entry");
 
     // Closes the position created by entry condition 1
     if (CrossBelow(SMA(10), SMA(20), 1))
         ExitLong("Condition 1 Entry");
 
     // Closes the position created by entry condition 2
     if (CrossBelow(RSI(14, 3), 70, 1))
         ExitLong("Condition 2 Entry");
} |



 
 


|  |
| --- |
| Tip:  If you do not specify a "fromEntrySignal" parameter the entire position is exited rendering your strategy flat. |



 
 


| ns |
| --- |
| protected override void OnBarUpdate()
{
 
   if (Position.MarketPosition == MarketPosition.Flat)
   {
     // Entry condition 1
     if (CrossAbove(SMA(10), SMA(20), 1))
         EnterLong("Condition 1 Entry");
   }
 
   if (Position.MarketPosition != MarketPosition.Flat)
   {
     // Scale in condition 2 for position management
     if (CrossAbove(RSI(14, 3), 30, 1))
         EnterLong("Condition 2 Entry");
 
     // Exit all positions using an empty string (could also use string.Empty)
     if (CrossBelow(SMA(10), SMA(20), 1))
         ExitLong("Exit All", "");
 
   }
} |


 |



![tog_minus](tog_minus.gif)        [Understanding core order objects](javascript:HMToggle('toggle','Understandingcoreorderobjects','Understandingcoreorderobjects_ICON'))




|  |
| --- |
| When using order methods such as [EnterLong()](enterlong.htm), [ExitShortLimit()](exitshortlimit.htm), etc, a direct [order object](order.htm) is returned for the NinjaTrader Core.  These objects can be used throughout the lifetime of your strategy to provide additional metadata concerning your strategy, as well as apply advanced concepts such as [CancelOrder()](managed_cancelorder.htm) and [ChangeOrder()](managed_changeorder.htm).  More information about this advanced concept which is discussed under the [Advanced Order Handling](advanced_order_handling.htm) section |



![tog_minus](tog_minus.gif)        [Internal Order Handling Rules that Reduce Unwanted Positions](javascript:HMToggle('toggle','InternalOrderHandlingRulesThatReduceUnwantedPositions','InternalOrderHandlingRulesThatReduceUnwantedPositions_ICON'))




|  |  |  |
| --- | --- | --- |
| To prevent situations in real-time in which you may have multiple orders working to accomplish the same task, there are some "under the hood" rules that a NinjaScript strategy follows when Managed order methods are called. For example, if your strategy had a limit order for 1 contract working as a Profit Target, but then your strategy was also programmed to reverse the position at the price very close to the target limit order, then submitting both orders can be risky, since it could lead to a larger position than the strategy is designed to enter if both orders got filled in quick succession by the exchange. 
 


|  |
| --- |
| Note: These rules do not apply to market orders, such as ExitLong() or ExitShort().  |



 
For the most part, you do not need to be intimately familiar with these rules as you develop your strategies. It is all taken care of for you internally within a strategy. If a rule is violated, you will be notified through an error log in the Control Center Log tab.
 


|  |
| --- |
| Note:  To prevent excessive logging which could degrade performance, you will only be notified of the very first order which has violated an order handling rule. Subsequent orders which violate a rule will not be notified through the error log. |



 
The following rules are true per unique signal name:
 
Methods that generate orders to enter a position will be ignored if:
•A position is open and an order submitted by a non market order exit method ([ExitLongLimit()](exitlonglimit.htm) for example) is active and the order is used to open a position in the opposite direction•A position is open and an order submitted by a set method ([SetStopLoss()](setstoploss.htm) for example) is active and the order is used to open a position in the opposite direction•A position is open and two or more Entry methods to reverse the position are entered together. In this case the second Entry order will be ignored.•The strategy position is flat and an order submitted by an enter method ([EnterLongLimit()](enterlonglimit.htm) for example) is active and the order is used to open a position in the opposite direction•The entry signal name is not unique 
Methods that generate orders to exit a position will be ignored if:
•A position is open and an order submitted by an enter method ([EnterLongLimit()](enterlonglimit.htm) for example) is active and the order is used to open a position in the opposite direction•A position is open and an order submitted by a set method ([SetStopLoss()](setstoploss.htm) for example) is active 
Set() methods that generate orders to exit a position will be ignored if:
•A position is open and an order submitted by an enter method ([EnterLongLimit()](enterlonglimit.htm) for example) is active and the order is used to open a position in the opposite direction•A position is open and an order submitted by a non market order exit method ([ExitLongLimit()](exitlonglimit.htm) for example) is active |



 


 


 




|  |  |
| --- | --- |
| [Advanced Order Handling](advanced_order_handling.htm) | Through advanced order handling you can submit, change and cancel orders at your discretion through any event-driven method within a strategy. |
| [CancelOrder()](managed_cancelorder.htm) | Cancels a specified order. |
| [ChangeOrder()](managed_changeorder.htm) | Amends a specified [Order](order.htm). |
| [EnterLong()](enterlong.htm) | Generates a buy market order to enter a long position. |
| [EnterLongLimit()](enterlonglimit.htm) | Generates a buy limit order to enter a long position. |
| [EnterLongMIT()](enterlongmit.htm) | Generates a buy MIT order to enter a long position. |
| [EnterLongStopLimit()](enterlongstoplimit.htm) | Generates a buy stop limit order to enter a long position. |
| [EnterLongStopMarket()](enterlongstopmarket.htm) | Generates a buy stop market order to enter a long position. |
| [EnterShort()](entershort.htm) | Generates a sell short market order to enter a short position. |
| [EnterShortLimit()](entershortlimit.htm) | Generates a sell short stop limit order to enter a short position. |
| [EnterShortMIT()](entershortmit.htm) | Generates a sell MIT order to enter a short position. |
| [EnterShortStopLimit()](entershortstoplimit.htm) | Generates a sell short stop limit order to enter a short position. |
| [EnterShortStopMarket()](entershortstopmarket.htm) | Generates a sell short stop order to enter a short position. |
| [ExitLong()](exitlong.htm) | Generates a sell market order to exit a long position. |
| [ExitLongLimit()](exitlonglimit.htm) | Generates a sell limit order to exit a long position. |
| [ExitLongMIT()](exitlongmit.htm) | Generates a sell MIT order to exit a long position. |
| [ExitLongStopLimit()](exitlongstoplimit.htm) | Generates a sell stop limit order to exit a long position. |
| [ExitLongStopMarket()](exitlongstopmarket.htm) | Generates a sell stop market order to exit a long position. |
| [ExitShort()](exitshort.htm) | Generates a buy to cover market order to exit a short position. |
| [ExitShortLimit()](exitshortlimit.htm) | Generates a buy to cover limit order to exit a short position. |
| [ExitShortMIT()](exitshortmit.htm) | Generates a buy to cover MIT order to exit a short position. |
| [ExitShortStopLimit()](exitshortstoplimit.htm) | Generates a buy to cover stop limit order to exit a short position. |
| [ExitShortStopMarket()](exitshortstopmarket.htm) | Generates a buy to cover stop market order to exit a short position. |
| [GetRealtimeOrder()](getrealtimeorder.htm) | Returns a matching real-time order object based on a specified historical order object reference. |
| [SetParabolicStop()](setparabolicstop.htm) | Generates a parabolic type trail stop order with the signal name "Parabolic stop" to exit a position. |
| [SetProfitTarget()](setprofittarget.htm) | Generates a profit target order with the signal name "Profit target" to exit a position. |
| [SetStopLoss()](setstoploss.htm) | Generates a stop loss order with the signal name "Stop loss" used to exit a position. |
| [SetTrailStop()](settrailstop.htm) | Generates a trail stop order with the signal name "Trail stop" to exit a position. |






 
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
 
 
 


HMInitToggle('OrderSubmissionForEntryAndExitMethodsBasicOperation\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'OrderSubmissionForEntryAndExitMethodsBasicOperation\',\'OrderSubmissionForEntryAndExitMethodsBasicOperation\_ICON\')');
HMInitToggle('OrderSubmissionForEntryAndExitMethodsBasicOperation','hm.type','dropdown','hm.state','0');
HMInitToggle('EntryMethods\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'EntryMethods\',\'EntryMethods\_ICON\')');
HMInitToggle('EntryMethods','hm.type','dropdown','hm.state','0');
HMInitToggle('QuantityTypeAndTif\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'QuantityTypeAndTif\',\'QuantityTypeAndTif\_ICON\')');
HMInitToggle('QuantityTypeAndTif','hm.type','dropdown','hm.state','0');
HMInitToggle('HowToCloseAPosition\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'HowToCloseAPosition\',\'HowToCloseAPosition\_ICON\')');
HMInitToggle('HowToCloseAPosition','hm.type','dropdown','hm.state','0');
HMInitToggle('Understandingcoreorderobjects\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'Understandingcoreorderobjects\',\'Understandingcoreorderobjects\_ICON\')');
HMInitToggle('Understandingcoreorderobjects','hm.type','dropdown','hm.state','0');
HMInitToggle('InternalOrderHandlingRulesThatReduceUnwantedPositions\_ICON','hm.type','dropdown','hm.state','0','hm.src0','tog\_plus.gif','hm.src1','tog\_minus.gif','onclick','HMToggle(\'toggle\',\'InternalOrderHandlingRulesThatReduceUnwantedPositions\',\'InternalOrderHandlingRulesThatReduceUnwantedPositions\_ICON\')');
HMInitToggle('InternalOrderHandlingRulesThatReduceUnwantedPositions','hm.type','dropdown','hm.state','0');



