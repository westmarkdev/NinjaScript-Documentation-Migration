










 


Ensuring indicator plots are valid before programmatically accessing them







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ensuring_indicator_plots_are_v.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Indicator](indicator2.htm) &gt;
Ensuring indicator plots are valid before programmatically accessing them | [Previous page](draw_objects.htm)
[Return to chapter overview](indicator2.htm)










When accessing NinjaScript indicators in other scripts it is important to check if the hosted indicator's plot values are already set prior to use in the hosting script. This check ensures that proper values are always used and that irrelevant values do not throw off the script logic. This reference sample demonstrates how to run these checks in a hosting indicator by checking another hosted indicator for set plot values.


 


Another example for when you would want to use this is if you were trying to access the Pivots indicator, but did not have enough days loaded to properly calculate those values yet. Basing logic on the Pivots in such a scenario would yield values that are not useful and can be detrimental if not handled correctly in your code.


 


Key concepts in this example
----------------------------


•Checking indicator plots for valid values

•Handling logic for when the indicator plots are not valid

 


Attached archive contains two indicator files
---------------------------------------------


•SampleEveryNBarTest is the hosting indicator

•SampleEveryNBar is the hosted indicator

 




|  |
| --- |
| Note: When hosting an indicator in an Indicator column in the Market Analyzer you will need to manually ensure enough bars back are loaded for the indicator to calculate correctly. |



 


Important related documentation
-------------------------------


•[IsValidDataPoint()](isvaliddatapoint.htm)

•[Series](seriest.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleEveryNBarTest\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleEveryNBarTest_NT8.zip)





 
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
 
 
 



