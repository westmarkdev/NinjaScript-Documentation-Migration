﻿










 


OnMarketDepth()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onmarketdepth.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
OnMarketDepth() | [Previous page](marketdataeventargs.htm)
[Return to chapter overview](common.htm)










Definition
----------


An event driven method which is called and guaranteed to be in the correct sequence for every change in level two market data (market depth) for the underlying instrument. The OnMarketDepth() method can be used to build your own level two book.


 




|  |
| --- |
| Notes
1.This is a real-time data stream and can be CPU intensive if your program code is compute intensive (not optimal) 2.This method is not called on historical data (backtest)  |



 



Method Return Value
-------------------


This method does not return a value.


 


 


Syntax
You must override the method in your strategy or indicator with the following syntax:
--------------------------------------------------------------------------------------------


   

protected override void OnMarketDepth(MarketDepthEventArgs marketDepthUpdate)   

{  

   

}


 




|  |
| --- |
| Tip:  The NinjaScript code wizards can automatically generate the method syntax for you when creating a new script. |



 


 


Parameters
----------




|  |  |
| --- | --- |
| marketDepthUpdate | [MarketDepthEventArgs](marketdeptheventargs.htm) representing the recent change in market data |





Examples
--------




| ns |
| --- |
| protected override void OnMarketDepth(MarketDepthEventArgs marketDepthUpdate)
{
     // Print some data to the Output window
     if (marketDepthUpdate.MarketDataType == MarketDataType.Ask &amp;&amp; marketDepthUpdate.Operation == Operation.Update)
         Print(string.Format("The most recent ask change is {0} {1}", marketDepthUpdate.Price, marketDepthUpdate.Volume));
}    |



 


 




|  |
| --- |
| Tips
1.With [multi-time frame and instrument strategies](multi-time_frame__instruments.htm), OnMarketDepth will be called for all unique instruments in your strategy. Use the [BarsInProgress](barsinprogress.htm) to filter the OnMarketDepth() method for a specific instrument. (BarsInProgress will return the first BarsInProgress series that matches the instrument for the event)2.Do not leave an unused OnMarketDepth() method declared in your NinjaScript object. This will unnecessarily attach a data stream to your strategy which uses unnecessary CPU cycles.3.Should you wish to run comparisons against prior values you will need to store and update local variables to track the relevant values.4.With NinjaTrader being multi-threaded, you should not rely on any particular sequence of events like OnMarketDepth() always being called before OnMarketData() or vice versa. |






 
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
 
 
 



