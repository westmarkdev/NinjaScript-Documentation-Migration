










 


MarketDataEventArgs







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?marketdataeventargs.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [OnMarketData()](onmarketdata.htm) &gt;
MarketDataEventArgs | [Previous page](onmarketdata.htm)
[Return to chapter overview](onmarketdata.htm)










Definition
----------


Represents a change in level one market data and is passed as a parameter in the [OnMarketData()](onmarketdata.htm) method.   

 


Methods and Parameters
----------------------




|  |  |
| --- | --- |
| Ask | A double value representing the ask price |
| Bid | A double value representing the bid price |
| Instrument | A Instrument object representing the instrument of the market data |
| IsReset | A bool value representing if a UI reset is needed after a manual disconnect.
 
Note: This is only relevant for columns. Whenever this property is true, the UI needs to be reset. |
| MarketDataType | Possible values are:
MarketDataType.Ask
MarketDataType.Bid
MarketDataType.DailyHigh
MarketDataType.DailyLow
MarketDataType.DailyVolume
MarketDataType.Last
MarketDataType.LastClose (prior session close)
MarketDataType.Opening
MarketDataType.OpenInterest (supported by IQFeed, Kinetick)
MarketDataType.Settlement |
| Price | A double value representing the price |
| Time | A [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) structure representing the time |
| ToString() | A string representation of the MarketDataEventArgs object |
| Volume | A long value representing volume |



 


 




|  |
| --- |
| Critical: If used with [TickReplay](tick_replay.htm), please keep in mind Tick Replay ONLY replays the Last market data event, and only stores the best inside bid/ask price at the time of the last trade event.  You can think of this as the equivalent of the bid/ask price at the time a trade was reported. Please also see [Developing for Tick Replay](developing_for__tick_replay.htm). |



 


 




|  |
| --- |
| Tips
•Not all connectivity providers support all MarketDataTypes.•For an example of how to use IsReset please see \MarketAnalyzerColumns\AskPrice.cs |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
     // Print some data to the Output window
     if (marketDataUpdate.MarketDataType == MarketDataType.Last)
         Print("Last = " + marketDataUpdate.Price + " " + marketDataUpdate.Volume);
     else if (marketDataUpdate.MarketDataType == MarketDataType.Ask)
         Print("Ask = " + marketDataUpdate.Price + " " + marketDataUpdate.Volume);
     else if (marketDataUpdate.MarketDataType == MarketDataType.Bid)
         Print("Bid = " + marketDataUpdate.Price + " " + marketDataUpdate.Volume);
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
 
 
 



