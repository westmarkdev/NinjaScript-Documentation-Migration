










 


GetRealtimeOrder()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getrealtimeorder.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order Methods](order_methods.htm) &gt; [Managed Approach](managed_approach.htm) &gt;
GetRealtimeOrder() | [Previous page](exitshortstopmarket.htm)
[Return to chapter overview](managed_approach.htm)










Definition
----------


Returns a matching real-time order object based on a specified historical order object reference.


 




|  |
| --- |
| Note:  This method is only needed if you have historical order references which you wish to transition and manage in real-time (i.e., you had a working order which was submitted historically and re-submitted in real-time as the strategy is enabled). This method only needs to be called once per order object, and should be done in OnOrderUpdate to handle all scenarios.  Please see the [Advanced Order Handling](advanced_order_handling.htm) section on transition orders for more details. |



 


 


Method Return Value
-------------------


Returns a real-time [order](order.htm) reference associated with the historical order object.  If no associated order exists (i.e. OrderState is Filled, Canceled, Rejected, Unknown), a null value returns


 


Syntax  

GetRealtimeOrder(Order historicalOrder)


 


Parameters
----------




|  |  |
| --- | --- |
| historicalOrder | The historical [order](order.htm) object to update to real-time |





Examples
--------




| ns |   |
| --- | --- |
| private Order myOrder;
 
protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
{
   // One time only, as we transition from historical
   // Convert any old historical order object references to the live order submitted to the real-time account
   if (myOrder != null &amp;&amp; myOrder.IsBacktestOrder &amp;&amp; State == State.Realtime)
       myOrder = GetRealtimeOrder(myOrder);
 
   // Assign Order objects here
   // This is more reliable than assigning Order objects in OnBarUpdate, as the assignment is not guaranteed to be complete if it is referenced immediately after submitting
   if (order.Name == "myOrder Signal Name")
       myOrder = order;
 
   // Null Entry order if filled or cancelled. We do not use the Order objects after the order is filled, so we can null it here
   if (myOrder != null &amp;&amp; myOrder == order)
    {
       if (order.OrderState == OrderState.Cancelled &amp;&amp; order.Filled == 0)
           myOrder = null;
       if (order.OrderState == OrderState.Filled)
           myOrder = null;
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
 
 
 



