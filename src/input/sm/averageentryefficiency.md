










 


AverageEntryEfficiency







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?averageentryefficiency.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
AverageEntryEfficiency | [Previous page](averagebarsintrade.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the average entry efficiency.  

 


Property Value
--------------


A double value that represents the average entry efficiency.


 


Syntax
<tradecollection>.TradesPerformance.AverageEntryEfficiency
-----------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the average entry efficiency
     Print("Average entry efficiency is: " + SystemPerformance.AllTrades.TradesPerformance.AverageEntryEfficiency);
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