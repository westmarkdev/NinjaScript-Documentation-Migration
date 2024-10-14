










 


Entering on one time frame and exiting on another







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?entering_on_one_time_frame_and.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Entering on one time frame and exiting on another | [Previous page](backtesting_ninjascript_strate.htm)
[Return to chapter overview](strategy2.htm)










You can submit orders to different bars objects. This allows you the flexibility of submitting orders to different timeframes. You can watch for trade conditions across different time frames and place orders on whichever one you want. This is useful for strategies that require more finesse in the exit than the entry. You can now enter trades on longer time frames and then monitor and exit your trade on a more granular time frame.



Key concepts in this example
----------------------------


•Comparing values across multiple time frames

•Submitting orders to a non-primary bar object

 


Important related documentation
-------------------------------


•[BarsArray](barsarray.htm)

•[BarsInProgress](barsinprogress.htm)

•[AddDataSeries()](adddataseries.htm)

•[BarsSinceExitExecution()](barssinceexitexecution.htm)

•[BarsRequiredToTrade()](barsrequiredtotrade.htm)

•[EnterLongLimit()](enterlonglimit.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleMultiTimeFrameOrders\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleMultiTimeFrameOrders_NT8.zip)





 
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
 
 
 



