










 


BarsSinceEntryExecution()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barssinceentryexecution.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
BarsSinceEntryExecution() | [Previous page](barsrequiredtotrade.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


Returns the number of bars that have elapsed since the last entry. When a signal name is provided, the number of bars that have elapsed since that last specific entry will be returned.



Method Return Value
-------------------


An int value that represents a number of bars. A value of -1 will be returned if a previous entry does not exist.


 


Syntax  

BarsSinceEntryExecution()  

BarsSinceEntryExecution(string signalName)


 


The following method signature should be used when working with [multi-time frame and instrument strategies](multi-time_frame__instruments.htm):


 


BarsSinceEntryExecution(int barsInProgressIndex, string signalName, int entryExecutionsAgo)


 




|  |
| --- |
| Note: When working with a multi-series strategy the BarsSinceEntryExecution() will return you the elapsed bars as determined by the first Bars object for the instrument specified by the barsInProgressIndex. |



 


 


Parameters
----------




|  |  |
| --- | --- |
| signalName | The signal name of an entry order specified in an order entry method.  |
| barsInProgressIndex | The index of the Bars object the entry order was submitted against. 
 
Note:  See the [BarsInProgress](barsinprogress.htm) property. |
| entryExecutionsAgo | Number of entry executions ago. Pass in 0 for the number of bars since the last entry execution. |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     if (CurrentBar &lt; BarsRequiredToTrade) 
         return; 
 
     // Only enter if at least 10 bars has passed since our last entry
     if ((BarsSinceEntryExecution() &gt; 10 || BarsSinceEntryExecution() == -1) &amp;&amp; CrossAbove(SMA(10), SMA(20), 1))
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
 
 
 



