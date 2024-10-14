










 


TradeCollection







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?tradecollection.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
TradeCollection | [Previous page](trade.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


A collection of [Trade](trade.htm) objects. You can access a trade object by providing an index value. Trades are indexed sequentially meaning the oldest trade taken in a strategy will be at an index value of zero. The most recent trade taken will be at an index value of the total trades in the collection minus 1.


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [TradesCount](tradecollection_tradescount.htm) | An int value representing the number of trades in the collection |
| [EvenTrades](eventrades.htm) | Gets a TradeCollection object of even trades |
| [GetTrades()](gettrades.htm) | Gets a TradeCollection object representing a specified position |
| [LosingTrades](losingtrades.htm) | Gets a TradeCollection object of losing trades |
| [TradesPerformance](tradesperformance.htm) | Gets a [TradesPerformance](tradesperformance.htm) object |
| [WinningTrades](winningtrades.htm) | Gets a TradeCollection object of winning trades |



 


 


Examples
--------





| nsExample 1 |
| --- |
| protected override void OnBarUpdate()
{
   // Accesses the first/last trade in the strategy (oldest trade is at index 0)
   // and prints out the profit as a percentage to the output window
   if (SystemPerformance.AllTrades.Count &gt; 1)
   {
       Trade lastTrade = SystemPerformance.AllTrades[SystemPerformance.AllTrades.Count - 1];
       Trade firstTrade = SystemPerformance.AllTrades[0];
 
       Print("The last trade profit is " + lastTrade.ProfitPercent);
       Print("The first trade profit is " + firstTrade.ProfitPercent);
   }
} |



 




| nsExample 2 |
| --- |
| protected override void OnBarUpdate()
{
   // Once the strategy has executed 20 trades loop through the losing trades
   // collection and print out the PnL on only long trades
   if (SystemPerformance.AllTrades.Count == 20)
   {
       Print("There are " + SystemPerformance.AllTrades.LosingTrades.Count + " losing trades.");
       foreach (Trade myTrade in SystemPerformance.AllTrades.LosingTrades)
       {
           if (myTrade.Entry.MarketPosition == MarketPosition.Long)
               Print(myTrade.ProfitCurrency);
       }
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
 
 
 



