---
title: "TradeCollection"
pathName: /docs/desktop/tradecollection
---

## Definition

A collection of [Trade](/docs/desktop/trade) objects. You can access a trade object by providing an index value. Trades are indexed sequentially meaning the oldest trade taken in a strategy will be at an index value of zero. The most recent trade taken will be at an index value of the total trades in the collection minus 1.

## Methods and Properties

|  |  |
| --- | --- |
| [TradesCount](/docs/desktop/tradecollection_tradescount) | An `int` value representing the number of trades in the collection |
| [EvenTrades](/docs/desktop/eventrades) | Gets a TradeCollection object of even trades |
| [GetTrades()](/docs/desktop/gettrades) | Gets a TradeCollection object representing a specified position |
| [LosingTrades](/docs/desktop/losingtrades) | Gets a TradeCollection object of losing trades |
| [TradesPerformance](/docs/desktop/tradesperformance) | Gets a [TradesPerformance](/docs/desktop/tradesperformance) object |
| [WinningTrades](/docs/desktop/winningtrades) | Gets a TradeCollection object of winning trades |

## Examples

| nsExample 1 |
| --- |
| protected override void OnBarUpdate() <br> { <br> &nbsp; &nbsp; // Accesses the first/last trade in the strategy (oldest trade is at index 0) <br> &nbsp; &nbsp; // and prints out the profit as a percentage to the output window <br> &nbsp; &nbsp; if (SystemPerformance.AllTrades.Count > 1) <br> &nbsp; &nbsp; { <br> &nbsp; &nbsp; &nbsp; &nbsp; Trade lastTrade = SystemPerformance.AllTrades[SystemPerformance.AllTrades.Count - 1]; <br> &nbsp; &nbsp; &nbsp; &nbsp; Trade firstTrade = SystemPerformance.AllTrades[0]; <br> &nbsp; &nbsp; &nbsp; &nbsp; Print("The last trade profit is " + lastTrade.ProfitPercent); <br> &nbsp; &nbsp; &nbsp; &nbsp; Print("The first trade profit is " + firstTrade.ProfitPercent); <br> &nbsp; &nbsp; } <br> } |

| nsExample 2 |
| --- |
| protected override void OnBarUpdate() <br> { <br> &nbsp; &nbsp; // Once the strategy has executed 20 trades loop through the losing trades <br> &nbsp; &nbsp; // collection and print out the PnL on only long trades <br> &nbsp; &nbsp; if (SystemPerformance.AllTrades.Count == 20) <br> &nbsp; &nbsp; { <br> &nbsp; &nbsp; &nbsp; &nbsp; Print("There are " + SystemPerformance.AllTrades.LosingTrades.Count + " losing trades."); <br> &nbsp; &nbsp; &nbsp; &nbsp; foreach (Trade myTrade in SystemPerformance.AllTrades.LosingTrades) <br> &nbsp; &nbsp; &nbsp; &nbsp; { <br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; if (myTrade.Entry.MarketPosition == MarketPosition.Long) <br> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Print(myTrade.ProfitCurrency); <br> &nbsp; &nbsp; &nbsp; &nbsp; } <br> &nbsp; &nbsp; } <br> } |