










 


AverageTimeInMarket







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?averagetimeinmarket.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
AverageTimeInMarket | [Previous page](averageexitefficiency.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the average duration of a trade weighted by quantity.  

 


Property Value
--------------


A TimeSpan value that represents the quantity-weighted average duration of a trade.


 


Syntax
<tradecollection>.TradesPerformance.AverageTimeInMarket
--------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the quantity-weighted average duration of all trades
     Print("Average time in market: " + SystemPerformance.AllTrades.TradesPerformance.AverageTimeInMarket);
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
 
 
 



</tradecollection>