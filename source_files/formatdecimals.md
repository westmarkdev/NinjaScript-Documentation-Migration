










 


FormatDecimals







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?formatdecimals.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Market Analyzer Column](market_analyzer_column.htm) &gt;
FormatDecimals | [Previous page](datatype.htm)
[Return to chapter overview](market_analyzer_column.htm)










Definition
----------


Rounds the value contained in [CurrentValue](currentvalue.htm) to a specified number of decimal places before displaying it in the Market Analyzer column.


 


Property Value
--------------


An int representing a number of decimal places to which to round CurrentValue


 


Syntax
------


FormatDecimals


 


Example
-------




| ns |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
       // Round CurrentValue to one decimal place
       FormatDecimals = 1;
   }
}
 
protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
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
 
 
 



