










 


IsTickReplay







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?istickreplay.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Bars](bars.htm) &gt;
IsTickReplay | [Previous page](isresetonnewtradingday.htm)
[Return to chapter overview](bars.htm)










Definition
----------


Indicates if the bar series is using the [Tick Replay](developing_for__tick_replay.htm) data series property.


 


Property Value
--------------


This property returns true if the bar series is using tick replay; otherwise, false.  This property is read-only.


 


Syntax
Bars.IsTickReplay
------------------------





|  |
| --- |
| Warning: A Tick Replay indicator or strategy CANNOT use a MarketDataType.Ask or MarketDataType.Bid series.  Please see [Developing for Tick Replay](developing_for__tick_replay.htm) for more information. |



 


 


Examples
--------




| ns |
| --- |
| private double askPrice;
protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
   if(Bars.IsTickReplay)
   {
     // if using tick replay, get the current ask price associated with the tick
     askPrice = marketDataUpdate.Ask;
   }
   else // otherwise, get the real-time market data price during MarketDataType.Ask event
     askPrice = marketDataUpdate.MarketDataType == MarketDataType.Ask ? marketDataUpdate.Price : double.MinValue;
 
   // only print if a value is set
   if(askPrice != double.MinValue)
   {
     Print("ask price: " + askPrice);
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
 
 
 



