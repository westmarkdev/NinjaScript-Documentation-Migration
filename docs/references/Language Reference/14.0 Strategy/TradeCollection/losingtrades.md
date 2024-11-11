---
title: LosingTrades
pathName: losingtrades
parent: tradecollection
section: references
status: imported
---

## Definition

A subcollection of **Trade** objects consisting of only the losing trades in a **TradeCollection**. You can access a trade object by providing an index value. Trades are indexed sequentially meaning the oldest trade taken in a strategy will be at an index value of zero. The most recent trade taken will be at an index value of the total trades in the collection minus 1.

## Methods and Properties

{% table %}

---

* [Count](tradecollection_tradescount.htm)
* An **int** value representing the number of trades in the collection

---

* [GetTrades()](gettrades.htm)
* Gets a **TradeCollection** object representing a specified position

---

* [TradesPerformance](tradesperformance.htm)
* Gets a **TradesPerformance** object
{% /table %}

## Syntax

<`tradecollection`>.**LosingTrades**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Accesses the first/last losing trade in the strategy (oldest trade is at index 0)
     // and prints out the profit as a percentage to the output window
     if (SystemPerformance.AllTrades.LosingTrades.Count > 1)
     {
         Trade lastTrade = SystemPerformance.AllTrades.LosingTrades[SystemPerformance.AllTrades.Count - 1];
         Trade firstTrade = SystemPerformance.AllTrades.LosingTrades[0];

         Print("The last losing trade's profit was " + lastTrade.ProfitPercent);
         Print("The first losing trade's profit was " + firstTrade.ProfitPercent);
     }
}
```
