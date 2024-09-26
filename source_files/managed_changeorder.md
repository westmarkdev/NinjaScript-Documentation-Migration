










 


ChangeOrder()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?managed_changeorder.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order Methods](order_methods.htm) &gt; [Managed Approach](managed_approach.htm) &gt;
ChangeOrder() | [Previous page](managed_cancelorder.htm)
[Return to chapter overview](managed_approach.htm)










Definition
----------


Amends a specified [Order](order.htm).


 




|  |
| --- |
| Note: This method is only relevant for Managed orders with IsLiveUntilCancelled set to true and Unmanaged orders. |



 


 


Syntax
------


ChangeOrder(Order order, int quantity, double limitPrice, double stopPrice)


 




|  |
| --- |
| Warning:  If you have existing historical [order](order.htm) references which have transitioned to real-time, you MUST update the order object reference to the newly submitted real-time order; otherwise errors may occur as you attempt to change the order.  You may use the [GetRealtimeOrder()](getrealtimeorder.htm) helper method to assist in this transition. |



 


 


Parameters
----------




|  |  |
| --- | --- |
| order | [Order object](order.htm) of the order you wish to amend |
| quantity | Order quantity |
| limitPrice | Order limit price. Use "0" should this parameter be irrelevant for the OrderType being submitted. |
| stopPrice | Order stop price. Use "0" should this parameter be irrelevant for the OrderType being submitted. |



 



Examples
--------




| ns |
| --- |
| private Order stopOrder = null;
 
protected override void OnBarUpdate()
{
     // Raise stop loss to breakeven when you are at least 4 ticks in profit
     if (stopOrder != null &amp;&amp; stopOrder.StopPrice &lt; Position.AveragePrice &amp;&amp; Close[0] &gt;= Position.AveragePrice + 4 * TickSize)
         ChangeOrder(stopOrder, stopOrder.Quantity, 0, Position.AveragePrice);
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
 
 
 



