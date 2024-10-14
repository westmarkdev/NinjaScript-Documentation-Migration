










 


CurrentValue







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?currentvalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Market Analyzer Column](market_analyzer_column.htm) &gt;
CurrentValue | [Previous page](currenttext.htm)
[Return to chapter overview](market_analyzer_column.htm)










Definition
----------


The value to be displayed in the Market Analyzer Column


 


Property Value
--------------


A double representing the value to be displayed in the column


 


Syntax
------


CurrentValue



Example
-------




| ns |
| --- |
| protected override void OnMarketData(Data.MarketDataEventArgs marketDataUpdate)
{
     CurrentValue = marketDataUpdate.Price;
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
 
 
 



