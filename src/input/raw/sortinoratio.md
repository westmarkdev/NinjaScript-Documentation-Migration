










 


SortinoRatio







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sortinoratio.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
SortinoRatio | [Previous page](sharperatio.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the Sortino ratio using a [risk free return](riskfreereturn.htm).  

 


Property Value
--------------


A double value that represents the Sortino ratio using a risk free return.


 


Syntax
<tradecollection>.TradesPerformance.SortinoRatio
-------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Set a 0% risk free return
     SystemPerformance.AllTrades.TradesPerformance.RiskFreeReturn = 0;
 
     // Print out the Sortino ratio of all trades based on a zero risk free return
     Print("Sortino ratio is: " + SystemPerformance.AllTrades.TradesPerformance.SortinoRatio);
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