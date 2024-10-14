










 


ExitOnSessionCloseSeconds







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?exitonsessioncloseseconds.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
ExitOnSessionCloseSeconds | [Previous page](execution.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


The number of seconds before the actual session end time that the "[IsExitOnSessionCloseStrategy](isexitonsessionclosestrategy.htm)" function will trigger. 


The time from which this property will be calculated is taken from the [Trading Hours](trading_hours.htm) EOD property set in the strategy's Trading Hours template. The ExitOnSessionCloseSeconds property can either be set programatically in the [OnStateChange()](onstatechange.htm) method or be driven by the UI at run time.


 




|  |
| --- |
| Note: This is a real-time only property, it will not have any effect on your ExitOnSessionClose time in backtesting processing historical data. |




Property Value
--------------


An int representing the number of seconds.  Default value is 30.


 




|  |
| --- |
| Warning: This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |





Syntax
------


ExitOnSessionCloseSeconds



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         // Triggers the exit on close function 30 seconds prior to trading day end 
         IsExitOnSessionCloseStrategy = true;
         ExitOnSessionCloseSeconds = 30;
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
 
 
 



