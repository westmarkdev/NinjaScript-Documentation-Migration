










 


GrossProfit







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?grossprofit.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
GrossProfit | [Previous page](grossloss.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the gross profit.  

 


Property Value
--------------


A double value that represents the gross profit.


 


Syntax
<tradecollection>.TradesPerformance.GrossProfit
------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the gross profit of all trades
     Print("Gross profit is: " + SystemPerformance.AllTrades.TradesPerformance.GrossProfit);
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