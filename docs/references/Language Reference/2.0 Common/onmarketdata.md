---
title: OnMarketData()
pathName: onmarketdata
parent: common
section: references
status: review
---

## Definition

An event driven method which is called and guaranteed to be in the correct sequence for every change in level one market data for the underlying instrument. **OnMarketData()** can include but is not limited to the bid, ask, last price and volume.

{% callout type="note" %}

1. This is a real-time data stream and can be CPU intensive if your program code is compute intensive (not optimal).
2. By default, this method is not called on historical data (backtest), however it can be called historically by using [TickReplay](tick_replay).
3. If used with [TickReplay](tick_replay), please keep in mind Tick Replay ONLY replays the Last market data event, and only stores the best inside bid/ask price at the time of the last trade event. You can think of this as the equivalent of the bid/ask price at the time a trade was reported. As such, historical bid/ask market data events (i.e., bid/ask volume) DO NOT work with Tick Replay. To obtain those values, you need to use a [historical bid/ask series](using_historical_bid_ask_serie) separately from TickReplay through **OnBarUpdate()**. More information can be found under [Developing for Tick Replay](developing_for_tick_replay.md).
4. With [multi-time frame and instrument strategies](multi_time_frame_instruments.md), a subscription will be created on all bars series added in your indicator or strategy (even if the instrument is the same). The market data subscription behavior occurs both in real-time and during [TickReplay](tick_replay) historical.
5. Do not leave an unused **OnMarketData()** method declared in your NinjaScript object. This will unnecessarily attach a data stream to your strategy which uses unnecessary CPU cycles.
6. Should you wish to run comparisons against prior values you will need to store and update local variables to track the relevant values.
7. The **OnMarketData()** method is expected to be called after [OnBarUpdate()](onbarupdate).
{% /callout %}

## Method Return Value

This method does not return a value.

## Syntax

You must override the method in your strategy or indicator with the following syntax.

**protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)**

{% callout type="note" %}

The NinjaScript code wizards can automatically generate the method syntax for you when creating a new script.

{% /callout %}

## Parameters

{% table %}

* Parameter
* Description

---

* **marketDataUpdate**
* [MarketDataEventArgs](marketdataeventargs) representing the recent change in market data
{% /table %}

## Examples

```csharp
protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
     // Print some data to the Output window
     if (marketDataUpdate.MarketDataType == MarketDataType.Last) 
           Print(string.Format("Last = {0} {1} ", marketDataUpdate.Price, marketDataUpdate.Volume));
     else if (marketDataUpdate.MarketDataType == MarketDataType.Ask)
         Print(string.Format("Ask = {0} {1} ", marketDataUpdate.Price, marketDataUpdate.Volume));
     else if (marketDataUpdate.MarketDataType == MarketDataType.Bid)
         Print(string.Format("Bid = {0} {1}", marketDataUpdate.Price, marketDataUpdate.Volume));
}
```
