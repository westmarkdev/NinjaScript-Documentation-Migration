﻿










 


AtmStrategyCreate()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?atmstrategycreate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [ATM Strategy Methods](atm_strategy_methods.htm) &gt;
AtmStrategyCreate() | [Previous page](atmstrategyclose.htm)
[Return to chapter overview](atm_strategy_methods.htm)










Definition
----------


Submits an entry order that will execute a specified ATM Strategy.  


 




|  |
| --- |
| Notes:
 
•Please review the section on using [ATM Strategies](using_atm_strategies.htm) •This method is NOT backtestable and will NOT execute on historical data •See the [AtmStrategyCancelEntryOrder()](atmstrategycancelentryorder.htm) to cancel an entry order •See the [AtmStrategyChangeEntryOrder()](atmstrategychangeentryorder.htm) to change the price of the entry order •The ATM Strategy will be created asyncronous on the hosting NinjaScripts UI Thread, a callback is provided solely to check when the ATM Strategy is started on that thread - accessing for example price data in that outside OnBarUpdate() context is not possible.•Please see the SampleATMStrategy build into NinjaTrader for example usage. |



 


 


Method Return Value
-------------------


This method does not return a value



Syntax
------


AtmStrategyCreate(OrderAction action, OrderType orderType, double limitPrice, double stopPrice, TimeInForce timeInForce, string orderId, string strategyTemplateName, string atmStrategyId, Action<cbi.errorcode, string=""> callback) 


 



Parameters
----------




|  |  |
| --- | --- |
| action | Sets if the entry order is a buy or sell order 
 
Possible values are:
 
•OrderAction.Buy•OrderAction.Sell |
| orderType | Sets the order type of the entry order
 
Possible values are:
 
•OrderType.Limit•OrderType.Market•OrderType.MIT•OrderType.StopMarket•OrderType.StopLimit |
| limitPrice | The limit price of the order |
| stopPrice | The stop price of the order |
| timeInForce | Sets the time in force of the entry order
 
Possible values are:
•TimeInForce.Day•TimeInForce.Gtc |
| orderId | The unique identifier for the entry order |
| strategyTemplateName | Specifies which strategy template will be used |
| atmStrategyId | The unique identifier for the ATM strategy |
| callback | The callback action is used to check that the ATM Strategy is successfully started |







|  |
| --- |
| Tip:  Unlike NinjaScript Strategy orders (both [managed](managed_approach.htm) and [unmanaged](unmanaged_approach.htm)), ATM strategies generated by the AtmStrategyCreate() method can then be managed manually by any order entry window such as the SuperDOM or within your NinjaScript strategy. |





Examples
--------




| ns |
| --- |
| private string atmStrategyId;
private string atmStrategyOrderId;
private bool   isAtmStrategyCreated = false;
 
protected override void OnBarUpdate()
{
   if (State &lt; State.Realtime)
       return;
 
   if (Close[0] &gt; SMA(20)[0])
   {
       atmStrategyId = GetAtmStrategyUniqueId();
       atmStrategyOrderId = GetAtmStrategyUniqueId();
 
       AtmStrategyCreate(OrderAction.Buy, OrderType.Market, 0, 0, TimeInForce.Day,
           atmStrategyOrderId, "MyTemplate", atmStrategyId, (atmCallbackErrorCode, atmCallbackId) =&gt; {
 
           // checks that the call back is returned for the current atmStrategyId stored
           if (atmCallbackId == atmStrategyId)
           {
               // check the atm call back for any error codes
               if (atmCallbackErrorCode == Cbi.ErrorCode.NoError)
               {
                   // if no error, set private bool to true to indicate the atm strategy is created
                   isAtmStrategyCreated = true;
               }
           }
       });
   }
 
   if(isAtmStrategyCreated)
   {
       // atm logic
   }
 
   else if(!isAtmStrategyCreated)
   {
       // custom handling for a failed atm Strategy
   }
}    |






 
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
 
 
 



</cbi.errorcode,>