










 


BarsRequest







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barsrequest.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
BarsRequest | [Previous page](submit.htm)
[Return to chapter overview](add_on.htm)










Definition
----------


BarsRequest can be used to request [Bars](bars.htm) data and subscribe to real-time Bars data events.


 




|  |
| --- |
| Notes: 
1.When using the DateTime fromLocal and toLocal parameters, the dates are converted to local daily timestamps (12:00 AM) and return a BarsRequest representing full trading days. If you need to request less than one full trading day, please use the barsBack parameter2.A BarsRequest should be called only once and subscribe to the .Update event. Remember to unsubscribe from the .Update Event handler if you are no longer using the subscription.3.A BarsRequest provides underlying market data for an instrument, but is not synchronized with an indicator or strategies primary data series.  You will need to implement your own BarsUpdateEvent logic.  4.BarsRequest data CANNOT be used as input for a NinjaTrader indicator5.Performing a BarsRequest in Playback will always yield bars up to the current playback time / slider position.6.The documented BarsRequest behavior would be the same for all NinjaScript types. |



 


 


Syntax
------


BarsRequest(Cbi.Instrument instrument, int barsBack)  

BarsRequest(Cbi.Instrument instrument, DateTime fromLocal, DateTime toLocal)


 


Parameters
----------




|  |  |
| --- | --- |
| Instrument | The [Instrument](instrument.htm) to request |
| barsBack | An int value determining the number of bars to request from the current time |
| fromLocal | A DateTime value determining the starting date to request |
| toLocal | A DateTime value determining the ending date to request |



 



Methods and Properties
----------------------




|  |  |
| --- | --- |
| Bars | The [Bars](bars.htm) object returned from the request |
| BarsBack | An int representing the number of bars back used in the request |
| BarsPeriod | The [BarsPeriod](barsperiod.htm) for the bars request |
| FromLocal | A DateTime representing the starting date used in the request |
| IsDividendAdjusted | A bool representing if the bars request will be [dividend adjusted](splits_and_dividends.htm) |
| IsResetOnNewTradingDay | A bool representing if the bars request will [Break at EOD](break_at_eod.htm) |
| IsSplitAdjusted | A bool representing if the bars request will be [split adjusted](splits_and_dividends.htm) |
| Instrument | The [Instrument](instrument.htm) of the bars request |
| LookupPolicy | The lookup policies for the bars request.  Possible Values are:
 
•Provider - Queries the provider. The repository is updated on provider's reply•Repository - Looks up the local repository only |
| [MergePolicy](barsrequest_mergepolicy.htm) | The [merge policy](mergepolicy.htm) for the bars request.  |
| [Request()](request.htm) | Requests the bars as parametrized |
| TradingHours | The [trading hours](tradinghours.htm) for the bars request |
| ToLocal | A DateTime representing the end date used in the request |
| Update | A BarsUpdateEvent handler for subscribing/unsubscribing to bar update events |



 



Examples
--------




| ns |
| --- |
| /* Example of subscribing/unsubscribing to bars data events from an Add On as well as making bars requests.
The concept can be carried over to any NinjaScript object you may be working on. */
public class MyAddOnTab : NTTabPage
{
 private int daysBack = 5;
 private bool barsRequestSubscribed = false;
 private BarsRequest barsRequest;
 
 public MyAddOnTab()
 {
   // create a new bars request.  This will determine the insturment and range for the bars to be requested
   barsRequest = new BarsRequest(Cbi.Instrument.GetInstrument("AAPL"), DateTime.Now.AddDays(-daysBack), DateTime.Now);
 
   // Parametrize your request. 
   barsRequest.BarsPeriod = new BarsPeriod { BarsPeriodType = BarsPeriodType.Minute, Value = 1 };
   barsRequest.TradingHours = TradingHours.Get("Default 24 x 7");
 
   // Attach event handler for real-time events if you want to process real-time data
   barsRequest.Update     += OnBarUpdate;
 
   // Request the bars
   barsRequest.Request(new Action<barsrequest, errorcode,="" string="">((bars, errorCode, errorMessage) =&gt;
   {
     if (errorCode != ErrorCode.NoError)
     {
       // Handle any errors in requesting bars here
       NinjaTrader.Code.Output.Process(string.Format("Error on requesting bars: {0}, {1}",
                                       errorCode, errorMessage), PrintTo.OutputTab1);
       return;
     }
 
     // Output the bars we requested. Note: The last returned bar may be a currently in-progress bar
     for (int i = 0; i &lt; bars.Bars.Count; i++)
     {
       // Output the bars
       NinjaTrader.Code.Output.Process(string.Format("Time: {0} Open: {1} High: {2} Low: {3} Close: {4} Volume: {5}",
                                       bars.Bars.GetTime(i),
                                       bars.Bars.GetOpen(i),
                                       bars.Bars.GetHigh(i),
                                       bars.Bars.GetLow(i),
                                       bars.Bars.GetClose(i),
                                       bars.Bars.GetVolume(i)), PrintTo.OutputTab1);
     }
 
     // If requesting real-time bars, but there are currently no connections
     lock (Connection.Connections)
       if (Connection.Connections.FirstOrDefault() == null)
         NinjaTrader.Code.Output.Process("Real-Time Bars: Not connected.", PrintTo.OutputTab1);
   }));
 }
 
 // This method is fired on real-time bar events
 private void OnBarUpdate(object sender, BarsUpdateEventArgs e)
 {
   /* Depending on the BarsPeriod type of your barsRequest you can have situations where more than one bar is
    updated by a single tick. Be sure to process the full range of updated bars to ensure you did not miss a bar. */
 
   // Output bar information on each tick
   for (int i = e.MinIndex; i &lt;= e.MaxIndex; i++)
   {
     // Processing every single tick
     NinjaTrader.Code.Output.Process(string.Format("Time: {0} Open: {1} High: {2} Low: {3} Close: {4}",
                                     e.BarsSeries.GetTime(i),
                                     e.BarsSeries.GetOpen(i),
                                     e.BarsSeries.GetHigh(i),
                                     e.BarsSeries.GetLow(i),
                                     e.BarsSeries.GetClose(i)), PrintTo.OutputTab1);
   }
 }
 
 // Called by TabControl when tab is being removed or window is closed
 public override void Cleanup()
 {
   // Make sure to unsubscribe to the bars request subscription
   if (barsRequest != null)
     {
        barsRequest.Update -= OnBarUpdate;
        barsRequest.Dispose();
       barsRequest = null;
      }
 }
 
 // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.
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
 
 
 



</barsrequest,>