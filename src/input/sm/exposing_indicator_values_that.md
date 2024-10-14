










 


Exposing indicator values that are not plots







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?exposing_indicator_values_that.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Exposing indicator values that are not plots | [Previous page](ensuring_indicator_plots_are_v.htm)
[Return to chapter overview](indicator2.htm)










There may be cases where you want to have your indicator calculate non-plotted values that you will want to access when using this indicator inside of another indicator or strategy.


 


Key concepts in this example
----------------------------


•Creating exposed BoolSeries objects

•Storing and retrieving values from BoolSeries objects

 


Important related documentation
-------------------------------


•[Series<t>](seriest.htm)

We suggest using an available class that implements the Series interface.


•[Price Series](priceseries.htm)

•[Time Series](timeseries.htm)

•[Volume Series](volumeseries.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleBoolSeries\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleBoolSeries_NT8.zip)





 
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
 
 
 



</t>