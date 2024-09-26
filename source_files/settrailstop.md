










 


SetTrailStop()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?settrailstop.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [Order Methods](order_methods.htm) &gt; [Managed Approach](managed_approach.htm) &gt;
SetTrailStop() | [Previous page](setstoploss.htm)
[Return to chapter overview](managed_approach.htm)










Definition
----------


Generates a trail stop order with the signal name "Trail stop" to exit a position. Trail stops are amended on a bar update basis, so dependent upon the [Calculate](calculate.htm) setting of the parent strategy. Trail stop orders are real working orders (unless simulated is specified in which case the stop order is locally simulated and submitted as market once triggered) submitted immediately to the market upon receiving an execution from an entry order.


 




|  |
| --- |
| Notes:
•The SetTrailStop() method can NOT be used concurrently with the [SetStopLoss()](setstoploss.htm) or [SetParabolicStop()](setparabolicstop.htm) method for the same position, if any of methods are called for the same position (fromEntrySignal) the [SetStopLoss()](setstoploss.htm) will always take precedence. You can however, use all three methods in the same strategy if they reference different signal names. •Trail stop orders are submitted in real-time on incoming executions from entry orders •Since they are submitted upon receiving an execution, the Set method should be called prior to submitting the associated entry order to ensure an initial level is set.•A strategy will either generate a trail stop order for each partial fill of an entry order or one order for all fills. See additional information under the [Strategies](options_strategies.htm) tab of the Options dialog window. •If a [profit target](setprofittarget.htm) order is generated in addition to a trail stop order, they are submitted as OCO (one cancels other) •Trail stop orders are submitted as stop-market orders •A trail stop order is automatically canceled if the managing position is closed by another strategy generated exit order•Should you have multiple Bars objects of the same instrument while using SetTrailStop() in your strategy, you should only submit orders for this instrument to the first Bars context of that instrument. This is to ensure your order logic is processed correctly and any necessary order amendments are done properly.•Trail stop orders are modified based on the strategies 'Calculate' settings. In the case of 'Calculate' on bar close, when the bar closes the trail stop order modification will occur using the lowest/highest price of the bar as the reference price to apply the trail offset. Subsequently if the open price of the next bar is significantly higher or lower than this price then there is a possibility that the calculated trail stop price is now an invalid stop price. This is a risk with modifying any stop order closer to the current market price since any modification above/below the current price would be rejected. |



 


Syntax


SetTrailStop(CalculationMode mode, double value)


SetTrailStop(string fromEntrySignal, CalculationMode mode, double value, bool isSimulatedStop)


 




|  |
| --- |
| Warnings:  
•This method CANNOT be called from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults•CalculationMode.Price and CalculationMode.Currency are irrelevant for trail stops.  Attempting to use one of these modes will log a message and the stop order be ignored.  Please use [SetStopLoss()](setstoploss.htm) for these modes instead. |



 


 


Parameters
----------




|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| mode | Determines the manner in which the value parameter is calculated
 
Possible values are:
 


|  |  |
| --- | --- |
| CalculationMode.Percent | Percentage away from the average entry, based on the average entry price. |
| CalculationMode.Pips | Pips away from average entry. |
| CalculationMode.Ticks | Ticks away from entry average entry. |



 
Please note in percentage calculation mode a value of 1 is equal to 100%, a value of 0.1 is equal to 10%, and a value of 0.01 will be 1% |
| isSimulatedStop | If true, will simulate the stop order and submit as market once triggered |
| value | The value the trail stop order is offset from the position entry price (exception is using .Price mode where 'value' will represent the actual price) |
| fromEntrySignal | The entry signal name. This ties the trail stop exit to the entry and exits the position quantity represented by the actual entry. Using an empty string will attach the exit order to all entries. |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Sets a trail stop of 12 ticks
         SetTrailStop(CalculationMode.Ticks, 12);
     }
} |



 


 




|  |
| --- |
| Tips (also see [Overview](managed_approach.htm)):
•It is suggested to call this method from within the strategy [OnStateChange()](onstatechange.htm) method if your trail stop price/offset is static •You may call this method from within the strategy [OnBarUpdate()](onbarupdate.htm) method should you wish to dynamically change the trail stop price while in an open position •Should you call this method to dynamically change the trail stop price in the strategy [OnBarUpdate()](onbarupdate.htm) method, you should always reset the trail stop price / offset value when your strategy is flat otherwise, the last price/offset value set will be used to generate your trail stop order on your next open position •The signal name generated internally by this method is "Trail stop" which can be used with various methods such as [BarsSinceExitExecution()](barssinceexitexecution.htm), or other order concepts which rely on identifying a signal name |



 





 
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
 
 
 



