










 


RiskFreeReturn







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?riskfreereturn.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
RiskFreeReturn | [Previous page](rsquared.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


The risk free return used in calculations of [Sharpe](sharperatio.htm) and [Sortino](sortinoratio.htm) ratios.  

 


Property Value
--------------


A double value that represents the risk free return.


 


Syntax
<tradecollection>.TradesPerformance.RiskFreeReturn
---------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Set a 3.5% risk free return
     SystemPerformance.AllTrades.TradesPerformance.RiskFreeReturn = 0.035;
 
     // Print out the Sharpe ratio of all trades based on a 3.5% risk free return
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