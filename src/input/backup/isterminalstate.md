










 


IsTerminalState()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isterminalstate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order](order.htm) &gt;
IsTerminalState() | [Previous page](order.htm)
[Return to chapter overview](order.htm)










Definition
----------


A static method used to determine if the an order's OrderState is considered terminal and no longer active.


 




|  |
| --- |
| Note:  This is a static method and is compared against an order state, NOT the order itself.  Please see the example below for correct syntax an usage. |



 


 


Method Return Value
-------------------


A bool value which will return true when an OrderState is equal to OrderState.Cancelled, OrderState.Filled, OrderState.Rejected, OrderState.Unknown; otherwise false.


 


Syntax
------


IsTerminalState(OrderState orderState)


 
Parameters
------------




|  |  |
| --- | --- |
| orderState | The OrderState to compare |




 


Examples
--------




| ns |
| --- |
| private Order entryOrder = null;
 
protected override void OnBarUpdate()
{
   // submit order under valid condition
   // note that the order assignment and handling is done in OnOrderUpdate()
   if (entryOrder == null &amp;&amp; Close[0] &gt; Open[0])
     EnterLongLimit(Close[0] - 1, "myEntryOrder");
}
 
protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
{
   // assign incoming order
   if (entryOrder == null)
   {
     // check that order matches by signal name, that order is not in terminal state
     if (order.Name == "myEntryOrder" &amp;&amp; !Order.IsTerminalState(order.OrderState))
         entryOrder = order;
   }
 
   if (entryOrder != null &amp;&amp; entryOrder == order)
   {
     // set "entryOrder" to null if it is Cancelled, Filled, Rejected, Unknown
     if (Order.IsTerminalState(entryOrder.OrderState))
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
 
 
 



