










 


MaxConsecutiveLoser







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?maxconsecutiveloser.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
MaxConsecutiveLoser | [Previous page](longestflatperiod.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the maximum number of consecutive losers seen.  

 


Property Value
--------------


An int value that represents the maximum number of consecutive losers seen.


 


Syntax
<tradecollection>.TradesPerformance.MaxConsecutiveLoser
--------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the max consecutive losers of all trades
     Print("Max # of consecutive losers is: " + SystemPerformance.AllTrades.TradesPerformance.MaxConsecutiveLoser);
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