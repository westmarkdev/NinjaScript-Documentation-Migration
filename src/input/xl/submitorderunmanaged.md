










 


SubmitOrderUnmanaged()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?submitorderunmanaged.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order Methods](order_methods.htm) &gt; [Unmanaged Approach](unmanaged_approach.htm) &gt;
SubmitOrderUnmanaged() | [Previous page](isunmanaged.htm)
[Return to chapter overview](unmanaged_approach.htm)










Definition
----------


Generates an [Unmanaged](isunmanaged.htm) order.


 


Method Return Value
-------------------


An [Order](order.htm) read-only object that represents the order. Reserved for experienced programmers, additional information can be found within the [Unmanaged Approach](unmanaged_approach.htm) section.



Syntax
------


SubmitOrderUnmanaged(int selectedBarsInProgress, OrderAction orderAction, OrderType orderType, int quantity)  

SubmitOrderUnmanaged(int selectedBarsInProgress, OrderAction orderAction, OrderType orderType, int quantity, double limitPrice)  

SubmitOrderUnmanaged(int selectedBarsInProgress, OrderAction orderAction, OrderType orderType, int quantity, double limitPrice, double stopPrice)  

SubmitOrderUnmanaged(int selectedBarsInProgress, OrderAction orderAction, OrderType orderType, int quantity, double limitPrice, double stopPrice, string oco)  

SubmitOrderUnmanaged(int selectedBarsInProgress, OrderAction orderAction, OrderType orderType, int quantity, double limitPrice, double stopPrice, string oco, string signalName)


 


 


Parameters
----------




|  |  |
| --- | --- |
| selectedBarsInProgress | The index of the Bars object the order is to be submitted against. This determines what instrument the order is submitted for.
 
Note:  See the [BarsInProgress](barsinprogress.htm) property.  |
| orderAction | Determines if the order is a buy or sell order
 
Possible values:
 
OrderAction.Buy
OrderAction.BuyToCover
OrderAction.Sell
OrderAction.SellShort |
| orderType | Determines the type of order submitted 
 
Possible values:
 
OrderType.Limit
OrderType.Market
OrderType.MIT
OrderType.StopMarket
OrderType.StopLimit |
| quantity | Sets the number of contracts to submit with the order |
| limitPrice | Order limit price. Use "0" should this parameter be irrelevant for the OrderType being submitted. |
| stopPrice | Order stop price. Use "0" should this parameter be irrelevant for the OrderType being submitted. |
| oco | A string representing the OCO ID used to link OCO orders together 
 
Note:  OCO strings should not be reused.  Use unique strings for each OCO group, and reset after orders in that group are filled/canceled |
| signalName | A string representing the name of the order. Max 50 characters. |



 


 


Examples
--------




| ns |
| --- |
| private Order entryOrder = null;
 
protected override void OnBarUpdate()
{
     // Entry condition
     if (Close[0] &gt; SMA(20)[0] &amp;&amp; entryOrder == null)
         SubmitOrderUnmanaged(0, OrderAction.Buy, OrderType.Market, 1, 0, 0, "", "Enter Long");
}
 
protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError)
{
   // Assign entryOrder in OnOrderUpdate() to ensure the assignment occurs when expected.
   // This is more reliable than assigning Order objects in OnBarUpdate, as the assignment is not gauranteed to be complete if it is referenced immediately after submitting
   if (order.Name == "Enter Long" &amp;&amp; orderState == OrderState.Filled)
       entryOrder = order;
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
 
 
 



