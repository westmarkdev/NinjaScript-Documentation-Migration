﻿










 


LongTrades







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?longtrades.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [SystemPerformance](systemperformance.htm) &gt;
LongTrades | [Previous page](alltrades.htm)
[Return to chapter overview](systemperformance.htm)










Definition
----------


LongTrades is a [TradeCollection](tradecollection.htm) object of long trades generated by a strategy.


 


Syntax
------


SystemPerformance.LongTrades



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the number of long trades
     Print("The strategy has taken " + SystemPerformance.LongTrades.Count + " long trades.");
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
 
 
 



