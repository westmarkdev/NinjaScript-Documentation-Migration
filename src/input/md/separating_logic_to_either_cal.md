










 


Separating logic to either calculate once on bar close or on every tick







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?separating_logic_to_either_cal.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Separating logic to either calculate once on bar close or on every tick | [Previous page](scaling_out_of_a_position.htm)
[Return to chapter overview](strategy2.htm)










Depending on your trade ideas, the timing of entries and exits could be crucial. Sometimes waiting 30 seconds for a bar to close is too long when you are trying to exit a position. To address this you could select your strategy to calculate on every single tick, but this may impact your entry timings. For example, crossover entries could flip back and forth making it difficult to place entry orders. If you are facing this issue, it is possible to separate out parts of your strategy logic to calculate on every single tick and other parts to calculate once at the end of each bar.


 


Key concepts in this example
----------------------------


•Running some logic once per bar

•Running other logic on every single tick

 


Important related documentation
-------------------------------


•[Calculate](calculate.htm)

•[IsFirstTickOfBar](isfirsttickofbar.htm)

•[CrossBelow()](crossbelow.htm)

•[EnterLong()](enterlong.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleEnterOnceExitEveryTick\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleEnterOnceExitEveryTick_NT8.zip)





 
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
 
 
 



