










 


ProfitFactor







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?profitfactor.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
ProfitFactor | [Previous page](points.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the profit factor.  

 


Property Value
--------------


A double value that represents the profit factor.


 


Syntax
<tradecollection>.TradesPerformance.ProfitFactor
-------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the profit factor of all trades
     Print("Profit factor is: " + SystemPerformance.AllTrades.TradesPerformance.ProfitFactor);
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