










 


BarsSinceExitExecution()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barssinceexitexecution.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
BarsSinceExitExecution() | [Previous page](barssinceentryexecution.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Returns the number of bars that have elapsed since the last exit. When a signal name is provided, the number of bars that have elapsed since that last specific exit will be returned.



Method Return Value
-------------------


An int value that represents a number of bars. A value of -1 will be returned if a previous exit does not exist.


 


Syntax
BarsSinceExitExecution()
BarsSinceExitExecution(string signalName)
-------------------------------------------------------------------------


 


The following method signature should be used when working with [multi-time frame and instrument strategies](multi-time_frame__instruments.htm):


   

BarsSinceExitExecution(int barsInProgressIndex, string signalName, int exitExecutionsAgo)  

 




|  |
| --- |
| Note: When working with a multi-series strategy the BarsSinceExitExecution() will return you the elapsed bars as determined by the first Bars object for the instrument specified in the barsInProgressIndex. |



 


 


Parameters
----------




|  |  |
| --- | --- |
| signalName | The signal name of an exit order specified in an order exit method. |
| barsInProgressIndex | The index of the Bars object the entry order was submitted against. 
 
Note:  See the [BarsInProgress](barsinprogress.htm) property. |
| exitExecutionsAgo | Number of exit executions ago. Pass in 0 for the number of bars since the last exit execution. |



 


 




|  |
| --- |
| Tip:  Please see [SetStopLoss()](setstoploss.htm), [SetProfitTarget()](setprofittarget.htm) or [SetTrailStop()](settrailstop.htm) for their corresponding signal name |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{ 
   if (CurrentBar &lt; BarsRequiredToTrade) 
       return; 
 
   // Only enter if at least 10 bars has passed since our last exit or if we have never traded yet
   if ((BarsSinceExitExecution() &gt; 10 || BarsSinceExitExecution() == -1) &amp;&amp; CrossAbove(SMA(10), SMA(20), 1))
       EnterLong();
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
 
 
 



