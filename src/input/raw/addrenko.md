﻿










 


AddRenko()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?addrenko.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [AddDataSeries()](adddataseries.htm) &gt;
AddRenko() | [Previous page](addpointandfigure.htm)
[Return to chapter overview](adddataseries.htm)










Definition
----------


Similar to the [AddDataSeries()](adddataseries.htm) method for adding Bars objects, this method adds a Renko Bars object for multi-series NinjaScript. 


 




|  |
| --- |
| Notes:  
1.When running NinjaScript, you will be able to choose the first instrument and bar interval to run on. This first Bars object will carry a [BarsInProgress](barsinprogress.htm) index of 0.2. In a multi-time frame and multi-instrument NinjaScript, supplementary Bars objects are added via this method in State.Configure state of the [OnStateChange()](onstatechange.htm) method and given an incremented BarsInProgress index value. See additional information on running [multi-bars scripts](multi-time_frame__instruments.htm).3.The [BarsInProgress](barsinprogress.htm) property can be used to filter updates between different bars series4.If using [OnMarketData()](onmarketdata.htm), a subscription will be created on all bars series added in your indicator or strategy strategy (even if the instrument is the same).  The market data subscription behavior occurs both in real-time and during [TickReplay](developing_for__tick_replay.htm) historical5.For adding regular Bars types please use [AddDataSeries()](adddataseries.htm)6.A Tick Replay indicator or strategy CANNOT use a MarketDataType.Ask or MarketDataType.Bid series.  Please see [Developing for Tick Replay](developing_for__tick_replay.htm) for more information. |



 


 


Syntax
------


AddRenko(string instrumentName, int brickSize, Data.MarketDataType marketDataType)  

AddRenko(string instrumentName, int brickSize, Data.MarketDataType marketDataType, string tradingHoursName)  

AddRenko(string instrumentName, int brickSize, Data.MarketDataType marketDataType, string tradingHoursName, bool?isResetOnNewTradingDay)


 




|  |
| --- |
| Warnings:  
•This method should ONLY be called from the [OnStateChange()](onstatechange.htm) method during State.Configure•Should your script be the host for other scripts that are creating indicators and series dependent resources in State.DataLoaded, please make sure that the host is doing the same AddRenko() calls as those hosted scripts would. For further reference, please also review the 'Adding additional Bars Objects to NinjaScript' section in [Multi-Time Frame &amp; Instruments](multi-time_frame__instruments.htm)•Arguments supplied to AddRenko() should be hardcoded and NOT dependent on run-time variables which cannot be reliably obtained during [State.Configure](state.htm) (e.g., [Instrument](instrument.htm), [Bars](bars.htm), or user input).  Attempting to add a data series dynamically is NOT guaranteed and therefore should be avoided.  Trying to load bars dynamically may result in an error similar to: Unable to load bars series. Your NinjaScript may be trying to use an additional data series dynamically in an unsupported manner. |



 


 


Parameters
----------




|  |  |
| --- | --- |
| instrumentName | A string determining instrument name such as "MSFT" |
| brickSize | An int determining the size (in ticks) of each bar |
| marketDataType | The MarketDataType used for the bars object (last, bid, ask)
 
Possible values are:
 
•MarketDataType.Ask•MarketDataType.Bid•MarketDataType.Last 
Note: Please see the article [here](using_historical_bid_ask_serie.htm) on using Bid/Ask series. |
| tradingHoursName | A string determining the trading hours template for the instrument |
| isResetOnNewTradingDay | A nullable bool* determining if the Bars object should [Break at EOD](break_at_eod.htm)
 
*Will accept true, false or null as the input.  If null is used, the data series will use the settings of the primary data series. |



 


 




|  |
| --- |
| Tip: You can optionally add the exchange name as a suffix to the symbol name. This is only advised if the instrument has multiple possible exchanges that it can trade on and it is configured within the Instruments window. For example: AddRenko("MSFT Arca", 2, MarketDataType.Last) |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.Configure)
     {
         // Add a 1 minute Renko Bars object for the ES 03-18 contract - BarsInProgress index = 1 
         AddRenko("ES 03-18", 2, MarketDataType.Last); 
     }
} 
 
protected override void OnBarUpdate() 
{ 
     // Ignore the primary Bars object and only process the Renko Bars object 
     if (BarsInProgress == 1)
     {
         // Do something;
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
 
 
 


