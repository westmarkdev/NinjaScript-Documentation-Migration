










 


PriorValue







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?priorvalue.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Market Analyzer Column](market_analyzer_column.htm) &gt;
PriorValue | [Previous page](onrender2.htm)
[Return to chapter overview](market_analyzer_column.htm)










Definition
----------


Contains the last value of [CurrentValue](currentvalue.htm). PriorValue is assigned the value of CurrentValue immediately before CurrentValue is updated.


 


Property Value
--------------


A double containing the last value contained in CurrentValue before its most recent update


 


Syntax
------


PriorValue


 



Example
-------




| ns |
| --- |
| protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
   if (marketDataUpdate.MarketDataType == MarketDataType.Last)
   {
       CurrentValue = marketDataUpdate.Price;
 
       // Trigger an alert if the current Last price update is greater than the previous one
       if(CurrentValue &gt; PriorValue)
           Alert("MA Alert", Priority.High, "Check Market Analyzer", "", 30, Brushes.Black, Brushes.White);
   }
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
 
 
 



