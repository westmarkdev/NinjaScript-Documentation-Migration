










 


ProfitPerMonth







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?profitpermonth.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradesPerformanceValues](tradesperformancevalues.htm) &gt;
ProfitPerMonth | [Previous page](largestwinner.htm)
[Return to chapter overview](tradesperformancevalues.htm)










Definition
----------


Returns the profit per month of the collection. This value is always returned as a percentage.  

 


Property Value
--------------


A double value that represents the profit per month of the collection as a percentage.


 


Syntax
<tradecollection>.TradesPerformance.<tradesperformancevalues>.ProfitPerMonth
-----------------------------------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the profit per month of all trades
     Print("Profit per month of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.ProfitPerMonth);
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