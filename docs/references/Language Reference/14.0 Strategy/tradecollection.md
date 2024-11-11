---
section: references
status: imported
parent: strategy
title: TradeCollection
pathName: tradecollection
---

## Definition

A collection of **Trade** objects. You can access a trade object by providing an index value. Trades are indexed sequentially meaning the oldest trade taken in a strategy will be at an index value of zero. The most recent trade taken will be at an index value of the total trades in the collection minus 1.

## Methods and Properties

{% table %}

---

* [TradesCount](tradecollection_tradescount)
* An **int** value representing the number of trades in the collection

---

* [EvenTrades](eventrades)
* Gets a TradeCollection object of even trades

---

* [GetTrades()](gettrades)
* Gets a TradeCollection object representing a specified position

---

* [LosingTrades](losingtrades)
* Gets a TradeCollection object of losing trades

---

* [TradesPerformance](tradesperformance)
* Gets a [TradesPerformance](tradesperformance) object

---

* [WinningTrades](winningtrades.md)
* Gets a TradeCollection object of winning trades
{% /table %}

## Examples

```csharp
protected override void OnBarUpdate()
{
   // Accesses the first/last trade in the strategy (oldest trade is at index 0)
   // and prints out the profit as a percentage to the output window
   if (SystemPerformance.AllTrades.Count > 1)
   {
       Trade lastTrade = SystemPerformance.AllTrades[SystemPerformance.AllTrades.Count - 1];
       Trade firstTrade = SystemPerformance.AllTrades[0];

       Print("The last trade profit is " + lastTrade.ProfitPercent);
       Print("The first trade profit is " + firstTrade.ProfitPercent);
   }
}
```

```csharp
protected override void OnBarUpdate()
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
}
```
