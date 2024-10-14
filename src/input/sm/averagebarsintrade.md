










 


AverageBarsInTrade







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?averagebarsintrade.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
AverageBarsInTrade | [Previous page](tradesperformance.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the average number of bars per trade.  

 


Property Value
--------------


A double value that represents the average number of bars per trade.


 


Syntax
<tradecollection>.TradesPerformance.AverageBarsInTrade
-------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the average number of bars per trade of all trades
     Print("Average # bars per trade is: " + SystemPerformance.AllTrades.TradesPerformance.AverageBarsInTrade);
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