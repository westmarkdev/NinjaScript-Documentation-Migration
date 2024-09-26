










 


EnterLongStopMarket()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?enterlongstopmarket.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order Methods](order_methods.htm) &gt; [Managed Approach](managed_approach.htm) &gt;
EnterLongStopMarket() | [Previous page](enterlongstoplimit.htm)
[Return to chapter overview](managed_approach.htm)










Definition
----------


Generates a buy stop market order to enter a long position.


 


Method Return Value
-------------------


An [Order](order.htm) read-only object that represents the order. Reserved for experienced programmers, additional information can be found within the [Advanced Order Handling](advanced_order_handling.htm) section.   

 


Syntax  

EnterLongStopMarket(double stopPrice)   

EnterLongStopMarket(double stopPrice, string signalName)


EnterLongStopMarket(int quantity, double stopPrice)


EnterLongStopMarket(int quantity, double stopPrice, string signalName)


 


The following method variation is for experienced programmers who fully understand [Advanced Order Handling](advanced_order_handling.htm) concepts:


 


EnterLongStopMarket(int barsInProgressIndex, bool isLiveUntilCancelled, int quantity, double stopPrice, string signalName) 


 





|  |
| --- |
| Note: If using a method signature that does not have the parameter quantity, the order quantity will be taken from the quantity value set in the strategy dialog window when running or backtesting a strategy  |





Parameters
----------




|  |  |
| --- | --- |
| signalName | User defined signal name identifying the order generated. Max 50 characters. |
| stopPrice | The stop price of the order. |
| quantity | Entry order quantity (if 0 is passed in, will be set to 1, except for stocks 100). |
| isLiveUntilCancelled | The order will NOT expire at the end of a bar, but instead remain live until the [CancelOrder()](managed_cancelorder.htm) method is called or its time in force is reached. |
| barsInProgressIndex | The index of the Bars object the order is to be submitted against. Used to determines what instrument the order is submitted for.
 
 
 See the [BarsInProgress](barsinprogress.htm) property. |





Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     if (CurrentBar &lt; 20)
         return;
 
     // Only enter if at least 10 bars has passed since our last entry
     if ((BarsSinceEntryExecution() &gt; 10 || BarsSinceEntryExecution() == -1) &amp;&amp; CrossAbove(SMA(10), SMA(20), 1))
         EnterLongStopMarket(GetCurrentAsk() + TickSize, "SMA Cross Entry");
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
 
 
 



