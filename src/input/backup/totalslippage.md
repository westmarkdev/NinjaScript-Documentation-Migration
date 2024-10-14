










 


TotalSlippage







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?totalslippage.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
TotalSlippage | [Previous page](totalquantity.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the total slippage.


 


Property Value
--------------


A double value that represents the total slippage. This is presented in points, I.E. 0.25 for 1 execution on E-mini S&amp;P 500 Futures.


 


Syntax
<tradecollection>.TradesPerformance.TotalSlippage
--------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the total slippage of all trades
     Print("Total slippage is: " + SystemPerformance.AllTrades.TradesPerformance.TotalSlippage);
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