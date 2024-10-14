










 


TotalQuantity







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?totalquantity.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
TotalQuantity | [Previous page](totalcommission.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the total quantity.


 


Property Value
--------------


A double value that represents the total quantity.


 


Syntax
<tradecollection>.TradesPerformance.TotalQuantity
--------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the total quantity of all trades
     Print("Total quantity is: " + SystemPerformance.AllTrades.TradesPerformance.TotalQuantity);
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