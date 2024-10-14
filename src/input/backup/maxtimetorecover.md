










 


MaxTimeToRecover







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?maxtimetorecover.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
MaxTimeToRecover | [Previous page](maxconsecutivewinner.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the maximum time to recover from a draw down.  

 


Property Value
--------------


A TimeSpan value that represents the maximum time to recover from a draw down.


 


Syntax
<tradecollection>.TradesPerformance.MaxTimeToRecover
-----------------------------------------------------------


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the maximum time to recover from a draw down
     Print("Max time to recover is: " + SystemPerformance.AllTrades.TradesPerformance.MaxTimeToRecover);
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