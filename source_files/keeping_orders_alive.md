










 


Keeping orders alive







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?keeping_orders_alive.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Keeping orders alive | [Previous page](halting_a_strategy_once_user_d.htm)
[Return to chapter overview](strategy2.htm)










The default behavior for NinjaTrader is to cancel limit orders if the trigger conditions are no longer true. It is possible to submit orders that stay active until cancelled by setting liveUntilCancelled to true. This sample demonstrates and explains the difference between submitting an order with isLiveUntilCancelled true and false. The comments contain a longer, more detailed explanation.


 


Key concepts in this example:
-----------------------------


•How to submit an order that stays active until it is explicitly canceled*

*Another sample demonstrating how to explicitly cancel orders can be found here: [Using CancelOrder() method to cancel orders](using_cancelorder_method_to_ca.htm)


 


Important related documentation
-------------------------------


•[EnterLongLimit()](enterlonglimit.htm)

•[isliveUntilCancelled](exitlonglimit.htm)

•[CrossAbove()](crossabove.htm)

•[CrossBelow()](crossbelow.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleIsLiveUntilCanceled\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleIsLiveUntilCanceled_NT8.zip)





 
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
 
 
 



