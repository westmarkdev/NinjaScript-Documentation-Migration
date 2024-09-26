﻿










 


AverageMae







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?averagemae.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradesPerformanceValues](tradesperformancevalues.htm) &gt;
AverageMae | [Previous page](averageetd.htm)
[Return to chapter overview](tradesperformancevalues.htm)










Definition
----------


Returns the average MAE (max adverse excursion) of the collection.  

 


Property Value
--------------


A double value that represents the average MAE of the collection.


 


Syntax
<tradecollection>.TradesPerformance.<tradesperformancevalues>.AverageMae
-------------------------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the average MAE of all trades in currency
     Print("Average MAE of all trades is: " + SystemPerformance.AllTrades.TradesPerformance.Currency.AverageMae);
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