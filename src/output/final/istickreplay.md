---
title: "IsTickReplay"
pathName: /docs/desktop/istickreplay
---

## Definition

Indicates if the bar series is using the [Tick Replay](/docs/desktop/developing_for__tick_replay) data series property.

## Property Value

This property returns true if the bar series is using tick replay; otherwise, false. This property is read-only.

### Syntax

```csharp
## Bars.IsTickReplay
```

{% callout type="warning" %}
A Tick Replay indicator or strategy CANNOT use a MarketDataType.Ask or MarketDataType.Bid series. Please see [Developing for Tick Replay](/docs/desktop/developing_for__tick_replay) for more information.
{% /callout %}

## Examples

```csharp
private double askPrice;

protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
    if (Bars.IsTickReplay)
    {
        // if using tick replay, get the current ask price associated with the tick
        askPrice = marketDataUpdate.Ask;
    }
    else // otherwise, get the real-time market data price during MarketDataType.Ask event
    {
        askPrice = marketDataUpdate.MarketDataType == MarketDataType.Ask ? marketDataUpdate.Price : double.MinValue;
    }

    // only print if a value is set
    if (askPrice != double.MinValue)
    {
        Print("ask price: " + askPrice);
    }
}
```

