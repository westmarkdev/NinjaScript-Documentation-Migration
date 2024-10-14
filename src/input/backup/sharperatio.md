










 


SharpeRatio







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?sharperatio.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
SharpeRatio | [Previous page](riskfreereturn.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the Sharpe ratio using a [risk free return](riskfreereturn.htm).  

 


Property Value
--------------


A double value that represents the Sharpe ratio using a risk free return.


 


Syntax
<tradecollection>.TradesPerformance.SharpeRatio
------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Set a 0% risk free return
     SystemPerformance.AllTrades.TradesPerformance.RiskFreeReturn = 0;
 
     // Print out the Sharpe ratio of all trades based on a zero risk free return
     Print("Sharpe ratio is: " + SystemPerformance.AllTrades.TradesPerformance.SharpeRatio);
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