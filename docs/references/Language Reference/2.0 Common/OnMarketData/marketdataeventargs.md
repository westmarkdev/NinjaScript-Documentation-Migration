---
title: MarketDataEventArgs
pathName: marketdataeventargs
parent: onmarketdata
section: references
status: review
---

## Definition

Represents a change in level one market data and is passed as a parameter in the **OnMarketData()** method.

## Methods and Parameters

{% table %}

* Ask
* Bid
* Instrument
* IsReset
* MarketDataType
* Price
* Time
* ToString()
* Volume

---

* A **double** value representing the ask price
* A **double** value representing the bid price
* A Instrument object representing the instrument of the market data
* A bool value representing if a UI reset is needed after a manual disconnect. Note: This is only relevant for columns. Whenever this property is true, the UI needs to be reset. Possible values are:
  * MarketDataType.Ask
  * MarketDataType.Bid
  * MarketDataType.DailyHigh
  * MarketDataType.DailyLow
  * MarketDataType.DailyVolume
  * MarketDataType.Last
  * MarketDataType.LastClose (prior session close)
  * MarketDataType.Opening
  * MarketDataType.OpenInterest (supported by IQFeed, Kinetick)
  * MarketDataType.Settlement
* A **double** value representing the price
* A **DateTime** structure representing the time
* A string representation of the MarketDataEventArgs object
* A long value representing volume
{% /table %}

{% callout type="note" %}

Critical: If used with **TickReplay**, please keep in mind Tick Replay ONLY replays the Last market data event, and only stores the best inside bid/ask price at the time of the last trade event. You can think of this as the equivalent of the bid/ask price at the time a trade was reported. Please also see **Developing for Tick Replay**.

{% /callout %}

{% callout type="note" %}

Tips

* Not all connectivity providers support all MarketDataTypes.
* For an example of how to use IsReset please see **MarketAnalyzerColumns\AskPrice.cs**.
{% /callout %}

## Examples

```csharp
protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
    // Print some data to the Output window
    if (marketDataUpdate.MarketDataType == MarketDataType.Last)
        Print("Last = " + marketDataUpdate.Price + " " + marketDataUpdate.Volume);
    else if (marketDataUpdate.MarketDataType == MarketDataType.Ask)
        Print("Ask = " + marketDataUpdate.Price + " " + marketDataUpdate.Volume);
    else if (marketDataUpdate.MarketDataType == MarketDataType.Bid)
        Print("Bid = " + marketDataUpdate.Price + " " + marketDataUpdate.Volume);
}
```
