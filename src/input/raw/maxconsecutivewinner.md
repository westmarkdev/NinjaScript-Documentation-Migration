










 


MaxConsecutiveWinner







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?maxconsecutivewinner.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
MaxConsecutiveWinner | [Previous page](maxconsecutiveloser.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the maximum number of consecutive winners seen.  

 


Property Value
--------------


An int value that represents the maximum number of consecutive winners seen.


 


Syntax
<tradecollection>.TradesPerformance.MaxConsecutiveWinner
---------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the max consecutive winners of all trades
     Print("Max # of consecutive winners is: " + SystemPerformance.AllTrades.TradesPerformance.MaxConsecutiveWinner);
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