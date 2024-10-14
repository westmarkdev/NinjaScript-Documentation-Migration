










 


TradesCount







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?tradecollection_tradescount.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt;
TradesCount | [Previous page](tradecollection.htm)
[Return to chapter overview](tradecollection.htm)










Definition
----------


Indicates the number of trades in the collection.


 


Property Value
--------------


An int value that represents the number of trades in the collection.


 


Syntax
<tradecollection>.Count
------------------------------


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Print out the number of long trades
     Print("The strategy has taken " + SystemPerformance.LongTrades.TradesCount + " long trades.");
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