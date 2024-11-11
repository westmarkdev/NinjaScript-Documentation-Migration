---
status: double_check
title: WinningTrades
pathName: winningtrades
parent: tradecollection
section: references
lg2m: true
---

## Definition

A subcollection of [Trade](trade) objects consisting of only the winning trades in a [TradeCollection](source_files/tradecollection.md). You can access a trade object by providing an index value. Trades are indexed sequentially meaning the oldest trade taken in a strategy will be at an index value of zero. The most recent trade taken will be at an index value of the total trades in the collection minus 1.

## Methods and Properties

{% table %}

* Method/Property

* Description

---

* [Count](source_files/tradecollection_tradescount.md)

* An int value representing the number of trades in the collection

---

* [GetTrades()](gettrades)

* Gets a [TradeCollection](source_files/tradecollection.md) object representing a specified position

---

* [TradesPerformance](tradesperformance)

* Gets a [TradesPerformance](tradesperformance) object

---

{% /table %}

## Syntax  

<`TradeCollection`>.**WinningTrades**

## Examples

```csharp
protected override void OnBarUpdate()  
{  
    // Accesses the first/last winning trade in the strategy (oldest trade is at index 0)  
    // and prints out the profit as a percentage to the output window  
    if (SystemPerformance.AllTrades.WinningTrades.Count > 1)  
    {  
        Trade lastTrade = SystemPerformance.AllTrades.WinningTrades[SystemPerformance.AllTrades.Count - 1];  
        Trade firstTrade = SystemPerformance.AllTrades.WinningTrades[0];  
   
        Print("The last winning trade's profit was " + lastTrade.ProfitPercent);  
        Print("The first winning trade's profit was " + firstTrade.ProfitPercent);  
    }  
}
```
