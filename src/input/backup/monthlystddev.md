










 


MonthlyStdDev







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?monthlystddev.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
MonthlyStdDev | [Previous page](maxtimetorecover.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the monthly standard deviation.


 


Property Value
--------------


A double value that represents the monthly standard deviation.


 


Syntax
<tradecollection>.TradesPerformance.MonthlyStdDev
--------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the monthly standard deviation
     Print("Monthly standard deviation is: " + SystemPerformance.AllTrades.TradesPerformance.MonthlyStdDev);
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