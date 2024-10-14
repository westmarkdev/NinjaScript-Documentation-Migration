










 


Monitoring for and trading a breakout







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?monitoring_for_and_trading_a_b.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Monitoring for and trading a breakout | [Previous page](modifying_the_price_of_stop_lo.htm)
[Return to chapter overview](strategy2.htm)










A common concept many traders use is the idea of a breakout. Points of interest are when the price breaks out from a consolidation range or from previous highs and lows.


 


Key concepts in this example
----------------------------


•Determining and storing the first 30 bar high

•Submitting a long stop order to be filled when price breaks out from the 30 bar high

•Closing positions after a certain amount of bars have passed

•Resetting the 30 bar high at the start of every new trading session

 


Important related documentation
-------------------------------


•[IsFirstBarOfSession](isfirstbarofsession.htm)

•[BarsSinceNewTradingDay](barssincenewtradingday.htm)

•[BarsSinceEntryExecution()](barssinceentryexecution.htm)

•[BarsSinceExitExecution()](barssinceexitexecution.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleBreakoutStrategy\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleBreakoutStrategy_NT8.zip)





 
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
 
 
 



