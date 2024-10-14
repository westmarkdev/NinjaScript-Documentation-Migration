










 


Getting indicator values from a specified time







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getting_indicator_values_from_.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Getting indicator values from a specified time | [Previous page](exposing_indicator_values_that.htm)
[Return to chapter overview](indicator2.htm)










Sometimes, you may want to access a value from a historical point in time, but have not kept track of the value to make this readily available. With NinjaScript, it is possible to pick a bar based on time to access that value. GetBar() returns the number of bars ago that holds the same timestamp of the time you request. This sample demonstrates how to get an indicator value from 9:30AM of the previous trading day.


 


Key concepts in this example
----------------------------


•Obtaining a Simple Moving Average value from a specific time by referencing the bar number for that time.

 


Important related documentation
-------------------------------


•[GetBar()](getbar.htm)

•[Draw.Line()](draw_line.htm)

•[Time](iseries_time.htm)

•[Sessions](tradinghours_sessions.htm)

•[DateTime](https://learn.microsoft.com/en-us/dotnet/api/system.datetime?view=netframework-4.8)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleGetBar\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleGetBar_NT8.zip)





 
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
 
 
 



