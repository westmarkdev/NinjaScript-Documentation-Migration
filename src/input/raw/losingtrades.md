










 


LosingTrades







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?losingtrades.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt;
LosingTrades | [Previous page](gettrades.htm)
[Return to chapter overview](tradecollection.htm)










Definition
----------


A subcollection of [Trade](trade.htm) objects consisting of only the losing trades in a [TradeCollection](tradecollection.htm). You can access a trade object by providing an index value. Trades are indexed sequentially meaning the oldest trade taken in a strategy will be at an index value of zero. The most recent trade taken will be at an index value of the total trades in the collection minus 1.


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [Count](tradecollection_tradescount.htm) | An int value representing the number of trades in the collection |
| [GetTrades()](gettrades.htm) | Gets a [TradeCollection](tradecollection.htm) object representing a specified position |
| [TradesPerformance](tradesperformance.htm) | Gets a [TradesPerformance](tradesperformance.htm) object |



 


Syntax
<tradecollection>.LosingTrades
-------------------------------------


 


 



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Accesses the first/last losing trade in the strategy (oldest trade is at index 0)
     // and prints out the profit as a percentage to the output window
     if (SystemPerformance.AllTrades.LosingTrades.Count &gt; 1)
     {
         Trade lastTrade = SystemPerformance.AllTrades.LosingTrades[SystemPerformance.AllTrades.Count - 1];
         Trade firstTrade = SystemPerformance.AllTrades.LosingTrades[0];
 
         Print("The last losing trade's profit was " + lastTrade.ProfitPercent);
         Print("The first losing trade's profit was " + firstTrade.ProfitPercent);
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
 
 
 



</tradecollection>