










 


SetProfitTarget()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?setprofittarget.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order Methods](order_methods.htm) &gt; [Managed Approach](managed_approach.htm) &gt;
SetProfitTarget() | [Previous page](setparabolicstop.htm)
[Return to chapter overview](managed_approach.htm)










Definition
----------


Generates a profit target order with the signal name "Profit target" to exit a position. Profit target orders are real working orders submitted immediately to the market upon receiving an execution from an entry order. 


 




|  |
| --- |
| Notes:
•Profit target orders are submitted in real-time on incoming executions from entry orders•Since they are submitted upon receiving an execution, the Set method should be called prior to submitting the associated entry order to ensure an initial level is set.•A strategy will either generate a target order for each partial fill of an entry order or one order for all fills. See additional information under the [Strategies](options_strategies.htm) tab of the Options dialog window. •If a [stop loss](setstoploss.htm) or [trail stop](settrailstop.htm) order is generated in addition to a profit target order, they are submitted as OCO (one cancels other) •A profit target order is automatically cancelled if the managing position is closed by another strategy generated exit order•Should you have multiple Bars objects of the same instrument while using SetProfitTarget() in your strategy, you should only submit orders for this instrument to the first Bars context of that instrument. This is to ensure your order logic is processed correctly and any necessary order amendments are done properly. |



   

 


Syntax  

SetProfitTarget(CalculationMode mode, double value)  

SetProfitTarget(CalculationMode mode, double value, bool isMIT)  

SetProfitTarget(string fromEntrySignal, CalculationMode mode, double value)  

SetProfitTarget(string fromEntrySignal, CalculationMode mode, double value, bool isMIT)


 




|  |
| --- |
| Warning:  This method CANNOT be called from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults |



 


 


Parameters
----------




|  |  |
| --- | --- |
| currency | Sets the profit target amount in currency ($500 profit for example) |
| isMIT | Sets the profit target as a market-if-touched order |
| mode | Determines the manner in which the value parameter is calculated
 
Possible values are:
 


|  |  |
| --- | --- |
| CalculationMode.Currency | PnL away from average entry. Calculated by the dollar per tick value for the order quantity used. When this mode is used, [StopTargetHandling](stoptargethandling.htm) will automatically be set to ByStrategyPosition |
| CalculationMode.Percent | Percentage away from the average entry, based on the average entry price. |
| CalculationMode.Pips | Pips away from average entry. |
| CalculationMode.Price | The absolute price point specified. |
| CalculationMode.Ticks | Ticks away from entry average entry. |



 
Please note in percentage calculation mode a value of 1 is equal to 100%, a value of 0.1 is equal to 10%, and a value of 0.01 will be 1% |
| value | The value the profit target order is offset from the position entry price (exception is using .Price mode where 'value' will represent the actual price) |
| fromEntrySignal | The entry signal name. This ties the profit target exit to the entry and exits the position quantity represented by the actual entry.  Using an empty string will attach the exit order to all entries. |



 


 




|  |
| --- |
| Tips (also see [Overview](managed_approach.htm)):
•It is suggested to call this method from within the strategy [OnStateChange()](onstatechange.htm) method if your profit target price/offset is static •You may call this method from within the strategy [OnBarUpdate()](onbarupdate.htm) method should you wish to dynamically change the target price while in an open position •Should you call this method to dynamically change the target price in the strategy [OnBarUpdate()](onbarupdate.htm) method, you should always reset the target price / offset value when your strategy is flat otherwise, the last price/offset value set will be used to generate your profit target order on your next open position •The signal name generated internally by this method is "Profit target" which can be used with various methods such as [BarsSinceExitExecution()](barssinceexitexecution.htm), or other order concepts which rely on identifying a signal name |




 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Submits a profit target order 10 ticks away from the avg entry price
         SetProfitTarget(CalculationMode.Ticks, 10);
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
 
 
 



