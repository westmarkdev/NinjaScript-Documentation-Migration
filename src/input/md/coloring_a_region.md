










 


Coloring a region







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?coloring_a_region.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Coloring a region | [Previous page](changing_fonts_for_draw_object.htm)
[Return to chapter overview](indicator2.htm)










Filling in a region between two DataSeries objects on your indicators can be beneficial for creating visual indicators. The colored regions allow for immediate recognition of various zones that can help a discretionary trader quickly identify what's important and trade accordingly.



This reference sample demonstrates the following concept
--------------------------------------------------------


•Coloring a region between two DataSeries objects

•Coloring a region between a DataSeries object and a double value

 


Important methods and properties used include
---------------------------------------------


•[Bollinger()](bollinger_bands.htm)

•[Draw.Region()](draw_region.htm)

Other methods and properties of interest include:


•[Draw.Diamond()](draw_diamond.htm)

•[Draw.Rectangle()](draw_rectangle.htm)

•[DrawOnPricePanel](drawonpricepanel.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleDrawRegion\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleDrawRegion_NT8.zip)





 
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
 
 
 



