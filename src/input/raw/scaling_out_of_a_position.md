










 


Scaling out of a position







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?scaling_out_of_a_position.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Scaling out of a position | [Previous page](rounding_values_to_the_nearest.htm)
[Return to chapter overview](strategy2.htm)










A common technique used by discretionary traders is scaling in and scaling out of a position. To scale out of a position refers to closing a portion of your position when you hit a profit target and then raising your stop to close your remaining portion later.


 


Key concepts in this example
----------------------------


•Submitting Profit Target orders

•Submitting Trailing Stop orders

•Closing half of your position at a time

 


Important related documentation
-------------------------------


•[MarketPosition](position_marketposition.htm)

•[SetProfitTarget()](setprofittarget.htm)

•[SetTrailStop()](settrailstop.htm)

•[EntriesPerDirection*](entriesperdirection.htm)

•[EntryHandling*](entryhandling.htm)

•[SetStopLoss()](setstoploss.htm)

 


* Entry handling properties can be either programmatically set or set through the Strategy dialog window


 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleScaleOut\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleScaleOut_NT8.zip)





 
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
 
 
 



