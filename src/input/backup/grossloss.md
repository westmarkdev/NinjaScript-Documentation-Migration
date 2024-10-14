










 


GrossLoss







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?grossloss.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
GrossLoss | [Previous page](currency.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the gross loss.  

 


Property Value
--------------


A double value that represents the gross loss.


 


Syntax
<tradecollection>.TradesPerformance.GrossLoss
----------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the gross loss of all trades
     Print("Gross loss is: " + SystemPerformance.AllTrades.TradesPerformance.GrossLoss);
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