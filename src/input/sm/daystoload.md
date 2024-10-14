










 


DaysToLoad







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?daystoload.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
DaysToLoad | [Previous page](connectionlosshandling.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Determines the number of trading days which will be configured when loading the strategy from the Strategies Grid.


 




|  |
| --- |
| Notes:  
1.This property does NOT affect a strategy configured of a Chart or the Strategy Analyzer.2.A trading day is defined by a [Trading Hour](using_the_trading_hours_window.htm) template |



 


Property Value
--------------


An int value determining the number of trading days to load for historical data processing.  Default value is 5, but can be configured and overridden  from the UI.



Syntax
------


DaysToLoad



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.SetDefaults)
     {
         DaysToLoad = 15;
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
 
 
 



