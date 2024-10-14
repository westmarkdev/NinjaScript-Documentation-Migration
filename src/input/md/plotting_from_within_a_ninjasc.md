










 


Plotting from within a NinjaScript Strategy







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?plotting_from_within_a_ninjasc.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Plotting from within a NinjaScript Strategy | [Previous page](monitoring_stop-loss_and_profi.htm)
[Return to chapter overview](strategy2.htm)










When running a strategy on a chart you may find the need to plot values onto a chart. If these values are internal strategy calculations that are difficult to migrate to an indicator, you can use the following technique to achieve a plot.


 


With NinjaTrader 8 we introduced strategy plots which provide the ability for a strategy to render its own plots. These plots must be specific to a single panel just like indicators. If you need to have strategy plots on more than a single panel then please use the technique seen in the attached sample. You can find documentation on the standard methods for plotting in the Indicator help guide section, although the documents are for indicators the plotting items are shared between indicators and strategies.


 


Important related documentation:
--------------------------------


•[Plotting from a strategy with Indicator plot methods](addplot.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleStrategyPlot\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleStrategyPlot_NT8.zip)





 
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
 
 
 



