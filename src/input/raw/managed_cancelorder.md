










 


CancelOrder()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?managed_cancelorder.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order Methods](order_methods.htm) &gt; [Managed Approach](managed_approach.htm) &gt;
CancelOrder() | [Previous page](advanced_order_handling.htm)
[Return to chapter overview](managed_approach.htm)










Definition
----------


Cancels a specified order.  This method is reserved for experienced programmers that fully understanding the concepts of advanced order handling.


 




|  |
| --- |
| Notes:
1.This method sends a cancel request to the broker and does not guarantee that an order is completely cancelled. Most of the time you can expect your order to come back 100% cancelled. 2.An order can be completely filled or part filled in the time that you send the cancel request and the time the exchange receives the request. Check the [OnOrderUpdate()](onorderupdate.htm) method for the state of an order you attempted to cancelled.  |



 


 


Syntax
CancelOrder(Order order)
-------------------------------





|  |
| --- |
| Warning:  If you have existing historical [order](order.htm) references which have transitioned to real-time, you MUST update the order object reference to the newly submitted real-time order; otherwise errors may occur as you attempt to cancel the order.  You may use the [GetRealtimeOrder()](getrealtimeorder.htm) helper method to assist in this transition. |



 


 


Parameters
----------




|  |  |
| --- | --- |
| order | An [Order](order.htm) object representing the order you wish to cancel. |



 



Examples
--------




| ns |
| --- |
| private Order myEntryOrder = null;
private int barNumberOfOrder = 0;
 
protected override void OnBarUpdate()
{
   // Submit an entry order at the low of a bar
   if (myEntryOrder == null)
   {
       // use 'live until canceled' limit order to prevent default managed order handling which would expire at end of bar
       EnterLongLimit(0, true, 1, Low[0], "Long Entry");
       barNumberOfOrder = CurrentBar;
   }
 
   // If more than 5 bars has elapsed, cancel the entry order
   if (CurrentBar &gt; barNumberOfOrder + 5)
       CancelOrder(myEntryOrder);
}
 
protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled,
   double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
{
   // Assign entryOrder in OnOrderUpdate() to ensure the assignment occurs when expected.
   // This is more reliable than assigning Order objects in OnBarUpdate, as the assignment is not gauranteed to be complete if it is referenced immediately after submitting
   if (order.Name == "Long Entry")
       myEntryOrder = order;
 
   // Evaluates for all updates to myEntryOrder.
   if (myEntryOrder != null &amp;&amp; myEntryOrder == order)
   {
       // Check if myEntryOrder is cancelled.
       if (myEntryOrder.OrderState == OrderState.Cancelled)
       {
           // Reset myEntryOrder back to null
           myEntryOrder = null;
       }
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
 
 
 



