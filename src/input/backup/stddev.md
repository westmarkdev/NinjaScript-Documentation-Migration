










 


StdDev







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?stddev.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradesPerformanceValues](tradesperformancevalues.htm) &gt;
StdDev | [Previous page](profitpermonth.htm)
[Return to chapter overview](tradesperformancevalues.htm)










Definition
----------


Returns the standard deviation of the collection on a per unit basis.  

 


Property Value
--------------


A double value that represents the standard deviation of the collection on a per unit basis.


 


Syntax
<tradecollection>.TradesPerformance.<tradesperformancevalues>.StdDev
---------------------------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the standard deviation of all trades
     Print("Standard deviation of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.StdDev);
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