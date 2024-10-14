










 


NetProfit







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?netprofit.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
NetProfit | [Previous page](monthlyulcer.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the net profit.  

 


Property Value
--------------


A double value that represents the net profit.


 


Syntax
<tradecollection>.TradesPerformance.NetProfit
----------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the net profit of all trades
     Print("Net profit is: " + SystemPerformance.AllTrades.TradesPerformance.NetProfit);
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