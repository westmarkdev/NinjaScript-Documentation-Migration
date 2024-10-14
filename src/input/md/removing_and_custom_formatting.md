










 


Removing and Custom Formatting an Indicator’s Chart Label







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?removing_and_custom_formatting.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Removing and Custom Formatting an Indicator’s Chart Label | [Previous page](multi-colored_plots.htm)
[Return to chapter overview](indicator2.htm)










If you create a NinjaScript indicator or strategy with many customizable parameters, you will have a long label when you load the NinjaScript onto your chart. This may be visually cumbersome so you may want to trim the displayed label to a more manageable size that only contains the most important parameters.


 


Key concepts in this example:
-----------------------------


•Creating a custom string for the label of the NinjaScript item.

 


Important related documentation
-------------------------------


•[Draw.TextFixed()](draw_textfixed.htm)

•[Draw.Text()](draw_text.htm)

•[Override DisplayName()](indicator_displayname.htm)

 


 




|  |
| --- |
| Tip: When adding an indicator onto a chart you can also completely remove any labeling on the chart of the indicator name. You can do this by clearing the "Label" field under the "General" category when you add the indicator onto the chart. |



 


 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleDisplayName\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleDisplayName_NT8.zip)





 
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
 
 
 



