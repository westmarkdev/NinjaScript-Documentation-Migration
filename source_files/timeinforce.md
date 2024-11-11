﻿










 


TimeInForce







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?timeinforce.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
TimeInForce | [Previous page](testperiod.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Sets the time in force property for all orders generated by a strategy. The selected TIF parameter is sent to your broker on order submission and will instruct how long you would like the order to be active before it is cancelled. 


 




|  |
| --- |
| Note:  This property is dependent on what time in force your broker may or may not support.  If a brokerage / exchange combination is not compatible with a particular time in force, the order will be rejected by the broker. NinjaTrader does not have a method to prevent an unsupported TIF to be sent to a particular exchange.  For questions about what TIF may be supported, please contact your broker directly. |



 


 


Property Value
--------------


An enum value that determines the time in force.  Default value is set to TimeInForce.Gtc.  Possible values are:




|  |  |
| --- | --- |
| TimeInForce.Day | Orders will be canceled by the broker at the end of the trading session |
| TimeInForce.Gtc | Order will remain working until the order is explicitly cancelled.  |
| TimeInForce.Gtd | Order will remain working until the specified date |



 


Syntax
------


TimeInForce


 


 



Examples
--------




| ns | Setting default TIF for all strategy orders |
| --- | --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         TimeInForce = TimeInForce.Day;
     }
} |



 




| ns | Setting TIF conditionally  |
| --- | --- |
|  
protected override void OnStateChange()
{
     if (State == State.Configure)
     {
 if (Instrument != null)
 {
         if (Instrument.Exchange == Exchange.Nybot)
                 TimeInForce = TimeInForce.Day;
         else if (Instrument.Exchange == Exchange.Globex)
                 TimeInForce = TimeInForce.Gtc;
 }
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
 
 
 


