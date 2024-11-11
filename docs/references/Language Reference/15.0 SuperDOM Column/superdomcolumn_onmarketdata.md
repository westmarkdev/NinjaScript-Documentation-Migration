---
title: OnMarketData()
pathName: onmarketdata
parent: superdom_column
status: imported
section: references
---

## Definition

Called and guaranteed to be in the correct sequence for every change in level one market data for the underlying instrument. The **OnMarketData()** method updates can include but is not limited to the bid, ask, last price and volume.

## Method Return Value

This method does not return a value.

## Syntax

**protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)**

## Parameters

{% table %}

* Parameter
* Description

---

* **marketDataUpdate**
* A [MarketDataEventArgs](marketdataeventargs) representing the change in market data
{% /table %}

## Examples

```csharp
protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
   if (marketDataUpdate.MarketDataType == Data.MarketDataType.Last)
   {
     // Do something
   }
}
```
