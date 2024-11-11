---
title: IsTickReplay
pathName: istickreplay
parent: bars
section: references
status: review
---

## Definition

Indicates if the bar series is using the **Tick Replay** data series property.

## Property Value

This property returns true if the bar series is using tick replay; otherwise, false. This property is read-only.

## Syntax

**Bars.IsTickReplay**

{% callout type="warning" %}

Warning: A Tick Replay indicator or strategy CANNOT use a **MarketDataType.Ask** or **MarketDataType.Bid** series. Please see [Developing for Tick Replay](developing_for_tick_replay.md) for more information.

{% /callout %}

## Examples

```csharp
private double askPrice;
protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
    if(Bars.IsTickReplay)
    {
        // if using tick replay, get the current ask price associated with the tick
        askPrice = marketDataUpdate.Ask;
    }
    else // otherwise, get the real-time market data price during MarketDataType.Ask event
        askPrice = marketDataUpdate.MarketDataType == MarketDataType.Ask ? marketDataUpdate.Price : double.MinValue;

    // only print if a value is set
    if(askPrice != double.MinValue)
    {
        Print("ask price: " + askPrice);
    }
}
```
