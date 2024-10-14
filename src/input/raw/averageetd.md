










 


AverageEtd







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?averageetd.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradesPerformanceValues](tradesperformancevalues.htm) &gt;
AverageEtd | [Previous page](tradesperformancevalues.htm)
[Return to chapter overview](tradesperformancevalues.htm)










Definition
----------


Returns the average ETD (end trade draw down) of the collection.  

 


Property Value
--------------


A double value that represents the average ETD of the collection.


 


Syntax
<tradecollection>.TradesPerformance.<tradesperformancevalues>.AverageEtd
-------------------------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the average ETD of all trades in currency
     Print("Average ETD of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.AverageEtd);
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