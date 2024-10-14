










 


Trading crossovers







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?trading_crossovers.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Trading crossovers | [Previous page](stopping_a_strategy_after_cons.htm)
[Return to chapter overview](strategy2.htm)










Similar in concept to a breakout, many traders like to trade crossovers. This can be a crossover of price from a certain threshold or even an indicator crossing over another indicator.


 


Key concepts in this example
----------------------------


•Determining and storing the first 15 bar high and low values for the current session

•Submitting long or short entry orders depending on which threshold is crossed

•Using a trail stop to exit positions

 




|  |
| --- |
| Tip: This reference sample sets Calculat to OnEachTick. The reason we are doing this is so we can submit orders as soon as a crossover occurs instead of waiting for the bar to close before submitting the order. |



 


 


Important related documentation
-------------------------------


•[Calculate](calculate.htm)

•[CrossAbove()](crossabove.htm)

•[CrossBelow()](crossbelow.htm)

•[SetTrailStop()](settrailstop.htm)

•[SetStopLoss()](setstoploss.htm)

•[SetProfitTarget()](setprofittarget.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleHighLowCross\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleHighLowCross_NT8.zip)





 
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
 
 
 



