










 


Ticks







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?ticks.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
Ticks | [Previous page](sortinoratio.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns a [TradesPerformanceValues](tradesperformancevalues.htm) object in ticks.  

 


Property Value
--------------


A TradesPerformanceValues object that is represented in ticks.


 


Syntax
<tradecollection>.TradesPerformance.Ticks
------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the avg. profit of all trades in ticks
     Print("Average profit: " + SystemPerformance.AllTrades.TradesPerformance.Ticks.AverageProfit);
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