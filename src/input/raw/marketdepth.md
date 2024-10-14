










 


MarketDepth







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?marketdepth.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
MarketDepth | [Previous page](marketdata.htm)
[Return to chapter overview](add_on.htm)










Definition
----------


MarketDepth can be used to access snapshot market depth and for subscribing to market depth events.


 




|  |
| --- |
| Notes: 
1.Remember to unsubscribe if you are no longer using the subscription.2.You should only unsubscribe to a market depth event if you are actually subscribed.3.You must unsubscribe from the same thread where the subscription is made. It is therefore recommended to user an [Instrument's](instrument.htm) Dispatcher to ensure this is handled properly. |



 


 


Properties
----------




|  |  |
| --- | --- |
| Asks | List of ask prices |
| Bids | List of bid prices |
| Instrument | [Instrument](instrument.htm) representing the instrument of the market depth event |
| Update | Event handler for subscribing/unsubscribing to market depth events |



 


Syntax
------


MarketDepth


 


 


Example
-------




| ns |
| --- |
| /* Example of subscribing/unsubscribing to market depth from an Add On. */
public class MyAddOnTab : NTTabPage
{
     private Instrument instrument;
 
     public MyAddOnTab()
     {
         instrument = Instrument.GetInstrument("AMD");
 
         if (instrument == null)
             return;
 
         // Follow this pattern to subscribe to MarketDepth events so they may be unsubscribed from the same instrument thread
         if (!instrument.Dispatcher.HasShutdownStarted)
             instrument.Dispatcher.InvokeAsync(() =&gt; instrument.MarketDepth.Update += OnMarketDepth);
 
         // Print the Ask's price ladder
          for (int i = 0; i &lt; instrument.MarketDepth.Asks.Count; i++)
          {
              NinjaTrader.Code.Output.Process(string.Format("Position: {0} Price: {1} Volume: {2}", i,
                 instrument.MarketDepth.Asks[i].Price, instrument.MarketDepth.Asks[i].Volume), PrintTo.OutputTab1);
          }
     }
 
     // This method is fired on market depth events and after the snapshot data is updated.
     private void OnMarketDepth(object sender, MarketDepthEventArgs e)
     {
         return;
     }
 
     // Called by TabControl when tab is being removed or window is closed
     public override void Cleanup()
     {
         // Follow this pattern to subscribe to MarketDepth events so they may be unsubscribed from the same intrument thread
         if (instrument != null &amp;&amp; !instrument.Dispatcher.HasShutdownStarted)
             instrument.Dispatcher.InvokeAsync(() =&gt; instrument.MarketDepth.Update -= OnMarketDepth);
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
 
 
 



