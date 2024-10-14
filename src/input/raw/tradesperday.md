










 


TradesPerDay







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?tradesperday.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
TradesPerDay | [Previous page](tradescount.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the average number of trades per day.  

 


Property Value
--------------


An int value that represents the average number of trades per day.


 


Syntax
<tradecollection>.TradesPerformance.TradesPerDay
-------------------------------------------------------


 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the average number of trades per day of all trades
     Print("Average # of trades per day is: " + SystemPerformance.AllTrades.TradesPerformance.TradesPerDay);
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