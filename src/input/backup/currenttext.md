










 


CurrentText







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?currenttext.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Market Analyzer Column](market_analyzer_column.htm) &gt;
CurrentText | [Previous page](market_analyzer_column.htm)
[Return to chapter overview](market_analyzer_column.htm)










Definition
----------


Sets text to be displayed in the Market Analyzer column.





|  |
| --- |
| Note: CurrentText will overrule any value set for [CurrentValue](currentvalue.htm). If both CurrentValue and CurrentText have assigned values, the value of CurrentText will display in the column. |




Property Value
--------------


A string representing text to display in the column


 


Syntax
------


CurrentText



Example
-------




| ns |
| --- |
| protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
   // Print "Ask" in the column if an Ask price update is received
   if(marketDataUpdate.MarketDataType == MarketDataType.Ask)
       CurrentText = "Ask";
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
 
 
 



