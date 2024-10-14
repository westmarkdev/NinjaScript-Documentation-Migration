










 


Modifying the price of stop loss and profit target orders







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?modifying_the_price_of_stop_lo.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Modifying the price of stop loss and profit target orders | [Previous page](keeping_orders_alive.htm)
[Return to chapter overview](strategy2.htm)










One of the benefits of NinjaScript is the ability to automatically submit stop loss and profit target orders in real-time triggered when your entry order is filled.


 


Key concepts in this example
----------------------------


•Submitting a stop loss and profit target order using default values offset from your entry order average fill price

•Modification of the stop loss order to a break even price once a desired level of profit has been reached

 


Important related documentation
-------------------------------


•[SetStopLoss()](setstoploss.htm)

•[SetProfitTarget()](setprofittarget.htm)

•[SetTrailStop()](settrailstop.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SamplePriceModification\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SamplePriceModification_NT8.zip)





 
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
 
 
 



