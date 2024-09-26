










 


OnMarketData()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?superdomcolumn_onmarketdata.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [SuperDOM Column](superdom_column.htm) &gt;
OnMarketData() | [Previous page](superdomcolumn_marketdepth.htm)
[Return to chapter overview](superdom_column.htm)










Definition
----------


Called and guaranteed to be in the correct sequence for every change in level one market data for the underlying instrument. The OnMarketData() method updates can include but is not limited to the bid, ask, last price and volume.


 


Method Return Value
-------------------


This method does not return a value.


 


Syntax
------


protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)  

{  

   

}


 


Parameters
----------




|  |  |
| --- | --- |
| marketDataUpdate | A [MarketDataEventArgs](marketdataeventargs.htm) representing the change in market data |





Examples
--------




| ns |
| --- |
| protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
   if (marketDataUpdate.MarketDataType == Data.MarketDataType.Last)
   {
     // Do something
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
 
 
 



