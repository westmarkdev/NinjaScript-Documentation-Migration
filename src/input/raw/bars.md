










 


Bars







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?bars.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
Bars | [Previous page](xmlignoreattribute.htm)
[Return to chapter overview](common.htm)










Definition
----------


Represents the data returned from the historical data repository. The Bars object contain several methods and properties for working with bar data.





|  |
| --- |
| Warning: The Bars object and its member should NOT be accessed within the [OnStateChange()](onstatechange.htm) method before the State has reached State.DataLoaded |



 


 


Additional Access Information
Members within the Bars class can be accessed without a null reference check in the OnBarUpdate() event handler. When the OnBarUpdate() event is triggered, there will always be a Bar object which holds the method or property. Should you wish to access these members elsewhere, check for null reference first. e.g. if (Bars != null)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [BarsSinceNewTradingDay](barssincenewtradingday.htm) | Number of bars that have elapsed since the start of the trading day |
| [GetAsk()](getask.htm) | Returns the Ask price |
| [GetBar()](getbar.htm) | Returns the bar index based on time |
| [GetBid()](getbid.htm) | Returns the Bid price |
| [GetClose()](getclose.htm) | Returns the closing price |
| [GetDayBar()](getdaybar.htm) | Returns a Bar object that represents a trading day whose properties for open, high, low, close, time and volume can be accessed. |
| [GetHigh()](gethigh.htm) | Returns the High price |
| [GetLow()](getlow.htm) | Returns the Low price |
| [GetOpen()](getopen.htm) | Returns the opening price |
| [GetTime()](gettime.htm) | Returns the time |
| [GetVolume()](getvolume.htm) | Returns the volume |
| [IsFirstBarOfSession](isfirstbarofsession.htm) | Returns true if the bar is the first bar of a session |
| [IsFirstBarOfSessionByIndex()](isfirstbarofsessionbyindex.htm) | Returns true if the bar is the first bar of a session |
| [IsLastBarOfSession](islastbarofsession.htm) | Returns true if the bar is the last bar of a session |
| [IsResetOnNewTradingDay](isresetonnewtradingday.htm) | Returns true if the chart bars should reset on a new trading day |
| [IsTickReplay](istickreplay.htm) | Returns true if the bars are using tick replay |
| [PercentComplete](percentcomplete.htm) | Value indicating the completion percent of a bar |
| [TickCount](tickcount.htm) | Total number of ticks of the current bar |
| [ToChartString()](tochartstring.htm) | Returns the bars series as a string formatted as the series would be displayed in the user interface |






 
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
 
 
 



