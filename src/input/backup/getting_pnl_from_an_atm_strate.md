










 


Getting PnL from an ATM strategy







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getting_pnl_from_an_atm_strate.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Getting PnL from an ATM strategy | [Previous page](entering_on_one_time_frame_and.htm)
[Return to chapter overview](strategy2.htm)










When integrating Advanced Trade Management templates into NinjaScript Strategies, the procedure for obtaining trade performance and order status is a little different than for strategies without ATM templates. The difference is that ATM templates basically take over and manage the trade separately from the NinjaScript portion of the strategy. Until the ATM trade terminates, the NinjaScript portion just observes and waits for another trading opportunity. Accessing all the trade data is still possible, but the set of commands to use differ from the traditional NinjaScript commands. This sample borrows code from the built-in strategy SampleAtmStrategy and doesn't include all the references specific to that strategy. In addition, this sample draws some profit/loss information right on the chart.


 




|  |
| --- |
| Note: This is a real-time strategy only. You will also need to first setup an ATM template titled "AtmStrategyTemplate" for this sample to work. You can set this up in the SuperDOM or Chart Trader windows. |





Key concepts in this example
----------------------------


•Obtaining unrealized and realized profit/loss from ATM templates initiated by a NinjaScript strategy

•Keeping a running total of all the realized profits/losses

 


Important related documentation
-------------------------------


•[GetAtmStrategyRealizedProfitLoss()](getatmstrategyrealizedprofitlo.htm)

•[GetAtmStrategyUnrealizedProfitLoss()](getatmstrategyunrealizedprofit.htm)

•[Draw.TextFixed()](draw_textfixed.htm)

•[RoundToTickSize()](roundtoticksize.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleATMPnL\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleATMPnL_NT8.zip)





 
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
 
 
 



