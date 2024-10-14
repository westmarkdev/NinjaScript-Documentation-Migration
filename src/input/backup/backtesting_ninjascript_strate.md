










 


Backtesting NinjaScript Strategies with an intrabar granularity







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?backtesting_ninjascript_strate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Backtesting NinjaScript Strategies with an intrabar granularity | [Previous page](strategy2.htm)
[Return to chapter overview](strategy2.htm)










You can submit orders to different Bars objects. This allows you the flexibility of submitting orders to different timeframes. Like in live trading, taking entry conditions from a 5min chart means executing your order as soon as possible instead of waiting until the next 5min bar starts building. You can achieve this by submitting your orders to a more granular secondary bar series to achieve an "intrabar" fill.


 


Key concepts in this example
----------------------------


•Finding entry conditions on the primary bar object

•Submitting orders to the secondary bar object for an intrabar fill


Important related documentation
-------------------------------


•[AddDataSeries()](adddataseries.htm)

•[BarsInProgress](barsinprogress.htm)

•[EnterLong()](enterlong.htm)

•[BarsArray](barsarray.htm)

•[EnterLongLimit()](enterlonglimit.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleIntrabarBacktest\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleIntrabarBacktest_NT8.zip)





 
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
 
 
 



