










 


AverageExitEfficiency







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?averageexitefficiency.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
AverageExitEfficiency | [Previous page](averageentryefficiency.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the average exit efficiency.  

 


Property Value
--------------


A double value that represents the average exit efficiency.


 


Syntax
<tradecollection>.TradesPerformance.AverageExitEfficiency
----------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the average exit efficiency
     Print("Average exit efficiency is: " + SystemPerformance.AllTrades.TradesPerformance.AverageExitEfficiency);
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