










 


IsLastBarOfSession







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?islastbarofsession.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
IsLastBarOfSession | [Previous page](isfirstbarofsessionbyindex.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Indicates if the current bar processing is the last bar updated in a trading session.


 




|  |
| --- |
| Notes:  
•This property will always return false on non-intraday bar periods (e.g., Day, Month, etc.)•When running Calculate.OnEachTick / OnPriceChange, this property will always return true on the most current real-time bar since it is the last bar that is updating in the trading session.  If you need to find a bar which coincides with the session end time, please use the [SessionIterator.ActualSessionEnd](actualsessionend.htm).   |



 


 


Property Value
--------------


This property returns true if the bar is the last processed in a session; otherwise, false.  This property is read-only.


 


Syntax
Bars.IsLastBarOfSession
------------------------------


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // Print the current bar number of the first bar processed for each session on a chart
   if(Bars.IsLastBarOfSession)
     Print(string.Format("Bar number {0} was the last bar processed of the session at {1}.", CurrentBar, Time[0]));
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
 
 
 



