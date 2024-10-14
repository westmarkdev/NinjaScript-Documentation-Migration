










 


RSquared







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?rsquared.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
RSquared | [Previous page](profitfactor.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the trade performance R-Squared value.  

 


Property Value
--------------


A double value that represents the R-Squared (R2)


 


Syntax
<tradecollection>.TradesPerformance.RSquared
---------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the R2 value of all trades
     Print("R-Squared is: " + SystemPerformance.AllTrades.TradesPerformance.RSquared);
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