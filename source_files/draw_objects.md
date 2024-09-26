










 


Draw Objects







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?draw_objects.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Draw Objects | [Previous page](creating_your_own_level_ii_dat.htm)
[Return to chapter overview](indicator2.htm)










Being able to mark visually conditions of interest on the chart is useful for the discretionary trader. With NinjaScript you can draw various objects onto your chart to alert you of these points of interest.


 


Key concepts in this example
----------------------------


•Drawing unique diamonds to mark the beginning and end of uptrends

•Drawing and updating a single rectangle that marks the current uptrend

 


Important related documentation
-------------------------------


•[Drawing](drawing.htm)

•[Draw.Diamond()](draw_diamond.htm)

•[Draw.Rectangle()](draw_rectangle.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript  

3.Select the downloaded file

 


[SampleDrawObject\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleDrawObject_NT8.zip)





 
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
 
 
 



