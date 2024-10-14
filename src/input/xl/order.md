










 


Order







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?order.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
Order | [Previous page](optimizationperiod.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Represents a read only interface that exposes information regarding an order.


 


•An Order object returned from calling an order method is dynamic in that its properties will always reflect the current state of an order 

•The property <order>.OrderId is NOT a unique value, since it can change throughout an order's lifetime.  Please see the [Advance Order Handling](advanced_order_handling.htm) section on "Transitioning order references from historical to live" for details on how to handle.

•The property <order>.Oco WILL be appended with a suffix when the strategy transitions from historical to real-time to ensure the OCO id is unique across multiple strategies for live orders

•To check for equality you can compare Order objects directly

 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| Account | The [Account](account_class.htm) the order resides |
| AverageFillPrice | A double value representing the average fill price of an order |
| Filled | An int value representing the filled amount of an order |
| FromEntrySignal | A string representing the user defined fromEntrySignal parameter on an order |
| Gtd | A [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) structure representing when the order will be canceled |
| HasOverfill | A bool value representing if the order is an overfill. For use when using [Unmanaged orders](unmanaged_approach.htm) and [IgnoreOverFill](ignoreoverfill.htm) |
| Instrument | An [Instrument](instrument.htm) value representing the instrument of an order |
| IsBacktestOrder | A bool that indicates if the order was generated while processing historical data. For use with [GetRealtimeOrder()](getrealtimeorder.htm) when transitioning historical order objects to live order objects when strategies transition to from State.Historical to State.Realtime.  |
| IsLiveUntilCancelled | A bool that when true, indicates the order will be canceled by [managed order handling](managed_approach.htm) at expiration |
| [IsTerminalState()](isterminalstate.htm) | A static method used to determine if the an order's OrderState is in considered terminal and no longer active |
| LimitPrice | A double value representing the limit price of an order |
| LimitPriceChanged | A double value representing the new limit price of an order. Used with [Account.Change()](change.htm) |
| Name | A string representing the name of an order which can be provided by the entry or exit signal name |
| Oco | A string representing the OCO (one cancels other) id of an order |
| OrderAction | Represents the action of the order.  Possible values are:
 
OrderAction.Buy
OrderAction.BuyToCover
OrderAction.Sell
OrderAction.SellShort |
| OrderId | A string representing the broker issued order id value (this value can change) |
| OrderState | The current state of the order.  See the order state values table below |
| OrderType | The type of order submitted.  Possible values are:
OrderType.Limit
OrderType.Market
OrderType.MIT
OrderType.StopMarket
OrderType.StopLimit |
| Quantity | An int value representing the quantity of an order |
| QuantityChanged | An int value representing the new quantity of an order. Used with [Account.Change()](change.htm) |
| StopPrice | A double value representing the stop price of an order |
| StopPriceChanged | A double value representing the new stop price of an order. Used with [Account.Change()](change.htm) |
| Time | A [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) structure representing the last time the order changed state |
| TimeInForce | Determines the life of the order.  Possible values are:
TimeInForce.Day
TimeInForce.Gtc |
| ToString() | A string representation of an order |





OrderState Values
-----------------




|  |  |
| --- | --- |
| OrderState.Initialized | Order is initialized in NinjaTrader |
| OrderState.Submitted | Order is submitted to the broker |
| OrderState.Accepted | Order is accepted by the broker or exchange |
| OrderState.TriggerPending | Order is pending submission  |
| OrderState.Working | Order is working in the exchange queue |
| OrderState.ChangePending | Order change is pending in NinjaTrader |
| OrderState.ChangeSubmitted | Order change is submitted to the broker |
| OrderState.CancelPending | Order cancellation is pending in NinjaTrader |
| OrderState.CancelSubmitted | Order cancellation is submitted to the broker |
| OrderState.Cancelled | Order cancellation is confirmed by the exchange |
| OrderState.Rejected | Order is rejected |
| OrderState.PartFilled | Order is partially filled |
| OrderState.Filled | Order is completely filled |
| OrderState.Unknown | An unknown order state. Default if broker does not report current order state.  |



 




|  |
| --- |
| Critical: In a historical backtest, orders will always reach a "Working" state. In real-time, some stop orders may only reach "Accepted" state if they are simulated/held on a brokers server |



 


Examples
--------




|  |  |
| --- | --- |
| ns |  |
| private Order entryOrder = null;
 
protected override void OnBarUpdate()
{
   if (entryOrder == null &amp;&amp; Close[0] &gt; Open[0])
       EnterLong("myEntryOrder");
}
 
protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
{
   // Assign entryOrder in OnOrderUpdate() to ensure the assignment occurs when expected.
   // This is more reliable than assigning Order objects in OnBarUpdate, as the assignment is not guaranteed to be complete if it is referenced immediately        after submitting
   if (order.Name == "myEntryOrder")
       entryOrder = order;
 
   if (entryOrder != null &amp;&amp; entryOrder == order)
   {
       Print(order.ToString());
       if (order.OrderState == OrderState.Filled)
           entryOrder = null;
   }
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
 
 
 



</order></order>