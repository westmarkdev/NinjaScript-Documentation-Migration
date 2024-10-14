










 


OnExecutionUpdate()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onexecutionupdate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
OnExecutionUpdate() | [Previous page](accountitemeventargs.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


An event driven method which is called on an incoming execution of an order managed by a strategy. An execution is another name for a fill of an order.


 


•An order can generate multiple executions (partial fills)

•OnExecutionUpdate is typically called after [OnOrderUpdate()](onorderupdate.htm) is called 

•Only orders which have been submitted and managed by the strategy will call OnExecutionUpdate()

•Executions drive the strategy [Position](position.htm) object, which is updated when this method is called

 




|  |
| --- |
| Notes:  
•Programming in this environment is reserved for the more [advanced user](advanced_order_handling.htm). If you are for example looking to protect a strategy managed position with a basic stop and target, then the [Set() methods](managed_approach.htm) would be more convenient.•When connected to the Playback connection, it is possible for OnExecutionUpdate() to trigger in the middle of a call to OnBarUpdate(). The Sim101 account adds a simulated random delay for processing execution events, but the Playback connection triggers executions immediately, for the sake of consistency in backtesting. Because of this, OnExecutionUpdate() can appear to be triggered earlier than it would in live trading, or when simulation trading on a live connection.•Please also review [Multi-Thread Considerations for NinjaScript](multi-threading.htm)•Its best practice to only work with the passed by value parameters and not reference parameters. This insures that you process each change of the underlying state. •Rithmic and Interactive Brokers Users: When using a NinjaScript strategy it is best practice to only work with passed by value data from OnExecutionUpdate(). Instances of multiple fills at the same time for the same instrument might result in an incorrect OnPositionUpdate, as sequence of events are not guaranteed due to provider API design.  |



 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
You must override the method in your strategy with the following syntax:
-------------------------------------------------------------------------------


 


protected override void OnExecutionUpdate(Execution execution, string executionId, double price, int quantity, MarketPosition marketPosition, string orderId, DateTime time)  

{ 


   

}


 


Parameters
----------




|  |  |
| --- | --- |
| execution | An [Execution](execution.htm) object passed by reference representing the execution |
| executionId | A string value representing the execution id |
| price | A double value representing the execution price |
| quantity | An int value representing the execution quantity |
| marketPosition | A [MarketPosition](position_marketposition.htm) object representing the position of the execution.  Possible values are:
•MarketPosition.Long•MarketPosition.Short |
| orderId | A string representing the order id |
| time | A [DateTime](http://msdn.microsoft.com/en-us/library/system.datetime.aspx) value representing the time of the execution |



 


 


 




| ns OnExecutionUpdate Example (See [SampleOnOrderUpdate](using_onorderupdate_and_onexec.htm) for complete example) |
| --- |
| private Order entryOrder = null; // This variable holds an object representing our entry order
private Order stopOrder = null; // This variable holds an object representing our stop loss order
private Order targetOrder = null; // This variable holds an object representing our profit target order
private int sumFilled = 0; // This variable tracks the quantities of each execution making up the entry order
 
protected override void OnExecutionUpdate(Execution execution, string executionId, double price, int quantity, MarketPosition marketPosition, string orderId, DateTime time)
{
   /* We advise monitoring OnExecutionUpdate() to trigger submission of stop/target orders instead of OnOrderUpdate() since OnExecution() is called after OnOrderUpdate()
 which ensures your strategy has received the execution which is used for internal signal tracking. */
   if (entryOrder != null &amp;&amp; entryOrder == execution.Order)
    {
       if (execution.Order.OrderState == OrderState.Filled || execution.Order.OrderState == OrderState.PartFilled || (execution.Order.OrderState == OrderState.Cancelled &amp;&amp; execution.Order.Filled &gt; 0))
        {
           // We sum the quantities of each execution making up the entry order
            sumFilled += execution.Quantity;
 
           // Submit exit orders for partial fills
           if (execution.Order.OrderState == OrderState.PartFilled)
            {
                stopOrder = ExitLongStopMarket(0, true, execution.Order.Filled, execution.Order.AverageFillPrice - 4 * TickSize, "MyStop", "MyEntry");
                targetOrder = ExitLongLimit(0, true, execution.Order.Filled, execution.Order.AverageFillPrice + 8 * TickSize, "MyTarget", "MyEntry");
            }
           // Update our exit order quantities once orderstate turns to filled and we have seen execution quantities match order quantities
           else if (execution.Order.OrderState == OrderState.Filled &amp;&amp; sumFilled == execution.Order.Filled)
            {
               // Stop-Loss order for OrderState.Filled
                stopOrder = ExitLongStopMarket(0, true, execution.Order.Filled, execution.Order.AverageFillPrice - 4 * TickSize, "MyStop", "MyEntry");
                targetOrder = ExitLongLimit(0, true, execution.Order.Filled, execution.Order.AverageFillPrice + 8 * TickSize, "MyTarget", "MyEntry");
            }
 
           // Resets the entryOrder object and the sumFilled counter to null / 0 after the order has been filled
           if (execution.Order.OrderState != OrderState.PartFilled &amp;&amp; sumFilled == execution.Order.Filled)
            {
                entryOrder = null;
                sumFilled = 0;
            }
        }
    }
 
   // Reset our stop order and target orders' Order objects after our position is closed. (1st Entry)
   if ((stopOrder != null &amp;&amp; stopOrder == execution.Order) || (targetOrder != null &amp;&amp; targetOrder == execution.Order))
    {
       if (execution.Order.OrderState == OrderState.Filled || execution.Order.OrderState == OrderState.PartFilled)
        {
            stopOrder = null;
            targetOrder = null;
        }
    }
} |



 


 




| ns Using Execution information to calculate Average Entry Price (Rithmic/Interactive Brokers Friendly Approach) |
| --- |
| private Order targetLong1   = null;
private Order stopLossLong1 = null;
private int sumFilledLong1 = 0; // This variable tracks the quantities of each execution making up the entry order
private List<double> LongEntry1Prices; // This List is used to track the fill prices of the entry order
 
protected override void OnExecutionUpdate(Execution execution, string executionId, double price, int quantity, MarketPosition marketPosition, string orderId, DateTime time)
{
   // Use execution.Name to identify the order, so we are not using execution.Order, which may not be up to date if an ExecutionUpdate is seen before an OrderUpdate in a partial fill
   if (execution.Name == "Long limit entry 1")
   {
       // We sum the quantities of each execution making up the entry order
       sumFilledLong1 += execution.Quantity;
 
       if (LongEntry1Prices.IsNullOrEmpty())
           LongEntry1Prices = new List<double>();
 
       for (int i = 0; i &lt; execution.Quantity; i++)
           LongEntry1Prices.Add(execution.Price);
 
       // Now we can calculate the average entry price, and use it to protect the specifc entry
       double averageEntryPrice = 0;
       for (int i = 0; i &lt; LongEntry1Prices.Count; i++)
           averageEntryPrice += LongEntry1Prices[i];
       averageEntryPrice /= LongEntry1Prices.Count;
 
       if (stopLossLong1 == null &amp;&amp; targetLong1 == null)
       {
           // Directly assign order objects from the method's return value. This prevents us from overprotecting the position by making sure our code changes the orders, instead of submitting new orders
           stopLossLong1 = ExitLongStopMarket(0, true, sumFilledLong1, averageEntryPrice - StopDistance * TickSize, "StopLossLong1", "Long limit entry 1");
           targetLong1 = ExitLongLimit(0, true, sumFilledLong1, averageEntryPrice + ProfitDistance * TickSize, "TargetLong1", "Long limit entry 1");
       }
       else
       {
           ChangeOrder(stopLossLong1, sumFilledLong1, 0, averageEntryPrice - StopDistance * TickSize);
           ChangeOrder(targetLong1, sumFilledLong1, averageEntryPrice + ProfitDistance * TickSize, 0);
       }
 
       // Entry Order filled, and stops and targets submitted. Reset Price list and running Filled quantity
       if (sumFilledLong1 == entryQuantity1)
       {
           // Move to Class?
           sumFilledLong1 = 0;
           LongEntry1Prices.Clear();
       }
   }
} |



   

Additional Reference Samples  

Additional reference code samples are available the NinjaScript Educational Resources section of our support forum.





 
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
 
 
 



</double></double>