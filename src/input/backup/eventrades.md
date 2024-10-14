










 


EvenTrades







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?eventrades.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt; [TradeCollection](tradecollection.htm) &gt;
EvenTrades | [Previous page](tradecollection_tradescount.htm)
[Return to chapter overview](tradecollection.htm)










Definition
----------


A subcollection of [Trade](trade.htm) objects consisting of only the non-winning and non-losing trades in a [TradeCollection](tradecollection.htm). 


 




|  |
| --- |
| Note: You can access a trade object by providing an index value. Trades are indexed sequentially meaning the oldest trade taken in a strategy will be at an index value of zero. The most recent trade taken will be at an index value of the total trades in the collection minus 1. |



 


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [Count](tradecollection_tradescount.htm) | An int value representing the number of trades in the collection |
| [GetTrades()](gettrades.htm) | Gets a [TradeCollection](tradecollection.htm) object representing a specified position |
| [TradesPerformance](tradesperformance.htm) | Gets a [TradesPerformance](tradesperformance.htm) object |



 


Syntax
<tradecollection>.EvenTrades
-----------------------------------



Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
     // Accesses the first/last losing trade in the strategy (oldest trade is at index 0)
     // and prints out the quantity NinjaScript Output window
     if (SystemPerformance.AllTrades.EvenTrades.Count &gt; 1)
     {
         Trade lastTrade = SystemPerformance.AllTrades.EvenTrades[SystemPerformance.AllTrades.Count - 1];
         Trade firstTrade = SystemPerformance.AllTrades.EvenTrades[0];
 
         Print("The last even trade's quantity was " + lastTrade.Quantity);
         Print("The first even trade's quantity was " + firstTrade.Quantity);
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