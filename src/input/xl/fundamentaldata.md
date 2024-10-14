﻿










 


FundamentalData







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?fundamentaldata.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
FundamentalData | [Previous page](controlcenter.htm)
[Return to chapter overview](add_on.htm)










Definition
----------


FundamentalData is used to access fundamental snapshot data and for subscribing to fundamental data events. 


 




|  |
| --- |
| Note: Remember to unsubscribe if you are no longer using the subscription. |



 


 


Properties
----------




|  |  |
| --- | --- |
| AverageDailyVolume | A double representing the average daily volume |
| Beta | A double representing the beta |
| CalendarYearHigh | A double representing the high price of the calendar year |
| CalendarYearHighDate | A DateTime representing the date of the calendar year's high price |
| CalendarYearLow | A double representing the low price of the calendar year |
| CalendarYearLowDate | A DateTime representing the date of the calendar year's low price |
| CurrentRatio | A double representing the current ratio |
| DividendAmount | A double representing the dividend amount |
| DividendPayDate | A DateTime representing the date dividends are paid |
| DividendYield | A double representing the dividend yield |
| EarningsPerShare | A double representing the earnings per share |
| FiveYearsGrowthPercentage | A double representing the 5yr growth percent |
| High52Weeks | A double representing the 52 week high |
| High52WeeksDate | A DateTime representing the date of the 52 week high price |
| HistoricalVolatility | A double representing the historical volatility |
| InsiderOwned | A double representing the insider owned amount |
| Instrument | An [Instrument](instrument.htm) representing the instrument |
| Low52Weeks | A double representing the 52 week low |
| Low52WeeksDate | A DateTime representing the date of the 52 week low price |
| MarketCap | A double representing the market capitalization |
| NextYearsEarningsPerShare | A double representing next year's earnings per share |
| PercentHeldByInstitutions | A double representing the percent held by institutions |
| PriceEarningsRatio | A double representing the P/E ratio |
| RevenuePerShare | A double representing the revenue per share |
| SharesOutstanding | A long representing the shares outstanding |
| ShortInterest | A double representing the short interest |
| ShortInterestRatio | A double representing the short interest ratio |
| VWAP | A double representing the VWAP |
| Update | Event handler for subscribing/unsubscribing to market depth events |



 


Syntax
------


FundamentalData


 


 


Example
-------




| ns |
| --- |
| /* Example of subscribing/unsubscribing to fundamental data from an Add On. The concept can be carried over
to any NinjaScript object you may be working on. */
public class MyAddOnTab : NTTabPage
{
 private Instrument instrument;
 
 public MyAddOnTab()
 {
         instrument = Instrument.GetInstrument("AAPL");
 
         if (instrument == null)
                 return;
 
         // Subscribe to fundamental data. Snapshot data is provided right on subscription
         if (!instrument.Dispatcher.HasShutdownStarted)
                 instrument.Dispatcher.InvokeAsync(() =&gt; instrument.FundamentalData.Update += OnFundamentalData);
 
         // Printing snapshot fundamental data for average daily volume
         NinjaTrader.Code.Output.Process(instrument.FundamentalData.AverageDailyVolume, PrintTo.OutputTab1);
 }
 
 // This method is fired on fundamental data events
 private void OnFundamentalData(object sender, FundamentalDataEventArgs e)
 {
          // Do something with fundamental data events
 }
 
 // Called by TabControl when tab is being removed or window is closed
 public override void Cleanup()
 {
         // Make sure to unsubscribe to the fundamental data subscription
         if (instrument != null)
                 instrument.FundamentalData.Update -= OnFundamentalData;
 }
 
 // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.
} |
|   |






 
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
 
 
 


