










 


Percent







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?percent.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
Percent | [Previous page](netprofit.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns a [TradesPerformanceValues](tradesperformancevalues.htm) object in percent.  

 


Property Value
--------------


A TradesPerformanceValues object that is represented in percent.


 


Syntax
<tradecollection>.TradesPerformance.Percent
--------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the avg. profit of all trades in percent
     Print("Average profit: " + SystemPerformance.AllTrades.TradesPerformance.Percent.AverageProfit);
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