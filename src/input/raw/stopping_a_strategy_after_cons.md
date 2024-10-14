










 


Stopping a strategy after consecutive losers







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?stopping_a_strategy_after_cons.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Stopping a strategy after consecutive losers | [Previous page](separating_logic_to_either_cal.htm)
[Return to chapter overview](strategy2.htm)










Trending days or ranging days can make or break a strategy. If you have a system that does extremely well on trending days, you may look for a way to turn that system off during range-bound days. A simple filter you may use could be something like, "If the last three trades were consecutive losers, stop trading for the rest of the session


 


Key concepts in this example
----------------------------


•Obtaining previous trade information to decide whether or not to keep trading for the day

 


Important related documentation
-------------------------------


•[SystemPerformance](systemperformance.htm)

•[TradeCollection](tradecollection.htm)

•[AllTrades*](alltrades.htm)

•[EnterLong()](enterlong.htm)

•[ExitLong()](exitlong.htm)

•[IsFirstBarOfSession](isfirstbarofsession.htm)

•[IsFirstTickOfBar](isfirsttickofbar.htm)

 


* This reference sample uses the .AllTrades property. This property will include all historical virtual trades as well as real-time trades. If you wish to only make calculations based on real-time trades you can use the .RealtimeTrades property.


 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleTradeObjects\_Nt8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleTradeObjects_Nt8.zip)





 
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
 
 
 



