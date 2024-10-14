










 


LargestWinner







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?largestwinner.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradesPerformanceValues](tradesperformancevalues.htm) &gt;
LargestWinner | [Previous page](largestloser.htm)
[Return to chapter overview](tradesperformancevalues.htm)










Definition
----------


Returns the largest win amount of the collection.  

 


Property Value
--------------


A double value that represents the largest win amount of the collection.


 


Syntax
<tradecollection>.TradesPerformance.<tradesperformancevalues>.LargestWinner
----------------------------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the largest win of all trades in currency
     Print("Largest win of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.LargestWinner);
} |






 
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
 
 
 



</tradesperformancevalues></tradecollection>