










 


CumProfit







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?cumprofit.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradesPerformanceValues](tradesperformancevalues.htm) &gt;
CumProfit | [Previous page](averageprofit.htm)
[Return to chapter overview](tradesperformancevalues.htm)










Definition
----------


Returns the cumulative profit of the collection.  

 


Property Value
--------------


A double value that represents the cumulative profit of the collection.


 


Syntax
<tradecollection>.TradesPerformance.<tradesperformancevalues>.CumProfit
------------------------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the cumulative profit of all trades in currency
     Print("Average cumulative profit of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.CumProfit);
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