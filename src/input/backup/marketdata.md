MarketData




Definition
----------
MarketData can be used to access snapshot market data and for subscribing to market data events.

|  |
| --- |
| Notes: 
1.Remember to unsubscribe if you are no longer using the subscription.2.You should only unsubscribe to a market data event if you are actually subscribed. |

Properties
----------
|  |  |
| --- | --- |
| Ask | A [MarketDataEventArgs](marketdataeventargs.htm) representing the ask price |
| Bid | A [MarketDataEventArgs](marketdataeventargs.htm)  representing the bid price |
| DailyHigh | A [MarketDataEventArgs](marketdataeventargs.htm)  representing the daily high |
| DailyLow | A [MarketDataEventArgs](marketdataeventargs.htm)  representing the daily low |
| DailyVolume | A [MarketDataEventArgs](marketdataeventargs.htm)  representing the daily volume |
| Instrument | An [Instrument](instrument.htm) representing the instrument |
| Last | A [MarketDataEventArgs](marketdataeventargs.htm)  representing the last price |
| LastClose | A [MarketDataEventArgs](marketdataeventargs.htm)  representing the last close |
| Opening | A [MarketDataEventArgs](marketdataeventargs.htm)  representing the opening price |
| OpenInterest | A [MarketDataEventArgs](marketdataeventargs.htm)  representing the open interest |
| Settlement | A [MarketDataEventArgs](marketdataeventargs.htm)  representing the settlement price |
| Update | Event handler for subscribing/unsubscribing to market depth events

Note:  Attempting to unsubscribe to this event before there is a subscription will generate errors. 


Syntax
------


MarketData


Example
-------
```
/* Example of subscribing/unsubscribing to market data from an Add On. The concept can be carried over
to any NinjaScript object you may be working on. */
public class MyAddOnTab : NTTabPage
{
 private Instrument instrument;
 
 public MyAddOnTab()
 {
         instrument = Instrument.GetInstrument("AAPL");
         if (instrument == null)
                 return;
 
         // Subscribe to market data. Snapshot data is provided right on subscription
         // Note: "instrument" is a placeholder in this example, you will need to replace 
         // with a valid Instrument object through various methods or properties available depending
         // on the NinjaScript type you are working with (e.g., Bars.Instrument or Instrument.GetInstrument()
         if (!instrument.Dispatcher.HasShutdownStarted)
                 instrument.Dispatcher.InvokeAsync(() =&gt; instrument.MarketData.Update += OnMarketData);
 
         // Printing snapshot market data for the last price and time
         NinjaTrader.Code.Output.Process(instrument.MarketData.Last.Price.ToString() + " " + instrument.MarketData.Last.Time.ToString(),
                 PrintTo.OutputTab1);
 }
 
 // This method is fired on market data events
 private void OnMarketData(object sender, MarketDataEventArgs e)
 {
         // Do something with market data events
 }
 
 // Called by TabControl when tab is being removed or window is closed
 public override void Cleanup()
 {
         // Make sure to unsubscribe to the market data subscription
         if (instrument != null)
                 instrument.MarketData.Update -= OnMarketData;
 }
 
 // Other required NTTabPage members left out for demonstration purposes. Be sure to add them in your own code.
} 
```



