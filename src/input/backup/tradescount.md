










 


TradesCount







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?tradescount.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
TradesCount | [Previous page](totalslippage.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the total # of trades.


 


Property Value
--------------


A double value that represents the total # of trades.


 


Syntax
<tradecollection>.TradesPerformance.TradesCount
------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the total # of trades
     Print("Trades count is: " + SystemPerformance.AllTrades.TradesPerformance.TradesCount);
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