










 


TotalCommission







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?totalcommission.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
TotalCommission | [Previous page](ticks.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the total commission.  

 


Property Value
--------------


A double value that represents the total commission.


 


Syntax
<tradecollection>.TradesPerformance.TotalCommission
----------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the total commission of all trades
     Print("Total commission is: " + SystemPerformance.AllTrades.TradesPerformance.TotalCommission);
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