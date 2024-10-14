










 


AverageTotalEfficiency







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?averagetotalefficiency.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
AverageTotalEfficiency | [Previous page](averagetimeinmarket.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the average total efficiency.  

 


Property Value
--------------


A double value that represents the average total efficiency.


 


Syntax
<tradecollection>.TradesPerformance.AverageTotalEfficiency
-----------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the average total efficiency
     Print("Average total efficiency is: " + SystemPerformance.AllTrades.TradesPerformance.AverageTotalEfficiency);
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