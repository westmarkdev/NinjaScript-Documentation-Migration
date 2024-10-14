










 


Calculating the highest high or lowest low for a specified time range







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?calculating_the_highest_high_o.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Calculating the highest high or lowest low for a specified time range | [Previous page](indicator2.htm)
[Return to chapter overview](indicator2.htm)










Determining a high or low value for given time range can be useful.


 


Key concepts in this example
----------------------------


•Converting time to bars ago values

•Getting the highest high and lowest low values

 


Important related documentation
-------------------------------


•[GetBar()](getbar.htm)

•[MAX()](maximum_max.htm)

•[MIN()](minimum_min.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleGetHighLowByTimeRange\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleGetHighLowByTimeRange_NT8.zip)





 
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
 
 
 



