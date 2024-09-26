










 


LongestFlatPeriod







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?longestflatperiod.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt; [TradesPerformance](tradesperformance.htm) &gt;
LongestFlatPeriod | [Previous page](grossprofit.htm)
[Return to chapter overview](tradesperformance.htm)










Definition
----------


Returns the longest duration of being flat.  

 


Property Value
--------------


A TimeSpan value that represents the longest duration of being flat.


 


Syntax
<tradecollection>.TradesPerformance.LongestFlatPeriod
------------------------------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the longest duration of being flat
     Print("Longest flat period: " + SystemPerformance.AllTrades.TradesPerformance.LongestFlatPeriod);
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