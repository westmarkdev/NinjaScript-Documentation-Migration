










 


Removing draw objects from the chart







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?removing_draw_objects_from_the.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Reference Samples](reference_samples.htm) &gt; [Strategy](strategy2.htm) &gt;
Removing draw objects from the chart | [Previous page](plotting_from_within_a_ninjasc.htm)
[Return to chapter overview](strategy2.htm)










Drawing objects can be used for a number of different purposes, like keeping track of where a strategy has its entry point, profit target, and stop loss. If a strategy draws an object(s) for every trade it takes, the chart could quickly become cluttered. This sample will show how to remove the objects that aren't necessary anymore.


 




|  |
| --- |
| Note: This is a real-time only strategy. Please view this strategy on a real-time data connection or the Simulated Data Feed. |





Key concepts in this example
----------------------------


•Drawing lines at the price where the orders are that extend for the duration of the trade

•Removing those lines when the trade is over

 


Important related documentation
-------------------------------


•[Draw](drawing.htm)

•[Line()](line.htm)

•[RemoveDrawObject()](removedrawobject.htm)

•[RemoveDrawObjects()](removedrawobjects.htm)

•[CrossAbove()](crossabove.htm)

•[CrossBelow()](crossbelow.htm)

 


Import instructions
-------------------


1.Download the file contained in this Help Guide topic to your PC desktop

2.From the Control Center window, select the menu Tools &gt; Import &gt; NinjaScript

3.Select the downloaded file

 


[SampleRemoveDrawObjects\_NT8.zip](https://ninjatrader.com/support/helpGuides/nt8/samples/SampleRemoveDrawObjects_NT8.zip)





 
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
 
 
 



