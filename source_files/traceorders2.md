﻿










 


TraceOrders







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?traceorders2.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Tips](tips.htm) &gt;
TraceOrders | [Previous page](strategy_position_vs__account_.htm)
[Return to chapter overview](tips.htm)










[TraceOrders](traceorders.htm) is a useful property when debugging the behavior of your orders. With the use of this property, you can track orders placed, amended, and canceled. The traces displayed in the NinjaScript Output window or if used, in the OnOrderTrace Override in the script where this was set. This will provide meaningful information for diagnosis when NinjaTrader ignores, changes or cancels orders when various strategy order methods are called.


 


To enable TraceOrders, add this line into the OnStateChange() method in the state SetDefaults of your NinjaScript strategy:




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         TraceOrders = true;
     }
} |



 


Trace output examples:




| ns |
| --- |
| Entered internal SubmitOrderManaged() method at 6/2/2015 8:42:00 AM: BarsInProgress=0 Action=Buy OrderType=Market Quantity=1 LimitPrice=0 StopPrice=0 SignalName='market order' FromEntrySignal='' |



 


This trace is outputted when we place an entry order. It tells us all the pertaining properties of our order as well as the time it was submitted.




| ns |
| --- |
| Amended open order at 6/2/2015 11:39:00 AM: BarsInProgress=0 Action=Buy OrderType=Limit Quantity=1 LimitPrice=130.41 StopPrice=0 SignalName='long order to be resubmitted' FromEntrySignal='' |



 


This trace tells us that a previously submitted order was modified instead of submitting a completely new order.




| ns |
| --- |
| Ignored SubmitOrderManaged() method at 6/2/2015 12:55:00 PM: BarsInProgress=0 Action=Buy OrderType=Limit Quantity=1 LimitPrice=129.92 StopPrice=0 SignalName='long order to be resubmitted' FromEntrySignal='' Reason='Exceeded entry signals limit based on EntryHandling and EntriesPerDirection properties' |



 


This trace provides the reason why our Limit order was ignored.




| ns |
| --- |
| Cancelled expired order: BarsInProgress=0, orderId='NT-00123-118' account='Sim101' name='long order to be resubmitted' orderState=Working instrument='AAPL' orderAction=Buy orderType='Limit' limitPrice=130.3 stopPrice=0 quantity=1 tif=Gtc oco='' filled=0 averageFillPrice=0 id=-1 gtd='2099-12-01' |



 


This trace tells us that our Limit order was canceled because it had expired.


 


 


A new concept in NinjaTrader 8 is the [OnOrderTrace](onordertrace.htm) override method.


 


This method prevents TraceOrders from printing the traces directly to the output window but instead sends this information to the OnOrderTrace override where you can do logic or format the trace how you would like and then print only what you need to see.




| ns |
| --- |
| protected override void OnOrderTrace(DateTime timestamp, string message)
{
     Print(string.Format("{0} {1}", timestamp, message));
} |



 


These examples illustrate the most common traces you will run across. They are mostly useful in determining the reason your orders are not submitted or cancelled. TraceOrders will only show you what is happening under the hood when you submit orders, but it will not tell you what happens after the order is submitted. To determine the behavior of your orders after submission you will need to look into your NinjaTrader trace logs. You can view those either through the "Log" tab on the "Control Center" or from the trace folder in My Documents\NinjaTrader 8\trace\.


 


For more information on how to debug your NinjaScript please review the [Debugging](debugging_your_ninjascript_cod.htm) tip.





 
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
 
 
 


