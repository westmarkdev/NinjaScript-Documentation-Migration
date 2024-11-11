---
title: EvenTrades
pathName: eventrades
parent: tradecollection
section: references
status: imported
---

## Definition

A subcollection of **Trade** objects consisting of only the non-winning and non-losing trades in a **TradeCollection**.

{% callout type="note" %}

You can access a trade object by providing an index value. Trades are indexed sequentially meaning the oldest trade taken in a strategy will be at an index value of zero. The most recent trade taken will be at an index value of the total trades in the collection minus 1.

{% /callout %}

## Methods and Properties

{% table %}

* Method/Property
* Description

---

* [Count](tradecollection_tradescount)
* An **int** value representing the number of trades in the collection

---

* [GetTrades()](gettrades)
* Gets a **TradeCollection** object representing a specified position

---

* [TradesPerformance](tradesperformance)
* Gets a **TradesPerformance** object
{% /table %}

## Syntax

**<`tradecollection`>.EvenTrades**

## Examples

```csharp
protected override void OnBarUpdate()
{
     // Accesses the first/last losing trade in the strategy (oldest trade is at index 0)
     // and prints out the quantity NinjaScript Output window
     if (SystemPerformance.AllTrades.EvenTrades.Count > 1)
     {
         Trade lastTrade = SystemPerformance.AllTrades.EvenTrades[SystemPerformance.AllTrades.Count - 1];
         Trade firstTrade = SystemPerformance.AllTrades.EvenTrades[0];

         Print("The last even trade's quantity was " + lastTrade.Quantity);
         Print("The first even trade's quantity was " + firstTrade.Quantity);
     }
}
```
