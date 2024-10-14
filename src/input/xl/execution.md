










 


Execution







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?execution.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
Execution | [Previous page](entryhandling.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Represents a read only interface that exposes information regarding an execution (filled order) resulting from an order and is passed as a parameter in the [OnExecutionUpdate()](onexecutionupdate.htm) method.


 




|  |
| --- |
| Note: Not all executions will have associated [Order](order.htm) objects (e.g [ExitOnSessionClose](isexitonsessionclosestrategy.htm) executions or [AtmStrategyCreate()](atmstrategycreate.htm) executions) |



 


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| Account | The [Account](account_class.htm) the execution occurred |
| BarsInProgress | An int value representing the [BarsArray](barsarray.htm) in which the execution occurred |
| Commission | A double value representing the commission of an execution |
| ExecutionId | A string value representing the exchange generated execution id |
| Instrument | An [Instrument](instrument.htm) value representing the instrument of an order |
| MarketPosition | The position of the execution.  
 
Possible values are:
 
•MarketPosition.Long•MarketPosition.Short |
| Name | A string representing the name of an order which can be provided by the entry or exit signal name |
| Order | An [Order](order.htm) value representing an order associated to the execution.  |
| OrderId | A string representing the unique id of the order which was executed |
| Position | An int value represents the current quantity of account position at the time of execution |
| PositionStrategy | An int value represents the current quantity of strategy position at the time of execution  |
| Price | A double value representing the price of an execution |
| Quantity | An int value representing quantity of an execution |
| Rate | A double value representing the exchange rate calculated for non-USD base products (1 if no rate was applied) |
| Slippage | A double value representing the number of ticks calculated between the last trade price and the execution price |
| Time | A [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) structure representing the time the execution occurred |
| ToString() | A string representation of an execution |





Examples
--------




| ns Finding the executions of a particular Order object |
| --- |
| // Example #1
private Order entryOrder = null;
 
protected override void OnBarUpdate()
{
     if (entryOrder == null &amp;&amp; Close[0] &gt; Open[0])
         EnterLong("myEntryOrder");
}
 
protected override void OnExecutionUpdate(Execution execution, string executionId, double price, int quantity, MarketPosition marketPosition, string orderId, DateTime time)
{
   // Assign entryOrder in OnExecutionUpdate() to ensure the assignment occurs when expected.
   // This is more reliable than assigning Order objects in OnBarUpdate, as the assignment is not guaranteed to be complete if it is referenced immediately after submitting
   if (execution.Order.Name == "myEntryOrder" &amp;&amp; execution.Order.OrderState == OrderState.Filled)
       entryOrder = execution.order;
 
     if (entryOrder != null &amp;&amp; entryOrder == execution.Order)
       Print(execution.ToString());
} |



 


 




| ns Generic execution logic not specific to a particular Order object |
| --- |
| // Example #2
protected override void OnExecutionUpdate(Execution execution, string executionId, double price, int quantity, MarketPosition marketPosition, string orderId, DateTime time)
{
     // Remember to check the underlying Order object for null before trying to access its properties
     if (execution.Order != null &amp;&amp; execution.Order.OrderState == OrderState.Filled)
         Print(execution.ToString());
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
 
 
 



